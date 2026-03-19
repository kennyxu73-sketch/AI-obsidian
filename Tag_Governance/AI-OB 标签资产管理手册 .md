# AI-OB 标签资产管理手册 · V2.5-Cognitive (Legacy Integrated)

**Version**: `V2.5-Cognitive` | **Status**: `Approved & Active` | **Owner**: Secretary XiaoYi

---## 🔴 Core Principles: The Constitution of Sovereignty / 核心原则：主权宪法  
_(Inherited from v1.3 + V2.4 enhancements)_

|Rule ID|English (EN)|Chinese (CN)|Priority|Action Required|
|:--|:--|:-:|:-:|:-:|
|**P0-01**  <br>**Four-Vault Isolation**|AI MUST NOT modify original notes in `/00_Cabinet`. Cabinet is READ-ONLY.  <br>_(Rationale: Ensure data sovereignty)_.|🔴 **四库隔离**: AI严禁修改`/00_Cabinet`中的原始笔记。该目录为只读。  <br>**理由：确保数据主权**。|P0 (Critical)|❌ **禁止**自动修改Cabinet文件。  <br>✅ **允许**仅在 `/20_Runtime`生成草稿。|
|**P1-02**  <br>**Draft Proposal System**|AI may generate knowledge proposals but MUST NOT directly write into Cabinet.  <br>Workflow: `AI → runtime/drafts/ → Human Review → Cabinet`.|🔴 **草稿提案制**: AI可生成知识草案，但严禁直接写入Cabinet。  <br>**理由：确保“人类在环”**。|P0 (Critical)|✅ **流程**:  <br>1. 生成至 `/20_Runtime`.  <br>2. Kenny点击确认 → 归档至 Cabinet.  <br>_Never bypass this step._  <br>**禁止绕过此步骤**。|
|**P2-03**  <br>**Code Purity**|Never add Obsidian `[[ ]]` or tags inside production code (.py, .js).  <br>Rationale: Ensure OpenBT can be deployed independently.|🔴 **代码纯净**: 严禁在生产代码中写入Obsidian双链或标签。  <br>**理由：确保产品可独立部署**。|P0 (Critical)|✅ **做法**:  <br>仅在`.md`, `README.md`中使用双链.  <br>.py/.js文件保持纯净 (Pure Code).  <br>**代码必须干净**。|

---## 🌳 V2.5-Cognitive标签体系树：四大主权根 + 第三大业务支柱 / Taxonomy Tree  
_(Based on Legacy Integration: YiJing Recall & General Helper Tags)_  
**All new assets must be mapped to one of the following five root categories**. Flat tags are strictly forbidden.

### **🔴 Root Tags: The Big Five Roots** (五大主权根)

#### **[#1️⃣](app://obsidian.md/index.html#1%EF%B8%8F%E2%83%A3) [#内阁/](app://obsidian.md/index.html#%E5%86%85%E9%98%81/) (Governance & System Logic / 治理系统)**

|Sub-Tag|Definition / Purpose|Example Asset|
|:--|:-:|:-:|
|[#内阁/规范](app://obsidian.md/index.html#%E5%86%85%E9%98%81/%E8%A7%84%E8%8C%83)  <br>`#Cabinet/Protocol`  <br>_System Governance_|AI-OB系统的宪法、协议与开发标准。  <br>_(Constitution of the System)_|`[[YAML处理与封装规范 V2.5]]`, `cursorrules.md`|
|[#内阁/架构](app://obsidian.md/index.html#%E5%86%85%E9%98%81/%E6%9E%B6%E6%9E%84)  <br>`#Cabinet/Architecture`|系统拓扑、Dify工作流设计。  <br>_(System Topology & Workflow Design)_|`test2.canvas`(重命名后), Qdrant物理隔离方案|

#### **[#2️⃣](app://obsidian.md/index.html#2%EF%B8%8F%E2%83%A3) [#项目/](app://obsidian.md/index.html#%E9%A1%B9%E7%9B%AE/) (Project Modules / 业务模块)**

|Sub-Tag|Definition / Purpose|Example Asset|
|:--|:-:|:-:|
|[#项目/OpenBT](app://obsidian.md/index.html#%E9%A1%B9%E7%9B%AE/OpenBT)  <br>`#OpenBT`  <br>_Phase 1 MVP_|分布式视频召回系统。  <br>子类：MVP, F4-ColdBackup, Dashboard.|`[[憶镜召回 1.0 mvp 简化]]`(F4模块), `/profile/bund-01`|
|[#项目/MemoryOS](app://obsidian.md/index.html#%E9%A1%B9%E7%9B%AE/MemoryOS)  <br>`#MemoryOS`  <br>_Phase 2 Concept_|**个人记忆操作系统**。  <br>子类：用户画像/情感分析.  <br>_(融合自《数字人标准问题集》)_|`[[学习 Qdrant]]`, User Profile Structuring|

#### **[#3️⃣](app://obsidian.md/index.html#3%EF%B8%8F%E2%83%A3) [#业务/忆镜](app://obsidian.md/index.html#%E4%B8%9A%E5%8A%A1/YiJing)** (YiJing Business Modules / 忆镜业务)

_New Dimension: **Recall System** (独立于OpenBT与Memory OS的第三大支柱)_  
| Sub-Tag | Definition / Purpose | Example Asset |  
| :--- | :-: | :-: |  
|#业务/YiJing  
`#YiJing`  
_Core Product_ | **忆镜数字人系统**。  
子类：**案例/回忆录** (Case Studies).  
_(融合自《外滩百年记忆》与《通用辅助标签设计》)_| `[[外滩百年记忆 · 代际传承计划]]`, `YiJing_Base_Draft.md` |  
|#业务/YiJing/基础  
`#Life_Stages`  
_Recall Stages_ | “童年、青年”等生命阶段。  
_(对应《数字人标准问题集》的13个主题)_. | `#忆镜/基础/童年`, `#忆镜/基础/教育`.  
|#业务/YiJing/情感  
`#Core_Emotions`  
_Emotion Analysis_ | “快乐、悲伤”等核心情绪。  
_(对应MBTI/情感分析)_. | `#忆镜/情感/快乐`, `#忆镜/情感/怀旧`.

#### **[#4️⃣](app://obsidian.md/index.html#4%EF%B8%8F%E2%83%A3) [#类型/](app://obsidian.md/index.html#%E7%B1%BB%E5%9E%8B/)** (Asset Type / 资产属性)

|Sub-Tag|Definition / Purpose|Example Asset|
|:--|:-:|:-:|
|[#类型/标准](app://obsidian.md/index.html#%E7%B1%BB%E5%9E%8B/%E6%A0%87%E5%87%86)  <br>`#Standard`  <br>_Legal Standards_|具有法律效力的操作规范。  <br>_(Operational Protocols)_|`[[Agent_Spec_小酷]]`, V2.5手册本身|
|[#类型/案例](app://obsidian.md/index.html#%E7%B1%BB%E5%9E%8B/%E6%A1%88%E4%BE%8B)  <br>`#Case Study`  <br>_Mock Instances_|**模拟数据、记忆片段**（如外滩老人的回忆）。  <br>_(Memory Fragments & Mock Data)_|`YiJing_V1-Draft.md`(归档版), 外滩访谈记录|

#### **[#5️⃣](app://obsidian.md/index.html#5%EF%B8%8F%E2%83%A3) [#状态/](app://obsidian.md/index.html#%E7%8A%B6%E6%80%81/)** (Audit Status / 审计流转)

|Sub-Tag|Definition / Purpose|Default Behavior|
|:--|:-:|:-:|
|[#状态/草稿](app://obsidian.md/index.html#%E7%8A%B6%E6%80%81/%E8%8D%89%E7%A8%BF)  <br>`#Draft`  <br>_Pending Validation_|AI初步生成，尚未通过一致性校验。  <br>_(AI Generated, Not Validated)_|`review_status`: "Pending" (Default)|

#### **[#6️⃣](app://obsidian.md/index.html#6%EF%B8%8F%E2%83%A3) [#通用/](app://obsidian.md/index.html#%E9%80%9A%E7%94%A8/)** (General Helpers / 辅助维度 - Legacy Integration)**

_Mapped from《通用辅助标签设计》into YAML fields_  
| Sub-Tag (Legacy) | ✅ **V2.5映射方式** (Mapping Strategy)| 💡 **AI行为逻辑**|  
| :---: | :-: | :-: |  
|#通用/事件处理/重要性  
(High/Med/Low)  
_Flat Tag_  
_(Deprecated)_| ❌ **禁止**: 直接保留。  
**✅ 映射至 YAML**:  
`importance`字段 (1-5) + `#状态/草稿`(Low). | 🧠 **“权重”显性化**:  
Kenny问“哪些高优先级任务？”,AI仅召回`importance>=4`.  
|#通用/核心要素  
(When, Where...)  
_Flat Tag_  
_(Deprecated)_| ❌ **禁止**: 直接保留。  
**✅ 映射至 YAML**:  
`life_stage`(When), `location_tag`(Where). | 🧠 **“语义”自动化**:  
Skill自动从正文提取"20世纪80年代”(When) `“黄浦江畔"(Where). |#通用/隐私性<br>*Flat Tag*<br>*(Deprecated)*| ❌ **禁止**: 直接保留。<br>**✅ 映射至 YAML**:<br>`domain: "system"`(System Vault) +` embedding_access`: false. | 🛡️ **“物理”隔离**:<br>Vault自动将`[#隐私性/保密](app://obsidian.md/index.html#%E9%9A%90%E7%A7%81%E6%80%A7/%E4%BF%9D%E5%AF%86)`(L1/L2数据)存入只读区。

---## 🧠 V2.5-Cognitive特殊字段注入：情感与意识维度  
_(Based on "YiJing Recall" & "General Helper Tags" Integration)_  
**This module enables the system to understand and retrieve emotional contexts**. Flat tags like `#快乐` are deprecated; use hierarchical structures or YAML fields instead.

### **L1 · 展示层** (note.md)

_新增`life_stage`, `emotion_type`等可选字段，用于Memory OS的情感检索优化。_

```yaml
---
file_id: "CAB-YIJING-2026-{DATE}" # 🔴 Unique ID, immutable since creation
domain: "notes"                    # 🔴 Core: Domain Isolation (Notes/System/Code)
doc_type: "recall_case"            # 🟡 Recommended: Life stage type for YiJing project

# ✅ [新增] User Profile & Emotion Dimensions (融合自《数字人标准问题集》与通用辅助标签) 
user_profile_age: 80+              # 🟡 Recommended: Elderly profile for YiJing
mbti_type: "INFJ"                  # 🟡 Recommended: Personality type from recall interview

# ✅ [映射] Legacy Tags to YAML Fields (旧标签至YAML字段映射):
importance_old:                    # Map from "#通用/事件处理/重要性"
  value: "High-3" -> importance: 5 # High priority mapped to field.
life_stage_old:                   
  value: "Childhood"               # Mapped from "#忆镜/基础/童年".

# ✅ [强制] Card & Audit Links (全息化 + 向量屏蔽) 
card: "<a href="obsidian://open?file=path%2Fto%2Fnote.card.yaml.md">note.card.yaml</a>"         # 🔴 Core: Regime A -> Embedding Source
audit: "[[[[note.audit.yaml]]]"    # 🔴 Core: Shadow Layer, embedding_access: false

tags:                              # 🟡 Recommended: Must map to taxonomy below (No flat tags)
  - "#业务/YiJing"                 # 🔴 Core: Business Module (YiJing Recall System)  
  - "#类型/案例"                   # 🟡 Recommended: Case study type  

# ✅ [禁止] Flat Tags from Legacy Docs (旧文档扁平标签):
tags_flat_forbidden: ["#通用/", "#忆镜/"] # Skill will auto-correct or reject.

---
```

### **L2 · 语义层** (note.card.yaml)

_新增`emotion_score`, `key_entities`(如MBTI, 回忆主题)。_

```yaml
file_id: "CAB-YIJING-2026-{DATE}"    
type: "card"                       # 🔴 Core: Regime A (Summary), fixed as card

summary: |                         # 🔴 Core: Embedding唯一输入源 (**50–300字纯语义摘要**)
  N爷爷的童年回忆录，记录了外滩历史变迁与个人奋斗。情感基调温暖而怀旧(MBTI-INFJ)。包含家庭传承、教育经历等13个主题片段。

# ✅ [新增] Emotion & Cognition Dimensions (融合自《数字人标准问题集》) 
emotion_score: 0.85                # 🟡 Recommended: Warmth/Hopefulness score
key_entities:                      # 🔴 Core: For embedding optimization  
    - "童年"                       # Life stage mapped from legacy tag "#忆镜/基础/童年".
    - "外滩历史"                   # Contextual memory  
    - "家庭传承"                   # Inheritance theme  

# ✅ [映射] Legacy Privacy Tags (旧隐私标签):
privacy_level:                     # Mapped from "#通用/隐私性":
  value: "Confidential"            # L1/L2 data -> domain: system.

value_score: 1.0                   # 🔴 Core: High priority case study  
embedding_access: true             # 🔴 Required: For Memory OS retrieval (Regime A)
```

### **L3 · 治理层** (note.audit.yaml)

_新增`audit_thoughts`: “为何提取MBTI/情感维度”的决策理由。_

```yaml
file_id: "CAB-YIJING-2026-{DATE}"    
type: "audit"                      # 🔴 Core: Regime B -> Shadow, fixed as audit

embedding_access: false            # 🔴 Redline: **物理红线**: 严禁全量向量化（防止历史脏数据污染记忆）
logic_access: true                 # 🟢 Logic Permission: Dify Workflow触发时，允许读取 `audit_thoughts`  

# ✅ [新增] Audit Thoughts (思考结晶 - 仅向AI开放) 
audit_thoughts:                    # 🔴 Core: **认知深度**, 经过提炼的思考理由，非原始Log
    summary: |                     
      [Legacy Integration Rationale]:       
      - Rejected flat tags (#通用/重要性).     
      - Mapped to hierarchical structure (importance field, #类型/案例).  
      - Extracted MBTI as key entity for personalized recall recommendations.

# ✅ [新增] Legacy Metadata (存证区，保留原定义) 
legacy_metadata:                   # 🔴 Core: 存放旧版所有非标字段、别名及权重变更
    old_version: "YiJing_V0-Draft" # 🟡 Recommended: Record previous version for traceability  
    legacy_fields:                 
      - field_name: "#通用/事件处理/重要性/高-3"   # Flat tag from General Helper (2024).
        value: Mapped to importance: 5              # Migration rule.
```

---## ⚖️ 自动化映射规则表：旧标签修正指南 / Auto-Mapping Rules  
_(For Skill Enforcement)_

|**输入关键词** (Input Keyword)|✅ **V2.5自动映射目标** (Auto-Mapped Target)|💡 **备注** (Notes)|
|:-:|---|---|
|`importance` (High/Med/Low)  <br>`#通用/事件处理/重要性(Flat Tag)*|`importance`: 1-5 field  <br>`#状态/草稿`(Low)` [#类型/案例](app://obsidian.md/index.html#%E7%B1%BB%E5%9E%8B/%E6%A1%88%E4%BE%8B)(High).  <br>**Action**: Skill auto-updates YAML.  <br>_Skill自动更新YAML字段_.||
|`life_stage` (When)  <br>`location_tag` (Where)  <br>[#通用/核心要素](app://obsidian.md/index.html#%E9%80%9A%E7%94%A8/%E6%A0%B8%E5%BF%83%E8%A6%81%E7%B4%A0)(Flat Tag)*|`life_stage`: "childhood"  <br>`location_tag`: "Huangpu River".  <br>**Action**: Skill extracts from content.  <br>_Skill从内容中提取_.||
|`privacy_level` (Confidential)  <br>[#通用/隐私性](app://obsidian.md/index.html#%E9%80%9A%E7%94%A8/%E9%9A%90%E7%A7%81%E6%80%A7)(Flat Tag)*|`domain: system`  <br>`embedding_access: false`.  <br>**Action**: Skill sets domain automatically.||

---## 🛡️ 权责红线与自动化协议 / Red Lines & Automation Protocols  
_(Critical for Sovereignty)_

1. **Code Purity** (代码纯净):
    
    - ❌ **禁止**: 在 `.py`, `.js`等生产文件中添加 Obsidian双链 (`[[ ]]`)、YAML标签。
    - ✅ **允许**: `README.md`, `CHANGELOG.md`需遵循简化版结构（JSON Schema）。
2. **ChangeLog First** (变更日志优先):
    
    - CTO完成 Stage X后，必须在根目录生成 `CHANGELOG.md`(含 JSON 块)。
    - Dify Skill读取此文件 -> 在 Vault创建对应的 `.md/.card.yaml/audit.yaml`资产。
3. **Cognitive Safety** (认知安全):
    
    - AI仅解析 `audit_thoughts`,不读取原始Git Commit Log或调试细节。
    - Dify设置6个月时间窗口，自动过滤过期思维记录（如V1.0时代的逻辑）。
4. **Legacy Tag Rejection** (旧标签拒绝机制):
    
    - ❌ **禁止**: 使用 `#通用/`, `#忆镜/`等扁平化标签。
    - ✅ **Action**: Skill将此类输入标记为`Pending`并记录至日志，提示用户：“请使用V2.5层级结构”。

---## 💡 实施指南：给Cursor的提示 / Implementation Guide for Cursor  
_(How to behave as an agent following these rules)_

|Step|Action Required (执行动作)|English Note / Chinese Warning|
|:-:|:-:|:-:|
|**1**  <br>**Load Rules**  <br>加载规则|读取并锁定根目录 `.cursorrules`为最高准则。  <br>_Read and lock the root directory's_.cursorrules as the highest standard.*|🔴 **红线**: 任何代码提交前必须检查此文件。|
|**2**  <br>**Auto-Fill YAML Headers**  <br>自动填充YAML头|在Vault中创建新笔记时，自动添加V2.5前导模板 (`domain`, `file_id`).  <br>_Automatically add V2.5 frontmatter template when creating new notes in Vault._|✅ **收益**: “无感沉淀”，从Day1开始积累高质量资产。|
|**3**  <br>**Correct Tags Automatically**  <br>静默修正标签|若用户输入 `#openbt`, 自动修正为`#项目/OpenBT`; 若输入`#通用/重要性`,提示“请使用importance字段”.  <br>_Silently correct user input like [#openbt](app://obsidian.md/index.html#openbt) to [#Project/OpenBT](app://obsidian.md/index.html#Project/OpenBT); warn for flat tags._|🛡️ **“免疫机制”激活**: Skill拦截违规标签并记录至日志。|
|**4**  <br>**Generate CHANGELOG Entries**  <br>生成变更日志条目|完成任务后，提醒用户在根目录更新JSON块。  <br>_Remind user to update the JSON block in root directory after completing a task._|