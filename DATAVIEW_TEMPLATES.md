# 内阁笔记 × Dataview 打通说明

小酷收割后的笔记都带有**统一表头（frontmatter）**，可直接被 Obsidian 的 Dataview 插件查询。  
把下面任意代码块复制到 `000_Cabinet_System/Templates/old templates` 里的模板中，即可在笔记里出现动态列表。

---

## 一、表头里有哪些字段可供 Dataview 用

| 字段 | 含义 | 示例 / 类型 |
|------|------|-------------|
| `date` | 收割日期 | `2025-02-21` |
| `tags` | 标签列表 | `[归档, 周记, 小忆]` |
| `content_type` | 内容类型 | 周记、笔记、文章… |
| `suggested_type` | 归档建议类型 | project_note、周记… |
| `primary_agent` | 主负责 agent | 小忆、小康… |
| `core_topic` | 核心主题 | 字符串 |
| `risk` | 风险摘要 | none / 其他 |
| `is_weekly_journal` | 是否周记 | true（仅周记有） |
| `source` | 来源/URL | 字符串 |
| `temporal_scope` | 时间范围 | `{ start, end, cycle }` |
| `structure_signals` | 结构信号 | `{ has_todo, has_done, has_reflection, has_time_range }` |

---

## 二、可直接贴进模板的 Dataview 示例

### 1. 列出「归档」下最近 20 条笔记（表格）

````markdown
```dataview
TABLE date, content_type, primary_agent
FROM "归档"
SORT file.mtime DESC
LIMIT 20
```
````

### 2. 只列周记（列表）

````markdown
```dataview
LIST
FROM "归档"
WHERE is_weekly_journal = true
SORT date DESC
```
````

### 3. 按内容类型筛选（例如 project_note）

````markdown
```dataview
TABLE date, core_topic, primary_agent
FROM "归档"
WHERE suggested_type = "project_note"
SORT date DESC
```
````

### 4. 按主负责 agent 分（小忆 / 小康）

````markdown
```dataview
TABLE date, core_topic, content_type
FROM "归档"
WHERE primary_agent = "小忆"
SORT date DESC
```
````

### 5. 本周内收割的笔记

````markdown
```dataview
TABLE date, content_type, core_topic
FROM "归档"
WHERE date >= date(today) - dur(7 days)
SORT date DESC
```
````

### 6. 带「复盘」信号的笔记（structure_signals.has_reflection）

````markdown
```dataview
TABLE date, core_topic
FROM "归档"
WHERE length(structure_signals) > 0 AND structure_signals.has_reflection = true
SORT date DESC
```
````

### 7. 按标签筛选（例如含 #周记）

````markdown
```dataview
LIST
FROM "归档"
WHERE contains(tags, "周记")
SORT date DESC
```
````

---

## 三、在 old templates 里怎么用

1. 打开 `000_Cabinet_System/Templates/old templates` 下任意模板。
2. 在需要「动态列表」的位置粘贴上面某一整段（含 \`\`\`dataview 和 \`\`\`）。
3. 保存模板；用该模板新建的笔记会在对应位置渲染出 Dataview 查询结果。
4. 若希望「只有用该模板的笔记在归档里时才显示表格」，可把 `FROM "归档"` 改成 `FROM ""` 并在 `WHERE` 里加 `file.path` 条件，或保持 `FROM "归档"` 专门做「归档总览」模板。

这样 old templates 就和 Dataview 打通了；小酷写入的 frontmatter 无需改，已兼容上述查询。
