---
description: Session-scoped checklists, lifecycle management, briefs, and knowledge maps.
trigger: always_on
---
# CORE PROTOCOLS & ARTIFACT SCHEMAS

## 1. SESSION ARTIFACTS
- Active Checklist: `.sessions/active/CHECKLIST.md`
- Active Reports: `.sessions/active/reports/[INDEX]_[CLUSTER].md` + `MANIFEST.json`
- Archive: `.sessions/archive/[SESSION_ID]/CHECKLIST.md` + `RETROSPECTIVE.md`
- Invariant: No static CHECKLIST.md in repository root.

## 2. SCHEMAS
- Brief (`.planning/briefs/[ROLE]-[TIMESTAMP].md`): Mission, inputs, outputs, acceptance criteria (exit 0, Q >= 9.0).
- Project Brain (`PROJECT_BRAIN.md`): Update on architecture changes or >=3 files modified. Tables: Module Registry, Dynamic 4-State Machine (`⬜ NOT_MADE`, `🔴 CHANGING`, `🟡 READY`, `✅ DONE`), Active Decisions, Speculative Assumptions.
- Subsystem Node Spec (`<module_dir>/NODE.md`): Interface contracts, public symbols, invariants, data lineage, and local verification test commands.
- Retrospective: Deliverables, verified exit codes, root causes, /learn candidates.

## 3. PROGRESSIVE CROSS-CHAT MEMORY PROTOCOL
- Auto-Rehydration (Turn 0): Read `PROJECT_BRAIN.md`, target module `<module_dir>/NODE.md`, and latest `.sessions/archive/*/RETROSPECTIVE.md` to restore full architectural state.
- Decision Immutability: Record non-trivial trade-offs in `PROJECT_BRAIN.md` under `DEC::GROUNDED`.
- Session Archival: At closure, persist accomplishments and pending debt to `.sessions/archive/[SESSION_ID]/RETROSPECTIVE.md`.
