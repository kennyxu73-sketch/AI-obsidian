# AI-OB 内阁系统变更日志 (CHANGELOG)

**版本**: v1.6.7-Pilot-Operational  
**维护者**: 小酷 (CTO)  
**协议**: 遵循 `.cursorrules` L0.7 要求  
**状态**: 🔄 活跃更新中

---

## 2026-03-29 | inbox→enseal→Patch 流水线文档与 L2 Dify 设计（TOOLS 配对）

### 变更概述
`Infrastructure/多源对话收件.md` 晋升路径（RAW→Triple-A drafts / 可选 Cognitive_Patch→TRUTH）；`Infrastructure/多源对话收件法典.md` 与 enseal 双径及 Runbook 链；`Agent/小忆/小忆_L2_inbox_enseal_patch.md`；`Dify/01_Ingest_&_Memory/WF_InboxRefine_Patch.md`；`Dify/_exports/README.md`；`Agent/AGENT_L1_PROMPTS.md`、`AGENT_INDEX.md` 增补 L2。TOOLS：`preflight_dify_zt.py`、`prompt_http_bridge.py`、`Manuals/inbox_enseal_seal_runbook.md`、`dialog_inbox.py` 注释。`ref_id` 三处一致如下。

### JSON（影子索引）
```json
{ "module": "inbox-enseal-dify-l2-pipeline-vault", "status": "done", "ref_id": "INFRA-DIFY-INBOX-20260329-01" }
```

---

## 2026-03-29 | Agent L1：Dify cabinet.* 白名单（TOOLS 配对）

### 变更概述
新增 `Agent/L1_DIFY_CABINET_TOOLS.md`、`Agent/dify_agent_tools_export.json`（自 TOOLS 导出）；`AGENT_L1_PROMPTS` / `AGENT_INDEX` / `数字内阁（Digital Cabinet）` 增加链接。权威 JSON 在 `Internal_Cabinet_Tools/config/agent_l1_registry.json`。

### JSON（影子索引）
```json
{ "module": "agent-l1-dify-registry-vault", "status": "done", "ref_id": "P1-AGENT-L1-DIFY-20260329" }
```

---

## 2026-03-29 | Agent 目录梳理同步（AGENT_INDEX / L1 矩阵 / agent_slug / 占位）

### 变更概述
`Agent/AGENT_INDEX.md`、`Agent/AGENT_L1_PROMPTS.md`；`小镜/`、`小康/` 占位；各角色 L1 主入口 YAML（`agent_slug`、`l1_entry`）；`数字内阁/AI-ob 数字内阁.canvas` 内链指向 `小欧/小欧`、`小记/小记`、`小镜/小镜`、`小康/小康`；`内阁-自由议事与安全执行方案.md` 增加 `aliases`。与 TOOLS 镜像 `000_Cabinet_System 1/Agent/` 配对；真库小忆主入口为 `小忆/小忆.md`。

### JSON（影子索引）
```json
{ "module": "agent-catalog-l1-slug-vault", "status": "done", "ref_id": "P1-AGENT-CATALOG-20260329" }
```

---

## 2026-03-29 | 多源对话运维策略（PSR/锁/日志巡检，TOOLS 配对）

### 变更概述
`Infrastructure/多源对话收件法典.md` 增补运维小节；配对 TOOLS manifest **fcntl**、`health_check dialog-sync-errors`、Runbook。`ref_id` 如下。

### JSON（影子索引）
```json
{ "module": "dialog-inbox-ops-balance", "status": "done", "ref_id": "P0-DIALOG-INBOX-OPS-20260329" }
```

---

## 2026-03-29 | 多源对话收件法典 + RUNTIME ai_dialogue_inbox（TOOLS 配对）

### 变更概述
`Infrastructure/多源对话收件法典.md` 落地；`RUNTIME_ROOT/ai_dialogue_inbox/` 约定见 TOOLS `dialog_inbox.py` 与 `.cursorrules` L2。配对审计如下。

### JSON（影子索引）
```json
{ "module": "dialog-inbox-multisource", "status": "done", "ref_id": "P0-DIALOG-INBOX-20260329" }
```

---

## 2026-03-28 | Kenny 主画像规范入口 + Cognitive Patch 防呆（TOOLS 配对）

### 变更概述
SSOT 新增 `Agent/小忆/Kenny画像/Kenny_Cognitive_Profile.md` 为规范主入口；`Infrastructure/AI-OB 主人身份与记忆.md` 增加 L0.5 路径勘误表；`RUNTIME/Cognitive_Patch_Draft.md` 增补 Gap Engine 模板块（`Target_SSOT_Path`）。工具侧见 TOOLS `CHANGELOG.md`，配对 `ref_id` 如下。

### JSON（影子索引）
```json
{ "module": "owner-context-cognitive-patch", "status": "done", "ref_id": "P0-OWNER-CONTEXT-20260328" }
```

---

## 2026-03-28 | PSR 哨兵令牌 + 写权限（TOOLS，配对）

### JSON（影子索引）
```json
{ "module": "psr-sentinel-token-wok", "status": "done", "ref_id": "P0-PSR-TOKEN-20260328" }
```

---

## 2026-03-28 | PSR 物理主权（TOOLS 实施，配对）

### 变更概述
TOOLS 已实施 PSR：哨兵文件、`health_check`、自愈脚本草案及法典 L0.6.3；封印/路径日志写盘前自检。本条配对审计；专项正文仍以 `项目进展文档/P0进度/...物理主权与路径隔离协议.md` 为准。

### JSON（影子索引）
```json
{ "module": "psr-physical-sovereignty", "status": "done", "ref_id": "P0-PSR-SENTINEL-20260328" }
```

---

## 2026-03-28 | 编排策略：第一阶段 n8n 可选（配对）

### 变更概述
TOOLS 侧 `.cursorrules` / 工作区注释已写明：P0 不强制 n8n。本条配对审计。

### JSON（影子索引）
```json
{ "module": "orchestration-pilot-n8n-optional", "status": "done", "ref_id": "POLICY-N8N-OPTIONAL-20260328" }
```

---

## 2026-03-28 | skill_manager / Dify 编排（TOOLS 侧，配对）

### 变更概述
`TOOLS_PATH` 已扩展 `skill_manager.py` 与 `dify_client.py`，支持 Dify 工作流 API 与内阁 `cabinet.*` 内置调用，供 HTTP/代码节点衔接。本条为配对审计。

### JSON（影子索引）
```json
{ "module": "skill-manager-dify-orchestration", "status": "done", "risk_level": "low", "ref_id": "P0-SKILL-DIFY-20260328" }
```

---

## 2026-03-28 | enseal_skill：封印闭环（配对审计）

### 变更概述
`TOOLS_PATH` 侧 `enseal_skill.py` 已支持自 `drafts/` 校验并入库 SSOT（L0.7 + SHA-256 + 双 CHANGELOG）。本条为配对审计。

### JSON（影子索引）
```json
{ "module": "enseal-seal-pipeline", "status": "done", "risk_level": "medium", "ref_id": "P0-ENSEAL-CLOSED-LOOP-20260328" }
```

---

## 2026-03-28 | Triple-A：metadata_parser（TOOLS 侧 YAML 提取）

### 变更概述
`TOOLS_PATH` 新增 `metadata_parser.py`，解析 note.md Frontmatter 与 `.card.yaml` / `.audit.yaml`，供向量化与审计流水线读取。本条为配对审计。

### JSON（影子索引）
```json
{ "module": "metadata-parser-triple-a", "status": "done", "risk_level": "low", "ref_id": "P0-METADATA-PARSER-20260328" }
```

---

## 2026-03-28 | L0.7：path_guardian（TOOLS 侧物理护栏）

### 变更概述
`TOOLS_PATH` 新增 `path_guardian.py`，实现 L0.7 SSOT 结构校验与扫描；违规时可记 `200_Operations/logs/path_conflict.log` 并追加 `Cognitive_Patch_Draft.md`。本条为配对审计。

### JSON（影子索引）
```json
{ "module": "path-guardian-l07", "status": "done", "risk_level": "low", "ref_id": "P0-PATH-GUARD-20260328" }
```

---

## 2026-03-28 | P0：封印技能 MVP（TOOLS 侧实现）

### 变更概述
`TOOLS_PATH` 已落地 `enseal_skill.py` + `tag_schema.json` 校验；草稿输出至 `obsidian_vault/200_Operations/drafts/`（Triple-A）。本条为配对审计。

### JSON（影子索引）
```json
{ "module": "enseal-mvp", "status": "done", "risk_level": "low", "ref_id": "P0-ENSEAL-20260328" }
```

---

## 2026-03-28 | 工具工作区目录注释（配对记录）

### 变更概述
`TOOLS_PATH` 侧新增 `WORKSPACE_工作区目录注释.md`，对 `Cursor_Workspace` 与 `Internal_Cabinet_Tools` 做结构说明；SSOT 侧本条仅作配对审计，无 Vault 内文件移动。

### JSON（影子索引）
```json
{ "module": "workspace-annotate", "status": "done", "risk_level": "low", "ref_id": "DOCS-WORKSPACE-20260328" }
```

---

## 2026-03-28 | 路径熵减与 SSOT 结构扁平化

### 变更概述
清理自动化误操作产生的路径碎屑，消除 SSOT 下冗余嵌套目录，合并重复项目根，降低双链与检索歧义。

### 关键动作
1. 删除 `Cursor_Workspace/-p`（空目录，`mkdir` 参数误用遗迹）。
2. 删除空目录 `obsidian_vault/200_Operationsmkdir`（路径拼接错误遗迹）。
3. 删除 `000_Cabinet_System/000_Cabinet_System/`（内层仅空占位文件；权威文件已在 `000_Cabinet_System/基础背景 prompt.md`）。
4. `Kenny's Projects 1` → 以 `Kenny's Projects/` 为主库，`rsync --ignore-existing` 合入增量后删除 `Kenny's Projects 1`。

### JSON（影子索引）
```json
{ "module": "entropy-reduce", "status": "done", "risk_level": "low", "ref_id": "ENTROPY-20260328-REDUCE" }
```

---

## 2026-03-28 | 物理主库合并（嵌套副本已删除）

### 变更概述
将误置于 `Cursor_Workspace/Volumes/Cabinet/cabinet/obsidian_vault/` 的运行期文件合并至唯一主库 `/Volumes/Cabinet/cabinet/obsidian_vault/`，并删除该嵌套目录树，避免双份编辑与分叉。

### 关键动作
1. 合并：`Active_Session.md`、`Cognitive_Patch_Draft.md`、`logs/path_conflict.log`、`本 CHANGELOG`。
2. 将嵌套路径下 `.../Internal_Cabinet_Tools/path_conflict.log` 片段追加至主库 `path_conflict.log`（带合并标记）。
3. 删除：`/Volumes/Cabinet/cabinet/Cursor_Workspace/Volumes/`（整树）。

### JSON（影子索引）
```json
{ "module": "path-merge", "status": "done", "risk_level": "low", "ref_id": "MERGE-20260328-VAULT" }
```

---

## 2026-03-28 | 系统基础设施对齐点火

### 变更概述
完成 AI-OB 系统 Canonical Path Map 与物理目录结构的全面对齐，消除路径冲突根源。

### 关键动作
1. **宪法更新**: 修订 `.cursorrules` L0.5 & L0.6，将路径锚定至现有 `obsidian_vault` 结构。
2. **目录补全**: 创建缺失的 `200_Operations/` 运行时目录及其子结构。
3. **文件初始化**: 创建本 CHANGELOG 及运行时关键文件。

### 技术详情
- **L0.5 新映射**:
  - `MEMOIR_PATH` = `$CABINET_ROOT/obsidian_vault/400_Chronicles/`
  - `RAW_PATH` = `$CABINET_ROOT/obsidian_vault/100_Inbox_Intelligence/`
  - `RUNTIME_ROOT` = `$CABINET_ROOT/obsidian_vault/200_Operations/`
  - `SSOT_ROOT` = `$CABINET_ROOT/obsidian_vault/000_Cabinet_System/`
  - `TOOLS_PATH` = `$CABINET_ROOT/Cursor_Workspace/Internal_Cabinet_Tools/`

### 审计痕迹
- **触发规则**: L0.7 (SSOT 结构护栏要求 CHANGELOG)
- **审批状态**: ✅ Kenny 直接指令执行
- **关联文件**: `$RUNTIME_ROOT/Cognitive_Patch_Draft.md`

### 下一步
- 处理 SSOT 结构白名单违规项
- 验证 3090 服务器端口连通性
- 推进 P0 点火具体技能开发

---
**变更日志结束** | 版本 v1.6.7 初始化完成