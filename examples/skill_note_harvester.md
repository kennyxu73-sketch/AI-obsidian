---
skill_id: "skill_002"
skill_name: "笔记收割器"
skill_version: "1.0.0"
skill_type: "automation"
skill_category: "Automation"

depends_on:
  - "[[skill_001]]"  # 依赖笔记审计器

inputs:
  - name: "vault_path"
    type: "string"
    required: false
    description: "Obsidian Vault 路径，默认使用配置路径"
  - name: "batch_size"
    type: "integer"
    required: false
    default: 5
    description: "批次处理大小"
  - name: "dry_run"
    type: "boolean"
    required: false
    default: true
    description: "是否为试运行模式（不实际修改文件）"

outputs:
  - name: "processed_count"
    type: "integer"
    description: "处理的笔记数量"
  - name: "results"
    type: "list"
    description: "每个笔记的审计结果列表"

execution:
  runtime: "python"
  timeout: 300
  requires_3090: true
  api_endpoint: ":8189"

author: "小酷"
created_at: "2024-01-01"
tags:
  - "#skill"
  - "#automation"
  - "#ai-generated"
  - "#stable"

permissions:
  read_vault: true
  write_vault: false
  network_access: true
  system_access: false
---

# 笔记收割器

## 功能描述
批量扫描 Obsidian Vault 中的笔记，调用笔记审计器进行分析，输出处理报告。

## 实现代码

```python
import os
import frontmatter
from pathlib import Path
from skill_manager import SkillManager

async def execute(inputs):
    """
    Skill 执行函数
    
    Args:
        inputs: dict，包含所有输入参数
        
    Returns:
        dict，包含所有输出结果
    """
    vault_path = inputs.get("vault_path")
    batch_size = inputs.get("batch_size", 5)
    dry_run = inputs.get("dry_run", True)
    
    # 使用配置路径或指定路径
    if not vault_path:
        from skill_manager import CONFIG
        vault_path = CONFIG["VAULT_PATH"]
    
    vault = Path(vault_path)
    if not vault.exists():
        raise ValueError(f"Vault 路径不存在: {vault_path}")
    
    # 扫描所有 Markdown 文件
    md_files = []
    for root, dirs, files in os.walk(vault):
        # 跳过隐藏目录和 Skills 目录
        dirs[:] = [d for d in dirs if not d.startswith('.') and d != 'Skills']
        for file in files:
            if file.endswith('.md'):
                md_files.append(os.path.join(root, file))
    
    # 加载审计器 Skill
    manager = SkillManager(vault_path=str(vault))
    auditor_skill = manager.load("skill_001")
    
    # 批量处理
    results = []
    processed_count = 0
    
    for i, note_path in enumerate(md_files[:batch_size]):
        try:
            # 读取笔记内容
            with open(note_path, 'r', encoding='utf-8') as f:
                post = frontmatter.load(f)
                note_content = post.content
            
            # 调用审计器
            audit_result = await manager.execute("skill_001", {
                "note_content": note_content,
                "audit_level": "standard"
            })
            
            results.append({
                "file_path": note_path,
                "file_name": os.path.basename(note_path),
                "audit": audit_result.get("audit_result", {}),
                "status": "success"
            })
            processed_count += 1
            
        except Exception as e:
            results.append({
                "file_path": note_path,
                "file_name": os.path.basename(note_path),
                "status": "error",
                "error": str(e)
            })
    
    return {
        "processed_count": processed_count,
        "total_found": len(md_files),
        "results": results,
        "dry_run": dry_run
    }
```

## 使用示例

```python
from skill_manager import SkillManager
import asyncio

async def main():
    manager = SkillManager()
    
    result = await manager.execute("skill_002", {
        "batch_size": 10,
        "dry_run": True
    })
    
    print(f"处理了 {result['processed_count']} 个笔记")
    for r in result['results']:
        print(f"  - {r['file_name']}: {r.get('audit', {}).get('action', 'unknown')}")

asyncio.run(main())
```

## 变更日志
- v1.0.0 (2024-01-01): 初始版本，实现批量笔记审计功能
