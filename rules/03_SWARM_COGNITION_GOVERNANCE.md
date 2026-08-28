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
- REQUIRED: Group by subsystem/directory clusters. Trace all files in cluster together.

## 4. ANTI-DIRECTED FRAMING (HYPOTHESIS ISOLATION)
- PROHIBITED: Injecting pre-conceived hypotheses into worker prompts (e.g., "check if line 1298 inverts signal"). Causes cognitive myopia where workers confirm prompts and miss structural defects.
- PROHIBITED: Silo auditing without cross-module integration tests. Every module must prove live data wiring to upstream and downstream sinks.
- REQUIRED PROMPT FORMAT:
  `"CLUSTER AUDIT: Disassemble ALL files in [DIR] together. Map all symbol inputs/outputs. Trace data lineage from [INGESTION] to [SINK]. Formulate hypotheses from evidence only. Report all cross-cluster seams."`

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


