
  

# AI-OB Four-Vault Architecture v1.0

  

AI-OB 四库系统架构定义

  

Author: AI-OB System

Status: Stable

Location: system/architecture/

---

# 1. 设计目标

  

AI-OB 采用 四库结构（Four-Vault Architecture），将 个人知识、系统架构、工具链、AI运行数据 完全隔离。

  

设计原则：

1. 系统与内容分离
    
2. 用户笔记独立
    
3. AI运行数据可审计
    
4. 工具与业务解耦
    

  

这样可以确保：

- 用户知识资产不会被系统污染
    
- 系统升级不会破坏个人笔记
    
- AI运行可以被审计与回滚
    
- 工具链可以独立升级
    

---

# 2. AI-OB 四库结构

  

AI-OB 由四个独立 Vault 组成：

```
AI-OB Root
│
├── cabinet/        （个人知识库）
├── system/         （系统架构库）
├── runtime/        （AI运行数据）
└── tools/          （工具与基础设施）
```

四个 Vault 物理隔离，逻辑协同。

---

# 3. Cabinet — 用户知识库

  

Cabinet 是 用户自己的 Obsidian Vault。

  

用于：

- 日常笔记
    
- 项目资料
    
- 研究资料
    
- 知识卡片
    
- 日记
    
- 回忆录素材
    

  

AI-OB 只读取，不控制结构。

  

推荐结构：

```
cabinet
│
├── daily/
│
├── projects/
│
├── knowledge/
│
├── research/
│
└── archive/
```

特点：

- 完全由用户管理
    
- 可在 Obsidian 中单独打开
    
- 不受 AI-OB 系统升级影响
    

  

Cabinet 是 AI-OB 的认知来源。

---

# 4. System — AI-OB系统架构库

  

System 是 AI-OB 的大脑。

  

负责：

- 系统规则
    
- 架构设计
    
- Cursor Rules
    
- AI Constitution
    
- 数据结构规范
    
- 系统文档
    

  

推荐结构：

```
system
│
├── constitution/
│   └── ai-ob-constitution.md
│
├── architecture/
│   ├── ai-ob-four-vault-architecture.md
│   ├── system-overview.md
│   └── runtime-model.md
│
├── rules/
│   └── cursor-rules.md
│
├── schemas/
│   ├── note.schema.md
│   ├── card.schema.yaml
│   └── audit.schema.yaml
│
├── workflows/
│   ├── note-generation.md
│   └── knowledge-ingestion.md
│
└── docs/
```

特点：

- 由人主导修改
    
- Cursor 只辅助编辑
    
- 所有系统行为以此为依据
    

  

System 是 AI-OB 的法律与宪法层。

---

# 5. Runtime — AI运行数据

  

Runtime 是 AI的运行时数据层。

  

用于存储：

- AI生成内容
    
- 语义卡片
    
- 审计记录
    
- embedding控制
    
- pipeline结果
    

  

推荐结构：

```
runtime
│
├── notes/
│   └── *.md
│
├── cards/
│   └── *.yaml
│
├── audits/
│   └── *.yaml
│
├── embeddings/
│
├── pipeline/
│
└── logs/
```

核心设计：

  

Triple-A 数据结构

  

每个知识对象由三部分组成：

```
note.md
card.yaml
audit.yaml
```

含义：

|文件|用途|
|---|---|
|note.md|人类阅读内容|
|card.yaml|语义结构|
|audit.yaml|生成审计|

Runtime 主要由AI写入。

---

# 6. Tools — 工具与基础设施

  

Tools 是 AI-OB 的基础设施库。

  

负责：

- docker
    
- n8n
    
- dify
    
- 本地AI模型
    
- automation
    
- CLI工具
    

  

推荐结构：

```
tools
│
├── docker/
│   ├── dify/
│   ├── n8n/
│   └── databases/
│
├── models/
│   ├── deepseek/
│   └── qwen/
│
├── scripts/
│   ├── ingest.py
│   ├── audit_check.py
│   └── build_cards.py
│
├── workflows/
│   └── n8n/
│
└── cli/
```

特点：

- 独立运行
    
- 不依赖 Obsidian
    
- 可单独部署
    

  

Tools 是 AI-OB 的执行层。

---

# 7. 数据流结构

  

AI-OB 的核心数据流：

```
Cabinet
   ↓
AI读取笔记
   ↓
Runtime
(note / card / audit)
   ↓
Tools
(embedding / pipeline)
   ↓
Dify / Agent
```

系统逻辑：

```
Human Knowledge → Cabinet
Cabinet → Runtime
Runtime → AI Memory
AI Memory → Agent
```

---

# 8. Cursor 使用方式

  

Cursor 只打开两个库：

```
system
tools
```

原因：

- 避免误操作用户笔记
    
- 避免污染运行数据
    

  

Cabinet 与 Runtime 只作为数据来源。

---

# 9. AI-OB 结构总览

  

最终系统结构：

```
AI-OB
│
├── cabinet
│
├── system
│
├── runtime
│
└── tools
```

四库职责：

|库|角色|
|---|---|
|Cabinet|用户知识|
|System|系统规则|
|Runtime|AI运行数据|
|Tools|基础设施|

---

# 10. 核心原则总结

  

AI-OB 四库设计遵循以下原则：

1. 知识资产与系统分离
    
2. 系统规则由人主导
    
3. AI生成内容可审计
    
4. 工具链独立运行
    
5. AI运行数据可回滚
    

---

# End of Document

  

AI-OB Four-Vault Architecture v1.0

:::

---
