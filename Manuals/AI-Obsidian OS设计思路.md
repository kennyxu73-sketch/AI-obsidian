
# AI-Obsidian Cursor Rules (v2.1 — Governance Edition)

本规则用于约束 **AI-Obsidian 工作系统中 Cursor 生成代码、文档与自动化逻辑的行为**。  
目标是确保系统具备：

- **长期可维护性**
- **完全可审计**
- **知识与向量主权**
- **本地算力优先**
- **架构稳定 5-10 年可扩展**

该规则适用于以下运行架构：

Knowledge Source
Obsidian

Agent Runtime
Dify

Workflow / External Integration
n8n

Model Gateway
OneAPI

Local Inference
RTX 3090

---

# 1. Repository Governance（存储库治理）

系统采用 **双层治理结构 + 条件化三层物理分离**。

## 1.1 双层治理结构

系统分为两个核心层级：

### System/（Authoritative Layer — 宪法层）

包含：

- 架构准则
- 安全分级
- 审计蓝皮书
- 向量治理规则

原则：

所有技术实现必须有 System 依据

若 Tools 修改但 System 未更新：

Technical Drift（技术漂移）

若 System 更新但 Tools 未同步：

Logic Break（逻辑断层）


---

### Tools/（Implementation Layer — 实现层）

包含：

- Python Skill
- 自动化脚本
- n8n Workflow
- Dify Tool

原则：

System 决定 Tools

Tools 变动必须反馈至 System

---

# 2. Triple-A Standard（条件化三层物理分离）

为了保证 **知识治理、AI 向量安全与审计能力**，系统采用 **Triple-A 文件结构**。

每个知识单元可拆分为三个物理文件：

note.md

note.card.yaml

note.audit.yaml

## 2.1 文件角色

### 展示层

note.md

用途：

- Obsidian UI 展示
- 极简内容
- 双链与标签

禁止包含：

- AI 摘要
- 审计信息
- 向量内容

---

### 语义层

note.card.yaml

用途：

- AI embedding
- 向量搜索
- 语义摘要

结构示例：

```yaml
file_id: mirror_001
title: Mirror System Architecture
summary: >
  介绍 Mirror Core 的基础架构以及与 AI-Obsidian
  系统之间的关系，包括 Agent Runtime 与 Knowledge OS。
embedding_access: true
````

摘要要求：
50-300 字

Embedding 只允许来自 card.yaml。

---

### 治理层

note.audit.yaml


用途：

- 审计记录
    
- 版本血缘
    
- 变更历史
    

必须硬编码：

embedding_access: false

示例：

file_id: mirror_001
version: 3
history:
  - v1: created
  - v2: summary updated
  - v3: structure revised
review_status: approved
embedding_access: false

---

## 2.2 条件化 Triple-A


为防止文件爆炸，仅在以下目录 强制 Triple-A：

System/
Project/
Tools/

以下目录 可选：

Knowledge/
Research/

以下目录 禁止 Triple-A：

Logs/
Archive/

---

# 3. Role Switching & Inference Logic（角色与算力调度）

  

Cursor 必须根据 文件类型与数据等级 自动切换工作模式。

---

## A. CTO Mode

  

触发条件：

编辑 .py / .js / .ts

关注点：

- 本地算力适配
    
- API 健壮性
    
- 自动化稳定性
    

  

算力建议：

L1 / L2 数据
→ 本地 3090

推荐模型：

DeepSeek-R1-Local
Qwen

复杂算法或重构：

云端 DeepSeek-V3 / Claude

禁止：
上传 L1 数据

---

## B. Architect Mode

  触发条件：

编辑 System/

关注点：

- 架构一致性
    
- 安全合规
    
- 审计逻辑
    

  

允许使用：

云端高智力模型

但禁止：

上传 L1 数据

---

## C. Knowledge Mode

  触发条件：

编辑 Knowledge/
Research/

目标：

- 语义整理
    
- 结构化知识
    
- RAG 预处理
    

  

任务包括：

生成 card.yaml
优化语义摘要
构建知识图谱

算力建议：

L3 / L4
可使用云端模型

---

# 4. Mandatory Change Summary（重大修改预检）

  

当执行 重大修改 时，Cursor 必须生成审计预检报告。

  重大修改包括：

新增 Tool
新增 Skill
修改 System
修改自动化架构
新增 Agent


格式：

[内阁审计预检]

关联法典：
[[System/...]]

涉及工具：
filename.py / workflow_xxx

安全等级：
L1 | L2 | L3 | L4

算力建议：
本地 3090 / 云端 DeepSeek

审计留痕：
是否符合蓝皮书增量审计？


以下情况 无需预检：

typo
小幅代码修复
文档修改

---

# 5. Audit & Integrity Protocol（审计协议）

  

遵循：

《本地笔记审计蓝皮书 v1.0》


核心原则：

## 增量优先

  
审计脚本必须：

基于 file_id + version

禁止：

全量扫描

---

## 异常挂起

若发生：

ID 冲突
摘要生成失败
YAML 冲突

必须生成：

.halt

等待人工复核。

  

禁止自动覆盖。

---

## 血缘守恒

  

衍生文件必须关联：

file_id

禁止产生：

孤儿文件

---

# 6. Vector Sovereignty（向量主权）

  

遵循：

统一蓝图 v3.0

向量系统分为两个 regime：

---

## Regime A
文件级摘要

来源：
note.card.yaml

用途：

快速检索

---

## Regime B

Chunk 级检索

来源：

原始文档

用途：

精确定位

---

## 向量隔离红线

  

严禁 embedding：

audit.yaml
系统审计日志
原始 YAML

代码向量化规则：

函数级
类级

禁止：

字符切块

---

# 7. Automation & n8n Positioning

  

n8n 定位为：

外事枢纽

用途：

- 企业微信
    
- 公众号
    
- 外部系统
    
- 跨 Agent 异步
    

  

原则：

内部逻辑优先 skills dify python 等

避免：

过度 n8n

---

# 8. Skill Interface Standard

  

所有 Tools/ Skill 必须支持：

  

输入：


task
context
metadata


输出：

```
result
summary
status
```

必须兼容：

```
Dify Tool
n8n Webhook
```

---

# 9. Network & Path Safety

  

路径安全：


禁止：

```
/Users/kenny/
/home/kenny/
```

统一：
```
/workspace/
/local/path/
```

网络优先：

```
ZeroTier
Docker service name
```

---

# 10. Security Classification

|Level|类型|原则|算力|
|---|---|---|---|
|L1|核心内阁数据|严禁离境|本地3090|
|L2|私有项目数据|本地优先|本地3090|
|L3|可交换数据|效率优先|云端|
|L4|公共数据|完全开放|云端|

默认规则：

```
security_level = L2
```

---

# 11. Knowledge Access Protocol

  

读取顺序：

```
1 System/
2 Project/
3 Knowledge/
4 Logs/
5 Archive/
```

原则：

```
System 优先
```

---

# 12. Conflict Resolution

  

冲突解决优先级：

  

1️⃣ 安全优先

```
违反安全分级 → 必须改为本地算力
```

2️⃣ 法典优先

```
用户指令与 System 冲突
→ 先更新法典
```

3️⃣ 本地优先

  

所有 Tools 必须支持：

```
3090 运行
```

---

# 13. Self-Correction Protocol（影子审计）

  

Cursor 生成任何代码或 YAML 后必须执行自检：

  

检查：

```
1 物理隔离
2 向量屏蔽
3 接口结构
4 审计状态
```

必须确认：

```
audit.yaml
embedding_access: false
```

若涉及架构级变更：

```
review_status: pending
```

等待人工批准。

---

# System Guardian Principle

  

如果发现任何操作可能导致：

```
L1 数据外泄
```

AI 必须：

```
停止执行
提出警告
建议替代方案
```

---

End of Document

AI-Obsidian Cursor Rules v2.1