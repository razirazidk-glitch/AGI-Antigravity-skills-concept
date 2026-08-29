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
- Project Brain (`PROJECT_BRAIN.md`): Update on architecture changes or >=3 files modified. Tables: Module Registry, Active Decisions, Speculative Assumptions.
- Retrospective: Deliverables, verified exit codes, root causes, /learn candidates.
