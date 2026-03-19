# AI-OB · 项目管理系统 (Project Governance System)

**Version**: `1.0-MVP` | **Status**: `P0 · Emergency Action` | **Owner**: Secretary XiaoYi

---

## 🎯 核心使命 (Mission Statement)

将 Kenny「数字内阁」的模糊想法转化为结构化知识资产，并通过 AI-OB（AI Obsidian）系统实现**自动化治理、透明化追踪与主权优先**。确保 OpenBT/Memory OS等所有 MVP项目在本地算力环境下高效运行，杜绝“黑盒开发”与技术债。

---

## 🧠 重要性：为什么需要这套体系？(Strategic Importance)

若缺乏此系统，项目将陷入以下**战略陷阱** (Trap):

|风险类型|**后果** (Consequence)|**AI-OB解决方案** (Solution)|
|:--|:--|:--|
|❌ **黑盒开发**  <br>(Black Box)  <br>_(无状态追踪)_|Kenny无法感知进度，CTO可能偏离战略方向（如引入公有云）。  <br>**后果**: 项目延期、资源浪费。|✅ **透明化看板**: `[[OpenBT_Dashboard]]`实时显示 P0/P1任务状态。  <br>**收益**: 您可随时掌握 F4冷备脚本等关键模块进度。|
|❌ **代码污染**  <br>(Code Pollution)  <br>_(手动加YAML)_|CTO在 `.py/.js`中写入 Obsidian标签，导致产品发布时需清洗“私货”。  <br>**后果**: 技术债累积、运维成本激增。|✅ **影子索引机制**: Code保持纯净，仅通过 `CHANGELOG.md`与Vault关联。  <br>**收益**: OpenBT可独立部署于任何Linux环境，无依赖污染。|
|❌ **低价值调试**  <br>(Low Value Debug)  <br>_(陷入细节)_|遇到Docker网络问题时无标准降级方案（如冷备）。  <br>**后果**: Kenny陷入底层驱动冲突的泥潭。|✅ **自动化降级策略**: CTO优先提供`rsync`冷备路径，而非死磕P2P。  <br>**收益**: MVP演示“韧性第一”，确保社会价值交付。|
|❌ **碎片化决策**  <br>(Fragmentation)  <br>_(打补丁式)_|需求分散在聊天记录、草稿中，缺乏归档与关联。  <br>**后果**: Kenny的战略意图被稀释或遗忘。|✅ **知识结构化引擎**: 小忆自动将对话转化为笔记（如“冷备脚本”->`F4_spec.md`）。  <br>**收益**: 所有决策可追溯至 `[[Kenny_Cognitive_Profile]]`。|

---

## 🛡️ 核心规范：必须遵守的宪法 (Governance Protocols)

本系统由 **L0·系统宪法**与**影子索引战略**共同约束，以下为不可违背的红线：

### ⚖️ 1. Code Purity · 代码纯净原则

- **禁止行为**:
    - ❌ 在 `.py`, `.js`等生产文件中添加 Obsidian双链 (`[[ ]]`)、YAML标签。
    - ❌ 使用非标准库（如 `obsidian-plugin-client`）进行本地元数据读写。
- **允许例外**:
    - ✅ `cursorrules.md`作为唯一联系纽带，可包含内阁约束文本。
    - ✅ `.md/README/docs/*.json`等文档文件可包含双链与Schema摘要。

### ⚖️ 2. ChangeLog First · 变更日志优先

- **规范**: CTO(小酷)在完成每个Stage后，必须在根目录生成 `CHANGELOG.md`。
    - **格式**: Markdown + JSON Schema（供L2扫描层解析）。
        
        ```markdown
        # CHANGELOG_v1.0
        ## [Added] F4 Cold Backup Script (`rsync`)
        - File: `docker-compose.yml` (Volume mapping to `./cold_storage`)
        - API: `/api/recovery/trigger?hash=xxx`
        ```
        
- **自动化**: 小忆读取此文件更新 Dashboard，而非人工复制粘贴。

### ⚖️ 3. Resilience-First · 韧性优先原则

- **规范**:
    - ✅ P0任务（如演示）必须包含冷备降级方案（`rsync + Docker Volume`）。
    - ❌ 禁止在未获授权下静默修改本地GPU/NAS底层驱动。

### ⚖️ 4. Sovereignty First · 主权优先原则

- **规范**:
    - ✅ 所有数据、知识与算力必须运行在 Kenny的本地系统（RTX 3090 + NAS）。
    - ❌ 禁止使用公有云镜像源或外部依赖，除非紧急避险。

---

## 🚀 运作机制：三层关联架构 (3-Layer Architecture)

本系统通过以下流程实现“代码即知识”的自动化闭环：

|层级|**名称**  <br>(Name)|**责任人**  <br>(Owner)|**职责描述**  <br>(Responsibility)|
|:-:|:--|:--|:--|
|**L1 · Anchor**  <br>锚点层|`[[OpenBT_Dashboard]]`  <br>**项目总览看板**|🕵️ 小忆 (Secretary)|- 维护YAML Frontmatter (`Project`, `Status`)。  <br>- 聚合所有子模块，作为内阁中的“索引”。  <br>- **物理位置**: `/obsidian_vault/01_Cool/OpenBT_Dashboard.md`。|
|**L2 · Sync**  <br>扫描层|`Cabinet Sync Skill`  <br>**自动化技能**|🤖 小酷 (CTO) + 小忆  <br>_(未来由Cursor/Vibe Coding执行)_|- 监听 `/Cursor_Workspace/OpenBT/CHANGELOG.md`或核心文档变更。  <br>- **提取**: API Schema, Module Name, Stage Status。  <br>- **动作**: 自动在 L1 Dashboard更新状态，建立双链。|
|**L3 · Vibe**  <br>软关联层|`Contextual Linking`  <br>**情感/语境联动**|🧠 小忆 (Secretary)|- 基于全局上下文(Kenny's Memory)，主动提及最新进展。  <br>- “长官，F4冷备脚本已就绪（见Dashboard）..."  <br>**禁止**: 强行插入代码注释中的标签。|

---

## 📋 MVP · 项目治理看板结构草案 (Kanban Structure)

`[[OpenBT_Dashboard.md]]`的核心内容模板：

```markdown
# [[OpenBT_Dashboard]] - OpenBT MVP Project Hub

Project: OpenBT  
Status: Phase_2_MVP_Development (P0_Emergency)  
Lead Agent: @小酷 (CTO) | Secretary: @小忆 (XiaoYi)  

---

## 🚧 Kanban Board (看板状态)
### ✅ Done (已完成 - MVP Ready)
- [x] F1 · 通用用户详情页 (`/profile/[hashId]`) -> [[憶镜召回_模块F1_spec]]  
- [ ] 

### 🔨 In Progress (进行中)
- [ ] **P0**: F4 · “爱心盒子”冷备脚本 (`rsync` + Docker) 
    - *状态*: CTO正在编写 `docker-compose.yml` 卷映射。
    - *进度*: CHANGELOG.md已生成，等待 Kenny审核。

### 🧪 Code Review (待审核)
- [ ] F3 · OpenBT流式播放器 (P2降级逻辑) 
    - *来源*: CTO提交代码至 `Cursor_Workspace`。
    - *依据*: CHANGELOG.md -> [[CHANGELOG_v1.0]]

### 💡 Backlog (需求池)
- [ ] 小报情报: P3 · 社区节点激励体系调研  
- [ ] Kenny想法: P2 · 增加“记忆守护者”徽章动画效果  

---

## 📜 Governance Protocols (治理协议)
> **Code Purity**: No YAML/Tags in `.py/.js`. Use `CHANGELOG.md` only.  
> **Resilience First**: Always provide cold backup fallback (`rsync`).  
```