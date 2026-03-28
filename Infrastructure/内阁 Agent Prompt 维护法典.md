# 内阁 Agent Prompt 维护法典 (P2 规范版)

**版本**：v2.3 (Function-Oriented)

**状态**：#Approved

**核心原则**：**将 Prompt 视为代码；逻辑函数化，引用标准化。**

**v2.3 修订**：存储拓扑与现网一致——目录名 **`Agent`**（单数）；L0 正文以 **`Agent/Prompts/Base_L0.md`** 为 SSOT，`Infrastructure/Prompts/Base_L0.md` 仅为转发桩。技能 YAML 示例中增补 **`imports` 符号 → vault 路径** 注释。

---

## 一、函数化存储拓扑 (Functional Topology)

内阁 Prompt 体系按**层级调用**组织，类比函数库；物理目录统一为 **`000_Cabinet_System/Agent/`**（不用 `Agents` 复数，避免文档与 vault 分叉）。

### 1. L0：静态基座 (Static Base)

- **SSOT 路径**：`000_Cabinet_System/Agent/Prompts/Base_L0.md` —— **只在此处维护正文**。
- **兼容桩**：`000_Cabinet_System/Infrastructure/Prompts/Base_L0.md` 指向上述真源，供旧链接与习惯路径；勿双写。
- **内容**：全局常量——系统宪法、Kenny 身份底色、全局语气与禁忌的**唯一权威**；Workflow 级**禁止**复述同一段风格说明。

### 2. L1：职能类 (Agent Class)

- **路径**：`000_Cabinet_System/Agent/[Agent名]/[Agent名]_职能定义.md`（若与现网「小憶说明书」等并存，可逐步收敛为此命名）。
- **内容**：**实例化**一个 Agent：声明 **Inherit** 哪些 L0 准则；**Attributes**（负责域、默认边界、工具/数据范围等）宜短列表化，避免与 L2 冗长重复。

### 3. L2：执行函数 (Action Functions)

- **路径**：`000_Cabinet_System/Agent/[Agent名]/Workflows/[技能名]_vX.md`
- **内容**：原子化 **Implementation**，只解决一个明确业务问题；命名与版本后缀 `_vX` 与 Obsidian 文件名一致。
- **现网兼容**：历史 Prompt、专题子目录（如 `Kenny画像/`、`4g梳理/`）可与 `Workflows` 同级存在；**新建**、且需同步 Dify 的技能，**优先**落入 `Workflows/`，便于检索与向量化。

---

## 二、技能文件 (L2) 的函数式标准格式

每个技能文档须像 **API 接口** 一样可扫读，避免长篇叙述。

### 1. 函数声明 (Metadata Header)

```yaml
---
fn_id: "REFINERY_CORE"
version: "2.3"
implements: "Cognitive_Induction" # 受控词表或团队约定枚举，便于检索与向量化标签
# imports：符号名 → Obsidian 真源路径（团队约定；同步 Dify 时展开正文，非把本行原样粘贴）
#   Base_L0          → 000_Cabinet_System/Agent/Prompts/Base_L0.md（SSOT）
#   Kenny_Profile_v1 → 如 Agent/小忆/Kenny画像/ 下既定画像 md，或 Dify 变量 {{KENNY_PROFILE}} 的供给源
imports: ["Base_L0", "Kenny_Profile_v1"]
runtime_binding: "Dify_Node_Refinery_Agent" # 对应 Dify 内节点/应用名，与运维表一致
last_sync: "2026-03-28"
---
```

`imports` 为**逻辑依赖名**；落盘时以第一节 L0/L1 路径为准，避免与 `Infrastructure/Prompts/Base_L0.md`（转发桩）混淆。

### 2. 逻辑体 (Logic Body)

**用指令取代描述**，固定区块如下：

- **`[IMPORT]`**  
  Obsidian 源码中可写 `Call Base_L0` 等符号化引用。  
  **拼接顺序（同步/打包时）**：`Base_L0`（及 `imports` 所列）→ **本函数** `[ACTION]` / `[STEPS]` / `[CONSTRAINTS]`；与 Dify 侧「系统 Prompt / 知识库 / 变量」的映射由 `runtime_binding` 与运维约定表维护。

- **`[ACTION]`**  
  一句话定义本函数职责（例如：对给定对话块执行 DIFF 并输出 Patch）。

- **`[STEPS]`（函数体）**  
  **动词开头**、可机读的步骤名，例如：

  1. `PRE_PROCESS`：识别输入中的角色与时间锚。
  2. `ANALYZE_DIFF`：对比当前画像，锁定 New / Change / Delete 信号。
  3. `OUTPUT_STRUCTURE`：封装为约定 Patch 或 JSON 结构。

- **`[CONSTRAINTS]`（断言与失败策略）**  
  - `ASSERT`：硬性不变量（如严禁改写历史 `Ref_ID`）。  
  - `ON_FAILURE`：无法判定时的出口（如统一标记 `#Review`）。  
  **说明（Gap Engine）**：本节即原「行为红线」的**结构化承载**；审计与越界检测以 **`[CONSTRAINTS]`** 为权威，不再要求单独的 `## 🚫 行为红线` 标题；若需人读摘要，可在 CONSTRAINTS 下用 bullet 复述，避免两处矛盾。

### 3. I/O 契约 (I/O Schema)

- **Input**：例如 `{{dialogue_block}}` 或 `inbox_manifest.jsonl` 派生字段（与团队数据契约一致即可）。
- **Output**：例如 `{{structured_json_patch}}` 或 `Memory_Patch.md`。  
  须与 Dify 节点变量、下游脚本字段**同名或显式映射**。

---

## 三、提炼效能：Prompt 简写语法 (Short-hand)

1. **逻辑算子化**：将自然语言长句收敛为算子式指令，如 `EXTRACT(...)`、`CLASSIFY(...)`。
2. **Few-Shot 占位**：正文用 `[[Example_Case]]` 指向示例库文档，**不把**长 few-shot 塞进每个 Workflow。
3. **环境继承**：已在 `Base_L0` 定义的风格、安全与输出格式，**禁止**在 L2 重复粘贴。

---

## 四、维护操作流 (DevOps for Prompts)

1. **单点维护**：修改某一技能逻辑时，**仅**改对应 `Agent/.../Workflows/[技能名]_vX.md`（或该 Agent 目录下既有的同名技能文件），避免在 Dify 上直接改漂移。
2. **Obsidian 为源码真相**：YAML、`[CONSTRAINTS]`、I/O 说明以 vault 为准。
3. **同步至 Dify**：  
   - **默认**：仅将 **Logic Body**（`[IMPORT]` 展开后的必要片段 + `[ACTION]` + `[STEPS]` + `[CONSTRAINTS]`）粘贴/注入节点系统 Prompt，保持线上**脱水**。  
   - **版本追溯**：Dify 应用说明、命名或环境变量中须能对应到 **`fn_id` + `version`**（可与 `last_sync` 同表维护），避免线上无法反查 Obsidian revision。  
4. **重大变更**：架构级调整（如 Agent 拆分）在 `CHANGELOG` 中记录 `Ref_ID`（与工具链惯例对齐）。

---

## 五、P2 演进预留 (Future Proofing)

- **Gap Engine**：以 L2 的 **`[CONSTRAINTS]`**（含 `ASSERT` / `ON_FAILURE`）为自动对比与越界检测的输入；新增约束时优先改此块并保持可解析。
- **Qdrant / Memory OS**：Prompt 文件将向量化作为元指令集；`fn_id`、`implements`、YAML 中的 `tags`（若增补）用作索引与过滤维度。

---

## 六、与执行环境的关系（非本文详述，须一致）

- **物理主权 (PSR)**、**inbox**、**晋升 SSOT** 等由 `cabinet_sentinel`、`dialog_inbox`、`enseal` 等工具与运维法典约束；本文件仅要求：**Prompt 层**不宣称绕过 Kenny 审批与 enseal 的自动升格。
