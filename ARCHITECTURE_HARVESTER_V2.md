# Harvester V2 调度器 · 两阶段协议 (2P-Protocol) 架构

## 一、整体架构

```
                    ┌─────────────────────────────────────────────────┐
                    │  Watchdog · 监听 ~/Documents/Obsidian/000_Inbox  │
                    │  触发：.md 文件新增/修改                           │
                    └─────────────────────────────────────────────────┘
                                        │
                                        ▼ 文件路径入队
                    ┌─────────────────────────────────────────────────┐
                    │  Step 1 · 本地哨兵 (xiaohei_synopsis + 增强)      │
                    │  - 调用 3090 获取基础缩影 JSON                     │
                    │  - 增强：privacy_level / task_count / core_entities│
                    │  降级：3090 宕机 → 纯文本移动，不阻塞              │
                    └─────────────────────────────────────────────────┘
                                        │
                                        ▼ 增强型缩影
                    ┌─────────────────────────────────────────────────┐
                    │  Step 2 · 智能分流器                              │
                    │  分支 A：weekly_journal 或 命中「战略/协议」       │
                    │          → 调用 Dify API（缩影 + 全文）→ 完整 JSON│
                    │  分支 B：word_count < 300 且 privacy_level=High   │
                    │          → 跳过云端，本地根据缩影生成 Frontmatter │
                    │  默认：  其他 → 本地缩影 Frontmatter 或 Dify（可配）│
                    └─────────────────────────────────────────────────┘
                                        │
                                        ▼
                    ┌─────────────────────────────────────────────────┐
                    │  Harvester · 落盘                                │
                    │  - 按 core_entities 决定存储路径（小康/小镜/…）    │
                    │  - JSON → Obsidian YAML Frontmatter + 正文       │
                    │  - 写入目标路径，原 Inbox 文件可移走或留档         │
                    └─────────────────────────────────────────────────┘
                                        │
                    ┌─────────────────────────────────────────────────┐
                    │  日志 · logs/cabinet.log                          │
                    │  所有处理过的文件、分支、错误均备案                │
                    └─────────────────────────────────────────────────┘
```

## 二、数据流与增强型缩影

- **基础缩影**（来自 xiaohei_synopsis）：`word_count`, `summary_200`, `file_type`, `source_path`。
- **增强字段**（调度器内计算）：
  - **privacy_level**：若正文命中敏感关键词（可配置），则为 `High`，否则 `Normal`。
  - **task_count**：统计 `[ ]`（未勾选待办）数量。
  - **core_entities**：关键词 → Agent 映射，如 `民政/百联/慧享福` → 小康，`回忆录/叙事/访谈` → 小镜，用于落盘子目录。

## 三、分流规则小结

| 条件 | 分支 | 行为 |
|------|------|------|
| file_type == weekly_journal 或 正文含「战略」「协议」 | 高智商 | 请求 Dify（缩影+全文），得到完整小黑 JSON，再落盘 |
| word_count < 300 且 privacy_level == High | 极简 | 不调云端，仅用缩影生成 Frontmatter，落盘 |
| 其他 | 默认 | 本地根据缩影生成 Frontmatter 落盘（或可配置为仅缩影调 Dify） |

## 四、3090 降级策略

- 若调用 xiaohei_synopsis 时 3090 超时/连接失败：**不阻塞**，进入「纯文本移动模式」：
  - 将文件移动到指定 fallback 目录（如 `000_Inbox/_fallback` 或 `归档/未分析`），
  - 不写入 Frontmatter，仅在日志中记录「3090 不可用，已移动」。
- 后续可人工或定时重试 fallback 目录中的文件。

## 五、落盘路径与 Frontmatter

- **存储根**：与现有 harvester 一致，为 `VAULT_PATH/归档/`。
- **子目录**：由 **core_entities** 决定，如 命中「小康」→ `归档/小康/`，命中「小镜」→ `归档/小镜/`，未命中 → `归档/Inbox/` 或 `归档/other/`。
- **Frontmatter**：Obsidian 标准 YAML，包含 word_count、summary_200、file_type、privacy_level、task_count、core_entities、date、source_path 等，与 Dataview 兼容。

## 六、技术要点

- **并发**：asyncio + httpx，单文件处理异步，多文件通过队列串行或可控并发。
- **错误处理**：3090/Dify 失败有明确降级与日志，不抛未捕获异常导致调度器退出。
- **日志**：所有处理记录写入 `logs/cabinet.log`，包含文件路径、分支、耗时、错误信息。

## 七、运行与配置

- **依赖**：`pip install -r requirements_harvester_v2.txt`（watchdog、httpx、python-frontmatter）
- **启动**：在项目根目录执行 `python harvester_v2_scheduler.py`，Ctrl+C 停止。
- **配置**：修改 `harvester_v2_scheduler.py` 顶部 `CONFIG`：
  - `INBOX_PATH`：监听的 Inbox 目录（默认 `~/Documents/Obsidian/000_Inbox`）
  - `VAULT_PATH`：Obsidian 库根
  - `DIFY_API_URL` / `DIFY_API_KEY`：高智商分支调用 Dify 工作流（也可用环境变量）
  - `SENSITIVE_KEYWORDS`：命中则 `privacy_level=High`
  - `CORE_ENTITY_KEYWORDS`：关键词 → 落盘子目录（小康/小镜等）
- **3090 不可用**：文件会被移动到 `归档/_fallback/`，可后续重试或人工处理。
