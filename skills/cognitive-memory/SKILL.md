---
name: cognitive-memory
description: >-
  Canonical Cognitive State Memory Architecture & Transactional Schema Engine for long-horizon agent state continuity. Trigger on mentions of: 'cognitive memory', 'state schema', 'save state', 'persist session', 'memory continuity', 'state transition', 'JSON schema memory', 'agent recall', or when managing multi-turn structured memory.
---
# SKILL: Cognitive Memory — Transactional State Schema & Persistence

> *"Memory is the enduring substrate of cognition. Schema enforcement guarantees sanity across time."*

---

## I. DOMAIN-INDEPENDENT CANONICAL MEMORY SCHEMA

`memory/session_state.json` provides the authoritative, machine-readable cognitive state of the system. It is strictly domain-agnostic and validated against a formal JSON-Schema standard.

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "system_identity": {
    "session_count": 1,
    "architecture_version": "v3.0.0",
    "active_conceptual_key": "GLOBAL_AGI_CORE"
  },
  "project_state": {
    "current_phase_id": "STAGE_1_METACOGNITION_AUDIT",
    "completed_milestones": [],
    "active_work_units": []
  },
  "blockers_registry": [],
  "priority_queue": [
    {"priority": 1, "action_id": "ACT-001", "description": "Execute Sector 1 Formal Audit", "dependency_hash": "a8f9..."}
  ],
  "epistemic_watchlist": {
    "active_hypotheses_count": 0,
    "under_falsification_count": 0
  },
  "state_integrity_hash": "<DYNAMIC_COMPUTED_SHA256_HASH_OF_PAYLOAD>"
}
```

---

## II. TRANSACTIONAL MEMORY OPERATIONS

### 1. Atomic Read-Modify-Write Protocol
All state updates must follow ACID-compliant atomic file updates using Python inline scripts:
```python
import json, hashlib, pathlib

state_path = pathlib.Path("memory/session_state.json")
if state_path.exists():
    data = json.loads(state_path.read_text())
    data["system_identity"]["session_count"] += 1
    data["state_integrity_hash"] = ""
    content_bytes = json.dumps(data, indent=2).encode('utf-8')
    data["state_integrity_hash"] = hashlib.sha256(content_bytes).hexdigest()
    
    temp_path = state_path.with_suffix(".tmp")
    temp_path.write_text(json.dumps(data, indent=2))
    temp_path.replace(state_path)
```

### 2. Multi-Agent Concurrent Memory Isolation
- Worker subagents write task results to `memory/logs/[subagent_id]_result.json`.
- The Master Orchestrator merges worker logs atomically into `session_state.json`.
- Workers and parallel subagents MUST NOT write directly to the primary `session_state.json`.
- Subagents write to isolated transaction logs (`memory/transactions/tx_[agent_id]_[timestamp].json`).
- The primary orchestrator merges transaction logs during state epoch synchronizations.
