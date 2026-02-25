---
skill_id: "skill_001"
skill_name: "笔记审计器"
skill_version: "1.0.0"
skill_type: "analysis"
skill_category: "Analysis"

depends_on: []

inputs:
  - name: "note_content"
    type: "string"
    required: true
    description: "笔记内容"
  - name: "audit_level"
    type: "string"
    required: false
    default: "standard"
    description: "审计级别：standard/detailed/strict"

outputs:
  - name: "audit_result"
    type: "json"
    description: "审计结果 JSON，包含 category, tags, summary, action"

execution:
  runtime: "python"
  timeout: 30
  requires_3090: true
  api_endpoint: ":8189"

author: "小酷"
created_at: "2024-01-01"
tags:
  - "#skill"
  - "#analysis"
  - "#ai-generated"
  - "#stable"

permissions:
  read_vault: true
  write_vault: false
  network_access: true
  system_access: false
---

# 笔记审计器

## 功能描述
对 Obsidian 笔记进行智能审计，输出结构化 JSON 结果。对接审计员小黑的逻辑。

## 实现代码

```python
import json
import httpx
from skill_manager import call_3090

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
    
    # 构建审计提示词
    system_prompt = """你是由小酷配置的审计员小黑。你的任务是分析笔记内容，并输出 JSON 格式。
要求包含：
1. category: 笔记类别（如：工作/生活/技术/思考等）
2. tags: 建议标签 (list)
3. summary: 50字简述
4. action: 处理建议 (keep/archive/delete)
5. priority: 优先级 (A/B/C/D)
6. confidence: 置信度 (0-1)

请严格按照 JSON 格式输出，不要包含其他文字。"""
    
    user_prompt = f"""请审计以下笔记内容（审计级别：{audit_level}）：

{note_content[:2000]}"""
    
    # 调用 3090 算力
    response_text = await call_3090(
        prompt=user_prompt,
        system_prompt=system_prompt,
        temperature=0.3
    )
    
    # 解析 JSON（尝试提取 JSON 部分）
    try:
        # 尝试直接解析
        audit_result = json.loads(response_text)
    except:
        # 如果失败，尝试提取 JSON 块
        import re
        json_match = re.search(r'\{.*\}', response_text, re.DOTALL)
        if json_match:
            audit_result = json.loads(json_match.group())
        else:
            audit_result = {
                "error": "无法解析 JSON",
                "raw_response": response_text
            }
    
    return {
        "audit_result": audit_result
    }
```

## 使用示例

```python
from skill_manager import SkillManager
import asyncio

async def main():
    manager = SkillManager()
    skill = manager.load("skill_001")
    
    result = await manager.execute("skill_001", {
        "note_content": "# 我的笔记\n这是一段测试内容...",
        "audit_level": "standard"
    })
    
    print(json.dumps(result, ensure_ascii=False, indent=2))

asyncio.run(main())
```

## 测试用例

```json
{
  "test_cases": [
    {
      "inputs": {
        "note_content": "# 工作笔记\n今天完成了项目A的开发工作。",
        "audit_level": "standard"
      },
      "expected_outputs": {
        "audit_result": {
          "category": "工作",
          "tags": ["工作", "项目"],
          "summary": "记录了项目A的开发进展",
          "action": "keep",
          "priority": "B",
          "confidence": 0.9
        }
      }
    }
  ]
}
```

## 变更日志
- v1.0.0 (2024-01-01): 初始版本，对接小黑审计逻辑
