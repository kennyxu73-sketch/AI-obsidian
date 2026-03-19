

---

# 📑 AIOB-Tag-Governance-Skill 开发需求书 (V1.0)

## 1. 定位与目标 (Target)

作为内阁的“标签警察”与“路由助手”，确保所有资产标签符合层级规范，实现 YAML 字段与 Obsidian 标签的绝对同步，并提供人工修正的留痕能力。

---

## 2. 核心逻辑模块 (Functional Modules)

### 模块 A：静默校验与纠偏 (Auto-Correction)

- **输入**：L1 (`note.md`) 的原始标签列表。
    
- **逻辑依据**：`tag_schema.json`（路由表）。
    
- **执行动作**：
    
    1. **扁平化转层级**：检测到 `#openbt` ➔ 自动更正为 `#项目/OpenBT`。
        
    2. **根标签补全**：检测到 `domain: "notes"` 且缺失对应标签 ➔ 自动补齐 `#内阁/笔记`。
        
    3. **状态联动**：若 `review_status: "Pending"` ➔ 强制注入 `#状态/待审`；若为 `"Approved"` ➔ 替换为 `#状态/资产`。
        

### 模块 B：冲突拦截与异常记录 (Exception Handling)

- **逻辑**：
    
    1. **黑名单拦截**：严禁出现单层标签（孤儿标签）。
        
    2. **白名单过滤**：若标签根路径不在 `tag_schema.json` 中，将其移动至 L3 (`.audit.yaml`) 的 `legacy_metadata`。
        
- **输出**：在 `audit_exception_log.json` 中追加记录，标注：`file_id`, `offending_tag`, `suggested_fix`。
    

### 模块 C：人工修正保护 (Human Override Protection)

- **逻辑**：
    
    1. 识别统帅手动添加的非标标签，不直接删除，而是将其存入 L3 的“人工备注区”。
        
    2. 若统帅手动修改了已有的层级标签，Skill 必须同步更新 L2 (`.card.yaml`) 的 `tags` 数组，保持语义层一致。
        

---

## 3. 核心接口定义 (API Spec)

Python

```
class TagManager:
    def __init__(self, schema_path: str):
        # 加载 tag_schema.json
        self.schema = load_json(schema_path)

    def validate_and_fix(self, tags: list, yaml_context: dict) -> tuple:
        """
        返回: (修正后的标签列表, 是否发生变更, 异常日志)
        """
        # 1. 检查根标签合法性
        # 2. 注入 YAML 联动标签 (Domain/Status)
        # 3. 纠正拼写与大小写
        pass

    def log_exception(self, file_id: str, error_msg: str):
        # 写入 audit_exception_log.json
        pass
```

---

## 4. 与现有规则的集成约束 (Integration)

1. **与《统一蓝图 v3.0》一致**：修正后的标签必须同步更新到 `.card.yaml` 的 `tags` 字段中，确保向量 Payload 包含正确的标签元数据。
    
2. **与《V2.3 规范》一致**：所有标签操作严禁触碰生产代码区（`.py`, `.js`），仅限知识资产层（`.md`, `.yaml`）。
    
3. **审计留痕**：任何 Skill 自动进行的标签更正，必须在 `.audit.yaml` 的 `history_logs` 中记录一条：`"action": "Auto-Tag-Correction"`。
    

---

## 🚀 给 Cursor 的一键生成指令 (Prompt)


> “小酷（CTO），现在请基于《AIOB-Tag-Governance-Skill 开发需求书》，为 `enseal_skill.py` 增加标签治理模块。
> 
> **要求**：
> 
> 1. 读取 `/00_Cabinet/00_System/Tag_Governance/tag_schema.json` 作为唯一真理来源。
>     
> 2. 实现标签与 YAML `domain`、`review_status` 的强一致性映射。
>     
> 3. 所有更正动作必须记录在 L3 的 `history_logs` 中。
>     
> 4. 严禁删除用户手动输入的非标标签，应将其转存至 `legacy_metadata` 并记录到异常日志中。
>     
> 5. 确保输出的 `.card.yaml` 标签数组是纯净且符合层级规范的。”
>     

---

