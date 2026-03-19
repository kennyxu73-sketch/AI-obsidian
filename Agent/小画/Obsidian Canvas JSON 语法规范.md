
# Obsidian Canvas JSON 语法规范（团队开发标准）

版本：v1.0  
适用范围：  
- Obsidian Canvas 文件开发  
- AI自动生成 Canvas（Cursor / LLM）  
- 手工编写 Canvas  
- Mirror Core / AI-Obsidian 项目结构图  

---

# 一、Canvas JSON 基本结构

Canvas 文件本质是 **标准 JSON 文件**，顶层结构必须包含两个字段：
```

{

“nodes”: [],

“edges”: []

}

```
规则：

1. `nodes` 必须存在
2. `edges` 必须存在
3. JSON 必须合法
4. 不允许 trailing comma（最后一个元素后多余逗号）
5. 所有 `id` 必须唯一

---

# 二、Node 节点语法

Canvas 中的每一个元素都是 **Node**。

标准结构：
```

{

“id”: “node_id”,

“type”: “text”,

“x”: 0,

“y”: 0,

“width”: 300,

“height”: 200,

“text”: “节点内容”

}

```
字段说明：

| 字段 | 类型 | 必须 | 说明 |
|----|----|----|----|
| id | string | 必须 | 节点唯一ID |
| type | string | 必须 | 节点类型 |
| x | number | 必须 | X坐标 |
| y | number | 必须 | Y坐标 |
| width | number | 必须 | 节点宽度 |
| height | number | 必须 | 节点高度 |
| text | string | text节点必须 | 节点内容 |

---

# 三、Node 类型

常见 Node 类型：

### text 节点

最常见类型
```

“type”: “text”

```
包含字段：
```

“text”: “显示文本”

```
---

### file 节点

用于引用 Markdown 文件
```

{

“id”: “file_node”,

“type”: “file”,

“file”: “note.md”,

“x”: 0,

“y”: 0,

“width”: 400,

“height”: 300

}

```
---

### group 节点

用于分组
```

{

“id”: “group1”,

“type”: “group”,

“x”: 0,

“y”: 0,

“width”: 800,

“height”: 600,

“label”: “系统模块”

}

```
---

# 四、Edge 连接线语法

Edge 用于连接节点。

标准结构：
```

{

“id”: “edge_id”,

“type”: “arrow”,

“fromNode”: “node1”,

“toNode”: “node2”

}

```
字段说明：

| 字段 | 类型 | 必须 | 说明 |
|----|----|----|----|
| id | string | 必须 | edge唯一ID |
| type | string | 必须 | 连接类型 |
| fromNode | string | 必须 | 起始节点 |
| toNode | string | 必须 | 目标节点 |

---

# 五、Edge 类型

常见类型：
```

“arrow”

```
箭头连接
```

“line”

```
普通线连接

建议统一使用：
```

“arrow”

```
---

# 六、节点颜色（可选）

Canvas 支持颜色标记。

字段：
```

“color”: “4”

```
颜色值：

| 数值 | 颜色 |
|----|----|
| 0 | 灰 |
| 1 | 红 |
| 2 | 橙 |
| 3 | 黄 |
| 4 | 绿 |
| 5 | 青 |
| 6 | 蓝 |
| 7 | 紫 |

示例：
```

{

“id”: “node1”,

“type”: “text”,

“x”: 0,

“y”: 0,

“width”: 300,

“height”: 200,

“text”: “示例”,

“color”: “4”

}

```
---

# 七、坐标系统

Canvas 使用二维坐标：
```

x → 水平方向

y ↓ 垂直方向

```
示例布局：
```

左侧节点

x = -600

  

中心节点

x = 0

  

右侧节点

x = 600

```
---

# 八、常见错误

## 错误1：Edge缺少 type

错误示例：
```

{

“id”: “e1”,

“fromNode”: “a”,

“toNode”: “b”

}

```
正确：
```

{

“id”: “e1”,

“type”: “arrow”,

“fromNode”: “a”,

“toNode”: “b”

}

```
---

## 错误2：节点ID重复

错误：
```

“id”: “node1”

“id”: “node1”

```
解决：

所有节点必须唯一。

---

## 错误3：fromNode 不存在
```

“fromNode”: “nodeA”

```
但 nodes 中没有 nodeA。

---

## 错误4：JSON语法错误

常见原因：

- 多余逗号
- 缺少引号
- 括号不匹配

---

# 九、标准 Canvas 模板

推荐模板：
```

{

“nodes”: [

{

“id”: “node1”,

“type”: “text”,

“x”: 0,

“y”: 0,

“width”: 320,

“height”: 200,

“text”: “节点1”

},

{

“id”: “node2”,

“type”: “text”,

“x”: 500,

“y”: 0,

“width”: 320,

“height”: 200,

“text”: “节点2”

}

],

  

“edges”: [

{

“id”: “edge1”,

“type”: “arrow”,

“fromNode”: “node1”,

“toNode”: “node2”

}

]

}

```
---

# 十、AI生成 Canvas 规则（团队必须遵守）

如果使用 AI / Cursor 自动生成 Canvas：

必须满足：

1. JSON 必须合法
2. nodes 必须存在
3. edges 必须存在
4. edge 必须包含 `type`
5. 所有 id 必须唯一
6. fromNode / toNode 必须存在
7. 坐标必须为数字
8. Canvas 文件必须可以直接在 Obsidian 打开

---

# 十一、团队推荐命名规范

节点：
```

mirror_core

weikan

openbt

memory_os

ai_recall

```
Edge：
```

e1

e2

e3

```
---

# 十二、开发建议

推荐流程：
```

Cursor / AI 生成

↓

JSON校验

↓

Obsidian Canvas测试

↓

提交仓库

```
建议使用工具：

- Cursor
- JSON Validator
- Obsidian Canvas

---

# 十三、版本管理

建议 Canvas 文件：
```

/canvas

mirror_core.canvas

system_architecture.canvas

product_map.canvas

```
---

**本规范用于 Mirror Core / AI-Obsidian 项目团队统一开发标准**
```