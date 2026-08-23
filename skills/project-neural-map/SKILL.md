---
name: project-neural-map
description: >-
  MANDATORY recursive long-term memory and session state persistence protocol implementing PROJECT_BRAIN.md, transactional state schemas, and SHA-256 session handoff cryptography. Trigger on mentions of: 'project brain', 'neural map', 'PROJECT_BRAIN.md', 'NODE.md', 'module status', 'long-term memory', 'cognitive memory', 'state schema', 'save state', 'persist session', 'session handoff', 'state hash', or at the start of any turn in an active multi-module project.
---
# 🧠 PROJECT NEURAL MAP — Recursive Long-Term System Memory

> 🔴 **ABSOLUTE LAW:** In any active project with an existing `PROJECT_BRAIN.md`, the FIRST MANDATORY ACTION of any turn is to run `view_file` on `PROJECT_BRAIN.md` and on the `NODE.md` files of all modules that will be modified. Initiating any code modification without first reading the map is STRICTLY PROHIBITED. No read = zero permission to modify.

---

## 1. Overview & The 4 Dynamic States

```
🔴 CHANGING  — This core module is being actively modified RIGHT NOW. No other agent may touch it.
               → Responsible Worker: [name] | Commenced at: [timestamp]
               → Automatic write-lock for peer agents.

✅ DONE      — Fully implemented, tested, and certified with empirical Q-Score ≥ 9.0.
               → Stable. Modifications permitted only under a new explicit BRIEF.md.

⬜ NOT_MADE  — Specified in ARCHITECTURE.md but not yet implemented.
               → Pending Worker availability or upstream dependencies.

🟡 READY     — Implemented and awaiting adversarial review, test verification, or approval.
               → Next step: QA Worker audits and promotes to DONE or returns for rework.
```

---

## INITIALIZATION PROTOCOL (Project Genesis)

### When to Create
Immediately upon user approval of the 5 planning documents from `deep-planning-protocol`, and BEFORE writing a single line of implementation code.

### Ownership
The Principal Agent (CEO Agent) instantiates `PROJECT_BRAIN.md` and an empty `NODE.md` (status `⬜ NOT_MADE`) for every module defined in `ARCHITECTURE.md`.

### File Topology
```
[project-root]/
  PROJECT_BRAIN.md          ← Global neural index (ALWAYS at project root)
  [module-a]/
    NODE.md                  ← Technical module specification for Module A
  [module-b]/
    NODE.md                  ← Technical module specification for Module B
  .planning/
    ARCHITECTURE.md
    RESEARCH.md
    ...
```

---

## TEMPLATE: PROJECT_BRAIN.md

```markdown
# 🧠 PROJECT BRAIN — [Project Name]
> Created at: [ISO timestamp]
> CEO Orchestrator: [Principal Agent]
> Last updated: [timestamp] by [agent/role]
> Version: [X.Y]

---

## 📊 CORE MODULES STATUS DASHBOARD

| Module Core | Path | Status | Assigned Agent | Last Transition | Q-Score |
|---|---|---|---|---|---|
| Core Engine | `core/engine.py` | ⬜ NOT_MADE | — | — | — |
| Data Layer | `data/feed.py` | ⬜ NOT_MADE | — | — | — |
| API Routes | `api/routes.py` | ⬜ NOT_MADE | — | — | — |
| UI Dashboard | `ui/app.tsx` | ⬜ NOT_MADE | — | — | — |
| Risk Engine | `core/risk.py` | ⬜ NOT_MADE | — | — | — |

**Legend:** 🔴 CHANGING | ✅ DONE | ⬜ NOT_MADE | 🟡 READY

---

## 🏢 ACTIVE MULTI-AGENT TOPOLOGY

```
CEO — [Principal Orchestrator]
├── CTO (ENG) — [Engineering Manager] — Conv: [conv-id]
│   ├── ENG-Worker-01 — [active module] — Conv: [conv-id]
│   └── ENG-Worker-02 — [active module] — Conv: [conv-id]
├── COO (QA) — [QA Manager] — Conv: [conv-id]
│   └── QA-Worker-01 — Awaiting ENG-Worker-01
├── CSO (RES) — [Research Manager] — Conv: [conv-id]
│   └── RES-Worker-01 — COMPLETED
├── CAO (AUD) — Inactive until Phase 4
└── CLO (LRN) — Inactive until Phase 5
```

---

## 📋 ARCHITECTURAL DECISION REGISTRY (DEC::GROUNDED — IMMUTABLE LOG)

> These decisions CANNOT be reverted without formal refactoring proposals and CEO sign-off.

| ID | Decision | Technical Rationale | Date | Approved By |
|---|---|---|---|---|
| DEC-001 | [Use FastAPI instead of Flask] | [Async performance + automatic OpenAPI generation] | 2026-08-21 | User |
| DEC-002 | [PostgreSQL as primary datastore] | [ACID compliance + JSONB document capabilities] | 2026-08-21 | CEO |

---

## 📈 MODULE QUALITY SCORE (Q-SCORE) REGISTRY

| Module | Q-Score | Quality Gate | Auditor | Date |
|---|---|---|---|---|
| `core/engine.py` | — | ⏳ Pending | — | — |
| `data/feed.py` | — | ⏳ Pending | — | — |

**Release Firewall:** No module may transition to DONE without verified Q ≥ 9.0 certified by QA audit.

---

## 🔗 NODE.md DIRECTORY INDEX

| Module | NODE.md Path | Last Synchronized |
|---|---|---|
| Core Engine | `core/NODE.md` | — |
| Data Layer | `data/NODE.md` | — |
| API Routes | `api/NODE.md` | — |

---

## 📜 RECENT STATE TRANSITION LOG (Last 10 Events)

| Timestamp | Agent | Action | Target Module | Transition |
|---|---|---|---|---|
| [ts] | ENG-Worker-01 | Created scaffold | `core/engine.py` | ⬜ → 🔴 |
| [ts] | ENG-Worker-01 | Completed implementation | `core/engine.py` | 🔴 → 🟡 |
| [ts] | QA-Worker-01 | Certified test pass | `core/engine.py` | 🟡 → ✅ |
```

---

## TEMPLATE: NODE.md (Per-Module Specification)

```markdown
# 🔵 NODE — [Module Name]
> Path: `[relative/path/to/module]`
> Status: [🔴 CHANGING | ✅ DONE | ⬜ NOT_MADE | 🟡 READY]
> Assigned Agent: [Current Worker or "—"]
> Last updated: [timestamp] by [agent]

---

## 🎯 Purpose
[One dense, precise sentence describing the exact role of this module in the system]

## 🔬 Deep Technical Theory
[Comprehensive explanation of HOW and WHY this module operates this way.
Include: underlying algorithms, mathematical derivations, selected design patterns,
evaluated trade-offs, and why this design was chosen over alternatives. Minimum 8-10 lines of dense technical content.]

## 📥 Inbound Dependencies (Upstream)
[What this module consumes — imports, public APIs, upstream modules]
- `[module/file]` — [contracted interface consumed]
- `[external API]` — [specific endpoint consumed]

## 📤 Outbound Dependents (Downstream)
[Subsystems that depend on this module — downstream importers]
- `[module]` — [contracted interface provided]

## 🔒 Invariants (Immutable Contracts)
[Rules that must NEVER be breached within this module]
- INV-001: [formal invariant contract]
- INV-002: [formal invariant contract]

## 📊 Current Q-Score: [X.X/10]
**Quality Gate:** [PASSED ≥ 9.0 | PENDING | FAILED < 7.0]
**Audited by:** [QA Worker] on [date]
**Identified Remediation Vectors:** [list if Q < 9.0]

## 📖 Version & Evolution History
| Timestamp | Agent | Modification | Concrete Rationale |
|---|---|---|---|
| [ts] | ENG-Worker-01 | Initial implementation | Phase 2 milestone |
| [ts] | ENG-Worker-02 | Added LRU caching | Reduced P99 latency by 40% |

## 🔴 Open Items & Blockers
[Remaining work or optimization targets for this module]
- [ ] [pending item 1]
- [ ] [pending item 2]

## 💡 Engineering Notes for Next Agent
[Known pitfalls, subtle edge cases, unverified assumptions, and non-obvious context]
```

---

## STATE TRANSITION GOVERNANCE RULES

### Rule 1: Upon INITIATING work on a module
```
1. Read PROJECT_BRAIN.md — inspect current global module states.
2. If status ≠ 🔴 CHANGING: update NODE.md → status = 🔴 CHANGING.
3. Update PROJECT_BRAIN.md → Core Modules Status Dashboard.
4. Append an entry to the State Transition Log with timestamp and agent ID.
```

### Rule 2: Upon COMPLETING work on a module
```
1. Update NODE.md with generated knowledge (theory, invariants, history).
2. Set Status → 🟡 READY (awaiting QA) OR ✅ DONE (if empirically proven with test trace).
3. Update PROJECT_BRAIN.md → Dashboard + Q-Score + State Log.
4. Report completion to Manager via send_message.
```

### Rule 3: Concurrency Conflicts (Module already 🔴 CHANGING)
```
1. STOP immediately — do not modify the file.
2. Report to Manager: "LOCK CONFLICT: [module] is currently CHANGING by [agent]".
3. Await explicit routing before proceeding.
```

### Rule 4: BRAIN.md Synchronization Frequency
- Workers synchronize their local `NODE.md` upon every significant atomic change.
- Managers synchronize `PROJECT_BRAIN.md` each turn upon receiving worker reports.
- `PROJECT_BRAIN.md` must ALWAYS reflect actual disk/runtime state — never planned state.

---

## MANDATORY PRE-FLIGHT READ PROTOCOL

```
ACTIVE REPO CONTEXT DETECTED: PROJECT_BRAIN.md exists in workspace.

MANDATORY FIRST ACTION BEFORE ANY CODE GENERATION:

1. view_file("PROJECT_BRAIN.md") → Check global topology and module states.
2. view_file("[target-module]/NODE.md") → Inspect technical contracts for target modules.
3. Verify: is any target module marked 🔴 CHANGING by another worker?
   → YES: STOP immediately and report lock conflict.
   → NO: Proceed with execution.

PROHIBITION: Any file modification without completing the steps above is a constitutional violation.
```

---

## INTEGRATION WITH CORPORATE SWARM OS

The Neural Map serves as the central nervous system for Corporate Swarm OS:
- **CEO** uses `PROJECT_BRAIN.md` to govern enterprise project status.
- **Managers** synchronize `PROJECT_BRAIN.md` upon receiving Worker deliverables.
- **Workers** update their local `NODE.md` throughout execution.
- **QA Workers** register audited Q-Scores in `PROJECT_BRAIN.md`.
- **Audit Workers** traverse `PROJECT_BRAIN.md` history to detect architectural drift.
