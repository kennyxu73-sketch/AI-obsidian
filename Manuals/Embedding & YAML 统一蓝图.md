

---

# Kenny AI Obsidian

  

# Embedding & YAML 统一蓝图 v3.0

---

# 0️⃣ 核心设计哲学

1. 展示层 ≠ 治理层 ≠ 语义层
    
2. YAML 是治理源头
    
3. Embedding 是语义出口
    
4. 多域必须物理隔离
    
5. 两规制是默认结构
    
6. 支持未来全量重建
    

---

# 1️⃣ 三层架构

```
展示层：Obsidian 文件 + 双链
治理层：YAML（frontmatter + card + audit）
语义层：Qdrant（多域 + 两规制）
```

---

# 2️⃣ 三域架构（Domain Separation）

  

## Domain A：Notes（知识笔记域）

- 思考
    
- 决策
    
- 模型
    
- 周报
    
- 经验沉淀
    

  

## Domain B：System（系统制度域）

- 蓝图
    
- 协议
    
- 规范
    
- 方法论
    

  

## Domain C：Code（代码工程域）

- 源代码
    
- 自动化脚本
    
- 配置逻辑
    

---

# 3️⃣ YAML 规范（治理层）

---

## 3.1 note.md Frontmatter（极简路由层）

  

允许字段：

```
file_id: ""
domain: "notes | system | code"
doc_type: ""
primary_agent: ""
created_at: ""
version: ""
yaml_spec_version: "1.0"
embedding_spec_version: "3.0"
```

约束：

- 不超过 8 行
    
- 不嵌套
    
- 不写审计信息
    
- 不写 legacy 信息
    

  

作用：

  

→ 决定 domain

→ 决定向量策略

→ 决定检索路由

---

## 3.2 card.yaml（资产语义层）

  

必须字段：

```
file_id: ""
asset_type: ""
value_score: 0
summary: ""
core_tags: []
priority: ""
```

规则：

- summary：50–300 字
    
- 不写审计记录
    
- 不写迁移历史
    
- 不写推断逻辑
    

  

Embedding 只读取：

- summary
    
- asset_type
    
- core_tags
    
- value_score
    

---

## 3.3 audit.yaml（制度审计层）

  

必须包含：

```
legacy_metadata:
conflict_notes:
migration_history:
timestamp_verification:
embedding_access: false
```

规则：

  

→ 永不进入 embedding

→ 永不进入 payload

---

# 4️⃣ Qdrant 物理结构

  

必须物理分离：

```
kenny_notes_summary
kenny_notes_chunks

kenny_system_summary
kenny_system_chunks

kenny_code_chunks
```

禁止混 collection。

---

# 5️⃣ 两规制向量结构

---

## Regime A：文件级 Summary 向量

  

适用域：

- Notes
    
- System
    

  

作用：

- 粗筛文件
    
- 降低 chunk 噪音
    

---

## Regime B：Chunk 级 向量

  

适用域：

- 全域
    

  

作用：

- 精准定位段落
    
- 支持生成回答
    

---

# 6️⃣ 不同域的 Embedding 策略

---

## 6.1 Notes 域

  

### 输入构造

```
【正文】
note.md 去除 frontmatter 后正文

【摘要】
card.summary

【标签】
asset_type
core_tags
```

### Chunk 规则

- chunk_size: 800–1200
    
- overlap: 150–200
    

  

### 强制生成

- summary 向量
    
- chunk 向量
    

---

## 6.2 System 域

  

### 输入构造

```
【完整正文】

【文件定位】
card.summary
asset_type
```

### Chunk 规则

- chunk_size: 1500–2000
    
- overlap: 0–100
    
- <2000 字不切块
    

  

### 强制生成

- summary 向量
    
- chunk 向量
    

---

## 6.3 Code 域

  

### 切分单位

- 一个函数 = 一个向量
    
- 一个类 = 一个向量
    

  

禁止按字符切块。

  

### 输入构造

```
函数签名
+
函数注释
+
函数体
```

如果无注释：

  

可选：本地 LLM 生成 2–3 行摘要。

  

### 不强制生成 summary 向量

  

除非存在 code.card.yaml。

---

# 7️⃣ Payload 标准（统一）

  

所有向量必须包含：

```
{
  "file_id": "",
  "domain": "",
  "chunk_index": 0,
  "doc_type": "",
  "asset_type": "",
  "value_score": 0,
  "created_at": "",
  "embedding_spec_version": "3.0"
}
```

规则：

- 扁平结构
    
- 不存全文
    
- 不存 YAML 原文
    
- 不存 audit 内容
    

---

# 8️⃣ 检索流程（强制）

```
Step1：问题分类 → 判定 domain
Step2：查询 summary collection → top N 文件
Step3：在选定文件内查 chunk
Step4：可选 rerank
Step5：生成回答
```

禁止：

  

直接跨域 top_k chunk 检索。

---

# 9️⃣ 不进入向量层的内容

  

以下永不进入 embedding：

- audit.yaml
    
- 版本迁移历史
    
- 冲突推断
    
- 原始 YAML frontmatter
    
- 系统内部审计记录
    

  

原则：

  

> 向量层只存“认知语义”，不存“制度历史”。

---

# 🔟 版本控制与重建策略

  

Frontmatter 必须记录：

```
embedding_spec_version: 3.0
```

当出现：

- 模型升级
    
- chunk 策略变更
    
- 域策略变更
    

  

必须：

```
删除对应 collection
全量重建
```

禁止混版本运行。

---

# 11️⃣ 权重优先级

  

检索时默认优先级：

```
System > Notes > Code
```

value_score ≥ 4 优先召回。

---

# 12️⃣ 当前阶段执行建议（4G 资产治理）

  

阶段建议：

1. 先完成 YAML 规范校准
    
2. 再按 domain 批量向量化
    
3. 先稳定 Notes + System
    
4. Code 域第二阶段接入
    
5. 统一 embedding 模型，不做双模型
    

---

# 13️⃣ 最终闭环结构

```
YAML → 决定 domain
Domain → 决定向量策略
card.summary → 进入 embedding
audit → 永远隔离
Qdrant → 两规制检索
Obsidian → 双链展示
```

---

