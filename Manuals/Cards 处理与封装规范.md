---
# --- 1. Core View (核心展示层) ---
title: "Cards 处理与封装规范"
date: 2026-02-23
protocol_v: "1.0"                  # 遵循最新的基建协议
primary_agent: "小酷"               # 架构设计者
file_type: "doc/standard"          # 属于文档族的标准协议
importance: 5                      # 最高重要性：内阁运行底座
review_status: "Approved"          # 统帅已阅准予执行
asset_phase: "Final"               # 终审归档阶段
tags: ["#内阁基建/规范", "#Cards/协议", "#Agent/小憶", "#Agent/小报"]

# --- 2. Audit Layer (审计层) ---
audit_status: "⚡ 全闭环发布"
audit_summary: |
  本规范定义了内阁原子卡片（Cards）的五大族群及处理标准。明确了小憶（内生）与小报（外生）作为核心处理者的权责分工，实现了从 YAML 数据到视觉看板的精准映射。
audit_keywords: ["原子卡片", "分级治理", "小憶", "小报", "数据驱动"]
audit_weights: {小酷: 1.0, 小憶: 0.8, 小报: 0.8}

# --- 3. System Meta (系统层) ---
system_meta:
  file_id: "CABINET-CARD-PROTOCOL-001"
  internal_v: "1.0"                # Cards 规范自身的版本
  parent_doc: "内阁数字化治理大纲"
  source_origin: "2026-02-23 统帅关于 Cards 族群与 Agent 分工的深度指示"
  kenny_notes: |
    [2026-02-23 14:30]: Kenny 明确小报为外部资料处理核心，小憶为日常互动核心，要求将此逻辑写入 Cards 规范。
  history_logs:
    - "V1.0 | 2026-02-23 | 初始版本发布：确立五大族群、双 Agent 处理机制及 YAML 映射规则。"
---
## 一、 Cards 定义与定位

- **定义**：内阁最小原子化信息载体，基于 YAML 1.3 协议的轻量化封装。
    
- **核心处理器**：
    
    - **小憶**：内生特工。负责统帅日常对话、碎片想法、即时感受的卡片化。
        
    - **小报**：情报特工。负责外部资讯、深度文章、行业研报的去粗取精与卡片化。
        

## 二、 五大原子卡片族群与权责分工

|**族群类型 (file_type)**|**核心使命**|**主要处理者**|**封装侧重点**|
|---|---|---|---|
|**`card/knowledge`**|**知识卡**：硬核定义与方法论。|小憶 / 小酷|剔除冗余，保留“第一性原理”。|
|**`card/spark`**|**灵感卡**：瞬间闪念与创意。|小憶|记录原始语境，保留灵感张力。|
|**`card/intel`**|**资讯卡**：外部情报与动态。|**小报**|**[核心]** 标注情报来源、真实度及对内阁的潜在影响。|
|**`card/memo`**|**备忘卡**：事务提醒与待办。|小憶|明确执行动作与 Kenny 的批阅优先级。|
|**`card/feeling`**|**感受卡**：感性认知与评价。|小憶|捕捉情绪锚点，为 2c 资产提供感性素材。|

---

## 三、 自动处理与映射规范 (Auto-Processing)

### 1. 封面金句提取 (The Hook)

- **动作**：从正文中提取最精华的一句话填充至 `audit_summary` 第一段。
    
- **小报特则**：小报在处理长篇外网资讯时，必须在 Hook 中体现“该资讯为什么对 Kenny 重要”。
    

### 2. 血缘强制溯源 (Ancestry)

- **动作**：必须填充 `system_meta.source_origin`。
    
- **小报要求**：必须包含原始 URL 或媒体来源，并在 `audit_keywords` 中标记来源权重。
    
- **小憶要求**：记录对话发生的时间轴及当时的讨论主题。
    

### 3. 字段克制与演进

- **原则**：严禁私自增加 YAML 字段。
    
- **执行**：所有非标准信息（如资讯的原始链接）统一存放在 `audit_summary` 结尾，由日后 AI Skill 统一处理。
    

---

## 四、 特工工作流协议 (Agent Workflow)

### 1. 小憶：对话即资产

- **识别**：从小记录的日常互动中抓取灵感（Spark）与感受（Feeling）。
    
- **生成**：默认 `review_status: Pending`，等待 Kenny 在晚间批阅看板。
    

### 2. 小报：情报即卡片

- **搜寻**：每日扫描外部资料，对有价值的内容进行“降维打击”（长文转短卡）。
    
- **过滤**：过滤掉噪音，仅产出 `card/intel`。
    
- **呈送**：自动挂载 `importance` 分级，确保高价值情报优先出现在统帅视野。
    

---

## 五、 官方封装样板 (以小报产出的资讯卡为例)

YAML

```
---
# --- 1. Core View ---
title: "2026 养老机器人行业突发进展"
date: 2026-02-23
protocol_v: "1.3"
primary_agent: "小报"           # 外部资料处理核心
file_type: "card/intel"
importance: 5                  # 极高重要性
review_status: "Pending"
asset_phase: "S2"
tags: ["#行业情报", "#养老机器人"]

# --- 2. Audit Layer ---
# 封面金句：小报提炼的价值点
audit_summary: |
  特斯拉二代养老伴随机器人宣布量产，其运动控制逻辑与我们小康 agent 的交互层高度互补。
audit_keywords: ["量产", "技术互补", "行业突发"]
audit_weights: {小报: 0.95}

# --- 3. System Meta ---
system_meta:
  file_id: "INTEL-20260223-088"
  parent_doc: "小康养老 AI 平台化产品白皮书"
  source_origin: "路透社 2026-02-23 科技早报"
  kenny_notes: |
    [小报提示]: 统帅，这可能影响我们下季度的硬件选型决策。
---
```