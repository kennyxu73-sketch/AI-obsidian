
---
created: {{date}}
creator: Kenny (via XiaoYi)
status: approved_for_production
related_agents: [小忆, 小康] 
tags: [gap-engine, sovereignty-first, controlled-augmentation]
canvas_ref: [[/Assets/canvas/认知补全.canvas]] # 👈 引用人工意图源，无噪点
---

# 🧠 Gap Engine v2.0 (主权增强版) - 设计说明与执行规范

> **核心定义**: 
> *   **通用底座**: 采用标准化思考框架 (`Problem/Solution/User...`)。
> *   **宪法内核**: 叠加 Kenny 的《系统宪法》(L0·1 主权优先、本地算力约束)。
> *   **定位**: 不是为“任意用户”设计，而是为您构建的**认知增强引擎**。

## [🔗] Canvas 意图溯源 (Source Intent)
[[/Assets/canvas/认知补全.canvas]]  
*(点击查看人工直觉的空间拓扑与职能定义)*

---

## 🛠️ 架构逻辑：从“通用模板”到“主权治理”

### 1. ⚙️ 输入结构化层 (Intent Parser & Universal Schema)
*   **标准框架**: 沿用 `Problem/Solution/User/Value` 等八维模型。
    *   *作用*: 将模糊想法转化为可检测的结构化对象。
*   **潜台词过滤**: 
    *   ✅ **显性目标**: “我想做一个 AI 养老系统”。
    *   ⚠️ **隐性信号 (Kenny Style)**: "提到养老” → `[[慰康]]` MVP；"纠结 Docker" → 转交小酷。

### 2. 🔍 缺口检测层 (Gap Detection)
*   **通用维度**: 
    - [ ] User (谁用？)
    - [ ] Value (价值何在？)
    - [ ] Feasibility (技术可行吗？)
-   **主权增强维度 (Kenny Specific)**:
    - 🛡️ **Sovereignty Risk**: 是否涉及公有云上传/数据出境？(违反 L0·1 → ⚠️阻断)
    - 💻 **Resource Constraint**: RTX 3090 显存能否承载？(本地算力评估)

### 3. 📝 补全建议层 (Completion Engine)
*   **拒绝直接结论**,仅提供选项：
    *   `Option A`: MVP (低成本, Prompt调整)。
    *   `Option B`: Upgrade (架构升级，需小酷介入)。
    *   `Action Item`: 下一步行动清单。

---

## 📜 机器逻辑视图 (Machine Logic View)

> 💡 *注：本区域仅包含纯文本/代码形式的拓扑结构，严禁插入非标准 Markdown 图片，以确保 Embedding 向量的纯度与检索效率。*

```mermaid
graph TD
    %% --- 1. 定义物理分区 (Subgraphs) ---
    
    subgraph INPUT [📥 输入感应层]
        P[开始] --> I1[🔍 Intent Parser<br/>显性目标 +<br/>潜台词识别]
        style INPUT fill:#e3f2fd,stroke:#1565c0,color:#000
    end

    subgraph MEMORY [📁 记忆上下文窗口]
        direction TB
        M1[(💾 Vault Native Search)]
        M2[Qdrant RAG<br/>按需触发开关]
        I2[📂 Context Window<br/>加载 Persona/Rule Base]
        
        M1 -.->|默认/快速| I2
        M2 -- "仅当复杂查询" --> I2
        
        style M1 fill:#e8f5e9,stroke:#2e7d32,color:#000
        style M2 fill:#ffebee,stroke:#c62828,stroke-dasharray: 5 5,color:#000
    end
    
    subgraph PROCESS [⚙️ 核心检测逻辑]
        direction TB
        D{缺口检测 MVP}
        T1[技术可行性?]
        B1[商业模型闭环?]
        U1[用户场景明确?]
        
        D --> T1
        D --> B1
        D --> U1
        
        style PROCESS fill:#f9fbe7,stroke:#fbc02d,color:#000
    end

    subgraph SAFETY [🛡️ 主权安全网关]
        direction TB
        S{违反本地优先?<br/>公有云风险?}
        R1["规则库: 禁止公有云上传"]
        W[⚠️ 阻断/转交小酷<br/>生成偏差报告]
        
        S -- "是" --> W
        R1 -.-> S
        
        style SAFETY fill:#ffebee,stroke:#c62828,color:#000
    end

    subgraph FINAL [📝 结构化输出区]
        direction TB
        O1[❌ Missing Elements<br/>缺失要素列表]
        O2[⚠️ Deviation Check<br/>偏差标记]
        O3[💡 Suggested Options<br/>补全选项 A/B/C]
        Rpt[📄 Gap Engine Report]
        W1{User Decision}
        OPT_A[MVP: Prompt调整<br/>低成本/快速]
        
        O1 --> Rpt
        O3 --> Rpt
        Rpt --> W1
        W1 -.->|选择 Option| OPT_A
        
        style O3 fill:#e8f5e9,stroke:#0277bd,color:#000
    end

    %% --- 全局流程连接 ---
    
    I1 --> MEMORY
    I2 -.-> PROCESS
    PROCESS --> SAFETY
    
    %% 安全网关输出分流
    S -.->|否/通过| O1 
    W --> O2

    style Rpt fill:#fff3e0,stroke:#ef6c00,color:#000

````

---

## 📄 Gap Engine Report (示例)

> **状态**: [P1] | **意图识别**: [项目名](app://obsidian.md/%E9%A1%B9%E7%9B%AE%E5%90%8D) MVP 设计讨论

---

#### ⚠️ 认知偏差检测 (Deviation Check)

- [ ] **主权风险**: 方案涉及云端依赖，建议本地化。
- [x] **无冲突**：符合“人类在环”原则。

#### ❓ 缺失要素清单 (Missing Elements)

1. **用户场景**: 未定义具体使用场景（是老人端还是管理端？）。
2. **技术边界**: 尚未评估 RTX 3090 显存对大模型推理的延迟影响。

#### 💡 补全建议 (Suggested Completions - Choose One)

- [ ] **Option A (MVP)**: 仅调整 Prompt，验证用户反馈。（耗时：15min）
- [x] **Option B (架构)**: 启动小酷设计本地化推理流程。（需投入资源较多）

#### 📈 进化路径 (Evolution Path)

- Phase 1: 完成场景定义（本周内）。
- Phase 2: 若 Option A 验证通过，再考虑 Option B。