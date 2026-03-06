# n8n 自动化枢纽与数据交换标准 (v1.5)

## 1. 文档目的与系统定位

本文件定义了 **AI-Obsidian** 体系中 **n8n** 作为“自动化工作流引擎”与“接口编排层（Orchestration Layer）”的核心职责。它连接了 3090 私有算力、Obsidian 知识库与外部云端 AI 服务。

**n8n 的角色：** 异构系统的自动化调度与数据交换中枢。

- **核心逻辑**：本地优先、先审后发、数据分级、流程中心化。
    1. 自动化流程编排
    2. 数据安全分级检查
    3. 外部AI调用代理
    4. 系统审计日志汇总
    5. 跨网络数据桥接
n8n 不承担：
- AI推理计算
- 知识库存储
- 用户交互界面
---

## 2. 系统拓扑与网络边界

数据跨越三个网络平面流转，n8n 负责物理隔离与协议转换。

- **L1：私有算力层 (3090 Cluster)**：运行 Dify、Ollama。数据通过 Docker 内部网络交互。
    
- **L2：虚拟骨干层 (ZeroTier V-LAN)**：连接手机、移动设备。允许安全穿透访问内网审计报告。
    
- **L3：公共代理层 (External API/Proxy)**：连接企微、GitHub、OneAPI。

所有 n8n workflow 必须遵循标准结构：

Trigger
↓
Security Level Check
↓
Data Sanitization
↓
AI Invocation
↓
Audit Logging
↓
Result Output
---


## 3. 接口规划与职责 (API Orchestration)

### 3.1 输入接口 (Ingress)

- **Obsidian 触发**：监听笔记更新、标签变动。
    
- **Git Webhook**：Cursor 提交触发审计流（需携带 `#Project` 标签）。
    
- **WeCom 回调**：接收 Kenny 的审批指令（Approve/Reject）。
    

### 3.2 AI 调用逻辑

- **调度路径**：`n8n` → `OneAPI Gateway` → `Target LLM`。
    
- **模型分工**：
    
    - **本地 Qwen/DeepSeek (3090)**：处理 L1/L2 级私密数据。
        
    - **云端服务**：作为逻辑增强或公共信息总结。
        
### n8n 自动化枢纽与数据交换标准
	AI-Obsidian Manual Section
	1. 文档目的与系统定位
	   n8n 作为 Orchestration Layer
	2. n8n 职责边界
	   Responsibilities
	   Non-Responsibilities
	3. 系统拓扑与网络边界
	   L1 Private Compute
	   L2 ZeroTier
	   L3 External API
	4. 接口规划与职责
	   4.1 Ingress
	   4.2 AI Invocation
	5. AI Routing Policy
	   Local vs Cloud
	6. 数据交换与安全分级
	   L1-L4
	7. 标准 Workflow 模板
	8. 审计与日志协议
	9. Cursor 维护协议
	10. 典型工作流示例
---

## 4. 数据交换与安全分级规范 (L1-L4)

所有通过 n8n 交换的数据必须强制进行级别标注，严禁跨级外发。

|**等级**|**说明**|**安全规则**|**存储位置**|
|---|---|---|---|
|**L1**|**核心私密**|禁止离开内网，仅限本地模型处理。|`Protected/`|
|**L2**|**内阁内部**|允许在 ZeroTier 覆盖的私有设备流转。|`Internal/`|
|**L3**|**可交换数据**|允许发送至云端 AI 进行增强分析（需脱敏）。|`Knowledge/`|
|**L4**|**公开数据**|无限制，可同步至外部 RSS 或 Web。|`Public/`|

**标准数据结构：**

JSON

```
{
  "source": "obsidian | cursor | wecom",
  "type": "note_update | git_audit | cmd_approve",
  "security_level": "L1 | L2 | L3 | L4",
  "content": "...",
  "metadata": {
    "project": "Comfcare",
    "network_env": "local | zerotier | public"
  }
}
```

LLM Layer
3090
Knowledge Layer
Obsidian
Agent Layer
Dify
Orchestration Layer
n8n
Network Layer
ZeroTier
---

## 5. 审计与日志协议

- **审计记录**：每一笔 AI 调用必须记录耗时、消耗 Token 及审计结论。
    
- **双向确认**：涉及系统配置修改（如 Dify DSL 变更），必须由 n8n 推送报告至企微，Kenny 回复 `OK` 后执行。
    
- **日志同步**：n8n 运行错误需自动写入 Obsidian `[[System_Audit_Logs]]`。
    

---

## 6. 🤖 Cursor 维护协议 (Maintenance for Cursor)

**当使用 Cursor 维护或生成 n8n JSON、Dify DSL 时，必须遵守以下指令：**

1. **环境感知**：Cursor 生成的任何 API 接口地址必须优先指向 **ZeroTier 静态 IP** 或 **Docker 服务名**，禁止硬编码公网 IP。
    
2. **脱敏逻辑注入**：在编写 n8n 的 JavaScript 节点时，必须默认包含隐私过滤函数（移除路径中的 `/home/kenny/` 等敏感字符串）。
    
3. **分级检查**：若生成的 JSON 涉及数据外发，必须包含一个 `If` 逻辑节点，判断 `security_level` 是否大于 L2。
    
4. **自描述性**：生成的 JSON/DSL 必须包含 `description` 字段，注明该流符合本手册的哪一条款（例如：`Match Manual Sec 3.1`）。
    

---

## 7. 典型工作流：[Comfcare] 跨境审计流

1. **触发**：Cursor `pre-commit` 拦截。
    
2. **传输**：n8n 捕获 Diff，识别项目为 `#Comfcare`。
    
3. **分析**：Dify (Gemini 1.5 Pro) 调用本地知识库进行架构对齐分析。
    
4. **决策**：分析结果推送到企微，Kenny 通过手机确认。
    
5. **入库**：n8n 将确权后的代码/笔记同步至 Obsidian 核心库。
    

---

**审计长小酷备注：** > "本手册是 AI-Obsidian 系统的神经元连接图。任何未经本规范定义的‘私自建联’均视为非法请求。"

---