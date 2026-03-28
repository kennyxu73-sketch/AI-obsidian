# 内阁 Agent · L1 Prompt 权威矩阵

> 与 `.cursorrules` **§ L1 · 画像与身份协议** 对齐：本表约定「对外默认引用哪一份」为 **L1 主入口**，与 Manuals 中 YAML「L1 展示层」术语无关。  
> **全局 Kenny 画像（条件读取）**：`小忆/Kenny画像/Kenny_Cognitive_Profile.md`（规范名；见 `.cursorrules`）。

**Dify / 编排可调用的 `cabinet.*`（按 `agent_slug` 白名单）**：见 [[L1_DIFY_CABINET_TOOLS]]；本库快照 [[agent_l1_registry.json]]（权威以 TOOLS `Internal_Cabinet_Tools/config/agent_l1_registry.json` 为准）；导出 [[dify_agent_tools_export.json]]。

## 维护规则

- 新 prompt 若意图**取代**某角色 L1 主入口，须经 Kenny 确认，并同步改本表 + [[AGENT_INDEX]]。
- 专项 / 历史文档不得冒充主入口；历史副本在表中标 **deprecated / 非 SSOT**。

## 矩阵

| 角色 | L1 主入口 | 专项 prompt / 能力 | 历史或非 SSOT | 与 Cursor L1 关系 |
|------|-----------|-------------------|---------------|-------------------|
| 小酷 | `小酷/小酷.md` | `小酷/AIOB-Core-Enseal-Skill cursor prompt.md`、专属口令、OpenBT/AI-OB 专项说明书 | `小酷/小酷 说明书.md`、`小酷/小酷工作背景介绍.md`、`小酷/小酷  - 技术内阁宪法.md` 等并列参考 | Cursor 默认 CTO 人格；工具链与 `.cursorrules` 对齐 |
| 小报 | `小报/小报.md` | `小报/小报 prompt.md`、联网脱敏规范、Cards 工作流 | 同上目录内流程文档为专项 | 多以外部/Dify 为主；Cursor 可引用主入口 |
| 小黑 | `小黑/小黑.md` | `小黑/小黑prompt.md`、`4g梳理/` 下脚本说明 | `小黑/小黑（XiaoHei）说明文档补充.md` | 分析轨；通常不当作对话主脑 |
| 小画 | `小画/小画.md` | `小画/ 文档转Canvas prompt.md`、Canvas JSON 规范、小画与数字内阁 | — | 可视化轨 |
| 小忆 | `小忆/小忆.md`（真库）；镜像仓库为 `小忆/小憶.md` | `小忆/小忆prompt.md`、`小忆 (XiaoYi) 系统提示词 .md`、议事守则、Obsidian 基建手册 | `小忆/Kenny画像/*` 为 **Kenny** 画像区（非小忆本体 prompt） | 秘书长；Kenny 画像路径见 `.cursorrules` |
| 小记 | `小记/小记.md` | — | — | Memory OS / 硬件枢纽；**≠ 小忆** |
| 小欧 | `小欧/小欧.md` | — | — | OpenBT / 数据资产顾问 |
| 小镜 | `小镜/小镜.md`（占位） | — | — | `prompt_status: TBD` |
| 小康 | `小康/小康.md`（占位） | — | — | `prompt_status: TBD` |
| 审计小酷（分身） | `审计 agents/审计小酷.md` | `审计 agents/审计小酷 Prompt.md`、`AIOB yaml 审计skill.md` | — | **非** 小酷本体；导师/审计轨 |

## agent_slug（wecom_adapter / 路由扫描）

各角色 **L1 主入口** 的 YAML `agent_slug` 须与本表一致：

| agent_slug | 角色 |
|------------|------|
| xiaoku | 小酷 |
| xiaobao | 小报 |
| xiaohei | 小黑 |
| xiaohua | 小画 |
| xiaoyi | 小忆 |
| xiaoji | 小记 |
| xiaoou | 小欧 |
| xiaojing | 小镜 |
| xiaokang | 小康 |
| audit_xiaoku | 审计小酷 |

详见各主入口文件 frontmatter。
