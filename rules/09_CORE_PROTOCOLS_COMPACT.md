---
description: Compact core protocols: Session-Scoped CHECKLIST, BRIEF, PROJECT_BRAIN, Session Lifecycle OS, and Retrospective.
trigger: always_on
---
# AGI LAYER 9: CORE PROTOCOLS COMPACT & SESSION OS

> **Mandate**: Session-Isolated Protocol Scaffolding, Zero Root Pollution, Clean Session Handoffs.

---

## 1. 📋 SESSION-SCOPED CHECKLIST PROTOCOL
Checklists are strictly scoped to the active session container to prevent cross-chat pollution:
- **Active Path**: `.sessions/active/CHECKLIST.md` (Created fresh on Session Genesis).
- **Archived Path**: `.sessions/archive/[SESSION_ID]/CHECKLIST.md` (Moved on Session Closure).
- **Root Invariant**: No static `CHECKLIST.md` in repository root.

### Template (`.sessions/active/CHECKLIST.md`):
```
# SESSION CHECKLIST — [SESSION_ID] — [ISO TIMESTAMP]
> Mission: [Objective] | Owner: [Role] | Status: IN_PROGRESS

## Phase 0: Pre-Flight & Routing
- [ ] Proactive routing emitted & skills mapped — PENDING
- [ ] Target files read via view_file — PENDING

## Phase 1: Planning & Contracts
- [ ] [item] — Criterion: [outcome] — PENDING

## Phase 2: Execution (TDD / Refactor)
- [ ] [item] — Criterion: exit code 0 — PENDING

## Phase 3: Verification & Closure
- [ ] Test suite passing (exit code 0) — PENDING
- [ ] Session Retrospective & Archive — PENDING
```
States: `[ ] PENDING` → `[/] IN_PROGRESS` → `[x] VERIFIED`

---

## 2. 🔄 SESSION LIFECYCLE MANAGEMENT (BOOTSTRAP & CLOSURE)
1. **Session Bootstrap ($T_{\text{start}}$)**:
   - Check `.sessions/active/`. If an unfinished session exists, prompt user to resume or archive it.
   - If starting a new mission: generate `SES-[TIMESTAMP]-[SLUG]`, write fresh `.sessions/active/CHECKLIST.md`, read `PROJECT_BRAIN.md`.
2. **Session Closure ($T_{\text{end}}$)**:
   - Verify all checklist items are `[x] VERIFIED`.
   - Move `.sessions/active/CHECKLIST.md` $\to$ `.sessions/archive/[SESSION_ID]/CHECKLIST.md`.
   - Write `.sessions/archive/[SESSION_ID]/RETROSPECTIVE.md`.
   - Synchronize `PROJECT_BRAIN.md` and clear `.sessions/active/`.

---

## 3. 📄 BRIEF.md — SUBAGENT BRIEFING
Path: `.planning/briefs/[ROLE]-[TIMESTAMP].md`:
- **MISSION**: Deliverable specifications & scope boundaries.
- **CONTEXT**: Path to `PROJECT_BRAIN.md` and `.sessions/active/CHECKLIST.md`.
- **ACCEPTANCE CRITERIA**: Exit code 0 / Zero TODOs / $Q \ge 9.0$.
- **ESCALATION**: 3 failures $\to$ send `BLOCKED: [reason]` to Manager.

---

## 4. 🧠 PROJECT_BRAIN.md — RECURSIVE KNOWLEDGE MAP
Update transactionally on major architectural shifts or $\ge 3$ files touched:
```markdown
# PROJECT_BRAIN — [PROJECT NAME]
> Last updated: [ISO timestamp] | Active Session: [SESSION_ID]

## Module Registry
| Module Path | Tier | Status (🔴 CHANGING | 🟡 READY | ✅ DONE) | Owner | Last Verified |

## Active Decisions (DEC::GROUNDED)
| ID | Decision | Rationale | Locked |

## Dangerous Assumptions (DEC::SPECULATIVE)
| ID | Assumption | Falsification Test | Verified |
```

---

## 5. 🧠 SESSION RETROSPECTIVE PROTOCOL
Path: `.sessions/archive/[SESSION_ID]/RETROSPECTIVE.md` (written upon session completion):
```markdown
## ✅ Mission Accomplished — [Deliverables & verified exit codes]
## 🔴 Failure Patterns & Circuit Breakers — [Causal analysis]
## 💡 Durable Heuristics — [Lessons learned]
## 🎓 /learn Candidates
| Insight | Layer 1 (Local) / Layer 2 (Global) | Rule / Skill Target |
## 🚀 Next Milestone Recommendation — [Next high-leverage entry point]
```
