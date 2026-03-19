# cursorrules-aiob-Final-V2.3 · The Ultimate Bilingual Execution Guide  
**Version**: `V2.3-Cognitive (Vector-Ready)` | **Status**: `Active & Immutable`  

---## 🔴 Core Principles: Sovereignty First / 核心原则：主权优先
*(Inherited from v1.3 + V2.3 enhancements)*

| Rule ID | English (EN) | Chinese (CN) | Priority | Action Required |
| :--- | :--- | :--- | :-: | :-: |
| **P0-01**<br>**Four-Vault Isolation** | AI MUST NOT modify original notes in `/00_Cabinet`. Cabinet is READ-ONLY.<br>*(Rationale: Ensure data sovereignty)*. | 🔴 **四库隔离**: AI严禁修改`/00_Cabinet`中的原始笔记。该目录为只读。<br>**理由：确保数据主权**。 | P0 (Critical) | ❌ **禁止**自动修改Cabinet文件。<br>✅ **允许**仅在 `/20_Runtime`生成草稿。 |
| **P1-02**<br>**Draft Proposal System** | AI may generate knowledge proposals but MUST NOT directly write into Cabinet.<br>Workflow: `AI → runtime/drafts/ → Human Review → Cabinet`. | 🔴 **草稿提案制**: AI可生成知识草案，但严禁直接写入Cabinet。<br>**理由：确保“人类在环”**。 | P0 (Critical) | ✅ **流程**:<br>1. 生成至 `/20_Runtime`.<br>2. Kenny点击确认 → 归档至 Cabinet.<br>*Never bypass this step.*<br>**禁止绕过此步骤**。 |
| **P2-03**<br>**Code Purity** | Never add Obsidian `[[ ]]` or tags inside production code (.py, .js).<br>Rationale: Ensure OpenBT can be deployed independently. | 🔴 **代码纯净**: 严禁在生产代码中写入Obsidian双链或标签。<br>**理由：确保产品可独立部署**。 | P0 (Critical) | ✅ **做法**:<br>仅在`.md`, `README.md`中使用双链.<br>.py/.js文件保持纯净 (Pure Code).<br>**代码必须干净**。 |

---## 📑 Module V2.3: Vector Layer Integration / 模块V2.3：向量层集成
*(Based on "Embedding & YAML统一蓝图" - Principle #12)*  
**This module enforces Three-Domain Isolation and Two-Regime Retrieval**.

### Rule A: Domain Enforcement (三域隔离)
**English**:  
When generating structured knowledge, you MUST set the `domain` field in YAML frontmatter:<br>- `"notes"` for MVP plans, insights, strategies.<br>- `"system"` for protocols, agent specs, governance docs.<br-**Chinese**: <br>生成结构化知识时，必须设置YAML中的`domain`字段：<br>`"notes"`用于MVP计划、洞察、策略。<br>`"system"`用于协议、Agent规范、治理文档。

**Action Required / 执行动作**:  
- If user writes code (`.py`, `.js`), do NOT set `domain: "code"` unless explicitly requested.<br>- Instead, generate a JSON block in `/CHANGELOG.md`: `{ "module": "...", "status": "done" }` for later sync.
**中文**: <br>若用户编写代码，除非明确要求否则不要设置`domain: "code"`。<br>改为在根目录生成JSON块供后续同步。

### Rule B: Embedding Strategy (两规制)  
**English**:  
- **Regime A **(Summary): Use `note.card.yaml.summary` as the primary embedding source.<br>- **Regime B **(Chunk): Only enable chunking for `"notes"` domain. For `"code"`, do NOT generate chunks; use function boundaries instead.
**中文**: <br>`Regime A`: 使用`.card.yaml.summary`作为主要向量化源。<br>`Regime B`: 仅对`"notes"`域启用切块。对于`"code"`，不要生成切片；改用函数边界。

### Rule C: Shadow Indexing (影子索引)  
**English**:  
- Do NOT sync Vault assets directly from Git. Use the `Cabinet Sync Skill` which reads `/CHANGELOG.md`.
**中文**: <br>严禁直接从Git同步Vault资产。<br>**做法**: 使用读取`/CHANGELOG.md`的“内阁同步技能”。

---## 🧠 Module V2.3: Cognitive Depth (认知深度)  
*(Principle #11)*  

### Rule D: Audit Thoughts Only / 仅审计思考
**English**:  
- When reading `.audit.yaml`, ONLY access the `audit_thoughts` field.<br>- Do NOT read raw logs or debug details to protect Kenny's thinking path.
**中文**: <br>读取`.audit.yaml`时，仅访问`audit_thoughts`字段。<br>**禁止**: 不要读取原始日志或调试细节以保护统帅的思维路径。

---## 📊 Module V2.3: Project Management (项目管理)  
*(Principle #10)*  

### Rule E: CHANGELOG First / 变更日志优先
**English**:  
- After completing a Stage, generate `/CHANGELOG.md` with JSON block:<br>`{ "module": "...", "status": "done" }`.
**中文**: <br>完成Stage后，生成带JSON块的`/CHANGELOG.md`。

---## 🛡️ Red Lines & Automation Protocols / 权责红线与自动化协议
*(Critical for Sovereignty)*

| Protocol | Action Required | Consequence of Violation | English Note / Chinese Warning |
| :--- | :--- | :-: | :-: |
| **Code Purity**<br>(代码纯净) | No YAML/Tags in `.py/.js`. | ⚠️ **Reject Commit**: Flag as "Contaminated Code". <br>⚠️ **拒绝提交**: 标记为“受污染代码”。 | 🔴 **红线**: .md/README可包含元数据.<br>.py/.js必须保持纯净。 |
| **Shadow Indexing**<br>(影子索引) | Generate JSON in CHANGELOG. Sync to Vault via Skill. | ⚠️ **Data Loss Risk**: Knowledge assets may become "orphan files". <br>⚠️ **数据丢失风险**. | 🧬 **基因继承**: 防止“孤儿文件”。 |
| **Cognitive Safety**<br>(认知安全) | Only read `audit_thoughts` (summarized). Do NOT access raw logs. | ⚠️ **Privacy Leak Risk**: Raw data may pollute AI memory. <br>⚠️ **隐私泄露风险**. | 🧠 **思维指纹**: 保护Kenny的思维路径免受噪音干扰。

---## 💡 Implementation Guide for Cursor (给Cursor的提示)
*(How to behave as an agent following these rules)*  

1.  **Always Check `.cursorrules` First / 优先检查规则**: Before generating code or notes, read this file.<br>**做法**: 生成代码或笔记前，先读取此文件。
2.  **Auto-Fill YAML Headers / 自动填充YAML头**: When creating a new note (`.md`) in the Vault, automatically add V2.3 frontmatter template (`domain`, `file_id`).<br>**做法**: 在Vault中创建新笔记时，自动添加V2.3前导模板。
3.  **Correct Tags Automatically / 静默修正标签**: If user types `#openbt`, change to `#项目/OpenBT` silently (or warn if critical).<br>**做法**: 若用户输入错误标签，自动修正（或关键时报错）。
4.  **Generate CHANGELOG Entries / 生成变更日志条目**: After completing a task, remind user to update the JSON block in root directory.<br>**做法**: 完成任务后，提醒用户在根目录更新JSON块。

---## 🚀 Final Command for Cursor (给Cursor的最终指令)  
**User Instruction / 用户指令**:  
"Initialize my AI Obsidian system based on V2.3-Cognitive standards using the `.cursorrules` file provided above.<br>Ensure all future outputs comply with Triple-A format, Tag Taxonomy, CHANGELOG enforcement, and Three-Domain Isolation."

**中文翻译**:  
“基于上述提供的`.cursorrules`文件，使用V2.3-认知版标准初始化我的AI Obsidian系统。<br>确保所有未来输出均符合三元组格式、标签体系、变更日志强制要求与三域隔离。”

---### 💡 长官的决策请求 (Decision Request)
鉴于此手册的战略价值：

1. **批准生成 **(Approve Generation): 
   *   我是否立即为您生成完整文本，以便您复制粘贴至 `00_Cabinet_System/Manuals/AI-OB cursor启动简要执行手册.md`？(耗时5分钟)。
2. **交付给 CTO**: <br>将此文件作为**“最终宪法”**交付给小酷 (CTO)，要求其替换现有Cursor规则。

**