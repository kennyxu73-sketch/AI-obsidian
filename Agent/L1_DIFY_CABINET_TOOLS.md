# L1 · Dify / 编排可调用的内阁工具（cabinet.*）

> 与 [[AGENT_L1_PROMPTS]]（人格 SSOT）并列：本页描述 **可被 Dify 代码节点或 shell 调用的 `cabinet.*` 键** 按 `agent_slug` 白名单。
> 机器注册表：`Internal_Cabinet_Tools/config/agent_l1_registry.json`（由 `agent_l1_registry.py` 校验）；真库可保留同名快照 `Agent/agent_l1_registry.json` 便于离线查阅。
> 小忆人格文件：真库多为 `小忆/小忆.md`，镜像可能为 `小忆/小憶.md`，见 [[AGENT_INDEX]]。

## 调用方式

- **工作目录**：`Internal_Cabinet_Tools 根目录`
- **CLI**：`python3 skill_manager.py cabinet-run <skill_key> [--inputs-json FILE | --inputs-inline JSON]`
- **说明**：Dify 侧可在「代码」节点中 subprocess 调用上述 CLI，或由网关将同参映射为 HTTP POST（需自研薄封装）；本仓库不内置 HTTP 服务。

## 各 `agent_slug` 与白名单技能

### `audit_xiaoku` — 审计小酷

- **人格入口**：`审计 agents/审计小酷.md`
- **职责摘要**：审计分身 / 合规扫描

| cabinet.* | 说明 | inputs 提示 |
|-----------|------|-------------|
| `cabinet.enseal.seal_scan` | 封印与合规扫描 | `{ 见 enseal_skill seal_scan 参数 }` |
| `cabinet.enseal.seal_batch` | 批量封印审计 | `{ 见 enseal_skill seal_batch 参数 }` |
| `cabinet.path_guardian.check_ssot` | 路径违规检测 | `{ "path": "相对 SSOT 或绝对路径", "as_dir": false }` |
| `cabinet.psr.status` | PSR 状态 | `{}` |
| `cabinet.dialog.inbox_validate` | inbox 抽检 | `{ "path": "RUNTIME 下 inbox md 绝对或相对路径" }` |

### `xiaobao` — 小报

- **人格入口**：`小报/小报.md`
- **职责摘要**：外情 / 入站质检 / 列表

| cabinet.* | 说明 | inputs 提示 |
|-----------|------|-------------|
| `cabinet.dialog.inbox_validate` | 入站 md 格式校验 | `{ "path": "RUNTIME 下 inbox md 绝对或相对路径" }` |
| `cabinet.dialog.inbox_list` | 列出 manifest 会话 | `{ "source": "" }` |
| `cabinet.metadata.extract_triple_a` | 元数据提取（定级辅助） | `{ "path": "..." }` |
| `cabinet.path_guardian.check_ssot` | 归档路径是否可写 SSOT 子路径 | `{ "path": "相对 SSOT 或绝对路径", "as_dir": false }` |

### `xiaohei` — 小黑

- **人格入口**：`小黑/小黑.md`
- **职责摘要**：分析 / 结构化 / 入库前控制

| cabinet.* | 说明 | inputs 提示 |
|-----------|------|-------------|
| `cabinet.dialog.inbox_validate` | inbox 块结构校验 | `{ "path": "RUNTIME 下 inbox md 绝对或相对路径" }` |
| `cabinet.metadata.extract_triple_a` | Triple-A 提取 | `{ "path": "..." }` |
| `cabinet.enseal.materialize_draft` | 材料化（经审批后） | `{ "draft_path": "..." }` |
| `cabinet.enseal.seal_scan` | 封印扫描 | `{ 见 enseal_skill seal_scan 参数 }` |

### `xiaohua` — 小画

- **人格入口**：`小画/小画.md`
- **职责摘要**：可视化 / 只读上下文

| cabinet.* | 说明 | inputs 提示 |
|-----------|------|-------------|
| `cabinet.dialog.inbox_list` | 只读列举会话（展示用） | `{ "source": "" }` |
| `cabinet.path_guardian.check_ssot` | 路径合法性（Canvas 链路径） | `{ "path": "相对 SSOT 或绝对路径", "as_dir": false }` |

### `xiaoji` — 小记

- **人格入口**：`小记/小记.md`
- **职责摘要**：Memory OS / 硬件 / 主权底座

| cabinet.* | 说明 | inputs 提示 |
|-----------|------|-------------|
| `cabinet.psr.status` | PSR 与挂载诊断 | `{}` |
| `cabinet.path_guardian.check_ssot` | 路径护栏 | `{ "path": "相对 SSOT 或绝对路径", "as_dir": false }` |
| `cabinet.metadata.extract_triple_a` | 元数据提取（资产登记辅助） | `{ "path": "..." }` |

### `xiaojing` — 小镜

- **人格入口**：`小镜/小镜.md`
- **职责摘要**：2C 占位

- **cabinet_skills**：*空* — prompt_status TBD；后续接入回忆录相关 cabinet.* 或工作流

### `xiaokang` — 小康

- **人格入口**：`小康/小康.md`
- **职责摘要**：2B 占位

- **cabinet_skills**：*空* — prompt_status TBD；后续接入慰康业务 cabinet.* 或 Dify 工作流

### `xiaoku` — 小酷

- **人格入口**：`小酷/小酷.md`
- **职责摘要**：CTO / 工具链 / 封印 / PSR / 路径护栏

| cabinet.* | 说明 | inputs 提示 |
|-----------|------|-------------|
| `cabinet.enseal.materialize_draft` | 从 Triple-A 草稿材料化 L1 | `{ "draft_path": "..." }` |
| `cabinet.enseal.materialize_from_inbox` | 从 inbox 炼化草稿 | `{ 见 enseal_skill / cabinet_builtins 入参 }` |
| `cabinet.enseal.materialize_from_cognitive_patch` | 从 Cognitive Patch 块炼化 | `{ 见 enseal_skill --materialize-from-cognitive-patch }` |
| `cabinet.enseal.seal_scan` | 封印扫描 | `{ 见 enseal_skill seal_scan 参数 }` |
| `cabinet.enseal.seal_batch` | 批量封印 | `{ 见 enseal_skill seal_batch 参数 }` |
| `cabinet.path_guardian.check_ssot` | SSOT 路径合规检查 | `{ "path": "相对 SSOT 或绝对路径", "as_dir": false }` |
| `cabinet.psr.status` | 物理主权哨兵诊断（只读） | `{}` |
| `cabinet.metadata.extract_triple_a` | Triple-A 元数据提取 | `{ "path": "..." }` |
| `cabinet.dialog.inbox_validate` | 单文件 inbox 校验 | `{ "path": "RUNTIME 下 inbox md 绝对或相对路径" }` |
| `cabinet.dialog.append_wecom_dedup` | 企微去重后追加 inbox | `{ "msg_id", "source", "session_id", "role", "text", ... }` |

### `xiaoou` — 小欧

- **人格入口**：`小欧/小欧.md`
- **职责摘要**：OpenBT / 数据资产路径

| cabinet.* | 说明 | inputs 提示 |
|-----------|------|-------------|
| `cabinet.path_guardian.check_ssot` | SSOT 写入路径检查 | `{ "path": "相对 SSOT 或绝对路径", "as_dir": false }` |
| `cabinet.metadata.extract_triple_a` | 元数据提取 | `{ "path": "..." }` |

### `xiaoyi` — 小忆

- **人格入口**：`小忆/小忆.md`
- **职责摘要**：秘书长 / Kenny 画像 / 调度上下文

| cabinet.* | 说明 | inputs 提示 |
|-----------|------|-------------|
| `cabinet.owner.load_context` | 加载 Kenny 画像与 owner 上下文 | `{ "max_chars": 12000, "profile_relative": "Agent/小忆/Kenny画像/Kenny_Cognitive_Profile.md" }` |
| `cabinet.patch.list_cognitive_blocks` | 列举 Cognitive Patch 块 | `{ "patch_heading_contains": "..." 或 "patch_slug": "..." }` |
| `cabinet.dialog.inbox_list` | 多源会话列表 | `{ "source": "" }` |
| `cabinet.dialog.inbox_merge_session` | L3 合并时间线 + silence_hint | `{ "session_id": "wecom:room", "source_prefix": "wecom_" }` |
| `cabinet.dialog.inbox_validate` | 抽检 inbox 文件 | `{ "path": "RUNTIME 下 inbox md 绝对或相对路径" }` |

---

## 导出

- `python3 agent_l1_registry.py export-dify-json` → `config/dify_agent_tools_export.json`（供外部工具链拼装 Dify Custom Tool / OpenAPI）。
