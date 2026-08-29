---
description: Session-scoped checklists, lifecycle management, briefs, and knowledge maps.
trigger: always_on
---
# CORE PROTOCOLS & ARTIFACT SCHEMAS

## 1. SESSION-SCOPED CHECKLIST
- Active: `.sessions/active/CHECKLIST.md` (Created on Genesis).
- Reports: `.sessions/active/reports/[INDEX]_[CLUSTER_NAME].md` + `MANIFEST.json`
- Archive: `.sessions/archive/[SESSION_ID]/CHECKLIST.md` (Moved on Closure).
- Invariant: No static CHECKLIST.md in repo root.

## 2. SESSION LIFECYCLE
1. Bootstrap: On new mission, create `SES-[TIMESTAMP]-[SLUG]`, write fresh checklist, read `PROJECT_BRAIN.md`.
2. Execution: Update checklist items [ ] -> [/] -> [x].
3. Closure: All items verified -> move checklist to archive, write `RETROSPECTIVE.md`, update `PROJECT_BRAIN.md`, clear `.sessions/active/`.

## 3. BRIEF SCHEMA
Path: `.planning/briefs/[ROLE]-[TIMESTAMP].md`
- Mission: Explicit deliverables, inputs, outputs.
- Context: Paths to `PROJECT_BRAIN.md` and active checklist.
- Acceptance: Exit code 0, zero TODOs/stubs, Q >= 9.0.
- Escalation: 3 failures -> send `BLOCKED: [reason]` to orchestrator.

## 4. PROJECT_BRAIN SCHEMA
Path: `PROJECT_BRAIN.md` (Update on architectural shifts or >=3 files modified):
- Module Registry: `| Path | Tier | Status (CHANGING/READY/DONE) | Owner | Last Verified |`
- Active Decisions: `| ID | Decision | Rationale | Locked |`
- Speculative Assumptions: `| ID | Assumption | Falsification Test | Verified |`

## 5. RETROSPECTIVE SCHEMA
Path: `.sessions/archive/[SESSION_ID]/RETROSPECTIVE.md`:
- Deliverables and verified exit codes.
- Failure patterns and root causes.
- Durable heuristics (/learn candidates).

