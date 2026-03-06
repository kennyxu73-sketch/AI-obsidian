# Kenny AI Obsidian：YAML 处理与封装全量规范 (V2.0 物理拆解版)

## 一、 整体设计原则 (General Design Principles)

1. **资产全息化 (Holographic Assets)**：元数据通过 `[[双链]]` 成为逻辑节点。
    
2. **纵横坐标系 (Matrix Coordinate)**：通过 `file_type` 与 `project_ref` 确立唯一坐标。
    
3. **血缘守恒 (Ancestry Conservation)**：通过 `parent_doc` 杜绝孤儿文件。
    
4. **三层物理分离 (Tiered Isolation)**：展示层 (Note) ≠ 语义层 (Card) ≠ 治理层 (Audit)，实现隐私与检索的隔离。
    
5. **约束等级制 (Constraint Grading)**：明确区分必填（🔴）、推荐（🟡）与可选（🟢）字段。
    
6. **内容终审权 (Final Review Authority)**：涉及实质变更必须通过 `Pending` 触发统帅人工审核。
    
7. **时间主权 (Timestamp Sovereignty)**：`date` 锁定资产真实的物理起源，区分 `date` (出生) 与 `deadline` (截止)。
    
8. **基因继承原则**：新规范必须是旧规范的增量升级，确保原始标签与核心属性不丢失。
    
9. **滚动审计原则**：`audit.yaml` 包含对前代版本结论的复核，形成有厚度的信用链条。
    

---

## 二、 物理拆解与字段规范 (The Triple-A Standard)

按照 **Step 2** 执行要求，资产将裂变为三个物理文件：

### 1️⃣ 展示层：`note.md` (极简路由)

**定位**：Obsidian 阅读主体，仅保留索引元数据。

|**字段名**|**约束等级**|**执行逻辑与红线要求 (Redline)**|
|---|---|---|
|**`file_id`**|**🔴 必填**|唯一永久 ID。严禁人工修改。|
|**`domain`**|**🔴 必填**|**域隔离**：`notes`|
|**`doc_type`**|**🔴 必填**|文档细分类型（如 `doc/standard`）。|
|**`primary_agent`**|**🔴 必填**|责任 Agent。权重 < 0.3 的自动剔除。|
|**`yaml_spec_version`**|**🔴 必填**|固定为 `"2.0"`。|
|**`card`**|**🔴 必填**|**强制双链**：指向 `[[note.card.yaml]]`。|
|**`audit`**|**🔴 必填**|**强制双链**：指向 `[[note.audit.yaml]]`。|
|`importance`|**🟡 推荐**|资产权重 (1-5)。|

---

### 2️⃣ 语义层：`note.card.yaml` (向量化动力源)

**定位**：Step 3 构造 `embedding_input` 的核心源。

|**字段名**|**约束等级**|**执行逻辑与红线要求 (Redline)**|
|---|---|---|
|**`file_id`**|**🔴 必填**|必须与主文件一致。|
|**`summary`**|**🔴 必填**|**50–300 字纯语义摘要**。Embedding 唯一合法输入。|
|**`asset_type`**|**🔴 必填**|资产分类（如 `strategy` / `insight`）。|
|**`core_tags`**|**🔴 必填**|核心语义标签。|
|`value_score`|**🟡 推荐**|决定检索优先级的价值评分。|

---

### 3️⃣ 治理层：`note.audit.yaml` (影子审计存证)

**定位**：存放所有历史、审计记录。**物理屏蔽向量化**。

|**字段名**|**约束等级**|**执行逻辑与红线要求 (Redline)**|
|---|---|---|
|**`embedding_access`**|**🔴 必填**|**固定为 `false`**。严禁进入向量库。|
|**`review_status`**|**🔴 必填**|`Approved` 或 `Pending`（涉及重塑必选）。|
|**`confirmed_by`**|**🔴 必填**|确权人（如 `Kenny`）。|
|**`audit_summary`**|**🔴 必填**|**全息滚动审计**。必须包含对前代版本的复核。|
|**`Legacy Metadata`**|**🔴 必填**|**差异沉淀**：存放旧别名、旧权重、1.6.1 遗留字段。|
|**`history_logs`**|**🔴 必填**|**全量编年史**。首条必须对齐 `date` 字段。|
|`audit_weights`|**🟡 推荐**|Agent 相关性评估。|
|`kenny_notes`|**🟢 可选**|记录推算逻辑、冲突或统帅特殊指示。|

---

## 三、 并网执行协议 (Automation Protocols)

1. **Step 1 筛选与 Step 2 裂变**：脚本必须先提取旧版 YAML 字段。标准字段进入主文件或 Card，非标/历史字段沉淀至 Audit 区的 `Legacy Metadata`。
    
2. **Step 3 输入构造**：向量化输入公式 = `note.md (正文)` + `note.card.yaml (summary)`。禁止读取 Audit 文件。
    
3. **V1.0 溯源原则**：拆解后的第一条 history log 必须锁定为 V1.0，日期与物理起源 `date` 一致。
    
4. **形态主权保护**：严禁抹除插件标记。重塑后保持原名关系以保护双链。
    
5. **决策节点挂起**：涉及系统变更必须处于挂起态，直至 Kenny 显式授权。
    

---

## 四、 规范官方封装样板 (V2.0)

### 文件 1: `note.md`

YAML

```
---
file_id: "CAB-PROT-2026-001"
domain: "system"
doc_type: "doc/standard"
primary_agent: "小酷"
created_at: 2026-02-15
importance: 5
yaml_spec_version: "2.0"
card: "[[note.card.yaml]]"
audit: "[[note.audit.yaml]]"
---
# 协议正文...
```

### 文件 2: `note.card.yaml`

YAML

```
file_id: "CAB-PROT-2026-001"
type: "card"
asset_type: "protocol"
summary: |
  本文件定义了 YAML V2.0 物理拆解规范，确立了展示、语义、治理三层隔离架构，确保 4GB 资产可安全向量化。
core_tags: ["#内阁基建/协议", "#治理/V2.0升级"]
value_score: 5
```

### 文件 3: `note.audit.yaml`

YAML

```
file_id: "CAB-PROT-2026-001"
type: "audit"
embedding_access: false
review_status: "Approved"
confirmed_by: "Kenny"
audit_summary: |
  [V2.0 全量滚动审计报告]:
  - 基因继承：完成从 V1.6.1 的物理拆解平移。
  - 隔离性：已通过物理路径验证，Audit 域已被向量引擎屏蔽。
  [Legacy Metadata]:
    - old_version: "1.6.1"
    - old_weights: "小黑: 0.7, 小酷: 1"
history_logs:
  - V2.0.0 | 2026-02-26 | 执行物理拆解升级，确立三位一体架构。
  - V1.0.0 | 2026-02-15 | 协议诞生：确立元数据封装理念。
```

### YAML v2.0 全量字段定义

#### 1️⃣ `note.md`：展示与索引字段 (Frontmatter)

|**字段名**|**来源**|**约束**|**定义与红线**|
|---|---|---|---|
|`file_id`|V1.6.1|🔴 必填|资产唯一身份证，禁止变更。|
|`title`|V1.6.1|🟡 推荐|资产人类可读标题。|
|`domain`|**V2.0**|🔴 必填|`notes` (笔记)|
|`doc_type`|V1.6.1|🔴 必填|文档细分类型，如 `doc/standard`。|
|`primary_agent`|V1.6.1|🔴 必填|责任 Agent（小憶/小镜/小康/小酷）。|
|`project_ref`|V1.6.1|🟡 推荐|双链格式项目引用，如 `[[AI obsidian]]`。|
|`importance`|V1.6.1|🟡 推荐|权重 (1-5)，5 为核心资产。|
|`date`|V1.6.1|🔴 必填|资产物理起源日期。|
|`deadline`|V1.6.1|🟢 可选|演进节点或任务截止日。|
|`tags`|V1.6.1|🟡 推荐|原始标签列表。|
|`card`|**V2.0**|🔴 必填|物理链接：`[[文件名.card.yaml]]`。|
|`audit`|**V2.0**|🔴 必填|物理链接：`[[文件名.audit.yaml]]`。|

#### 2️⃣ `note.card.yaml`：语义与向量字段 (Semantic Layer)

|**字段名**|**来源**|**约束**|**定义与红线**|
|---|---|---|---|
|`file_id`|**V2.0**|🔴 必填|必须与主文件对齐。|
|`type`|**V2.0**|🔴 必填|固定为 `card`。|
|`summary`|**V2.0**|🔴 必填|**50-300字纯语义摘要**，向量化主输入。|
|`key_entities`|**V2.0**|🟡 推荐|提取的正文核心实体词。|
|`asset_type`|V1.6.1|🔴 必填|资产属性（如 `protocol`, `insight`）。|
|`value_score`|**V2.0**|🟡 推荐|语义价值评分 (0-1)。|

#### 3️⃣ `note.audit.yaml`：治理与存证字段 (Shadow Layer)

|**字段名**|**来源**|**约束**|**定义与红线**|
|---|---|---|---|
|`embedding_access`|**V2.0**|🔴 必填|**固定为 `false`**，屏蔽向量化。|
|`review_status`|V1.6.1|🔴 必填|`Approved`|
|`confirmed_by`|**V2.0**|🔴 必填|终审确权人：`Kenny`。|
|`audit_status`|V1.6.1|🟡 推荐|审计里程碑描述。|
|`audit_summary`|V1.6.1|🔴 必填|滚动审计报告内容。|
|`audit_keywords`|V1.6.1|🟡 推荐|影子审计关键词双链。|
|`legacy_metadata`|V1.6.1|🔴 必填|**存证区**：存放旧版本的所有非标字段。|
|`history_logs`|V1.6.1|🔴 必填|全量时间轴记录。|