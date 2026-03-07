# AI-OB Cursor Rules
Version: 1.0
Scope: Code generation, document modification, automation scripts

This rule file constrains AI behaviour inside the AI-Obsidian system.

The system architecture includes:

Knowledge Base: Obsidian
Agent Runtime: Dify
Workflow: n8n
Model Gateway: OneAPI
Local Inference: RTX 3090

Cursor must follow these rules strictly.

---

# 1. Stability First

Do NOT refactor working systems without explicit instruction.

Preferred order of action:

1 Fix bug
2 Patch minimal change
3 Avoid rewrite

Large refactors require user confirmation.

---

# 2. System Authority

Architecture rules are defined in:

System/

If code changes conflict with System rules:

STOP  
Explain the conflict  
Request System update

Never silently override architecture.

Priority order:

System > Tools > Knowledge

---

# 3. Triple-A Knowledge Structure

When generating structured knowledge files the system may use:

note.md
note.card.yaml
note.audit.yaml

Roles:

note.md  
Human readable content only.

note.card.yaml  
AI semantic summary and embedding source.

note.audit.yaml  
Audit and version history.

Rules:

card.yaml → embedding_access: true  
audit.yaml → embedding_access: false

Embedding must NEVER read audit.yaml.

---

# 4. Vector Sovereignty

Embedding sources allowed:

note.card.yaml  
structured summaries

Embedding sources forbidden:

audit.yaml  
log files  
raw yaml configs  
system audit data

If vectorization is requested on forbidden files:
STOP and warn the user.

---

# 5. Local Inference Priority

Sensitive data must remain local.

Security levels:

L1 Core internal data  
L2 Private project data  
L3 Exchangeable data  
L4 Public data

Rules:

L1 / L2 → local inference (RTX 3090)

Recommended models:

DeepSeek-R1 local  
Qwen local

Cloud models allowed only for L3/L4.

---

# 6. Docker Safety

Never automatically execute destructive commands.

Forbidden without confirmation:

docker compose down -v  
docker system prune  
volume deletion

When editing docker-compose:

Explain impact first.

---

# 7. Automation Architecture

n8n role:

External integration only

Examples:

Enterprise WeChat  
Public account  
Webhook bridges

Internal logic should prefer:

Python tools  
Dify Skills  
Local services

Avoid complex distributed architectures.

---

# 8. File Governance

Prevent uncontrolled file duplication.

Forbidden file patterns:

*_final.md  
*_copy.md  
*_new.md

Use versioning instead.

Required identifiers:

file_id  
version

Derived files must reference parent file_id.

---

# 9. Path Safety

Never expose real system user paths.

Forbidden examples:

/Users/name/
/home/name/

Use neutral paths:

/workspace/
/local/path/

---

# 10. Change Response Format

When modifying system code, always respond using:

1 Cause  
2 Proposed Change  
3 Code or Command  
4 Expected Result

---

# 11. Failure Handling

If system integrity is uncertain:

Generate

.halt

and stop execution.

Never overwrite conflicting YAML automatically.

---

# End of Cursor Rules