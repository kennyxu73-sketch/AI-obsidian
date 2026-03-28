# 内阁 Agent 目录索引

> **小记 ≠ 小忆**：小记 = Memory OS / 硬件与生态枢纽；小忆 = 秘书长 / 调度与 Kenny 画像治理。  
> **L1 prompt 权威矩阵**：见 [[AGENT_L1_PROMPTS]]。  
> **L2 任务向（示例）**：小忆 `小忆/小忆_L2_inbox_enseal_patch.md`（inbox→Patch 炼化编排）；设计文档 `Dify/01_Ingest_&_Memory/WF_InboxRefine_Patch.md`。

## 角色总表

| 角色 | agent_slug | 目录 | L1 主入口 | 主要职责 | 数字内阁 v2 层 | Aliases |
|------|------------|------|-----------|----------|----------------|---------|
| 小酷 | xiaoku | `小酷/` | `小酷/小酷.md` | CTO / 工具链 / 3090 / 安全 | 领域专家与执行层 | — |
| 小报 | xiaobao | `小报/` | `小报/小报.md` | 外部情报 / 脱敏 / 抓取 | 外部输入 | — |
| 小黑 | xiaohei | `小黑/` | `小黑/小黑.md` | 暗箱分析 / 结构化 / JSON | 内部分析层 | — |
| 小画 | xiaohua | `小画/` | `小画/小画.md` | Canvas / 可视化交互 | 交互与展示层 | — |
| 小忆 | xiaoyi | `小忆/` | `小忆/小忆.md` | 秘书长 / 调度 / 议事 | 交互与展示层 | 镜像仓库主文件名为 `小憶.md` |
| 小记 | xiaoji | `小记/` | `小记/小记.md` | Memory OS / 硬件架构 | 领域专家（扩展） | — |
| 小欧 | xiaoou | `小欧/` | `小欧/小欧.md` | OpenBT / 数据资产 / Web3 | 跨项目底座 | — |
| 小镜 | xiaojing | `小镜/` | `小镜/小镜.md` | 2C 回忆录 / 数字人（占位） | 领域专家 | `prompt_status: TBD` |
| 小康 | xiaokang | `小康/` | `小康/小康.md` | 2B 养老平台（占位） | 领域专家 | `prompt_status: TBD` |
| 审计小酷 | audit_xiaoku | `审计 agents/` | `审计 agents/审计小酷.md` | 审计分身 / 导师 | 治理轨 | — |

## 元文档区（方案 A）

跨角色规约与架构说明位于 **`数字内阁/`**：

| 文件 | 说明 |
|------|------|
| `数字内阁/数字内阁（Digital Cabinet）.md` | v2 架构总览 |
| `数字内阁/内阁 Agent 互访与议事规则.md` | 群聊与议事 |
| `数字内阁/Agent SOP(工作流协议) 配置方案.md` | 工作流 |
| `数字内阁/内阁-自由议事与安全执行方案.md` | 自由议事 V5（真库文件名；镜像侧为 `内阁自由议事与安全执行方案.md`） |
| `数字内阁/外部信息知识分级原则 (Instruction).md` | 外部分级（或小报目录下副本，以实际双链为准） |
| `数字内阁/AI-ob 数字内阁.canvas` | 画布 |
| `数字内阁/数字内阁sop.canvas` | 画布 |

入口笔记：本文件 `Agent/AGENT_INDEX.md`、矩阵 `Agent/AGENT_L1_PROMPTS.md`、**Dify/cabinet 工具 L1** [[L1_DIFY_CABINET_TOOLS]]（快照：`agent_l1_registry.json`、`dify_agent_tools_export.json`；以 TOOLS 内 JSON 为权威）。

## wecom_adapter 预埋（与企微策略 v1.1）

将来可由适配器扫描各 **L1 主入口** `.md` 的 YAML：`agent_slug`（必填）、可选 `routing` / `prompt_status`，生成企微侧路由表；具体会话键与 SSOT [[数字内阁-企微多Bot与会话策略]] 对齐。

---

## 与 Cursor_Workspace 镜像同步说明

- **已同步**（约 2026-03-29）：`agent_slug` / `l1_entry`、占位 `小镜` `小康`、本索引与 `AGENT_L1_PROMPTS.md`。  
- **真库差异**：小忆 L1 主入口文件名为 **`小忆.md`**；镜像 `Internal_Cabinet_Tools/000_Cabinet_System 1/Agent/小忆/` 使用 **`小憶.md`**。`.cursorrules` 仅约束目录名 `小忆/` 与 `Kenny画像/` 路径。  
- 画布 `AI-ob 数字内阁.canvas` 内链已指向 `小欧/小欧`、`小记/小记` 主入口。
