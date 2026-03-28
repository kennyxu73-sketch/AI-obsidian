# 数字内阁 · 企业微信多 Bot 与会话策略（v1.2）

**状态**：草案（与 `dialog_inbox`、Prompt 法典、多文件 inbox 现网行为对齐）

**维护**：小酷（CTO）· 批准：Kenny

**关联**：[[数字内阁-SSOT索引]] · [[数字内阁-索引]]

---

## 0. 目标与边界

- **目标**：多企微应用（多 Bot）+ 空间锚定；对话统一进 `RUNTIME_ROOT/ai_dialogue_inbox/`；支持同群 **L3 穿透读取**；**防死循环**与**企微重试去重**。
- **边界**：约束适配器与 L3；不替代 Kenny 审批与 SSOT / enseal。企微字段以实际开通能力为准。
- **部署前提（去重库）**：**单机单写入路径**（同一适配器进程或明确单点 ingress）。多机多实例勿共 NFS 挂 SQLite；应改为集中式去重或单点网关。

---

## 1. 会话键与文件模型（写侧）

### 1.1 `session_id`（按群固定）

- **格式**：`wecom:{roomid}`（`roomid` 不含冒号）。
- **同一群**内所有参与同轴穿透的写入共用**同一** `session_id`。

**配置**：`WECOM_ROOM_*` 等环境变量或映射表，真值只维护一处。

### 1.2 `source`（按接入 / Bot 分文件）

- **格式**：`wecom_{agent_slug}`（小写 + 下划线）。
- **用户话轮（推荐）**：`wecom_human` 或 `wecom_ingest`，保证 L3 合并时间线完整。

### 1.3 维持「多源多文件」

- 与现网 `(source, session_id)` 一致；**不**改为「一群单 .md」，降低多 Bot 同文件并发改写风险。
- **审计**：按 `source` 分文件追溯各 Agent。

### 1.4 与落盘 slug 一致

- L3 筛选文件须使用与 `dialog_inbox` **相同的** `session_stem` / slug 规则；禁止对原始 `wecom:...` 做简单 glob 猜测。

---

## 2. L3 穿透读取（读侧）

### 2.1 合并

- 收集同 `session_id` 下相关 `wecom_*` 与 `wecom_human` 文件；解析 `## User` / `## Assistant` 与 `<!-- captured_at: ... -->`。
- 按 **captured_at 升序**合并；同时刻按约定次序决胜（如先 User 后 Assistant，或按 `source` 字典序）。

### 2.2 轻量「在场感知」（可选）

- **默认**：由 L3 根据本 room 涉及的 `source` 列表生成 `present_sources` 注入提示，**不必**写 manifest。
- **可选**：manifest 增加会话级元数据行（如伪 `wecom_session_meta`）含 `room_name`；**首期不强制**持久化 `active_agents`。

---

## 3. 消息去重（企微重试防抖）

### 3.1 内容层（审计）

- 每块保留企微消息锚，例如：  
  `<!-- wecom_msg_id: <MsgId> -->`  
- Bot 自生成无 MsgId 时：`<!-- client_ref_id: <uuid> -->`。

### 3.2 原子层（SQLite，推荐）

**路径（优先）**：

- **`{RUNTIME_ROOT}/wecom_dedup/dedup.db`**（与 `ai_dialogue_inbox` 同卷，便于 PSR、备份与权限与现网 RUNTIME 一致）。
- 若适配器仅挂载 Tools 目录且未注入 `RUNTIME_ROOT`：可暂用 `Internal_Cabinet_Tools/runtime/dedup.db`，文档须声明 **仅单点写入、与 inbox 同机**。

**库配置**：

- 开启 **WAL**；适配器使用短连接或受控连接；避免多进程无协调共写同一库文件。

**表结构（示例）**：

| 列 | 说明 |
|----|------|
| `session_id` | TEXT，如 `wecom:wrkxxx` |
| `msg_id` | TEXT，企微 MsgId（或与 client_ref_id 统一规则） |
| `source` | TEXT，可选，写入方 |
| `created_at` | TEXT ISO8601 |
| `status` | TEXT，可选：`committed` / `failed` |

**唯一约束**：`UNIQUE(session_id, msg_id)`（或若 MsgId 全局唯一可单键 `msg_id`，以企微文档为准；**推荐复合键**更稳）。

**流程**：

1. `INSERT` 新行；若触发 **UNIQUE 冲突** → 视为重复回调，**直接返回**，不再 `append_turn`。
2. 插入成功后调用 `append_turn()`。
3. **若 `append_turn` 失败**：删除该行或标 `status=failed`，**允许**企微重试重新走全流程（避免「库有记录、盘无块」永久丢消息）。策略二选一写死并在运维中一致执行。

**说明**：SQLite 负责 **msg 级去重**；**不替代** `inbox_manifest.jsonl` 的 **fcntl** 互斥；二者并存。

### 3.3 禁止单独作为唯一手段的做法

- **禁止**仅以「grep 全 inbox 再 append」作为唯一防抖（存在 TOCTOU 双写）。

---

## 4. 防死循环与回声

### 4.1 物理阻断（默认必开）：Human-Only Trigger

- 仅 **人类** 消息触发「调 Dify / 生成并发送群回复」。
- **Bot / 应用账号** 发出的回调：**不**进入自动回复链（可配置是否仍 `append_turn` 入库，须与产品一致；**禁止**因此再次触发模型回复）。

### 4.2 逻辑阈值：连续 Assistant 冷静期

- 数据来自 **L3 合并视图**的最近 N 个块（**不用** manifest 行代替消息级 role）。
- 示例：最近连续 3 块均为 `## Assistant` 且无新 `## User`（或超过时间窗）→ **SILENCE**，不发群；可记 `ON_FAILURE: SILENCE` 或固定短句交 Kenny。

### 4.3 语义反循环（可选）

- **P0**：与上一条 Assistant 规范化全文比对，相等或极高重叠则拦截。
- **P1**：向量相似度；注意成本、延迟与模板误杀。

---

## 5. Bot 映射表（字段）

| 列 | 说明 |
|----|------|
| `agent_slug` | 如 `xiaoyi` |
| `wecom_app` / `agent_id` | 应用标识 |
| `inbox_source` | 如 `wecom_xiaoyi` |
| `allowed_roomids` | 白名单 |
| `session_id` | `wecom:{roomid}` |
| `runtime_binding` / Dify | 与 Prompt 法典一致 |

---

## 6. 验收用例（最小集）

- [ ] 双 Bot 互发：不触发对端自动回复（Human-Only）。
- [ ] 同消息 webhook 重放：DB 唯一约束拦截，inbox **单块**。
- [ ] `append` 失败：dedup 行删除或标 `failed`，重试可恢复。
- [ ] 同 room 多文件 L3 合并顺序与 `captured_at` 一致。
- [ ] 连续 Assistant 冷静期生效。
- [ ] PSR：`append_turn` 前仍 `cabinet_sentinel`。

---

## 7. 工具链实现状态（Internal_Cabinet_Tools）

| 能力 | 模块 / 命令 | 说明 |
|------|-------------|------|
| SQLite 去重 | `wecom_dedup.py`、`dialog_inbox.py dedup-init` | `{RUNTIME_ROOT}/wecom_dedup/dedup.db` |
| 带去重写入 | `append_turn_with_wecom_dedup`、`append --dedup-msg-id` | 先 claim 再 `append_turn`，失败 `release_claim` |
| 块注释 | `append_turn(..., wecom_msg_id= / client_ref_id=)` | 校验与解析已支持 |
| L3 合并 + 冷静期提示 | `merge_inbox_session_timeline`、`silence_recommended_for_assistant_chain`、`merge-session` | 按 manifest 聚合 `wecom_*` 同源 `session_id` |
| 内置 Skill | `cabinet.dialog.inbox_merge_session`、`cabinet.dialog.append_wecom_dedup` | 供 Dify / skill_manager |

**未在本仓库实现（须在企微适配器侧完成）**：Webhook 接入、sender 判定 **Human-Only**、调用 Dify、出站发群。

---

## 8. 修订记录

| 版本 | 日期 | 摘要 |
|------|------|------|
| v1.0 | 2026-03-28 | 多文件、L3、三锁防循环、注释去重。 |
| v1.1 | 2026-03-28 | 3.2 原子层：RUNTIME_ROOT 下 SQLite + UNIQUE(session_id,msg_id) + 失败回滚策略；部署前提单写入。 |
| v1.2 | 2026-03-29 | 增加 §7 工具链落地表（Python 已实现入库 / 合并 / 去重）。 |
