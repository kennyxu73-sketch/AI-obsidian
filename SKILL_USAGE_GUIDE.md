# Obsidian Skill 使用指南
> 小酷 (CTO) 编写 | 快速上手指南

## 目录
1. [快速开始](#快速开始)
2. [创建你的第一个 Skill](#创建你的第一个-skill)
3. [Skill 管理器 API](#skill-管理器-api)
4. [最佳实践](#最佳实践)
5. [故障排查](#故障排查)
6. [与现有系统集成](#与现有系统集成)

## 快速开始

### 1. 安装依赖

```bash
pip install python-frontmatter httpx pyyaml
```

### 2. 配置路径

编辑 `skill_manager.py` 中的 `CONFIG`：

```python
CONFIG = {
    "VAULT_PATH": "/Users/kenny/Documents/My_Obsidian_Vault",  # 你的 Vault 路径
    "SKILLS_DIR": "Skills",
    # ...
}
```

### 3. 创建 Skills 目录结构

```bash
cd /path/to/your/vault
mkdir -p Skills/{Core,Analysis,Automation,Integration,Custom}
```

### 4. 运行 Skill 管理器

```python
from skill_manager import SkillManager

manager = SkillManager()
manager.update_registry()  # 更新注册表
skills = manager.list_skills()  # 列出所有 Skill
```

## 创建你的第一个 Skill

### 步骤 1: 创建 Skill 文件

在 `Skills/Analysis/` 目录下创建 `skill_my_first.md`：

```markdown
---
skill_id: "skill_my_first"
skill_name: "我的第一个 Skill"
skill_version: "1.0.0"
skill_type: "analysis"
skill_category: "Analysis"

inputs:
  - name: "text"
    type: "string"
    required: true

outputs:
  - name: "result"
    type: "string"

execution:
  runtime: "python"
  timeout: 30
  requires_3090: false

author: "你的名字"
tags:
  - "#skill"
  - "#custom"

permissions:
  read_vault: false
  write_vault: false
  network_access: false
---

# 我的第一个 Skill

## 实现代码

```python
async def execute(inputs):
    text = inputs.get("text", "")
    return {
        "result": f"处理结果: {text.upper()}"
    }
```
```

### 步骤 2: 验证 Skill

```python
from skill_manager import SkillManager

manager = SkillManager()
is_valid, errors = manager.validate("Skills/Analysis/skill_my_first.md")

if is_valid:
    print("✅ Skill 验证通过")
else:
    print(f"❌ 验证失败: {errors}")
```

### 步骤 3: 执行 Skill

```python
result = await manager.execute("skill_my_first", {
    "text": "Hello World"
})
print(result)  # {"result": "处理结果: HELLO WORLD"}
```

## Skill 管理器 API

### SkillManager 类

#### `discover() -> List[str]`
发现所有 Skill 文件

```python
skill_files = manager.discover()
```

#### `load(skill_id: str, force_reload: bool = False) -> Skill`
加载 Skill

```python
skill = manager.load("skill_001")
```

#### `validate(file_path: str) -> tuple[bool, List[str]]`
验证 Skill 格式

```python
is_valid, errors = manager.validate("path/to/skill.md")
```

#### `execute(skill_id: str, inputs: Dict, timeout: Optional[int] = None) -> Dict`
执行 Skill

```python
result = await manager.execute("skill_001", {
    "note_content": "...",
    "audit_level": "standard"
})
```

#### `update_registry()`
更新 Skill 注册表

```python
manager.update_registry()
```

#### `list_skills() -> List[Dict]`
列出所有 Skill

```python
skills = manager.list_skills()
for skill in skills:
    print(f"{skill['id']}: {skill['name']}")
```

### 调用 3090 算力

在 Skill 代码中使用：

```python
from skill_manager import call_3090

async def execute(inputs):
    response = await call_3090(
        prompt="你的提示词",
        system_prompt="系统提示词",
        temperature=0.3
    )
    return {"result": response}
```

## 最佳实践

### 1. Skill 命名规范

- 使用有意义的名称：`skill_note_auditor.md`
- 保持一致性：`skill_<功能>_<版本>.md` 或 `skill_<编号>.md`
- 避免特殊字符和空格

### 2. 版本管理

- 使用语义化版本号：`1.0.0`, `1.1.0`, `2.0.0`
- 重大变更时升级主版本号
- 在变更日志中记录所有修改

### 3. 依赖管理

使用 Obsidian 双链声明依赖：

```yaml
depends_on:
  - "[[skill_001]]"
  - "[[skill_002]]"
```

### 4. 错误处理

所有 Skill 必须包含异常处理：

```python
async def execute(inputs):
    try:
        # 你的代码
        result = do_something()
        return {"result": result}
    except Exception as e:
        return {
            "error": str(e),
            "success": False
        }
```

### 5. 权限最小化

- 默认 `write_vault: false`
- 只在必要时启用网络访问
- 避免系统调用权限

### 6. 测试

为每个 Skill 提供测试用例：

```markdown
## 测试用例

```json
{
  "test_cases": [
    {
      "inputs": {"text": "test"},
      "expected_outputs": {"result": "TEST"}
    }
  ]
}
```
```

### 7. 文档

- 清晰的功能描述
- 完整的使用示例
- 变更日志

## 故障排查

### 问题 1: Skill 加载失败

**错误**: `FileNotFoundError: 未找到 Skill: skill_xxx`

**解决**:
1. 检查 Skill ID 是否正确
2. 确认文件在 `Skills/` 目录下
3. 运行 `manager.update_registry()` 更新注册表

### 问题 2: 代码执行失败

**错误**: `RuntimeError: 编译 Skill 代码失败`

**解决**:
1. 检查代码块格式：必须是 ` ```python` 或 ` ```python:skill`
2. 确认 `execute` 函数已定义
3. 检查语法错误

### 问题 3: 权限错误

**错误**: `PermissionError: Skill 需要网络访问但未声明`

**解决**:
1. 在 frontmatter 中添加 `network_access: true`
2. 如果修改文件，添加 `write_vault: true` 和 `#modifies-original` 标签

### 问题 4: 3090 API 调用失败

**错误**: `RuntimeError: 调用 3090 失败`

**解决**:
1. 检查网络连接
2. 确认 3090 服务运行在 `:8189`
3. 检查 API URL 配置

## 与现有系统集成

### 对接小黑（审计员）

```python
# 小黑输出 JSON 判决书
xiaohei_judgment = {
    "category": "工作",
    "tags": ["工作", "项目"],
    "action": "keep",
    "priority": "B"
}

# 小酷执行收割
result = await manager.execute("skill_003", {
    "xiaohei_judgment": xiaohei_judgment,
    "note_path": "/path/to/note.md",
    "action_mode": "apply"
})
```

### 对接 n8n (总管)

在 n8n workflow 中使用 Python 节点：

```python
from skill_manager import SkillManager

manager = SkillManager()
result = await manager.execute("skill_001", {
    "note_content": $json.note_content
})
```

### 对接 Dify (大脑)

将 Skill 注册为 Dify Tool：

```python
# Dify Tool 配置
{
    "name": "note_auditor",
    "description": "审计笔记内容",
    "parameters": {
        "note_content": {"type": "string"}
    },
    "execute": lambda inputs: manager.execute("skill_001", inputs)
}
```

### 批量处理

```python
import asyncio

async def batch_process():
    manager = SkillManager()
    
    # 获取所有笔记
    notes = [...]  # 你的笔记列表
    
    # 并发处理
    tasks = [
        manager.execute("skill_001", {"note_content": note})
        for note in notes
    ]
    
    results = await asyncio.gather(*tasks)
    return results
```

## 示例工作流

### 完整的笔记处理流程

```python
from skill_manager import SkillManager
import asyncio

async def process_note_workflow(note_path: str):
    """完整的笔记处理工作流"""
    manager = SkillManager()
    
    # 1. 审计笔记
    audit_result = await manager.execute("skill_001", {
        "note_content": read_note(note_path),
        "audit_level": "standard"
    })
    
    # 2. 应用小黑的判决书
    if audit_result.get("audit_result", {}).get("action") == "keep":
        await manager.execute("skill_003", {
            "xiaohei_judgment": audit_result["audit_result"],
            "note_path": note_path,
            "action_mode": "apply"
        })
    
    # 3. 生成双链
    await manager.execute("skill_004", {
        "note_path": note_path,
        "link_strategy": "smart"
    })
    
    print(f"✅ 处理完成: {note_path}")

# 批量处理
async def batch_harvest():
    manager = SkillManager()
    
    # 使用收割器 Skill
    result = await manager.execute("skill_002", {
        "batch_size": 20,
        "dry_run": False
    })
    
    print(f"处理了 {result['processed_count']} 个笔记")

asyncio.run(batch_harvest())
```

## 进阶技巧

### 1. Skill 组合

创建组合 Skill，调用多个子 Skill：

```python
async def execute(inputs):
    manager = SkillManager()
    
    # 调用多个 Skill
    result1 = await manager.execute("skill_001", {...})
    result2 = await manager.execute("skill_002", {...})
    
    return {
        "combined_result": {
            "audit": result1,
            "harvest": result2
        }
    }
```

### 2. 动态 Skill 加载

```python
# 根据条件动态选择 Skill
skill_id = "skill_001" if condition else "skill_002"
result = await manager.execute(skill_id, inputs)
```

### 3. Skill 链式调用

```python
# 链式处理
result1 = await manager.execute("skill_001", inputs)
result2 = await manager.execute("skill_002", {
    **inputs,
    **result1  # 传递上一步的结果
})
```

---

**维护者**：小酷 (CTO)  
**最后更新**：2024-01-01  
**版本**：1.0.0

如有问题，请查看 `skill_specification.md` 获取详细规范。
