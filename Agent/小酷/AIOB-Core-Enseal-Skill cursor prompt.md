。

---

### 第一阶段：环境准备

在 Cursor 中新建一个文件夹 `AIOB_Tools`，并在其中创建两个文件：

1. `enseal_skill.py` (核心代码)
    
2. `requirements.txt` (填入 `pyyaml`)
    

---

### 第二阶段：Cursor 指令 (The Ultimate Prompt)

**请将以下这段文字直接贴给 Cursor 的 Chat 界面（建议使用 Claude 3.5 Sonnet 模式）：**

> **Role**: 你是一名顶级的 Python 架构师，擅长自动化治理与文件系统操作。
> 
> **Task**: 请开发一个名为 `AIOB-Core-Enseal-Skill` 的 Python 工具，用于将原始文本物理拆分为 L1(Note), L2(Card), L3(Audit) 三个文件。
> 
> **Core Logic (参考 V2.2 规范与审计蓝皮书)**:
> 
> 1. **物理拆解 (AAA Standard)**:
>     
>     - 输入一段 Markdown 文本后，根据传入的 `file_id` 在指定目录下生成或更新三个文件。
>         
>     - `note.md`: 仅保留 Frontmatter 索引。
>         
>     - `.card.yaml`: 存储提炼的语义摘要，`embedding_access` 必须设为 `true`。
>         
>     - `.audit.yaml`: 存储治理存证，`embedding_access` 必须设为 `false`，但 `logic_access` 设为 `true`。
>         
> 2. **增量审计逻辑 (Incremental Audit)**:
>     
>     - **Diff 检查**: 如果文件已存在，读取旧的 `.audit.yaml`，对比新旧版本差异。
>         
>     - **血缘继承**: 必须从旧文件中读取 `legacy_metadata` 并合并到新生成的 L3 文件中，严禁丢失历史字段。
>         
>     - **审计日志**: 在 `history_logs` 中追加一条包含 `date`, `agent_id`, `version="V2.2"` 和 `note` (变更摘要) 的记录。
>         
> 3. **认知共情注入**:
>     
>     - 必须包含一个 `audit_thoughts` 节点，接受传入的 `thoughts` 参数，记录统帅或 AI 的决策理由。
>         
> 4. **异常预警**:
>     
>     - 若 `importance` 发生降权或 `file_id` 不匹配，自动将 `review_status` 设为 "Pending"。
>         
> 
> **Output Requirement**:
> 
> - 代码需模块化，包含 `EnsealEngine` 类。
>     
> - 提供一个简单的命令行接口 (CLI) 用于测试输入。
>     
> - 确保 YAML 输出时保持 ISO8601 时间格式。
>     

---

### 第三阶段：执行方案 (Step-by-Step Action Plan)

#### Step 1: 核心逻辑跑通 (1-2 小时)

- **动作**: 让 Cursor 生成代码后，你先手动运行 `python enseal_skill.py` 进行一次模拟拆分。
    
- **验证**: 检查你的文件夹里是否真的出现了三个文件，且 `.audit.yaml` 里是否正确记录了 `audit_thoughts`。
    

#### Step 2: 审计 Diff 测试 (1 小时)

- **动作**: 再次运行脚本，传入相同的 `file_id` 但修改正文内容。
    
- **验证**: 查看 `.audit.yaml` 里的 `history_logs` 是否变成了两条记录，且旧的元数据（Legacy Metadata）是否还在。
    

#### Step 3: Dify 适配 (1 小时)

- **动作**: 让 Cursor 将这个 Python 脚本封装成一个简单的 FastAPI 接口（或者直接作为 Dify 的 Custom Tool 代码）。
    
- **验证**: 在 Dify 界面上传这个工具，测试能否通过 API 成功在你的本地磁盘生成文件。
    

---

### 🛡️ 统帅开发秘籍 (Pro Tips for Kenny)

1. **“喂”入原始规范**: 在 Cursor 开发过程中，如果它写错了，立刻把《YAML V2.2 规范》和《审计蓝皮书》的内容复制一段发给它，并说：“**注意，规范第 X 条明确要求 L3 严禁向量化，你的代码里 `embedding_access` 写错了，请修正。**”
    
2. **强制要求注释**: 要求 Cursor 在代码的关键位置写上中文注释，标明这里对应的是规范的哪一条（例如：`# 对应 V2.2 原则 08：基因继承`）。这能帮你这个非开发人员快速理解代码。
    
3. **安全性检查**: 提醒 Cursor 不要使用会破坏文件系统权限的库，确保 `00_Cabinet` 目录的安全。
    

