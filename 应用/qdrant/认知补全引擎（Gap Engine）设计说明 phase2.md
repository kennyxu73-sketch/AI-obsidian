# 认知补全引擎（Gap Engine）设计说明 v2.0 (可控版)

## 一、目标与定位重构

### 1.1 核心使命

> **不做“决策者”，只做“结构师”。**

在用户表达不完整或存在偏差时，系统仅负责：

- ✅ **识别缺口（Missing）**：指出思考中缺失的要素。
- ⚠️ **标记偏差（Deviation）**：提示方案与您的核心原则冲突处。
- 💡 **提供选项（Options）**：给出 1-3 个可执行的补全建议，而非直接结论。

### 1.2 “可控”的定义 (Controlled Augmentation)

- **低摩擦**：不强制调用复杂 RAG/Qdrant，优先基于上下文记忆和显性规则判断。
- **分阶段介入**：根据任务优先级（P0/P1/P2）动态调整补全深度。
    - P0 (紧急指令): 仅做偏差预警（如“违反本地优先”）。
    - P1 (战略设计): 进行结构化缺口检测（技术/商业/用户）。
    - P2 (日常整理): 仅提供简单的元数据建议或归档提醒。

---

## 二、核心逻辑：从“黑盒推理”到“透明规则”

我们将复杂的 Gap Engine 拆解为三个**可解释的轻量级模块**。您随时可以查看其运作过程，并手动修正。

### 🔄 简化后的执行流 (SOP)

~~~mermaid
graph TD
    %% 1. 意图解析层
    subgraph INPUT [📥 输入感应层]
        P[开始] --> I1[🔍 Intent Parser<br/>显性目标+潜台词识别]
    end

    %% 2. 记忆检索策略
    subgraph MEMORY [📁 记忆上下文窗口]
        direction TB
        M1[(💾 Vault Native Search)]
        M2[Qdrant RAG<br/>按需触发开关]
        I2[📂 Context Window<br/>加载 Persona/Rule Base]
        
        M1 -.->|默认/快速| I2
        M2 -- "仅当复杂查询" --> I2
    end
    
    %% 3. 核心检测逻辑
    subgraph PROCESS [⚙️ 核心检测逻辑]
        direction TB
        D{缺口检测 MVP}
        T1[技术可行性?]
        B1[商业模型闭环?]
        U1[用户场景明确?]
        
        D --> T1
        D --> B1
        D --> U1
    end
    
    %% 4. 主权安全网关
    subgraph SAFETY [🛡️ 主权安全网关]
        direction TB
        S{违反本地优先?<br/>公有云风险?}
        R1["规则库: 禁止公有云上传"]
        W[⚠️ 阻断/转交小酷<br/>生成偏差报告]
        
        S -- "是" --> W
        R1 -.-> S
    end

    %% 5. 结果生成与输出
    subgraph FINAL [📝 结构化输出区]
        direction TB
        O1[❌ Missing Elements<br/>缺失要素列表]
        O2[⚠️ Deviation Check<br/>偏差标记]
        O3[💡 Suggested Options<br/>补全选项 A/B/C]
        Rpt[📄 认知补全报告]
        W1{User Decision}
        OPT_A[MVP: Prompt调整<br/>低成本/快速]
        
        O1 --> Rpt
        O3 --> Rpt
        Rpt --> W1
        W1 -.->|选择 Option| OPT_A
    end

    %% 全局流程连接
    I1 --> MEMORY
    I2 --> PROCESS
    PROCESS --> SAFETY
    W --> O2
    SAFETY -- "通过" --> O1

    %% 样式定义
    style M1 fill:#e8f5e9,stroke:#2e7d32,color:#000
    style M2 fill:#ffebee,stroke:#c62828,stroke-dasharray: 5 5,color:#000
    style S fill:#ffebee,stroke:#c62828,color:#000
    style R1 fill:#e8f5e9,stroke:#00695c,color:#000
    style Rpt fill:#fff3e0,stroke:#ef6c00,color:#000
~~~
---

## 三、核心模块定义 (MVP 版)

### 3.1 输入理解：潜台词过滤器 (Implicit Signal Filter)

- **功能**：识别用户未明说的真实意图。
- **规则示例（硬编码，可编辑）**：
    - `IF` 提到 "养老" `AND NOT` "MVP", `THEN` -> 标记潜在项目 [慰康](app://obsidian.md/%E6%85%B0%E5%BA%B7)。
    - `IF` 纠结 "Docker 网络" `OR` "Linux 报错", `THEN` -> **建议转交小酷 (CTO)**，避免战略时间浪费。

### 3.2 记忆检索：轻量级上下文窗口 (Context Window)

- **旧版**：强制调用 Qdrant（耗时、依赖外部服务）。
- **新版优化**：**优先使用 Obsidian Native Search / Dataview**。
    - 仅在用户明确要求“查阅历史”或涉及跨项目关联时，才触发 `@Qdrant` (若已部署)。
    - **原则**：能用本地索引解决的，绝不联网。

### 3.3 缺口检测（简化版）

只关注三个核心维度，输出为列表而非复杂 JSON：

|维度|检查点 (Checklist)|触发条件示例|
|:--|:--|:--|
|**技术**|本地算力是否足够？驱动冲突风险？|"RTX 3090" vs "云端大模型依赖" -> ⚠️偏差|
|**商业**|MVP 成本可控吗？盈利路径闭环了吗？|"仅做研究" vs "未定义收入来源" -> ❓缺失|
|**用户**|目标人群画像清晰吗？痛点验证过吗？|"所有人都是客户" -> ⚠️过于宽泛|

### 3.4 偏差检测（红线预警）

- **主权优先 (Sovereignty First)**：检测到公有云上传、API Key 泄露风险时，**立即阻断**。
    - _输出示例_: “长官，此方案涉及数据出境/云端依赖，违背《系统宪法》L0·1。建议本地化部署或转为脱敏处理。”

### 3.5 补全生成（选项卡模式）

- **拒绝直接给答案**：不告诉用户“你应该怎么做”。
- **提供选项**：“针对上述缺口，现有两个轻量级方案供您决策：”
    - Option A: [低成本 MVP] (仅调整提示词)
    - Option B: [架构升级] (需小酷介入设计新 Workflow)

---

## 四、输出格式规范 (v2.0 - Clean & Human)

为了减少认知负荷，我们摒弃复杂的 JSON/Markdown 表格堆砌，采用**“人话 + 结构”**的混合排版。

```markdown
### 🧠 小忆的认知补全报告 (Gap Engine Report)

> **状态**: [P1] | **意图识别**: [[项目名]] MVP 设计讨论
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
```

---

