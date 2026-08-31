#!/usr/bin/env python3
"""
Deterministic Progressive Memory & Project Brain Initializer for Antigravity Workspaces.
Scaffolds:
1. PROJECT_BRAIN.md at project root
2. .agents/rules/00_PROJECT_GROUNDING.md for automatic rule injection
3. .sessions/active/ and .sessions/archive/ directories
"""
import sys
import datetime
from pathlib import Path

PROJECT_BRAIN_TEMPLATE = """# 🧠 PROJECT BRAIN — {project_name}
> Created at: {timestamp}
> Orchestrator: Antigravity Sovereign Executive
> Memory Engine: project-neural-map

---

## 📊 CORE MODULES STATUS DASHBOARD

| Module Core | Path | Status | Assigned Agent | Last Transition | Q-Score |
|---|---|---|---|---|---|
| Main System | `src/` | ⬜ NOT_MADE | — | — | — |

**Legend:** 🔴 CHANGING | ✅ DONE | ⬜ NOT_MADE | 🟡 READY

---

## 🏆 GOLDEN REFERENCE CORE (PROD STABLE BASELINE)

> Canonical production files and real validation harnesses. These files define the ground-truth baseline for all experimental sandboxes.

| Subsystem / Core | Canonical Path | Invariant Role | Ground Truth Baseline Spec |
|---|---|---|---|
| Main System Engine | `src/` | Proven calculation & execution | Mathematical & invariant contract |
| Validation Harness | `tests/` | Ground truth test benchmark | Deterministic real-data test feed |

---

## 📋 ARCHITECTURAL DECISION REGISTRY (DEC::GROUNDED — IMMUTABLE LOG)

> These decisions CANNOT be reverted without formal refactoring proposals and CEO sign-off.

| ID | Decision | Technical Rationale | Date | Approved By |
|---|---|---|---|---|
| DEC-001 | Initialized Progressive Memory Architecture | Enabled persistent cross-chat state tracking and grounding | {date} | Co-CEO |

---

## 📈 MODULE QUALITY SCORE (Q-SCORE) REGISTRY

| Module | Q-Score | Quality Gate | Auditor | Date |
|---|---|---|---|---|
| Core | — | ⏳ Pending | — | — |

---

## 🔗 NODE.md DIRECTORY INDEX

| Module | NODE.md Path | Last Synchronized |
|---|---|---|
| Core | `NODE.md` | — |

---

## 📜 RECENT STATE TRANSITION LOG

| Timestamp | Agent | Action | Target Module | Transition |
|---|---|---|---|---|
| {timestamp} | Antigravity | Initialized Project Brain | `PROJECT_BRAIN.md` | ⬜ Genesis |
"""

PROJECT_GROUNDING_RULE = """---
description: Progressive cross-chat memory rehydration and neural grounding.
trigger: always_on
---
# PROJECT MEMORY REHYDRATION & GROUNDING

## 1. TURN 0 MEMORY REHYDRATION
- Invariant: Before analyzing or modifying code, verify and read `PROJECT_BRAIN.md` at root.
- Read the latest `.sessions/archive/*/RETROSPECTIVE.md` to restore context from previous chats.
- Strictly adhere to decisions logged in `DEC::GROUNDED`.

## 2. STATE PERSISTENCE ON CLOSURE
- Log any new architectural decision in `PROJECT_BRAIN.md`.
- Mark completed module transitions (`🔴 CHANGING` -> `✅ DONE`).
"""

def bootstrap_memory(workspace_dir: Path) -> int:
    workspace_dir = workspace_dir.resolve()
    project_name = workspace_dir.name
    now = datetime.datetime.now(datetime.timezone.utc).isoformat()
    today = datetime.date.today().isoformat()

    print(f"[*] Bootstrapping progressive memory in: {workspace_dir}")

    # 1. Scaffolding .agents/rules
    rules_dir = workspace_dir / ".agents" / "rules"
    rules_dir.mkdir(parents=True, exist_ok=True)
    grounding_file = rules_dir / "00_PROJECT_GROUNDING.md"
    if not grounding_file.exists():
        grounding_file.write_text(PROJECT_GROUNDING_RULE, encoding="utf-8")
        print(f"  [+] Created: {grounding_file.relative_to(workspace_dir)}")
    else:
        print(f"  [.] Exists: {grounding_file.relative_to(workspace_dir)}")

    # 2. Scaffolding .sessions/active and .sessions/archive
    active_sessions = workspace_dir / ".sessions" / "active"
    archive_sessions = workspace_dir / ".sessions" / "archive"
    active_sessions.mkdir(parents=True, exist_ok=True)
    archive_sessions.mkdir(parents=True, exist_ok=True)
    print("  [+] Verified directories: .sessions/active and .sessions/archive")

    # 3. Scaffolding PROJECT_BRAIN.md
    brain_file = workspace_dir / "PROJECT_BRAIN.md"
    if not brain_file.exists():
        content = PROJECT_BRAIN_TEMPLATE.format(
            project_name=project_name,
            timestamp=now,
            date=today
        )
        brain_file.write_text(content, encoding="utf-8")
        print(f"  [+] Created: {brain_file.relative_to(workspace_dir)}")
    else:
        print(f"  [.] Exists: {brain_file.relative_to(workspace_dir)}")

    print("[✓] Progressive memory architecture bootstrapped successfully.")
    return 0

if __name__ == "__main__":
    target = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.cwd()
    sys.exit(bootstrap_memory(target))
