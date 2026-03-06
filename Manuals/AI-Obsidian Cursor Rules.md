
# AI-Obsidian Cursor Rules (v1.9)

本规则用于约束 **AI-Obsidian 工作系统**中 Cursor 生成代码、文档和自动化逻辑的行为。  
目标是确保系统 **长期可维护、可审计、可扩展**，并与本地及云端算力调度保持一致。

---

# 1. Repository Governance（存储库治理）

系统采用 **双层治理结构**：

## System/ （Authoritative Layer - 宪法层）
内容包括：架构准则、安全分级、项目治理逻辑。  
**原则**：所有技术实现必须有 System 依据。

## Tools/ （Implementation Layer - 实现层）
内容包括：Skill 工具、自动化脚本、n8n Workflow。  
**原则**：Tools 的变动必须反馈至 System 进行逻辑对齐。

核心规则：

- **System 决定 Tools**
- 若 Tools 变动没有 System 依据 → 视为 **技术漂移 (Technical Drift)**
- 若 System 更新但 Tools 未同步 → 视为 **逻辑断层 (Logic Break)**

---

# 2. Role Switching & Inference Logic（角色与算力调度）

Cursor 必须根据文件路径和数据等级切换思考模式及算力建议：

### A. 编辑 `.py` / `.js` (CTO 模式)

重点关注：

- 3090 本地算力适配
- n8n 接口兼容
- API 健壮性

算力建议：

- **L1/L2 级逻辑**  
  建议使用 **本地 3090 (DeepSeek-R1-Local / Qwen)**

- **复杂算法 / 大规模重构**  
  建议使用 **云端 DeepSeek-V3 / Claude**

禁忌：

- 禁止不必要的复杂封装
- 禁止破坏本地优先的数据流

---

### B. 编辑 `System/` 下 `.md` (架构师模式)

重点关注：

- 架构逻辑一致性
- 安全分级合规
- 与 **慰康 / 憶镜项目战略对齐**

算力建议：

- 可使用 **云端高智力模型（DeepSeek / Claude）进行逻辑推演**
- **禁止上传 L1 级私密数据**

---

# 3. Mandatory Change Summary（强制变动摘要）

在执行任何重大修改或提交前，Cursor 必须输出以下格式的预检报告：

```
[内阁审计预检]

关联法典：[[相关 System 文件路径]]

涉及工具：
filename.py / skill_xxx / workflow_xxx

安全等级：
L1 | L2 | L3 | L4

算力建议：
本地 3090 / 云端 DeepSeek

联动建议：
例如：因 Tools 变动，需更新 System 第 2.1 章节
```

---

# 4. Network & Path Safety（安全规范）

### 网络安全

禁止：

- 硬编码公网 IP
- 直接连接未知云端 API

规范：

优先使用：

- **ZeroTier IP (10.147.17.x)**
- **Docker 服务名**

---

### 路径安全

禁止泄露：

```
/Users/kenny/
/home/kenny/
```

统一替换为：

```
/workspace/
/local/path/
```

---

# 5. Security Classification（数据安全分级）

| Level | 类型 | 处理原则 | 算力选择 |
|------|------|------|------|
| L1 | 核心内阁数据 | 严禁离境 | 仅限本地 3090 |
| L2 | 私有项目数据 | 敏感处理 | 本地优先 / 受控云端 |
| L3 | 可交换数据 | 效率优先 | 云端 DeepSeek / Claude |
| L4 | 公共数据 | 全量开放 | 云端 DeepSeek / GPT |

---

# 6. Skill & Tool 标准接口规范

所有在 `Tools/` 下生成的 Skill 必须支持 **原子化调用结构**：

### 输入

```
task
context
metadata
```

### 输出

```
result
summary
status
```

### 兼容要求

必须兼容：

- **n8n Webhook 触发**
- **Dify Tool 调用协议**

---

# 7. Agent Collaboration Protocol（协作协议）

系统支持多 Agent 协作。

主要 Agent：

| Agent | 角色         |
|------|------|
| 小憶 | Daily 工作助手 |
| 小镜 | 憶镜 2C 用户服务 |
| 小康 | 慰康 2B 养老服务 |
| 小酷 | 审计与技术守护    |
| 小报 | 资讯收集与整理+   |

协作模式：

```
Agent 提议
      ↓
审计小酷 (Dify)
      ↓
Kenny 最终决策
```

---

# 8. Automation Stack（运行架构约束）

Cursor 生成的任何代码或自动化逻辑  
必须默认兼容 **AI-Obsidian 的运行架构**：

```
Workflow Orchestration
    n8n

Agent Runtime
    Dify

Model Gateway
    OneAPI

Knowledge Source
    Obsidian

Local Inference
    RTX 3090
```

禁止生成不必要的额外运行层，例如：

- 独立 LangChain Server
- 冗余 Agent 框架
- 未授权云服务

---

# 9. Default Security Level（默认安全等级）

如果某个任务 **未声明 security_level**：

默认规则：

```
security_level = L2
```

含义：

- 视为 **私有项目数据**
- **禁止直接发送到外部云端 API**
- 必须优先使用 **本地 3090 模型处理**

---

# 10. Knowledge Access Protocol（知识访问协议）

当 Cursor 或 Agent 需要读取 **Obsidian 知识库**时  
必须遵循以下优先顺序：

```
1.System/      (架构与法典)
2. Project/     (具体项目资料)
3. Knowledge/   (研究资料)
4. Logs/        (系统日志)
5.  Archive/    (历史记录)
   ```

原则：

- **System 优先级最高**
- 技术实现必须遵守 System 的规则

# 11. Implementation & Conflict Resolution（执行与冲突解决）

当 Cursor 在执行任务时遇到矛盾，必须遵循以下优先级进行决策：

1. **安全优先**：若“实现功能”与“Section 5 (数据安全分级)”冲突，必须优先选择安全（即切换至本地 3090）。
    
2. **法典优先**：若“用户口头指令”与“System/ (宪法层)”冲突，必须提醒用户：“此指令可能导致技术漂移，建议先更新 System/ 法典。”
    
3. **本地优先**：所有 `Tools/` 层的逻辑生成，默认必须包含在 3090 上进行测试的选项或说明。
    

# 12. Self-Correction Mechanism（自我修正机制）

Cursor 在生成任何 `Skill` 或 `n8n workflow JSON` 后，必须进行最后一次“影子审计”：

- **自检项 1**：代码中是否包含硬编码的个人路径？（Section 4 检查）
    
- **自检项 2**：接口是否符合 `task/context/metadata` 结构？（Section 6 检查）
    
- **自检项 3**：是否已经将变动同步到了 `Mandatory Change Summary`？（Section 3 检查



---

# Note（系统守护原则）

如果 Cursor 发现用户指令违反任何规则  
尤其是 **L1 数据外泄风险**：

必须：

```
停止执行
提出安全警告
建议替代方案
```

---

# End of Document
AI-Obsidian Cursor Rules v1.9