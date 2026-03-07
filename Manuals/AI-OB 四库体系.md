

---

# AI-OB Four-Vault Architecture v1.1

  

AI-OB 四库系统架构定义（Draft Proposal 更新版）

Author: AI-OB System

Status: Stable

Location: system/architecture/

---

## 1. 设计目标

  

AI-OB 采用 四库结构（Four-Vault Architecture），将个人知识、系统架构、工具链、AI运行数据完全隔离。

设计原则：

1. 系统与内容分离
    
2. 用户笔记独立
    
3. AI生成内容可审计
    
4. 工具与业务解耦
    

  

确保：

- 用户知识资产不会被系统污染
    
- 系统升级不会破坏个人笔记
    
- AI生成内容可审计、回滚
    
- 工具链可独立升级
    

---

## 2. AI-OB 四库结构

  

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

## 3. Cabinet — 用户知识库

  

Cabinet 是 用户自己的 Obsidian Vault。

用途：

- 日常笔记
    
- 项目资料
    
- 研究资料
    
- 知识卡片
    
- 日记与回忆录素材
    

  

AI-OB 访问策略：

- 只读访问
    
- AI可生成草稿至 runtime/drafts/，由 Human 审核批准后写入 Cabinet
    
- 避免污染个人笔记
    

  

推荐结构：

```
cabinet/
├── daily/
├── projects/
├── knowledge/
├── research/
└── archive/
```

特点：

- 完全由用户管理
    
- 可在 Obsidian 单独打开
    
- 不受 AI-OB 系统升级影响
    

---

## 4. System — AI-OB系统架构库

  

System 是 AI-OB 的规则与宪法库。

职责：

- 系统规则与政策
    
- 架构蓝图
    
- Cursor Rules / AI Constitution
    
- 数据结构规范
    
- 系统文档与审计标准
    

  

推荐结构：

```
system/
├── constitution/
│   └── ai-ob-constitution.md
├── architecture/
│   ├── ai-ob-four-vault-architecture.md
│   ├── system-overview.md
│   └── runtime-model.md
├── rules/
│   └── cursor-rules.md
├── schemas/
│   ├── note.schema.md
│   ├── card.schema.yaml
│   └── audit.schema.yaml
├── workflows/
│   ├── note-generation.md
│   └── knowledge-ingestion.md
└── docs/
```

特点：

- 人类主导修改
    
- Cursor 仅提供提案和辅助编辑
    
- 所有系统行为以此为依据
    

---

## 5. Runtime — AI运行数据

  

Runtime 是 AI的运行时数据层，用于存储：

- AI生成内容（note.md / card.yaml / audit.yaml）
    
- Semantic 卡片 / Embeddings
    
- 审计记录
    
- Pipeline 结果
    

  

推荐结构：

```
runtime/
├── drafts/        ← AI生成草稿，由 Human 审核批准后可入 Cabinet
├── notes/
├── cards/
├── audits/
├── embeddings/
├── pipeline/
└── logs/
```

特点：

- AI可写入 drafts/ 和 notes/cards/audits/
    
- Triple-A 数据结构：
    
    - note.md — 人类可读内容
        
    - card.yaml — 语义结构与 Embedding 来源
        
    - audit.yaml — 审计记录
        
    
- Drafts 中内容需 Human 审核后才能写入 Cabinet
    

---

## 6. Tools — 工具与基础设施

  

Tools 是 AI-OB 的执行层，负责：

- Docker、n8n、Dify
    
- 本地 AI 模型
    
- Automation 脚本与 CLI
    
- Pipeline 执行
    

  

推荐结构：

```
tools/
├── docker/
│   ├── dify/
│   ├── n8n/
│   └── databases/
├── models/
│   ├── deepseek/
│   └── qwen/
├── scripts/
│   ├── ingest.py
│   ├── audit_check.py
│   └── build_cards.py
├── workflows/
│   └── n8n/
└── cli/
```

特点：

- 独立运行
    
- 不依赖 Cabinet 或 Runtime
    
- 可单独部署与升级
    

---

## 7. 核心数据流结构

  

AI-OB 核心数据流包含 Draft Proposal 流程：

```
Cabinet
   ↑ Human Approval
   |
runtime/drafts/  ← AI生成草稿
   ↓
Runtime (note / card / audit)
   ↓
Tools / Pipeline / Embeddings
   ↓
Agent Memory & Interface
```

系统逻辑：

1. Human Knowledge → Cabinet
    
2. AI 读取 Cabinet → Runtime Drafts
    
3. Human 审核 Drafts → Cabinet
    
4. Runtime → Tools → Agent
    

---

## 8. Cursor 使用方式

- Cursor 只打开：system/ 与 tools/
    
- Cabinet 与 Runtime 仅作为 数据来源
    
- AI生成草稿进入 runtime/drafts/，Human确认后可写入 Cabinet
    
- 确保 四库隔离与数据主权
    

---

## 9. 四库职责总结

|库|角色|
|---|---|
|Cabinet|用户知识（Human Only，AI只读，草稿审核后可写）|
|System|系统规则与宪法（人类主导）|
|Runtime|AI运行数据（AI可写入 drafts/、notes/cards/audits/）|
|Tools|基础设施与执行环境（Docker、n8n、Dify、CLI）|

---

## 10. 核心原则

1. 知识资产与系统完全隔离
    
2. 系统规则由人类主导
    
3. AI生成内容可审计与回滚
    
4. 工具链独立运行
    
5. Draft Proposal 流程确保 Cabinet 安全
    
6. AI只写入 Runtime / Drafts，Human 审核批准后写入 Cabinet
    

---

End of Document

AI-OB Four-Vault Architecture v1.1

---
