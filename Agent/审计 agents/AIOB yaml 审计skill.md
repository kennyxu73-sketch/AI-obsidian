

---

# 📑 AIOB-Core-Enseal-Skill 开发说明文档 (V1.0)

## 1. 定位与目标 (Positioning)

本 Skill 是数字内阁的**“法律执行器”**。它负责将任意原始输入（代码变更、笔记、随手记）按照“三层物理分离”原则进行封装，并同步完成“增量审计留痕”。

- **执行标准**：YAML V2.2-Cognitive 规范。
    
- **审计灵魂**：增量扫描、差异比对、导师模式（解释“为什么”）。
    

---

## 2. 核心功能模块 (Core Modules)

### 模块 A：三层全息封印 (Triple-A Enseal)

- **输入**：Raw Text + Metadata Context。
    
- **动作**：
    
    1. **L1 生成 (Note)**：提取核心字段（`file_id`, `domain`, `importance`），锁定 `created_at`（时间主权）。
        
    2. **L2 生成 (Card)**：由 LLM 预提炼语义摘要，强制 `embedding_access: true`。
        
    3. **L3 生成 (Audit)**：这是审计核心。
        
        - **逻辑入库**：将 LLM 提炼的决策理由写入 `audit_thoughts`（认知深度）。
            
        - **血缘锁定**：自动继承旧版的 `legacy_metadata`。
            

### 模块 B：增量审计留痕 (Incremental Audit)

- **逻辑依据**：《本地笔记审计蓝皮书》。
    
- **动作**：
    
    1. **Diff 计算**：如果文件已存在，自动对比新旧版本差异。
        
    2. **异常报警**：若发现 `file_id` 冲突或核心字段（如 `importance`）非正常降权，触发 `review_status: "Pending"`。
        
    3. **快照存证**：在 `history_logs` 中记录本次操作的 Agent 身份（@小忆/@小酷）与时间戳。
        

### 模块 C：影子索引适配 (Shadow Indexing)

- **逻辑依据**：《项目管理体系》。
    
- **动作**：
    
    1. **JSON 解析**：专门接口解析 `CHANGELOG.md` 中的 JSON 摘要。
        
    2. **自动化映射**：根据模块名（如 F4）自动寻找或创建 Cabinet 中的对应资产路径。
        

---

## 3. 接口参数定义 (API Spec)

### `execute_enseal` (主封印接口)

|**参数名**|**类型**|**说明**|**约束**|
|---|---|---|---|
|`raw_content`|String|笔记或代码的正文|必填|
|`intent_context`|JSON|包含 `domain`, `project_ref`, `importance`|必填|
|`thoughts`|String|本次决策的理由 (写入 L3)|建议|
|`agent_id`|String|当前执行操作的 Agent (@小忆/小酷)|必填|

---

## 4. 审计逻辑判定 (Audit Logic)

Skill 在执行时会自问三个问题（由代码硬逻辑控制）：

1. **血缘合法性**：该文件的 `file_id` 是否在内阁已有记录？如果有，新旧版本是否逻辑连贯？
    
2. **权限合规性**：`embedding_access` 是否仅对 L2 开放？L3 是否已物理屏蔽？
    
3. **决策透明度**：`audit_thoughts` 是否为空？（若为空，强制要求 Agent 补充“决策理由”）。
    

---

## 5. 对统帅的价值 (Value for Kenny)

1. **无感审计**：你不需要专门去审计文件，在你保存文件的那一刻，Skill 已经按照《蓝皮书》的要求完成了 Diff 记录和合规检查。
    
2. **认知共情**：它强制要求 AI 记录“为什么这么做”，这为以后小忆通过 `logic_access` 理解你的思维路径打下了基础。
    
3. **主权隔离**：即使小酷（Cursor）在 Workspace 搞乱了代码，Skill 在同步时也会把干净的“知识资产”提取出来，保护内阁不受污染。