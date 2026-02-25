---
skill_id: "skill_003"
skill_name: "小黑集成器"
skill_version: "1.0.0"
skill_type: "integration"
skill_category: "Integration"

depends_on:
  - "[[skill_001]]"

inputs:
  - name: "xiaohei_judgment"
    type: "json"
    required: true
    description: "小黑输出的 JSON 判决书"
  - name: "note_path"
    type: "string"
    required: true
    description: "笔记文件路径"
  - name: "action_mode"
    type: "string"
    required: false
    default: "report"
    description: "执行模式：report/apply/archive"

outputs:
  - name: "execution_result"
    type: "json"
    description: "执行结果"
  - name: "modified_files"
    type: "list"
    description: "修改的文件列表（如果有）"

execution:
  runtime: "python"
  timeout: 60
  requires_3090: false
  api_endpoint: ""

author: "小酷"
created_at: "2024-01-01"
tags:
  - "#skill"
  - "#integration"
  - "#ai-generated"
  - "#stable"

permissions:
  read_vault: true
  write_vault: true
  network_access: false
  system_access: false
---

# 小黑集成器

## 功能描述
接收小黑输出的 JSON 判决书，执行相应的操作（标签添加、归档、删除等）。
符合 SOP：小黑出 JSON 判决书，小酷写 Python 执行收割。

## 实现代码

```python
import json
import shutil
from pathlib import Path
from datetime import datetime

async def execute(inputs):
    """
    Skill 执行函数
    
    Args:
        inputs: dict，包含所有输入参数
        
    Returns:
        dict，包含所有输出结果
    """
    xiaohei_judgment = inputs.get("xiaohei_judgment")
    note_path = inputs.get("note_path")
    action_mode = inputs.get("action_mode", "report")
    
    # 解析判决书
    if isinstance(xiaohei_judgment, str):
        judgment = json.loads(xiaohei_judgment)
    else:
        judgment = xiaohei_judgment
    
    note_file = Path(note_path)
    if not note_file.exists():
        raise FileNotFoundError(f"笔记文件不存在: {note_path}")
    
    # 读取笔记
    import frontmatter
    with open(note_file, 'r', encoding='utf-8') as f:
        post = frontmatter.load(f)
    
    modified_files = []
    execution_log = []
    
    # 根据 action_mode 执行操作
    if action_mode == "report":
        # 仅报告，不修改
        execution_log.append(f"📋 报告模式：建议操作 = {judgment.get('action', 'unknown')}")
        
    elif action_mode == "apply":
        # 应用判决书的建议
        
        # 1. 添加标签
        suggested_tags = judgment.get("tags", [])
        current_tags = post.metadata.get("tags", [])
        
        # 合并标签（去重）
        new_tags = list(set(current_tags + suggested_tags))
        if new_tags != current_tags:
            post.metadata["tags"] = new_tags
            execution_log.append(f"✅ 添加标签: {set(new_tags) - set(current_tags)}")
        
        # 2. 添加分类
        category = judgment.get("category")
        if category:
            post.metadata["category"] = category
            execution_log.append(f"✅ 设置分类: {category}")
        
        # 3. 添加审计元数据
        post.metadata["xiaohei_audit"] = {
            "audited_at": datetime.now().isoformat(),
            "summary": judgment.get("summary", ""),
            "priority": judgment.get("priority", "C"),
            "confidence": judgment.get("confidence", 0.5)
        }
        
        # 保存文件
        with open(note_file, 'w', encoding='utf-8') as f:
            f.write(frontmatter.dumps(post))
        
        modified_files.append(str(note_file))
        execution_log.append(f"💾 已保存修改: {note_file.name}")
        
    elif action_mode == "archive":
        # 归档操作
        action = judgment.get("action", "keep")
        
        if action == "archive":
            # 移动到归档目录
            archive_dir = note_file.parent / ".archive"
            archive_dir.mkdir(exist_ok=True)
            
            archive_path = archive_dir / note_file.name
            shutil.move(str(note_file), str(archive_path))
            
            modified_files.append(str(archive_path))
            execution_log.append(f"📦 已归档: {note_file.name} -> {archive_path}")
        
        elif action == "delete":
            # 删除操作（需要额外确认）
            execution_log.append(f"⚠️ 建议删除: {note_file.name}（未执行，需手动确认）")
    
    return {
        "execution_result": {
            "judgment": judgment,
            "action_mode": action_mode,
            "log": execution_log,
            "success": True
        },
        "modified_files": modified_files
    }
```

## 使用示例

```python
from skill_manager import SkillManager
import asyncio

async def main():
    manager = SkillManager()
    
    # 模拟小黑输出的 JSON 判决书
    xiaohei_judgment = {
        "category": "工作",
        "tags": ["工作", "项目", "重要"],
        "summary": "记录了项目A的开发进展",
        "action": "keep",
        "priority": "B",
        "confidence": 0.9
    }
    
    result = await manager.execute("skill_003", {
        "xiaohei_judgment": xiaohei_judgment,
        "note_path": "/path/to/note.md",
        "action_mode": "apply"  # 或 "report"/"archive"
    })
    
    print("执行结果:")
    for log in result["execution_result"]["log"]:
        print(f"  {log}")

asyncio.run(main())
```

## 变更日志
- v1.0.0 (2024-01-01): 初始版本，实现小黑判决书执行逻辑
