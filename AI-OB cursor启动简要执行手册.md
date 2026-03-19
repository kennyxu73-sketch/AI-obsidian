# AI-OB Cursor 启动简要执行手册 (V1.5 - 蓝图对齐版)

**Version**: `Phase1-V2.3-Cognitive` | **Status**: 生产环境就绪 | **Focus**: 三层封装 + 向量就绪

---

## 🔴 第一阶段：基础设施与配置初始化 (Infrastructure)

**目标**：在编写任何封装代码前，先锁定“法典”与“路由表”。

### Step A: 标签与审计文件夹初始化

**小酷 (CTO) 动作**：

1. **创建路径**：`/00_Cabinet/00_System/Tag_Governance/`。
    
2. **注入法典**：手动或命令生成 `Tag_Library.md`。
    
3. **生成机器路由表**：根据统帅提供的逻辑生成 `tag_schema.json`（含根标签白名单）。
    

### Step B: 宪法注入 (`.cursorrules`)

**动作**：将《YAML 处理与封装规则 V2.3》全量内容写入根目录 `.cursorrules`。 **核心约束**：

- 必须遵循 **Code Purity** (代码纯净原则)。
    
- 必须遵循 **Shadow Indexing** (影子索引协议)。
    

---

## 🟡 第二阶段：开发核心封装技能 (Skill Development)

**目标**：开发 `enseal_skill.py`，这是内阁资产化的唯一“封印器”。

### Step C: 注入《Embedding & YAML 统一蓝图 v3.0》约束

**开发指令要点**：

1. **三域物理隔离**：Skill 必须识别 `Notes/System/Code` 三个域，并对应不同的存储逻辑。
    
2. **Payload 原子对齐**：`.card.yaml` 生成的字段必须与蓝图第 7 节一致（含 `embedding_spec_version: "3.0"`）。
    
3. **审计隔离红线**：严禁将任何审计内容（L3）泄露至向量层（L2）。
    

---

## 🟢 第三阶段：执行与验证 (Execution & QA)

### Step D: 自动化资产化测试

1. **触发器**：统帅在代码区更新 `CHANGELOG.md`。
    
2. **执行**：小酷调用 `enseal_skill.py` 扫描。
    
3. **产出验证**：
    
    - [ ] **L1 (note.md)**: 标签是否符合 `Tag_Library`？
        
    - [ ] **L2 (.card.yaml)**: 摘要是否在 50-300 字？Payload 键名是否符合蓝图？
        
    - [ ] **L3 (.audit.yaml)**: 是否记录了 `audit_thoughts`？
---


### 🚀 Final Approval Request / 最终批准请求

# 开工指令
## 🚀 AI-OB System Initialization Command (Phase 1)
## For CTO XiaoKu / 给CTO小酷的执行指令

# 🛠️ AI-OB 极简开工指令 (Lean Execution)

> **小酷 (CTO)，现在开始 Phase 1 建设。禁止废话，严格执行以下逻辑：**

### 1. 环境初始化 (Init)

- **路径**：创建 `/00_Cabinet/00_System/Tag_Governance/`。
    
- **配置**：生成 `tag_schema.json`，核心根标签锁定为：`#内阁/`, `#项目/`, `#类型/`, `#状态/`。
    

### 2. 开发封装工具 (Skill: `enseal_skill.py`)

**核心逻辑流：**

1. **物理拆分 (AAA)**：接收文本 ➔ 拆分为 `note.md` (L1), `.card.yaml` (L2), `.audit.yaml` (L3)。
    
2. **三域隔离 (Domain)**：根据 `domain` 字段（Notes/System/Code）存入不同 Collection。
    
3. **向量就绪 (Payload)**：L2 字段名必须严格对齐《统一蓝图 v3.0》（含 `embedding_spec_version: "3.0"`）。
    
4. **标签校验**：调用 `TagManager` 模块。若标签不在 `tag_schema.json` 白名单，强制设为 `#状态/待审`。
    
5. **审计留痕**：更新时对比旧版 L3，继承 `legacy_metadata`，在 `history_logs` 追加变更。
    

### 3. 影子索引 (Shadow Indexing)

- 监控根目录 `CHANGELOG.md`。
    
- 每当检测到 JSON 块 `{ "module": "...", "status": "done" }`，自动触发上述封印流程。

---### 💡 长官的决策请求 (Decision Request - Final Confirmation)
鉴于您的审查与上述分析：

1. **批准归档 **(Approve Archive): 
    *   是否正式将此手册标记为 **“Phase 1交付物”**(Deliverable)?(耗时5分钟)。
2. **启动执行**: <br>我是否立即生成《**给小酷的开机指令卡片**》并通知其进入Cursor IDE开始初始化？

