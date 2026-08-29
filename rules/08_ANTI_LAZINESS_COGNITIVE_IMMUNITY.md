---
description: Anti-laziness, cognitive immunity, strict data contracts, and deterministic grounding.
trigger: always_on
---
# ANTI-LAZINESS & COGNITIVE IMMUNITY

## 1. INVIOLABLE LAWS
1. Integral Code: No TODOs, pass, stubs, or mock arrays in production paths. 100% complete executable code.
2. Zero-Synthetic Proxy: No mock data, np.sin proxies, or fake approximations. Real schemas only.
3. No Speculative Diagnosis: Inspect via view_file and trace causal DAG before diagnosing.
4. No Shotgun Edits: No random parameter changes or silent try/catch wrapping.
5. Exit Code 0: Task is DONE only when tests, builds, or traces return exit code 0.
6. Anti-Sycophancy: Refute incorrect premises with causal proofs; implement verified designs.
7. Pre-Flight Grounding: Never edit a file without prior view_file.
8. Domain-Cluster Law: Group files by subsystem clusters (concurrency <= 2). Never 1 agent per file.
9. Zero-Polling: Yield turn after async dispatch. Never poll status loops.
10. Zero-Linger: Teardown sockets, threads, WebGL, listeners with linger=0 and bounded timeouts (<=0.5s).
11. No Error Suppression: No empty catch blocks, unchecked type casts, or ignored warnings.
12. Workspace Isolation: Local conventions stay in .agents/. Global rules stay domain-agnostic.
13. Silent Default Ban: dict.get(key, default) is PROHIBITED for decision engines, physics pipelines, feature tensors, and trading signals. Missing keys MUST raise typed exceptions (DataLineageMissingError).
14. Empirical Variance Mandate: Every computed tensor/feature series on historical data (N>=100) must satisfy len(set(s)) > 1 and np.std(s) > 0. If std == 0, auto-FAIL for Ghost Data. Exit code 0 with static/mock data is invalid proof.
15. Radical Zero-Trust Mandate: Assume 0% of codebase is verified a priori. Actively hunt for simplified stubs, dead code, corrupted mathematical states, silent fallback traps, and memory/socket leaks.
16. Hypothesis-Free Neutral Prompting: Never dictate what bug to find or pre-diagnose the defect in prompts. Prescriptive prompts (such as "find bug X in logic Y") trigger model confirmation bias and hallucinations. Prompts MUST state ONLY inputs, outputs, boundaries, and observed symptoms.
17. Uncompressed High-Density Reports: Never persist lossy or compact summaries of audits or refactors. Physical report files must contain 100% of AST findings, line citations, before/after diffs, and raw execution evidence.

## 2. 5-PHASE CAUSAL DIAGNOSIS
1. Reproduce: Minimal script failing with exit code != 0.
2. Trace: Backward DAG trace from failure to corrupted state.
3. Diagnose: Single falsifiable hypothesis explaining invariant breach.
4. Atomic Fix: Minimum change restoring invariant.
5. Verify: Test suite exit code 0 on real data.
Circuit Breaker: Halt after 3 failed attempts, re-read files from disk, log to FAILURE_REGISTRY.md.

## 3. STRICT TYPED CONTRACT PATTERN
```python
# PROHIBITED: dict.get(k, default)
# REQUIRED: Strict typed dataclass or explicit missing-key accessor
from dataclasses import dataclass

@dataclass(frozen=True)
class SignalRow:
    signal: float  # required, no default

def strict_get(d: dict, key: str):
    if key not in d:
        raise DataLineageMissingError(f"Missing '{key}'. Keys: {list(d.keys())}")
    return d[key]
```

## 4. GHOST DATA DETECTION PROTOCOL
```python
# Mandate for all tensor/feature pipelines:
series = [compute(x) for x in historical_bars] # N >= 100
assert len(set(series)) > 1, f"Ghost data: constant value {series[0]}"
assert np.std(series) > 0, "Ghost data: zero variance"
assert min(series) != max(series), "Ghost data: min equals max"
```

## 5. EVIDENCE TAXONOMY
- T1 (Disk): view_file/grep line citations.
- T2 (Execution): Command/test output with exit code 0.
- T3 (Formal): Logical derivation from T1/T2.
- T4 (Inference): Tag [T4 - unverified] and verify via tools before asserting.


