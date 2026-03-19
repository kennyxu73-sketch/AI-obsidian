---
title: Doc 处理与封装规则
date: 2026-02-23
protocol_v: "1.4"
primary_agent: 小酷
file_type: doc/standard
project_ref: AI obsidian
importance: 5
review_status: Approved
asset_phase: Final
tags:
  - "#内阁基建/规范"
  - "#Doc/协议"
  - "#Agent/小酷"
  - "#资产/治理"
audit_status: 🏛️ 深度闭环
audit_summary: |
  本规范定义了内阁文档族（Doc）的六大分层体系，确立了从私人性格（Personal）到结构化视图（View）的全维度封装标准。结合 YAML 1.4 协议，实现了文档资产在项目维度上的横向穿透。
audit_keywords:
  - 文档分层
  - 数字化人生
  - 结构化资产
  - 小镜
  - 小康
audit_weights:
  小酷: 1
  小康: 0.8
  小镜: 0.8
system_meta:
  file_id: CABINET-DOC-PROTOCOL-001
  internal_v: "1.4"
  parent_doc: 内阁数字化治理大纲
  source_origin: 2026-02-23 统帅关于 Personal/Log/View 三大维度增补的指示
  kenny_notes: |
    [2026-02-23 15:30]: Kenny 强调 Doc 规范必须涵盖性格模型与结构化逻辑，作为未来回忆录与 2b 业务的根基。
  history_logs:
    - V1.1 | 2026-02-23 | 维度扩容：新增 doc/personal, doc/log, doc/view 分类，对齐 YAML 1.4 纵横协议。
    - V1.0 | 2026-02-23 | 初始版本发布：确立文档族群定义与三层封装架构。
---
# 🏛️ Doc 处理与封装规范 (V1.0)

根据[[YAML处理与封装规范 V2.2]] 
## 一、 Doc 定义与使命

- **定义**：Doc（文档族）是内阁中**长周期、高价值、结构化**的资产沉淀。
- **使命**：为决策提供纵深支持（Strategy），为人生留存感性血肉（Personal），为运行提供标准化法典（Standard）。
- **核心物理标志**：YAML 字段 `file_type: doc/*`。
    

## 二、 六大核心文档族群 (Taxonomy)

小酷、小康、小镜在处理 4G 遗产及新资产时，必须按以下族群归类：

| **族群类型 (file_type)** | **子类维度 (Sub-types)**    | **职责 Agent** | **核心价值**               |
| -------------------- | ----------------------- | ------------ | ---------------------- |
| **`doc/personal`**   | 性格模型、人生哲学、回忆录素材         | **小镜**       | 捕捉统帅的灵魂底色，2c 资产核心。     |
| **`doc/log`**        | 日记、周记、月报、季度 OKR         | **小憶**       | 记录内阁运行的节奏与统帅的时间线。      |
| **`doc/view`**       | 思维导图、甘特图、Canvas、看板      | **小酷**       | 存储纯文本之外的结构化逻辑与视觉框架。    |
| **`doc/strategy`**   | 养老平台规划、业务大纲、技术白皮书       | **业务agents** | 驱动 2b 平台化落地，内阁的商业大脑。   |
| **`doc/standard`**   | YAML 协议、Agent 行为准则、内阁法典 | **小酷**       | 维护系统底层秩序，确保人机协同的一致性。   |
| **`doc/archive`**    | 4G 历史旧文、已完成项目总结、原始档案    | **小黑**       | 尊重历史，将旧数据转化为可检索的数字化资产。 |

---

## 三、 YAML 1.3 协议在 Doc 中的深度映射

Doc 必须严格执行 **YAML 1.3**，其字段映射侧重点如下：

### 1. 封面与索引层 (Core View)

- **`title`**：严禁包含版本号，版本号由 `internal_v` 维护。
    
- **`file_type`**：必须精准到二级分类（如 `doc/personal`）。
    
- **`asset_phase`**：Doc 必须经历从 `S1(初排)` 到 `Final(归档)` 的完整周期。
    
- **`project_ref`**：**[纵横链接]** 标注该文档当前服务于哪个横向项目。
    

### 2. 深度审计层 (Audit Layer)

- **`audit_summary`**：要求 150-300 字。不再是简单的金句，而是**结构化摘要**（背景、核心内容、结论）。
    
- **`audit_keywords`**：提取 5-8 个关键词，确保全局搜索的覆盖度。
    

### 3. 系统追踪层 (System Meta)

- **`parent_doc`**：**[强制项]** 标明文档在知识树中的父级。
    
- **`history_logs`**：Doc 的演进史极其重要，每次重大修订必须记录。
    

---

## 四、 自动化处理规范 (Auto-Processing)

### 1. 结构化重塑 (Restructuring)

- **Cursor 指令**：处理 4G 遗产长文时，Cursor 必须自动生成层级目录（TOC），并将其逻辑映射到 `audit_summary` 
- **格式统一**：正文统一采用 Markdown 语法，表格与 Mermaid 图表需进行兼容性校验。
### 2. 关联感应 (Relational Induction)
- **碎片聚合**：当同类 Card 达到一定数量时，小酷应提示统帅将碎片聚合为一份 `doc/strategy` 或 `doc/knowledge`。
- **血缘锁定**：Doc 移动或更名时，关联的 Card 必须通过 `parent_doc` 字段保持链接不失效。
### 3. 性格与情绪提取 (Emotional Extraction)

- 针对 `doc/personal` 和 `doc/log`，小镜在封装时需额外在 `kenny_notes` 中备注统帅在此文档中表现出的**核心偏好**或**情绪基调**。
    

---

## 五、 官方样板 (以“定期记录”为例)

YAML

```
---
# --- 1. Core View ---
title: "2026年Q1内阁基建与养老平台落地计划"
date: 2026-02-23
protocol_v: "1.3"
primary_agent: "小康"
file_type: "doc/log"             # 族群：定期记录
importance: 5
review_status: "Approved"
asset_phase: "Final"
project_ref: "4G 遗产重塑大工程"   # 关联横向项目
tags: ["#OKR", "#年度计划", "#小康"]

# --- 2. Audit Layer ---
audit_status: "🚀 推进中"
audit_summary: |
  本文件详细规划了 2026 年第一季度的核心任务。重点在于内阁底层协议（YAML 1.3）的封顶，以及养老 AI 平台从 4G 遗产中提取核心逻辑并完成首批 Card 化重塑。
audit_keywords: ["Q1规划", "基建封顶", "平台落地"]
audit_weights: {小康: 0.9, 小酷: 0.8}

# --- 3. System Meta ---
system_meta:
  file_id: "LOG-2026-Q1-001"
  internal_v: "1.0"
  parent_doc: "内阁数字化治理大纲"
  source_origin: "2026-02-23 统帅部春季会议记录"
  kenny_notes: |
    [2026-02-23]: Kenny 强调，Q1 的重中之重是 4G 遗产的清洗质量。
  history_logs:
    - "V1.0 | 2026-02-23 | OKR 建立，遵循基建 1.3 协议。"
---
```

---