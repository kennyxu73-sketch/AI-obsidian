---
title: 内阁 · AI-OB Skills 应用规范
aliases:
  - AI-OB Skills 应用与产品化规范
  - 内阁能力域与 Skills 目录规范
role: SSOT · 架构与文档治理
status: active
updated: 2026-03-29
---

# 内阁 · AI-OB Skills 应用规范

> **定位**：约定 **「应用域 / 人类维度」** 与 **「实现域（`cabinet.*`、Dify、脚本）」** 的双轨关系；支撑 **内化治理**、**Obsidian 插件融合叙事**、以及 **未来外向产品化** 的母版与储备。  
> **真源**：可执行能力以 `Internal_Cabinet_Tools/cabinet_builtins.py`、`config/agent_l1_registry.json` 与 **`config/dify_agent_tools_export.json`**（`cabinet_skill_key` 与 **`dify_suggested_name`** 配对）为准；Dify 侧人类可读说明见 `Agent/L1_DIFY_CABINET_TOOLS.md`。本规范 **不**替代代码、registry 与 JSON。

---

## 0. 阶段规划（P1 / P2）

| 阶段 | 范围 | 说明 |
|------|------|------|
| **P1（当前 AI-OB）** | **系统记录与储备** | 落地本规范、维护 **`Skills/`（或 `内阁应用域_Skills/`）** 下应用域叙事与索引；**不**实现 Claude Code 导出流水线、**不**强制维护 `cc_skills` 产物目录。 |
| **P2** | **外向导出与工具化** | 开发 manifest + 封装工具（如 `cc_skill_packager`），从 SSOT **裁剪脱敏** 生成 `Skills/cc_skills/<skill_id>/SKILL.md`；与对外发布、CHANGELOG/ref_id 配对。 |

**P2 封装工具硬条件（摘要）**：`cc_skill_packager` **仅处理** 成熟度为 **Standard** 且 `Skills/README.md` 矩阵中 **Auth = User-Level** 的应用域；导出正文以 **§5.3 P2 导出审计区** 的锚点为界 **物理裁剪**（仅保留线 **之上**）。**Legacy / Draft** 与 **System-Only** 默认 **不进入** 对外包。

P1 期间可在正文写作中 **习惯区分「可对外 / 仅内网」** 段落，为 P2 裁剪做准备；**无需**上自动化。

---

## 1. 术语

| 术语 | 含义 |
|------|------|
| **实现型 Skill** | `cabinet.<模块>.<动作>`，经 `skill_manager` / `dispatch_builtin` 执行，返回结构化结果。 |
| **应用域 Skill** | 以 **人类可理解的应用/系统名** 组织的 **叙事与目录**（可与 Claude Code `SKILL.md` 风格兼容），每条 **映射** 到实现键、Dify、Runbook、插件。 |
| **双轨** | 同一能力：**应用名** 沟通；**`cabinet.*`** 执行与审计。 |
| **cc_skills（P2）** | 计划中的子目录：仅放 **可对外** 的 Claude Code 规范包；P1 **仅在本规范中保留名称与意图**，目录可空或不建。 |
| **脑（意图）** | 应用域叙事：人类可读的目标、场景、红线；**不**等同于可执行键。 |
| **手套（接口）** | 外部编排（Dify、小酷工作流等）识别能力的名称；真源为 JSON 中的 **`dify_suggested_name`**（与 `cabinet_skill_key` 成对）。 |
| **手（执行）** | **`cabinet.*`**，由 `skill_manager` / `dispatch_builtin` 落地。 |
| **P2 导出审计区（Audit Buffer）** | 应用域文档内 **固定锚点以下** 的区域，存放内网私密配置；P2 导出时 **裁掉线以下**。见 §5.3。 |
| **`dify_suggested_name`** | `dify_agent_tools_export.json` 字段：与 Dify 工具注册名对齐的 **建议唯一 ID**；应用域文档 **必须** 摘引此字段，**禁止**臆造短名。 |
| **Skill 配套 Canvas** | 与 Standard 主 Skill **同目录、同主文件名 stem** 的 Obsidian **`*.canvas`**（JSON），用节点双链挂主文档与法典；**导读用**，不替代正文。见 §5.6。 |

---

## 2. 目标

1. **内化**：按 **「系统在干什么」** 找能力，而非死记多个实现键。  
2. **插件融合**：大量 Obsidian 插件时，各有 **语义、路径红线、与炼化/封印关系** 的可登记处。  
3. **外向与产品化（P2）**：应用域命名可复用于对外模块与集成说明；导出前须 **脱敏** 与 **版本/ref 配对**。  
4. **与 Agent / Dify 并列**：`Agent/` = 人格与 Prompt；`Dify/` = 工作流真源；**`Skills/`** = **能力与应用域（人机共同语言）**。

---

## 3. 命名原则

- **应用域**：中文 + 可系统化，如 **多 Agent 企微与会话编排**、**统帅画像 · 记录与提炼**、**内阁封印 · 档案与补丁双径**；标题中 **不写** `cabinet.*`。  
- **英文 slug**（可选）：供产品/URL，与实现键 **解耦**。  
- **Claude Code / Cursor Skill**：偏 **软约束**；**`cabinet.*`** 为 **硬执行**；应用域文档可采用 **SKILL 风格**，且须含 **「实现映射」**。

---

## 4. 目录结构（P1 可逐步落地）

在 `000_Cabinet_System/` 下与 `Agent/`、`Dify/` **同级**：

| 方案 | 路径 | 说明 |
|------|------|------|
| **A（推荐）** | `Skills/` | 短；`README.md` 首行注明 **≠ Cursor 全局 `.cursor/skills`**。 |
| **B** | `内阁应用域_Skills/` | 歧义更少。 |

**P2 预留（勿在 P1 强做）**：`Skills/cc_skills/` — 仅放对外 Claude Code 包。

**示例子目录（6～8 个域）**（编号前缀仅作索引，标题以域内文档为准）：

| 编号 | 应用域（工作名） | 说明（摘要） |
|------|------------------|--------------|
| 01 | 多 Agent 企微讨论 / 会话编排 | 企微多 Bot → `ai_dialogue_inbox`；去重、L3 合并 |
| 02 | 统帅画像 · 记录与提炼 | 占位 |
| 03 | 内阁封印 · 档案与补丁双径 | 占位 |
| 04～08 | （待定） | 随体系扩充登记 |

**现状（P1）**：`Skills/README.md` 维护 **能力成熟度矩阵**（含 Auth）与 **分区 A/B**；已落地示例目录 `01_多Agent企微讨论/`。详见 `[[Skills/README]]`（路径以本库 `000_Cabinet_System` 为准）。

---

## 5. 应用域文档强制结构（P2 裁剪预埋）

以下适用于 **成熟度 Standard** 的应用域主文档；**Legacy / Draft** 不强制全文结构，但 **不得** 默认进入 `cc_skill_packager`。

### 5.1 三位一体映射（脑 / 手套 / 手）

| 隐喻 | 含义 | 真源 |
|------|------|------|
| **脑** | 意图与场景叙事 | 正文「应用目标 / 场景 / 红线」 |
| **手套** | 外部 Agent 识别能力的接口名 | **`dify_agent_tools_export.json` → `dify_suggested_name`**（与 `cabinet_skill_key` 成对）；说明可链 [[L1_DIFY_CABINET_TOOLS]] |
| **手** | 实际执行 | **`cabinet.*`**，以 `cabinet_builtins.dispatch_builtin` 为准 |

**变更顺序**：先更新 **代码 + `dify_agent_tools_export.json` +（如需）`agent_l1_registry.json`**，再更新应用域文档与 L1 叙事，避免文书领先于实现。

### 5.2 能力对照表（强制）

每个 **Standard** 应用域 **必须** 含一张 **能力对照表**，**禁止** 仅写描述而不对齐实现。列至少包括：

1. **意图摘要**（脑）  
2. **`dify_suggested_name`**（手套，摘自 JSON）  
3. **`cabinet_skill_key`**（手）

可选：L1 文档锚点、多 `agent_slug` 多条 `dify_suggested_name` 的备注。

### 5.3 P2 导出审计区（Audit Buffer）

- **推荐结构**：在需隔离处使用 **水平线 `---`**，紧接着 **固定标题** `### P2 导出审计区`（供 P2 脚本解析）。  
- **线以上**：可作对外 **产品说明书**（无内网 IP、私密 `session_id`、未脱敏路径真值等）。  
- **线以下**：**内阁私密配置**（IP、库路径、`session_id` 与群映射等）。**P2** 从 SSOT 生成对外包时 **物理裁剪**：只保留线 **之上**（实现以工具代码为准）。  
- **全覆盖**：每个 **Standard** 文档 **均须预留** 该区；暂无敏感项时可留空表或写「暂无」。

### 5.4 运行时降级说明（强制）

- **Obsidian 笔记为静态展示面**，**不**自执行 `cabinet.*`；执行发生在 **适配器 / Dify 代码节点 / `skill_manager` / `dispatch_builtin`**。  
- **须含小节「运行时降级说明」**：当网关或内置调用失败时，须 **非阻塞**；保障统帅侧 **L0 RAW**（多源对话落盘）不因单次失败而 **静默丢失**（如法典约定的错误日志、重试、人工补录入口等）。  
- **日志路径**以法典为准，例如 [[多源对话收件法典]] 约定之 `RUNTIME_ROOT/ai_dialogue_inbox/sync_errors.log`；**禁止** 将 vault 内不存在的路径写为权威 SSOT。

### 5.5 Mermaid 图示（强制）

每个 **Standard** 应用域主文档 **必须** 包含 **「图示（Mermaid）」** 小节（或标题等价、位置明确的同级小节），**禁止** 仅有纯文字叙事而无 **任何** Mermaid 图。

**推荐位置**：该小节宜放在 **§5.3「P2 导出审计区」锚点（`### P2 导出审计区`）之前**，作为正文 **末段集中图示区**，使 P2 裁剪时图示仍属 **线以上**；**勿** 将整块 Mermaid 放在审计区标题 **之下**，以免与内阁私密配置混排或破坏导出边界。

**最低要求**（可按域增删，但不得少于下列意图的覆盖）：

1. **数据流或架构**：至少一张图表达 **主路径**（例如：外部入口 → 适配器/网关 → `cabinet.*` → RUNTIME 或下游）。  
2. **与三位一体一致**：至少一张图体现 **脑 / 手套 / 手** 的关系，或与 **§5.2 能力对照表** 可互证。  
3. **可选**：错误/降级旁路、与 L0/L1 炼化衔接（若该域相关）。

**写法约束**：

- 使用围栏代码块：\`\`\`mermaid … \`\`\`。  
- **节点 ID** 使用英文字母/数字/下划线，**避免** 空格与 Mermaid 保留冲突；中文说明放在 **方括号标签** 内。  
- **子图** `subgraph` 的 ID 建议英文，label 可用中文。  
- **真值**：参数、路径、键名以 **正文表格、法典与 JSON** 为准；图仅用于 **对齐认知**，与正文冲突时 **以正文+法典为准**。

### 5.6 配套 Obsidian Canvas（强制）

每个 **Standard** 应用域主 Skill 笔记旁 **必须** 新增或维护 **一张配套 `.canvas` 文件**，与主文档 **成对** 交付。

| 项 | 约定 |
|----|------|
| **位置** | 与主 Skill **同一子目录**（如 `Skills/01_…/`）。 |
| **命名** | 与主 Markdown **主文件名 stem 一致**，扩展名为 **`.canvas`**。例：`多Agent企微讨论_应用域Skill.md` ↔ `多Agent企微讨论_应用域Skill.canvas`。 |
| **格式** | Obsidian Canvas **JSON**（`nodes` + `edges`）；节点类型以 `text` 为主，正文内用 **wikilink** 指向主 Skill、相关法典、[[L1_DIFY_CABINET_TOOLS]]、`[[Skills/README]]` 等。 |
| **职责** | **鸟瞰与 onboarding**；不承载未在正文出现的秘密真值（私密细节仍在 **§5.3 审计区**）。 |
| **与 Mermaid 关系** | Canvas **不替代** §5.5：二者应 **同构互补**（Canvas 便于拖拽总览，Mermaid 便于在 Git/评审中 diff）。 |
| **治理参考** | 全局 Canvas 约定见库内 **[[AI-OB Canvas 规范]]**（`Manuals/AI-OB Canvas 规范.canvas`）；配色与节点风格宜与之协调。 |

**README 登记**：`Skills/README.md` **分区 A** 表格须含 **Canvas** 列，每条 Standard 应用域 **wikilink** 至对应 `.canvas`；暂无则填「待补」。

**P2 提示**：`cc_skill_packager` 以 Markdown 裁剪为主时，**默认可不收录** `.canvas`；若对外交付需要图解，须在 manifest 中 **单独声明** 附件策略（本规范 P1 仅要求 vault 内成对存在）。

---

## 6. `Skills/README.md` 与目录成熟度

### 6.1 身份类别

| 类别 | 典型位置 | 含义 | 与 packager |
|------|-----------|------|-------------|
| **Standard** | `Skills/01_…`、`02_…` | 双轨 + §5 强制结构（含 **§5.5 Mermaid**、**§5.6 Canvas**） | 仅 **User-Level** 可候选 |
| **Legacy** | `Skills/` 根下历史 `.md`（**保留原名**） | 规则 / 治理参考 | **System-Only**，默认不打包 |
| **Draft** | 规划占位 | 仅标题与成熟度 | **System-Only** 或 **Exclude** |

### 6.2 索引与双链

- `Skills/README.md` 须含 **能力成熟度矩阵**（列含 **Auth** 等），见该文件。  
- **分区 A** 须含 **Canvas** 列，与 **§5.6** 成对登记 Standard 应用域的 `.canvas`。  
- **严禁** 仅为整理而 **重命名** 已有 `.md`/`.canvas`，以免破坏 Obsidian **双链**；身份靠 **README 矩阵 + 分区** 区分；若改名须 **同步** 更新双链与 README。

### 6.3 Auth（摘要）

| Auth | 含义 |
|------|------|
| **User-Level** | 经封装层可调用的能力叙事；可对外包候选（仍须人工审核与脱敏）。 |
| **System-Only** | 统帅手动或系统自查；**禁止** packager **默认** 外发。 |
| **Exclude** | 明确不参与外向导出。 |

**`cc_skill_packager`（P2）** 须以 README 中的 **成熟度 + Auth** 与 **§5.3 审计区边界** 为硬闸门。
