

# AI-OB Cursor Rules (Enhanced)

  

Version: 1.2

Scope: Code generation, document modification, automation scripts, Canvas visual status

System components:

Knowledge Base: Obsidian

Agent Runtime: Dify

Workflow: n8n

Model Gateway: OneAPI

Local Inference: RTX 3090

Cursor must follow these rules strictly.

---

## 1. Stability First

  

Do NOT refactor working systems without explicit instruction.

Preferred order of action:

1. Fix bug
    
2. Patch minimal change
    
3. Avoid rewrite
    
    Large refactors require user confirmation.
    

---

## 2. System Authority

  

Architecture rules are defined in: system/

If code changes conflict with System rules:

- STOP
    
- Explain the conflict
    
- Request System update
    
    Never silently override architecture.
    
    Priority order:
    
    System > Tools > Knowledge
    

---

## 3. Four-Vault Architecture (Mandatory)

  

The AI-OB system is physically separated into four vaults:

  

3.1 Cabinet (User Knowledge)

- Purpose: Human knowledge repository
    
- Examples: project/, knowledge/, research/, daily-notes/
    
- Rules:
    
    • Cabinet is READ-ONLY for AI
    
    • AI must NEVER automatically modify or delete files
    
    • Cabinet represents Human Approved Knowledge
    

  

3.2 System (Architecture Governance)

- Contains: AI-OB Constitution, Cursor Rules, Architecture Blueprints, Governance policies
    
- Rules: Human governed; AI may suggest changes but must wait for approval
    

  

3.3 Runtime (AI Workspace)

- Contains AI-generated artifacts: cards/, audits/, embeddings/, drafts/, agent-memory/
    
- AI has write permission here
    

  

3.4 Tools (Infrastructure)

- Contains runtime infrastructure: n8n/, dify/, scripts/
    
- Provides compute, orchestration, and integration
    
- Cursor is NOT responsible for Docker
    

---

## 4. Draft Proposal System

- AI may generate knowledge proposals but may NOT directly write into Cabinet
    
- Workflow:
    
    AI → runtime/drafts/ → Human Review → Human Approval → Cabinet
    
- Rules:
    
    • All AI-generated documents must first be stored in runtime/drafts/
    
    • Only humans may move files into Cabinet
    
- This preserves knowledge authority
    

---

## 5. Triple-A Knowledge Structure

  

When structured knowledge is generated, use the Triple-A format.

Files:

- note.md
    
- note.card.yaml
    
- note.audit.yaml
    

  

Roles:

- note.md — Human readable content
    
- note.card.yaml — Semantic summary and embedding source
    
- note.audit.yaml — Audit history
    

  

Rules:

- card.yaml → embedding_access: true
    
- audit.yaml → embedding_access: false
    
- Embedding systems must NEVER read audit.yaml
    

---

## 6. Vector Sovereignty

  

Allowed embedding sources:

- note.card.yaml
    
- structured summaries
    

  

Forbidden sources:

- audit.yaml
    
- log files
    
- raw yaml configs
    
- system audit data
    

  

If embedding is requested on forbidden sources:

- STOP
    
- Warn the user
    

---

## 7. Local Inference Priority

  

Sensitive data must remain local.

Security levels:

- L1 Core internal data
    
- L2 Private project data
    
- L3 Exchangeable data
    
- L4 Public data
    

  

Rules:

- L1 / L2 → local inference only
    
- Recommended models: DeepSeek-R1 (local), Qwen (local)
    
- Cloud models allowed only for L3 / L4
    
- Local compute device: RTX 3090
    

---

## 8. Docker Safety

  

Never execute destructive commands automatically.

Forbidden without explicit confirmation:

- docker compose down -v
    
- docker system prune
    
- volume deletion
    

  

When editing docker-compose:

- Explain impact first
    
- Cursor does NOT handle Docker 自动化
    

---

## 9. Automation Architecture

  

n8n role: External integration only

Examples: Enterprise WeChat, Public accounts, Webhook bridges

Internal logic should prefer: Python tools, Dify Skills, Local services

Avoid complex distributed architectures

---

## 10. File Governance

  

Prevent uncontrolled duplication.

Forbidden naming patterns: *_final.md, *_copy.md, *_new.md

Use structured versioning instead

Required identifiers: file_id, version

Derived files must reference their parent: parent_file_id

---

## 11. Path Safety

  

Never expose real system user paths.

Forbidden examples: /Users/name/, /home/name/

Use neutral paths: /workspace/, /local/path/

---

## 12. Change Response Format

  

When modifying system code, always respond using:

1. Cause
    
2. Proposed Change
    
3. Code or Command
    
4. Expected Result
    

---

## 13. Failure Handling

  

If system integrity is uncertain:

- Create file: .halt
    
- Stop execution
    
- Never overwrite conflicting YAML automatically
    

---

## 14. System Guardian Principle

  

If any instruction risks:

- leaking L1 data
    
- violating the Four-Vault isolation
    
- modifying Cabinet automatically
    

  

Cursor must:

- STOP
    
- Explain the risk
    
- Suggest a safer alternative
    

---

## 15. Visual Status Protocol

1. 状态控制核心
    
    - 🔴 Critical / Pending → 暂停自动化，等待 Kenny 点击确认
        
    - 🟠 Processing → 执行任务 / Skills，实时更新 audit
        
    - 🟢 Completed → 任务完成，更新 Canvas 节点颜色并归档
        
    
2. Cursor 触发规则
    
    - 当节点状态变为 🔴 → 自动暂停对应 Agent 流程
        
    - 当节点状态变为 🟠 → 恢复执行，记录 audit
        
    - 当节点状态变为 🟢 → 通知调度 Agent，更新 Canvas
        
    
3. Kenny 控制关键点
    
    - 所有 🔴 状态必须由 Kenny 点击确认后才能继续
        
    - Cursor 不自动操作关键节点，保持人机同步