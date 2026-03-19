#### Step A: **本地部署Qdrant** (Local Deployment)*

在RTX3090服务器上启动Docker容器：

```bash
docker run -d \
  --name qdrant-local \
  -p 6333:6333 \
  -v /data/qdrant:/qdrant-data \
  qdrant/qdrant
```

- **配置**:
    - `embedding_model`: BGE-M3 (本地中文优化模型)。
    - `collection_schema`: 定义`domain`, `asset_type`,`agent_id`等字段。

#### Step B: **迁移现有笔记** (Migration)*

编写脚本将Obsidian中的`.md`文件向量化并导入Qdrant：

```python
# Pseudo-code for Migration Script (Python)
def migrate_to_qdrant(note_path):
    content = read_md(note_path)  # Read note.md body + card.yaml summary
    embedding_model.embed(content) # Generate vector using BGE-M3
    
    payload = {
        "file_id": extract_file_id(note),
        "domain": note.get("domain", "notes"), # notes/system/code
        "asset_type": note.get("doc_type", "strategy")
    }
    
    qdrant_client.upsert(collection="kenny_notes_summary", payload=payload, vector=embedding)

# Run migration in background (non-blocking MVP development)
```

- **策略**:
    - 仅向量化 `.card.yaml`中的 `summary`字段 (Regime A)。
    - Code域按函数切块生成向量 (非字符级),存入独立Collection。

#### Step C: **更新Dify Workflow** (Update Dify)*

在Dify中配置RAG节点：

- **触发器**: Kenny提问或Agent调用API。  
    - **检索策略**:
    1. `kenny_notes_summary` Collection (Top-K=5, domain过滤).  
        2. `code_chunks` Collection (仅当问题涉及技术实现时启用)。