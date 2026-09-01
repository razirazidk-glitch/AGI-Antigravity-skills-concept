---
description: Swarm governance, concurrency boundaries, anti-directed framing, and cluster lineage.
trigger: always_on
---
# SWARM COGNITION & MULTI-AGENT GOVERNANCE

## 1. CONCURRENCY & POLLING
- Max 2 concurrent subagents (C_max <= 2).
- Polling prohibited: yield turn after dispatch; wake reactively on completion.
- Built-in types: "self" or "research". Custom types require define_subagent first.

## 2. DOMAIN-CLUSTER DELEGATION
- Group by cohesive subsystem clusters (<=12 related files per agent).
- Prohibited: 1 subagent per single file. Monolithic multi-subsystem dumps (>12 files) prohibited.

## 3. ANTI-DIRECTED FRAMING
- Prohibited: Injecting bug hypotheses, line numbers, or failure mode names into worker prompts.
- Prohibited: Listing specific error types or prescriptive search targets.
- Required Prompt Format: "CLUSTER AUDIT: Inspect files in [DIR/MODULE] (max 10-12 files). Map all symbol inputs/outputs. Trace live data lineage from [INGESTION] to [SINK]. Derive invariants from AST and execution evidence. Report interface seams and contract breaches."

## 4. PRE-DISPATCH CHECK & INTEGRATION SEAMS
- Before dispatch: Verify prompt has no location hints, no bug hypotheses, and includes adjacent module seams.
- Before marking DONE: Verify live upstream feeding, live downstream consumption, and satisfied type contracts.

## 5. HANDOFF REPORT & DISK PERSISTENCE
- Worker report: 1. Observation, 2. Logic Chain, 3. Caveats, 4. Conclusion, 5. Verification (exit code 0).
- Mandatory disk persistence at `.sessions/active/reports/[INDEX]_[CLUSTER].md` and manifest update.
- Subagents modifying code must first execute view_file on the audit report.

## 6. REAL SUBAGENT INVOCATION MANDATE (ANTI-SIMULATION LAW)
- When the user explicitly requests a team of real subagents (e.g., "time de subagents reais", "swarm", "equipe de subagentes", "multi-agent team"), the orchestrator MUST dispatch authentic subagents via `invoke_subagent`.
- Strictly Prohibited: Simulating multi-agent swarms by authoring audit files or executing single-agent audits directly in the parent context pretending to be separate workers.
- The orchestrator must NEVER bypass `invoke_subagent` using local file creation or mock audit reports when real subagents are requested.

