---
description: Swarm governance, concurrency boundaries, anti-directed framing, and cluster lineage.
trigger: always_on
---
# SWARM COGNITION & MULTI-AGENT GOVERNANCE

## 1. CONCURRENCY & POLLING
- Concurrency: Maximum 2 concurrent subagents (C_max <= 2).
- Polling: PROHIBITED. Yield turn after dispatch; wake reactively on completion.

## 2. SUBAGENT REGISTRATION & TYPES
- Built-in types: TypeName MUST be "self" or "research".
- Custom types: Must be registered via define_subagent before invoke_subagent.

## 3. DOMAIN-CLUSTER DELEGATION
- PROHIBITED: Spawning 1 subagent per single file.
- PROHIBITED: Monolithic multi-subsystem dumps (>12 files or multiple disjoint engines in 1 subagent).
- REQUIRED: Group by cohesive subsystem clusters (bounded to <=12 related files per agent). Trace all files in cluster together.

## 4. ANTI-DIRECTED FRAMING (HYPOTHESIS ISOLATION & ZERO BUG-TYPE ENUMERATION)
- PROHIBITED: Injecting pre-conceived hypotheses into worker prompts (e.g., "check if line 1298 inverts signal"). Causes cognitive myopia where workers confirm prompts and miss structural defects.
- PROHIBITED: Listing specific bug categories, error types, or hypothetical failure modes in worker prompts (e.g., "look for bug X", "check for memory leaks", "verify math in Y"). Causes categorical tunnel vision where workers filter for matching keywords, alucinate matching patterns, and miss emergent systemic defects.
- PROHIBITED: Prescribing search targets or diagnosis scripts.
- PROHIBITED: Silo auditing without cross-module integration tests. Every module must prove live data wiring to upstream and downstream sinks.
- REQUIRED PROMPT FORMAT:
  `"CLUSTER AUDIT: Inspect files in [BOUNDED_DIR/MODULE] (max 10-12 files). Map all symbol inputs/outputs. Trace live data lineage from [INGESTION_DATA] to [SINK_CONSUMER]. Derive invariants strictly from AST and execution evidence. Report interface seams and contract breaches."`

## 5. CEO PRE-DISPATCH 3-QUESTION GATE
Before dispatching any worker, verify:
1. Telling worker WHERE to look? -> Remove location hint.
2. Telling worker WHAT the bug is? -> Remove hypothesis. State symptom only.
3. Scope includes integration seams to adjacent modules? -> Expand if missing.

## 6. INTEGRATION SEAM VERIFICATION
Before marking any module or cluster DONE:
- Upstream: Live connection feeding in verified (not assumed).
- Downstream: Live consumption by sink verified (not assumed).
- Contracts: Type contracts and value ranges satisfied across boundaries.
- PROHIBITED: Declaring modules valid solely from isolated unit tests.

## 7. 5-COMPONENT HANDOFF REPORT
Workers must return:
1. Observation (files, lines, logs)
2. Logic Chain (deductive reasoning)
3. Caveats (edge cases, unverified assumptions)
4. Conclusion (actionable output)
5. Verification (deterministic command, exit code 0)

## 8. PHYSICAL REPORT PERSISTENCE INVARIANT
1. **Mandatory Disk Persistence**:
   Every worker subagent dispatched for audit, forensics, benchmarking, or refactoring MUST have its complete 5-component handoff report persisted immediately to disk at:
   `.sessions/active/reports/[INDEX]_[CLUSTER_NAME].md`
2. **Active Session Manifest (`MANIFEST.json`)**:
   The orchestrator maintains `.sessions/active/reports/MANIFEST.json` tracking inspected clusters, responsible subagent conversation IDs, and completion timestamps.
3. **Brain Consolidation**:
   Key findings, interfaces, contracts, and module statuses from individual reports are systematically cataloged into `PROJECT_BRAIN.md`.


