---
description: Engineering, TDD standards, causal root-cause debugging, and strict data contracts.
trigger: always_on
---
# ENGINEERING & TDD STANDARDS

## 1. RED-GREEN-REFACTOR TDD INVARIANT
1. RED: Write minimal failing test first. Verify it fails for expected causal reason.
2. GREEN: Implement minimal production code to pass test (exit code 0).
3. REFACTOR: Clean AST, enforce strict types, remove redundancy. Zero regressions.

## 2. 4-PHASE CAUSAL DEBUGGING
Trial-and-error shotgun edits strictly prohibited:
1. Reproduce: Deterministic failing test isolating the defect.
2. Isolate: Backward causal trace to corrupted state.
3. Diagnose: Single falsifiable hypothesis explaining invariant breach.
4. Verify: Atomic fix + full test suite exit code 0.

## 3. STRICT DATA CONTRACTS & NO SYNTHETIC PROXIES
- Prohibited: Injecting fake datasets, mock arrays, or np.sin proxies in production/test pipelines.
- Prohibited: dict.get(key, default) for decision/physics/ML pipelines.
- Required: Strict typed @dataclass or functions raising DataLineageMissingError on missing keys.

## 4. AGNOSTIC BOTTOM-UP EXCAVATION
When auditing unfamiliar codebases:
1. Zero premature hypotheses before 100% node inventory.
2. Catalog all symbols, inputs, outputs across files in cluster.
3. Trace live pipeline from ingestion to output sinks.
4. Scan conditionals for restrictive thresholds and normalization errors.

## 5. CIRCUIT BREAKER & ESCALATION
- After 3 consecutive failed fixes: HALT edits immediately.
- Re-read target files from disk via view_file, reset assumptions, log to FAILURE_REGISTRY.md.

## 6. SOCKET & RESOURCE TEARDOWN
- Configure socket.setsockopt(LINGER, 0) and socket.close(linger=0) before exit.
- Join threads and teardown WebGL/listeners with bounded timeouts (<=0.5s).

