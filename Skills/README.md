---
title: 内阁 · Skills 能力地图
role: SSOT · 应用域索引
status: active
updated: 2026-03-30
---

# 内阁 · Skills 能力地图

> **本目录**（`000_Cabinet_System/Skills/`）是 **内阁 AI-OB 应用域与能力叙事**，**不等于** Cursor / VS Code 全局目录 `.cursor/skills`。后者由编辑器生态管理；此处为 **Obsidian SSOT** 与人的「系统在干什么」索引。

**母规范**：[[Infrastructure/AI-OB Skills 应用规范]]。

**P2 预留**：计划中的 `Skills/cc_skills/` 仅放 **可对外** 的 Claude Code 规范包；**P1 不建该目录**。封装工具 **`cc_skill_packager`（P2）** 必须以本页 **成熟度 + 权限等级 (Auth)** 与规范 **§5.3 P2 导出审计区** 为 **硬闸门**：**仅 Standard + User-Level** 可进入默认外发包；**System-Only / Legacy / Draft** 为 **禁区**。

**Canvas 与 Mermaid**：每个 **Standard 应用域** 须满足母规范 **§5.5（Mermaid）**、**§5.6（Canvas）**：主 Skill 内含 **「图示（Mermaid）」** 小节；同目录 **同名 stem 的 `.canvas`**，双链回主文档与法典；**真值以 Markdown + 法典 + JSON 为准**。

---

## 能力成熟度矩阵

| 类别 | 命名 / 位置约定 | 说明 | 示例 | 权限等级 (Auth) |
|------|-----------------|------|------|-----------------|
| **Standard（应用域）** | `01_…`、`02_…` 子目录 | 双轨叙事 + **能力对照表** + **P2 导出审计区** + **运行时降级**（见规范 §5） | `01_多Agent企微讨论/` | **User-Level**（Agent 经 Dify / skill_manager / 适配器调用；外发须再审核脱敏） |
| **Legacy（遗留 / 治理）** | `Skills/` **根目录**既有 `.md`，**禁止为整理而改名** | 规则、进度、治理说明；**非**完整 cabinet 编排应用域 | `开发进度控制 Skill.md`、`AI-OB · 项目管理体系.md` | **System-Only**（仅供统帅手动或系统自查；**禁止** packager 默认外发） |
| **Draft（规划占位）** | `_draft_` 或待建 `09_…` 等 | 仅有标题与成熟度标记，未定稿 | （P1 可仅占位行） | **System-Only** 或 **Exclude** |

---

## 分区 A · 标准应用域（能力叙事）

| 编号 | 域 | 主文档 | Canvas | 状态 |
|------|----|--------|--------|------|
| 01 | 多 Agent 企微讨论 / 会话编排 | [[01_多Agent企微讨论/多Agent企微讨论_应用域Skill]] | [[01_多Agent企微讨论/多Agent企微讨论_应用域Skill.canvas]] | 已填 |
| 02 | 统帅画像 · Tier C 与 Inbox DSL | [[02_用户画像运维/用户画像运维]] | [[02_用户画像运维/用户画像运维.canvas]] | 已填 |
| 03 | 内阁封印 · 档案与补丁双径 | （待补） | （待补） | 待补 |

---

## 分区 B · 系统治理与历史文档（Legacy）

与 **分区 A** 的边界：**B** 侧重 **规则、流程、项目管理**，**不**要求 §5 全套结构；**不**作为 `cc_skill_packager` 默认输入。

| 文档 | 说明 |
|------|------|
| [[开发进度控制 Skill]] | 历史 / 治理向 Skill 叙事 |
| [[AI-OB · 项目管理体系]] | 项目与协作治理 |

---

## 双链与改名禁令

- **严禁** 仅为目录整洁 **重命名** 已有笔记，以免 Obsidian **双链断裂**。  
- 新增身份通过 **本 README 矩阵 + 分区** 标注即可。
