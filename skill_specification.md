# Obsidian Skill 规范 v1.0
> 小酷 (CTO) 核定 | 基于 Obsidian 双链结构的 Skill 系统

## 1. 设计理念

### 1.1 核心原则
- **本地优先**：所有 Skill 代码和配置存储在 Obsidian Vault 中，确保隐私
- **双链结构**：利用 Obsidian 的 `[[链接]]` 和标签系统组织 Skill 依赖关系
- **显式标注**：所有 AI 生成的 Skill 必须标注 `#ai-generated` 标签
- **目录不乱**：Skill 统一存放在 `Skills/` 目录下，严格分类

### 1.2 Skill 生命周期
```
创建 → 验证 → 注册 → 执行 → 监控 → 归档
```

## 2. Skill 文件结构

### 2.1 文件位置
```
Obsidian_Vault/
├── Skills/                    # Skill 根目录
│   ├── Core/                  # 核心 Skill（系统级）
│   ├── Analysis/              # 分析类 Skill
│   ├── Automation/            # 自动化类 Skill
│   ├── Integration/           # 集成类 Skill（对接小黑/小镜/小康）
│   └── Custom/                # 自定义 Skill
└── Skills/.registry.md        # Skill 注册表（自动生成）
```

### 2.2 Markdown 文件格式

每个 Skill 是一个 `.md` 文件，包含：

#### YAML Frontmatter（必需）
```yaml
---
skill_id: "skill_001"                    # 唯一标识符
skill_name: "笔记审计器"                  # 显示名称
skill_version: "1.0.0"                   # 版本号
skill_type: "analysis"                   # 类型：core/analysis/automation/integration/custom
skill_category: "Analysis"              # 分类目录

# 依赖关系（利用 Obsidian 双链）
depends_on:
  - "[[skill_000]]"                      # 依赖的其他 Skill
  - "[[skill_002]]"

# 输入输出定义
inputs:
  - name: "note_content"
    type: "string"
    required: true
    description: "笔记内容"
  - name: "audit_level"
    type: "string"
    required: false
    default: "standard"
    description: "审计级别"

outputs:
  - name: "audit_result"
    type: "json"
    description: "审计结果 JSON"

# 执行配置
execution:
  runtime: "python"                      # python/javascript/shell/api
  timeout: 30                            # 超时时间（秒）
  requires_3090: true                    # 是否需要 3090 算力
  api_endpoint: ":8189"                  # 如果使用 API，指定端点
  
# 元数据
author: "小酷"
created_at: "2024-01-01"
tags:
  - "#skill"
  - "#analysis"
  - "#ai-generated"                      # AI 生成标记
  - "#stable"                            # 稳定性标记：stable/testing/deprecated

# 权限与安全
permissions:
  read_vault: true                       # 是否可读取 Vault
  write_vault: false                     # 是否可写入 Vault（默认 false）
  network_access: false                  # 是否允许网络访问（默认 false）
  system_access: false                  # 是否允许系统调用（默认 false）
---
```

#### 正文内容
```markdown
# 笔记审计器

## 功能描述
对 Obsidian 笔记进行智能审计，输出结构化 JSON 结果。

## 实现代码

\`\`\`python
# [Skill Code Block]
import json
import httpx

async def execute(inputs):
    """
    Skill 执行函数
    
    Args:
        inputs: dict，包含所有输入参数
        
    Returns:
        dict，包含所有输出结果
    """
    note_content = inputs.get("note_content")
    audit_level = inputs.get("audit_level", "standard")
    
    # 调用 3090 算力
    payload = {
        "model": "internlm3-8b-instruct",
        "messages": [
            {"role": "system", "content": "你是审计员小黑..."},
            {"role": "user", "content": note_content[:2000]}
        ],
        "temperature": 0.3
    }
    
    async with httpx.AsyncClient() as client:
        response = await client.post(
            "http://101.43.29.236:8189/v1/chat/completions",
            json=payload,
            timeout=30.0
        )
        result = response.json()
    
    return {
        "audit_result": result
    }
\`\`\`

## 使用示例

\`\`\`python
from skill_manager import SkillManager

manager = SkillManager()
skill = manager.load("skill_001")
result = await skill.execute({
    "note_content": "# 我的笔记\n内容...",
    "audit_level": "standard"
})
\`\`\`

## 测试用例

\`\`\`json
{
  "test_cases": [
    {
      "inputs": {"note_content": "测试内容"},
      "expected_outputs": {"audit_result": {...}}
    }
  ]
}
\`\`\`

## 变更日志
- v1.0.0 (2024-01-01): 初始版本
```

## 3. Skill 类型定义

### 3.1 Core Skills（核心 Skill）
- 系统级功能，如文件操作、配置管理
- 位置：`Skills/Core/`
- 权限：通常需要 `write_vault: true`

### 3.2 Analysis Skills（分析类 Skill）
- 数据分析、内容审计、知识提取
- 位置：`Skills/Analysis/`
- 通常需要 `requires_3090: true`

### 3.3 Automation Skills（自动化类 Skill）
- 工作流自动化、定时任务
- 位置：`Skills/Automation/`
- 可能对接 n8n (`:5678`)

### 3.4 Integration Skills（集成类 Skill）
- 对接小黑、小镜、小康的接口
- 位置：`Skills/Integration/`
- 示例：`skill_xiaohei_audit.md`、`skill_xiaojing_archive.md`

### 3.5 Custom Skills（自定义 Skill）
- 用户自定义功能
- 位置：`Skills/Custom/`

## 4. Skill 注册表

`Skills/.registry.md` 自动维护所有 Skill 的索引：

```markdown
# Skill 注册表
> 自动生成，请勿手动编辑

| Skill ID | 名称 | 版本 | 类型 | 状态 | 最后更新 |
|---------|------|------|------|------|---------|
| skill_001 | 笔记审计器 | 1.0.0 | analysis | stable | 2024-01-01 |
| skill_002 | 笔记收割器 | 1.0.0 | automation | stable | 2024-01-01 |
```

## 5. 安全与权限

### 5.1 权限级别
- **read_vault**: 读取 Vault 文件
- **write_vault**: 写入/修改 Vault 文件（需谨慎）
- **network_access**: 网络请求（需明确声明）
- **system_access**: 系统调用（高风险，需审核）

### 5.2 安全规则
1. 所有 Skill 默认 `write_vault: false`
2. 网络访问必须明确声明用途
3. AI 生成的 Skill 必须标注 `#ai-generated`
4. 修改原始笔记的 Skill 必须标注 `#modifies-original`

## 6. 最佳实践

1. **命名规范**：`skill_<功能>_<版本>.md` 或 `skill_<编号>.md`
2. **版本管理**：使用语义化版本号
3. **依赖管理**：使用 Obsidian 双链 `[[skill_xxx]]` 声明依赖
4. **错误处理**：所有 Skill 必须包含异常处理
5. **日志记录**：关键操作需记录日志
6. **测试覆盖**：提供测试用例

## 7. 与现有系统集成

### 7.1 对接小黑
```python
# Skill 接收小黑输出的 JSON 判决书
skill_input = {
    "xiaohei_judgment": json_judgment,  # 小黑的 JSON
    "note_path": note_path
}
```

### 7.2 对接 3090 算力
```python
# Skill 自动使用配置中的 3090 端点
if skill.metadata["execution"]["requires_3090"]:
    api_url = "http://101.43.29.236:8189/v1/chat/completions"
```

### 7.3 对接 n8n/Dify
```python
# Skill 可以作为 n8n workflow 的节点
# 或作为 Dify Agent 的 Tool
```

---

**维护者**：小酷 (CTO)  
**最后更新**：2024-01-01  
**版本**：1.0.0
