---
skill_id: "skill_004"
skill_name: "笔记双链生成器"
skill_version: "1.0.0"
skill_type: "core"
skill_category: "Core"

depends_on: []

inputs:
  - name: "note_path"
    type: "string"
    required: true
    description: "笔记文件路径"
  - name: "link_strategy"
    type: "string"
    required: false
    default: "smart"
    description: "链接策略：smart/auto/manual"

outputs:
  - name: "links_added"
    type: "integer"
    description: "添加的链接数量"
  - name: "suggested_links"
    type: "list"
    description: "建议的链接列表"

execution:
  runtime: "python"
  timeout: 60
  requires_3090: true
  api_endpoint: ":8189"

author: "小酷"
created_at: "2024-01-01"
tags:
  - "#skill"
  - "#core"
  - "#ai-generated"
  - "#modifies-original"
  - "#testing"

permissions:
  read_vault: true
  write_vault: true
  network_access: true
  system_access: false
---

# 笔记双链生成器

## 功能描述
为 Obsidian 笔记自动生成双链（`[[链接]]`），增强笔记之间的关联性。
⚠️ 此 Skill 会修改原始笔记，已标注 `#modifies-original`。

## 实现代码

```python
import re
from pathlib import Path
import frontmatter
from skill_manager import call_3090

async def execute(inputs):
    """
    Skill 执行函数
    
    Args:
        inputs: dict，包含所有输入参数
        
    Returns:
        dict，包含所有输出结果
    """
    note_path = inputs.get("note_path")
    link_strategy = inputs.get("link_strategy", "smart")
    
    note_file = Path(note_path)
    if not note_file.exists():
        raise FileNotFoundError(f"笔记文件不存在: {note_path}")
    
    # 读取笔记
    with open(note_file, 'r', encoding='utf-8') as f:
        post = frontmatter.load(f)
    
    content = post.content
    original_content = content
    
    # 扫描 Vault 中的所有笔记标题（用于链接建议）
    vault_path = note_file.parent.parent  # 假设 Vault 是父目录
    all_notes = {}
    for md_file in vault_path.rglob("*.md"):
        if md_file == note_file:
            continue
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                note_post = frontmatter.load(f)
                title = note_post.metadata.get("title") or md_file.stem
                all_notes[title] = str(md_file.relative_to(vault_path))
        except:
            continue
    
    # 根据策略生成链接
    if link_strategy == "smart":
        # 使用 3090 智能分析并生成链接建议
        prompt = f"""分析以下笔记内容，建议应该链接到哪些其他笔记（使用双链 [[笔记名]] 格式）。

笔记内容：
{content[:1500]}

可用的笔记标题：
{', '.join(list(all_notes.keys())[:50])}

请输出 JSON 格式，包含：
{{
  "suggested_links": ["笔记1", "笔记2", ...],
  "reasoning": "为什么建议这些链接"
}}"""
        
        response = await call_3090(prompt, temperature=0.3)
        
        # 解析响应（简化处理）
        import json
        try:
            # 尝试提取 JSON
            json_match = re.search(r'\{.*\}', response, re.DOTALL)
            if json_match:
                suggestions = json.loads(json_match.group())
                suggested_links = suggestions.get("suggested_links", [])
            else:
                suggested_links = []
        except:
            suggested_links = []
    
    elif link_strategy == "auto":
        # 自动检测关键词并链接
        suggested_links = []
        for title, rel_path in all_notes.items():
            if title.lower() in content.lower():
                suggested_links.append(title)
    
    else:  # manual
        # 手动模式，仅返回建议
        suggested_links = []
    
    # 添加链接到内容
    links_added = 0
    for link_title in suggested_links[:10]:  # 限制最多10个链接
        # 检查是否已存在链接
        if f"[[{link_title}]]" not in content:
            # 在第一次出现标题的地方添加链接
            pattern = re.compile(re.escape(link_title), re.IGNORECASE)
            matches = list(pattern.finditer(content))
            if matches:
                # 在第一个匹配处添加链接
                pos = matches[0].start()
                content = content[:pos] + f"[[{link_title}]]" + content[pos:]
                links_added += 1
    
    # 保存修改
    if links_added > 0:
        post.content = content
        with open(note_file, 'w', encoding='utf-8') as f:
            f.write(frontmatter.dumps(post))
    
    return {
        "links_added": links_added,
        "suggested_links": suggested_links,
        "modified": links_added > 0
    }
```

## 使用示例

```python
from skill_manager import SkillManager
import asyncio

async def main():
    manager = SkillManager()
    
    result = await manager.execute("skill_004", {
        "note_path": "/path/to/note.md",
        "link_strategy": "smart"
    })
    
    print(f"添加了 {result['links_added']} 个链接")
    print(f"建议的链接: {result['suggested_links']}")

asyncio.run(main())
```

## 变更日志
- v1.0.0 (2024-01-01): 初始版本，实现智能双链生成
