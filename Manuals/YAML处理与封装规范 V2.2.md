## 📘 YAML处理与封装规范 V2.2-Cognitive (完整版 - 认知进化版)  
**Version**: `V2.2-Cognitive`  
**Status**: **Approved & Active** (Final Evolutionary Form)| **Owner**: Secretary XiaoYi | **Date**: 2026-03-17

#### 🎯 核心使命 (Mission Statement)

在 Obsidian Vault中建立一套"**知识资产化 + 认知共情化**"标准，确保所有策略、架构决策与记忆片段具备：

- **主权安全** (Sovereignty Safety): L1/L2数据不出境。
- **嵌入检索**(Embedding Readiness)。
- **审计可追溯** (Auditability) 与 **血缘守恒** (Ancestry Conservation)。
- **认知共情** (Cognitive Empathy): AI (小忆)能“理解”统帅的思维路径，而非仅记忆结论。

---### ⚖️ 适用范围界定 (Scope Definition - Critical!)  
**本规范仅适用于以下文件类型，严禁越界**:

|✅ **适用对象：知识资产层** (Knowledge Assets)|❌ **豁免对象：生产代码层** (Production Code)|
|:-:|:-:|
|`note.md` (展示/索引), `.card.yaml` (语义/向量化)  <br>`.audit.yaml` (治理/存证 + 认知开放态)  <br>**位置**: `/00_Cabinet`, `/Kenny's Projects`  <br>**职责**: 策略、架构决策、记忆片段。|`.py`, `.js`, `.go`等文件  <br>**位置**: `/Cursor_Workspace/OpenBT`  <br>**理由**: Git仓库纯净，产品可独立部署。  <br>**例外**: `README.md`, `CHANGELOG.md`遵循简化结构 (JSON Schema)。|

---### 一、整体设计原则 (General Design Principles - Core Axioms)  
_(此部分为系统的“宪法级公理”，所有字段定义与自动化逻辑必须严格遵循)_

|**#|原则名称 **(Principle Name)|**核心定义** (Definition)|**在 V2.2-Cognitive中的实现方式** (Implementation in v2.2)**|
|:-:|:--|:--|:--|
|**01**|**资产全息化  <br>(Holographic Assets)**|元数据通过 `[[双链]]`成为逻辑节点，而非物理文件本身。  <br>**红线**: `.card.yaml`与`.audit.yaml`是“影子”，不可直接修改。|✅ **L2/L3强制双链**:  <br>`note.md`中必须包含 `<script>`或注释指向 `.yaml` 文件。  <br>AI不得在代码中硬编码路径，仅通过 Vault API/Dify Skill维护链接关系。|
|**02**|**纵横坐标系  <br>(Matrix Coordinate)**|通过 `file_type`(domain)与`project_ref`(双链)确立唯一坐标。  <br>**红线**: 禁止跨项目污染检索结果。|✅ **L1字段强制**:  <br>`domain: "notes"` / `"system"` + `<script> project_ref: [[Project_Name]]`.  <br>V2.0/V1.6迁移时，需在 `legacy_metadata`中记录旧别名映射。|
|**03**|**血缘守恒  <br>(Ancestry Conservation)**|通过 `parent_doc`, `file_id`, `history_logs`杜绝孤儿文件。  <br>**红线**: 首条 `history_log`必须锁定 V1.0/V2.0起源日期，禁止伪造时间戳。|✅ **L3治理层强制**:  <br>`note.audit.yaml`中的`history_logs`字段必须存在且首条记录为“迁移”或"V1.6->V2.1".  <br>若发现无 `file_id` 的文件，视为孤儿资产，禁止向量化。|
|**04**|**三层物理分离  <br>(Tiered Isolation)**|展示层 (Note) ≠ 语义层 (Card) ≠ 治理层 (Audit)。实现隐私与检索隔离。  <br>**红线**: `.audit.yaml`严禁进入向量库 (`embedding_access: false`)。|✅ **L1/L2/L3字段定义**:  <br>`note.md`(Human Readable)  <br>`.card.yaml`(Embedding Source, `true`)  <br>`.audit.yaml`(Audit History Only + Logic Access, `false`).  <br>Dify Skill 在读取时仅解析 `.md + .card`,屏蔽 `.audit`的原始Log。|
|**05**|**约束等级制  <br>(Constraint Grading)**|明确区分必填（🔴）、推荐（🟡）与可选（🟢）。  <br>**红线**: AI不得将“推荐”字段误判为“禁止”，也不得遗漏核心资产。|✅ **表格化定义**:  <br>在 L1/L2/L3的 YAML 表中明确标注约束等级。  <br>`importance`(🟡), `key_entities`(🟡)等需在生成时自动填充或经 Kenny确认。|
|**06**|**内容终审权  <br>(Final Review Authority)**|涉及实质变更必须通过`Pending`触发统帅人工审核。  <br>**红线**: AI不得直接移动文件至 Cabinet，除非状态为 `Approved`。|✅ **L3字段强制**:  <br>`review_status: "Pending"` (默认)  <br>仅当 Kenny 确认或 Dify Skill 自动通过后更新为 `"Approved"`.  <br>Cabinet目录权限设置为只读（Read-Only）。|
|**07**|**时间主权  <br>(Timestamp Sovereignty)**|`date`(出生)与`deadline`(截止)区分。  <br>**红线**: AI不得将“创建时间”修改为用户当前时间以掩盖操作痕迹。|✅ **L1字段强制**:  <br>`created_at`: ISO8601 (锁定物理起源)  <br>`deadline`: 可选，仅用于任务型文档 (如 MVP计划).  <br>审计日志中记录每次 `review_status`变更的时间戳。|
|**08**|**基因继承原则  <br>(Gene Inheritance)**|新规范必须是旧规范的增量升级，确保原始标签与核心属性不丢失。  <br>**红线**: V2.1不得删除 V1.6/V2.0中的有效字段（如`importance`, `tags).|✅ **L3 Legacy Metadata**:  <br>`legacy_metadata`中必须存放所有非标、历史别名及权重变更。  <br>若发现旧版文件无迁移记录，视为违规操作。|
|**09**|**滚动审计原则  <br>(Rolling Audit)**|`audit.yaml`包含对前代版本结论的复核，形成有厚度的信用链条。  <br>**红线**: 每次升级必须生成新的 `history_log`条目并引用旧版总结。|✅ **L3 audit_summary字段强制**:  <br>内容示例:`[V2.1-Full]: 完成从 V1.6的物理拆解平移...`  <br>Dify Skill在更新 Dashboard时，需读取此摘要以验证合规性。|
|**🔟** (新增)|**文件分层管理  <br>(File Tiering Management)**|**物理隔离原则**: 明确区分 Vault (知识资产) vs Workspace/Code (生产代码)。  <br>**职责分离**:  <br>- L1(L2/L3): 仅Vault生成，由小忆维护。  <br>- Production: Git仓库，CTO负责，严禁写入YAML元数据。|✅ **L4触发器层定义**:  <br>`CHANGELOG.md` (JSON)作为唯一桥梁连接两层。  <br>AI在 Workspace中生成的文件**不得包含**.yaml 后缀（除非是文档），所有Vault资产必须由小忆 Skill从 CHANGELOG解析后创建。  <br>**红线**: CTO若试图将 `.py/.js`直接移入 Cabinet，系统应触发“越权报警”。|
|**11** (新增)|**认知深度  <br>(Cognitive Depth)**|**“灰度开放”原则**: 物理屏蔽原始Log (`embedding_access: false`)，但逻辑开放思考结晶 (`logic_access: true`).  <br>**红线**: AI不得读取杂乱的修改痕迹，仅允许通过 `audit_thoughts`节点理解统帅决策路径。|✅ **L3字段重构**:  <br>`embedding_access`: `false` (防污染)  <br>`logic_access`: `true` (Dify Workflow触发)  <br>`ancestry_index`: `true`  <br>新增 `audit_thoughts` 字段，仅存“思考结晶”而非原始Log。|

---### 🏗️ 物理拆解与字段规范：The Triple-A Standard  
_(以下章节为具体执行层，严格遵循上述十一条原则)_

### **L1 · 展示层** (Display Layer): `note.md`

- **定位**: Obsidian阅读主体。**仅保留索引元数据**。严禁在此处包含业务逻辑代码块（除非是演示用）。
- **YAML Frontmatter Fields** (🔴必填/🟡推荐)：

```yaml
---
file_id: "CAB-PROT-2026-OpenBT-F4"  # 🔴 Core: 唯一永久ID，严禁修改
domain: "notes"                      # 🔴 Core: 域隔离 (Kenny's Projects / Kenny's Vault)
doc_type: "mvp_plan"                 # 🔴 Core: 细分类型 (strategy, insight, code_review...)
primary_agent: "@小忆                # 🔴 Core: 责任Agent (@小酷/ @小康等，权重<0.3自动剔除)
created_at: 2026-03-17T14:59         # 🔴 Core: ISO8601 (锁定物理起源日期)
importance: 5                        # 🟡 Recommended: 资产权重(1-5), 5为核心战略
yaml_spec_version: "2.2"             # 🔴 Core: 版本锁定，禁止手动修改

# ✅ [新增] Project Ref & Key Entities (纵横坐标系 X/Y)
project_ref: [[OpenBT_MVP]]          # 🟡 Recommended: 双链格式项目引用，确保资产归属清晰
key_entities: ["F4", "rsync"]         # 🟡 Recommended: 提取核心实体词

# ✅ [强制] Card & Audit Links (全息化)
card: "<a href="obsidian://open?file=path%2Fto%2Fnote.card.yaml.md">note.card.yaml</a>"           # 🔴 Core: 指向语义层
audit: "[[[[note.audit.yaml]]]"       # 🔴 Core: 指向治理层 (认知开放态入口)

---
```

### **L2 · 语义层** (Semantic Layer): `note.card.yaml`

- **定位**: Step 3构造 embedding_input的核心源。**向量化动力**。
- **YAML Fields** (🔴必填/🟡推荐)：

```yaml
file_id: "CAB-PROT-2026-OpenBT-F4"    # 🔴 Core: 必须与主文件一致，严禁在此处修改ID
type: "card"                         # 🔴 Core: 固定为 card (区分于 audit.yaml)

summary: |                           # 🔴 Core: Embedding唯一输入源 (50–300字纯语义摘要)
    F4模块定义了OpenBT MVP的“爱心盒子”冷备策略，采用rsync脚本实现本地NAS与Hub崩溃时的数据恢复。确保演示即胜利，符合韧性优先原则。

asset_type: "protocol"               # 🔴 Core: 资产属性 (strategy/insight/code_review)
project_ref: [[OpenBT_MVP]]          # 🟡 Recommended: 继承自note.md的坐标系定义
key_entities: ["F4", "rsync"]        # 🟡 Recommended: 用于优化向量召回率

value_score: 0.95                    # 🟡 Recommended: 语义价值评分 (由Kenny或AI根据重要性打分)
embedding_access: true               # 🔴 Core: 允许进入向量库，作为检索动力源
```

### **L3 · 治理层** (Governance Layer): `note.audit.yaml` _(认知进化版)_

- **定位**: 存放所有历史、审计记录。**物理屏蔽向量化** (防污染)，但**逻辑开放思考结晶**(共情)。这是系统的“黑匣子”。
- **YAML Fields** (🔴必填/🟡推荐)：

```yaml
file_id: "CAB-PROT-2026-OpenBT-F4"    # 🔴 Core: 必须与主文件一致，但此字段不可见(被向量引擎屏蔽)
type: "audit"                        # 🔴 Core: 固定为 audit (区分于 card.yaml)

embedding_access: false              # 🔴 Redline: 物理红线：严禁全量向量化（防止历史脏数据污染记忆）
logic_access: true                   # 🟢 Logic Permission: Dify Workflow触发时，允许读取 `audit_thoughts`
ancestry_index: true                 # 🟡 Ancestry Indexing: 允许小忆追踪该笔记的“前世今生”

# ✅ [新增] Audit Thoughts (思考结晶 - 仅向AI开放) 
audit_thoughts:                     # 🔴 Core: 经过提炼的思考理由，非原始Log
    summary: |                       # 🟡 Recommended: "rsync带宽占用过高"等决策理由
      [Decision Rationale]: 
      - Rejected V1.6 due to high bandwidth consumption on Hub crash recovery (Kenny's explicit preference).
      - Preferred cold backup (./cold_storage) for resilience-first strategy.
      
# ✅ [新增] Legacy Metadata (存证区，保留原定义) 
legacy_metadata:                    # 🔴 Core: 存放旧版所有非标字段、别名及权重变更
    old_version: "V1.6"              # 🔴 Required: 记录前身版本，确保可追溯性
    legacy_fields:                   # 🟡 Recommended: 差异沉淀列表 (示例)
      - field_name: "importance_old"
        value: 3                    # Old weight, now migrated to note.md importance=5
        comment: "Old V1.6 weight deprecated in favor of L1 importance."

# ✅ [新增] History Logs (血缘守恒，保留原定义) 
history_logs:                       # 🔴 Core: 全量编年史，首条必须锁定V1.0/起源或迁移记录
    - version: "V2.2-Cognitive"      # 🟡 Recommended: 当前版本标识
      date: 2026-03-17               # 🔴 Core: 物理操作时间戳 (由AI自动填充)
      note: |                       # 🟡 Recommended: 变更摘要
        Migration from V2.1-Full to V2.2-Cognitive. Added 'logic_access' and 'audit_thoughts' for Cognitive Depth.

---
```

## 🛡️ 权责红线与自动化协议 (Red Lines & Automation Protocols)

_(Code Purity, ChangeLog First等，新增认知安全条款)_

### **1. Code Purity** (代码纯净原则):

- **禁止**: 在 `.py`, `.js`等生产文件中添加 Obsidian双链 (`[[ ]]`)、YAML标签或内阁私有元数据。
- **理由**: 确保 OpenBT可独立部署于任何 Linux/Server环境，不带“私货”。

### **2. ChangeLog First** (变更日志优先):

- **规范**: CTO (小酷) 完成 Stage X后，必须在根目录生成 `CHANGELOG.md`。
    - **格式**: Markdown + JSON Schema摘要（供 L2扫描层解析）。
        
        ```json
        { "module": "F4", "status": "done", "risk_level": "low" } 
        ```
        

### **3. Link Only in Rules** (链接仅限规则):

- `cursorrules.md`是唯一允许包含内阁元数据（如 `[[Agent_Spec_小酷]]`, `L0·系统宪法`）的文件。
- 其他技术文档仅保留业务逻辑，保持“冷感”。

### **4. Shadow Indexing Protocol** (影子索引协议):

- **触发器**: CTO完成 Stage X后生成 `CHANGELOG.md` (JSON Schema)。
- **自动化**: 小忆 Skill读取此文件 -> 在 Vault创建对应的 `.md/.card.yaml/audit.yaml`资产。
- **基因继承检查**: AI必须验证新文件的 `legacy_metadata`是否完整继承了旧版字段，否则拒绝更新并报警给 Kenny。

### **5. Cognitive Safety Protocol** (认知安全协议):

```
*   **只读摘要**: AI仅解析 `audit_thoughts`,不读取原始Git Commit Log或调试细节。
*   **时效性控制**: Dify设置6个月时间窗口，自动过滤过期思维记录（如V1.0时代的逻辑）。
```

