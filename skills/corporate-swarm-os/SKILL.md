---
name: corporate-swarm-os
description: >-
  Corporate Swarm OS for multi-agent workflows, BRIEF.md, SECTOR.md, and batch orchestration. Trigger on: multi-agent, agent team, subagents, swarm, delegate, team of agents, corporate swarm, batch orchestration, swarm hierarchy, BRIEF.md, SECTOR.md, CEO agent, multi-agent project.
---
# 🏢 CORPORATE SWARM OS — High-Standard Enterprise Multi-Agent Operating System

> 🔴 **ABSOLUTE MANDATE:** Every complex project is operated like a next-generation enterprise organization. Vague subagents, brief prompts, and delegations lacking explicit context are STRICTLY PROHIBITED. Every agent receives an exhaustive BRIEF.md, operates within a formal sector with quantifiable KPIs, and reports via a structured closeout report. Zero informality. Zero ambiguity.

---

## 1. FORMAL CORPORATE HIERARCHY

```
CEO — Principal Agent (Supreme Orchestrator)
├── CTO — Engineering Manager
│   ├── Senior Engineer Worker (module implementation)
│   └── Architecture Worker (system design, contracts)
├── COO — QA Manager
│   ├── QA Engineer Worker (testing, validation)
│   └── Red Team Worker (adversarial audit)
├── CSO — Research Manager
│   ├── Domain Researcher Worker (SOTA, benchmarks, papers)
│   └── Data Prospector Worker (APIs, datasets, authentic sources)
├── CAO — Audit Manager
│   └── Deep Auditor Worker (deep code & architecture review)
└── CLO — Learning Manager
    └── Insight Extractor Worker (knowledge synthesis, new skills)
```

**Hierarchy Governance Rules:**
- The CEO never executes implementation tasks directly — always delegates.
- Workers report directly to their immediate Manager, never to the CEO directly.
- Managers synthesize worker reports and report to the CEO with sector-wide perspective.
- No Worker may commence execution without first reading the complete BRIEF.md for their assignment.

---

## 2. BRIEF.md — MANDATORY PER-AGENT BRIEFING TEMPLATE

> **PROTOCOL:** Before invoking any subagent, the CEO or Manager MUST write the BRIEF.md file to disk. The subagent reads this file as its FIRST ACTION before any execution.

**Canonical Path:** `.planning/briefs/[SECTOR]-[ROLE]-[TIMESTAMP].md`

```markdown
# BRIEF — [AGENT NAME / SECTOR]
> Issued at: [ISO timestamp]
> Issued by: [CEO / Sector Manager]
> Version: 1.0

---

## 🎯 MISSION
[Dense, precise description of what this agent must accomplish. Minimum 5 lines.
Do not use vague language. Specify the final deliverable with concrete technical details.]

## 🗺️ PROJECT CONTEXT
- Project: [name]
- PROJECT_BRAIN.md: [path to file — MANDATORY TO READ before starting]
- Relevant NODE.md files: [list of paths to modules that will be touched]
- Current Project Phase: [e.g., Phase 2 — Core Engine]
- Active Architectural Decisions: [summary of DEC::GROUNDED impacting this task]

## 📊 CHAIN OF COMMAND
- Direct Superior: [Manager name or CEO]
- Peer Agents: [other active Workers in the project right now]
- Dependent Agents: [who depends on this task's output to start]

## 📥 INPUT DEPENDENCIES (PRECONDITIONS)
[Exact list of what must be ready BEFORE starting]
- [ ] [required file/system/data]
- [ ] [approval or output from another Worker]
If any prerequisite is missing: STOP and report to Manager immediately.

## 📤 EXPECTED OUTPUT (FORMAL DELIVERABLES)
[Exact list of everything to be created/modified]
- [ ] `[path/file.ext]` — [description of expected content]
- [ ] Completion report via send_message to [Conversation ID]

## ✅ ACCEPTANCE CRITERIA (Q ≥ 9.0)
[What defines this task as COMPLETE with production-grade quality]
- [ ] [measurable criterion 1]
- [ ] [measurable criterion 2]
- [ ] Zero TODOs, zero stubs, zero static mocks
- [ ] All test suites passing (exit code 0)
- [ ] Self-evaluated Q-Score ≥ 9.0/10

## 🔒 INVARIANTS (NEVER VIOLATE)
[Absolute rules this agent must never break]
- PROHIBITED: [specific prohibited action]
- PROHIBITED: Starting implementation without reading PROJECT_BRAIN.md
- PROHIBITED: Modifying modules with 🔴 CHANGING status assigned to another agent
- PROHIBITED: Declaring DONE without empirical evidence (screenshot, exit code, test trace)

## 📋 SLA / ESTIMATE
- Estimated Complexity: [Low / Medium / High / Critical]
- Maximum Deadline: [estimate in turns or hours]

## 🚨 ESCALATION PROTOCOL
If encountering blockers, ambiguity, or critical failures:
1. STOP immediately — do not attempt unguided workarounds.
2. Send send_message to [Manager/CEO ID] stating: `BLOCKED: [blocker description]`
3. Await explicit instruction before continuing.
```

---

## 3. SECTOR.md — FORMAL SECTOR CHARTER TEMPLATE

**Canonical Path:** `.planning/sectors/[SECTOR-NAME].md`

```markdown
# SECTOR — [SECTOR NAME] ([Acronym])
> [e.g., Engineering (ENG) / QA (QA) / Research (RES) / Audit (AUD) / Learning (LRN)]

## 🎯 Sector Mission
[Description of why this sector exists within the project]

## 👥 Current Roster
| Role | Agent | Conversation ID | Status |
|---|---|---|---|
| Manager | [name] | [conv-id] | Active |
| Worker-01 | [name] | [conv-id] | Working on X |

## 📊 Sector KPIs
| Metric | Target | Current | Status |
|---|---|---|---|
| Mean Q-Score | ≥ 9.0 | — | — |
| Rework Rate | < 10% | — | — |
| SLA Compliance | 100% | — | — |

## 📋 Delivery Contracts
| Deliverable | Deadline | Status | Q-Score |
|---|---|---|---|
| [module] | [date] | NOT_MADE | — |

## 📖 Decision Log (DEC::GROUNDED)
| Date | Decision | Rationale | Approved By |
|---|---|---|---|
| [date] | [decision] | [why] | [CEO/User] |

## 🔍 Retrospective
[Key lessons learned in this sector during the project — populated upon milestone completion]
```

---

## 4. SUBAGENT DISPATCH PROTOCOL (CEO → Worker)

### Step 1: CEO writes BRIEF.md to disk
```python
# The CEO writes the file BEFORE invoking the subagent
write_to_file(
  TargetFile=".planning/briefs/ENG-worker-01-[timestamp].md",
  CodeContent="[Complete BRIEF.md with all fields populated]",
  Description="Write formal subagent mission brief",
  Overwrite=True
)
```

### Step 2: CEO invokes subagent with pointer to BRIEF
```json
{
  "TypeName": "self",
  "Role": "Senior Engineer Worker — [Specific Module]",
  "Prompt": "ACTIVE MISSION — Corporate Swarm OS\n\nYou are a Senior Engineer Worker. Your first and most critical action is:\n\n1. Run view_file on: .planning/briefs/ENG-worker-01-[timestamp].md\n2. Run view_file on: PROJECT_BRAIN.md\n3. Run view_file on all NODE.md files listed in the BRIEF as relevant\n4. ONLY THEN begin implementation\n\nUpon completion, send a formal report via send_message to [MANAGER_CONV_ID]."
}
```

### Step 3: Worker acknowledges receipt and executes
The Worker MUST begin its execution by confirming:
```
✅ BRIEF READ: .planning/briefs/ENG-worker-01-[timestamp].md
✅ BRAIN READ: PROJECT_BRAIN.md (module status confirmed)
✅ NODES READ: [list of consulted NODE.md files]

🔴 UPDATING STATUS → [module] = CHANGING
Commencing execution...
```

---

## 5. STRUCTURED CLOSEOUT REPORT (Worker → Manager)

Every Worker sends this format via `send_message` upon task completion:

```markdown
## COMPLETION REPORT — [ROLE] — [TIMESTAMP]

**Status:** COMPLETED | BLOCKED | PARTIAL

### 📤 Delivered Outputs
- [x] `path/file.py` — [description of implemented logic]
- [x] NODE.md updated at `path/NODE.md`
- [ ] [undelivered item] — reason: [explanation]

### ⚡ Deviations from Original Plan
[What differed from the BRIEF and why — maintain objective transparency]

### 📋 Pending Items
[What was deferred and why — include recommendations for the downstream agent]

### 📊 Self-Evaluated Q-Score: [X.X/10]
**Rationale:** [justification for this score — exercise rigorous self-critique]

### 🔴 Final Status of Touched Modules
| Module | Previous Status | Current Status |
|---|---|---|
| [module] | 🔴 CHANGING | ✅ DONE |

### 💡 Recommendations for Next Agent
[What the incoming Worker needs to know before starting]
```

---

## 6. REAL-WORLD EXAMPLES OF COMPLETED BRIEFS

### Example A — Engineering Worker (Module Implementation)

```markdown
# BRIEF — Senior Engineer Worker / Trading Engine Core
> Issued at: 2026-08-21T20:00:00Z | Issued by: CTO (Engineering Manager)

## 🎯 MISSION
Implement the `core/risk_engine.py` module for the quantitative trading engine.
This module is responsible for computing real-time position sizing using the
adapted Kelly Criterion formula: f* = (bp - q) / b, where b = odds,
p = win probability, q = 1 - p. The module must consume volatility data from
`data/market_feed.py` via the contracted interface in CONTRACTS.md Section 3.2.
Output: RiskSignal object with fields: size_lots, stop_loss_pips, take_profit_pips,
confidence_score (0-1).

## 🗺️ PROJECT CONTEXT
- Project: QuantumTradingMachine v2.0
- PROJECT_BRAIN.md: `C:/projects/qtm/PROJECT_BRAIN.md`
- Relevant NODE.md: `core/NODE.md`, `data/NODE.md`
- Current Phase: Phase 2 — Core Engine
- Active DEC::GROUNDED: "Use Kelly Criterion with 2% hard risk cap per trade (DEC-007)"

## 📥 INPUT DEPENDENCIES
- [x] `data/market_feed.py` — status: ✅ DONE (confirmed in BRAIN.md)
- [x] CONTRACTS.md Section 3.2 — MarketData interface defined
- [ ] `core/position_sizer.py` — NOT ready. POTENTIAL BLOCKER: verify BRAIN.md

## 📤 EXPECTED OUTPUT
- [ ] `core/risk_engine.py` — complete implementation with docstrings and type hints
- [ ] `tests/test_risk_engine.py` — test suite with 15+ test cases covering edge cases
- [ ] `core/NODE.md` — updated with Kelly Criterion derivation and status DONE
```

### Example B — QA Worker (System Audit)

```markdown
# BRIEF — QA Engineer Worker / API Layer Audit
> Issued at: 2026-08-21T21:00:00Z | Issued by: COO (QA Manager)

## 🎯 MISSION
Conduct a deep adversarial audit of module `api/routes.py` marked as 🟡 READY
in PROJECT_BRAIN.md. You must: (1) Read all code in the module, (2) Execute the
existing test suite and report test coverage, (3) Attempt to break the system
with malformed inputs, extreme payloads, and race conditions, (4) Verify that
all contracts defined in CONTRACTS.md Section 4.x are satisfied, (5) Emit a
formal verification verdict.

## ✅ ACCEPTANCE CRITERIA
- [ ] Test coverage ≥ 90% across all endpoints
- [ ] Zero injection vulnerabilities (SQL, command, path traversal)
- [ ] All contracts in CONTRACTS.md empirically verified
- [ ] Q-Score ≥ 9.0 for status promotion to DONE
- [ ] If Q < 9.0: enumerate exact blocking flaws and return to COO
```

---

## 7. HIERARCHICAL TRANSACTIONAL CHECKLIST PROTOCOL

Every mission, audit, and refactoring cycle MUST generate and consume a `CHECKLIST.md`. This is the external persistent memory that survives context window resets.

### 7.1 CHECKLIST Structure

```markdown
# CHECKLIST — [MISSION NAME] — [ISO TIMESTAMP]
> Owner: [CEO / Manager] | Phase: [N] | Status: IN_PROGRESS

## Phase 0: Structural Inventory
- [ ] Recursive file tree scan complete — [N] files catalogued
- [ ] All modules registered in PROJECT_BRAIN.md with Tier classification
- [ ] 100% node coverage confirmed before any subagent is deployed

## Phase 1: Cluster Audit Deployment
- [ ] Cluster [A] → Agent [conv-id] — Status: PENDING | RUNNING | VERIFIED
- [ ] Cluster [B] → Agent [conv-id] — Status: PENDING | RUNNING | VERIFIED

## Phase 2: Report Validation
- [ ] Report Cluster [A] received at `.reports/cluster-A.md`
- [ ] Embedded checklist inside cluster-A.md fully verified (0 open items)
- [ ] Report Cluster [B] received at `.reports/cluster-B.md`

## Phase 3: Refactor Deployment
- [ ] Refactor Agent [R-A] assigned to cluster-A findings — BRIEF.md written
- [ ] Refactor Agent [R-A] completed — Exit Code 0, Q ≥ 9.0
- [ ] PROJECT_BRAIN.md updated with new module statuses

## Phase 4: Final Tribunal
- [ ] Red/Blue Team adversarial audit dispatched
- [ ] Q ≥ 9.0 achieved across all audited modules
- [ ] CHECKLIST closed — all items VERIFIED
```

### 7.2 Invariants

- **CHECKLIST is written to disk BEFORE any subagent is deployed.** Never plan in memory.
- **No subagent proceeds to Phase N+1 items** until all Phase N checkboxes are marked `VERIFIED`.
- **Each audit report embeds its own sub-CHECKLIST** covering every finding it raises.
- **Context Reset Recovery:** If agent context is lost, reading `CHECKLIST.md` and `PROJECT_BRAIN.md` is sufficient to resume from the exact last verified state.
- **Tribunal Gate:** The final Red/Blue adversarial review item is only added to the checklist after all preceding phases are 100% verified.

