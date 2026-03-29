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
> **真源**：可执行能力以 `Internal_Cabinet_Tools/cabinet_builtins.py` 与 `config/agent_l1_registry.json` 为准；本规范 **不**替代代码与 registry。

---

## 0. 阶段规划（P1 / P2）

| 阶段 | 范围 | 说明 |
|------|------|------|
| **P1（当前 AI-OB）** | **系统记录与储备** | 落地本规范、维护 **`Skills/`（或 `内阁应用域_Skills/`）** 下应用域叙事与索引；**不**实现 Claude Code 导出流水线、**不**强制维护 `cc_skills` 产物目录。 |
| **P2** | **外向导出与工具化** | 开发 manifest + 封装工具（如 `cc_skill_packager`），从 SSOT **裁剪脱敏** 生成 `Skills/cc_skills/<skill_id>/SKILL.md`；与对外发布、CHANGELOG/ref_id 配对。 |

P1 期间可在正文写作中 **习惯区分「可对外 / 仅内网」** 段落，为 P2 裁剪做准备；**无需**上自动化。

---

## 1. 术语

| 术语 | 含义 |
|------|------|
| **实现型 Skill** | `cabinet.<模块>.<动作>`，经 `skill_manager` / `dispatch_builtin` 执行，返回结构化结果。 |
| **应用域 Skill** | 以 **人类可理解的应用/系统名** 组织的 **叙事与目录**（可与 Claude Code `SKILL.md` 风格兼容），每条 **映射** 到实现键、Dify、Runbook、插件。 |
| **双轨** | 同一能力：**应用名** 沟通；**`cabinet.*`** 执行与审计。 |
| **cc_skills（P2）** | 计划中的子目录：仅放 **可对外** 的 Claude Code 规范包；P1 **仅在本规范中保留名称与意图**，目录可空或不建。 |

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

**示例子目录（6～8 个域）**：
