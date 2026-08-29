---
description: Anti-laziness, cognitive immunity, strict data contracts, and deterministic grounding.
trigger: always_on
---
# ANTI-LAZINESS & COGNITIVE IMMUNITY

## 1. INVIOLABLE LAWS
1. Integral Code: No TODOs, pass, stubs, or mock arrays in production paths. 100% complete executable code.
2. Zero-Synthetic Proxy: No mock data, np.sin proxies, or fake approximations.
3. No Speculative Diagnosis: Inspect via view_file and trace causal DAG before diagnosing.
4. No Shotgun Edits: No random parameter changes or silent error suppression.
5. Exit Code 0: Task is DONE only when tests/builds return exit code 0.
6. Anti-Sycophancy: Refute incorrect premises with causal proof; implement verified designs.
7. Pre-Flight Grounding: Never edit a file without prior view_file.
8. Domain-Cluster Law: Group files by subsystem clusters (concurrency <= 2).
9. Zero-Polling: Yield turn after async dispatch.
10. Zero-Linger: Teardown sockets and listeners with linger=0 and bounded timeouts (<=0.5s).
11. No Error Suppression: No empty catch blocks, unchecked casts, or ignored warnings.
12. Silent Default Ban: dict.get(key, default) prohibited for decision/physics/tensor pipelines; raise typed DataLineageMissingError.
13. Empirical Variance Mandate: Every computed tensor/feature series on historical data (N>=100) must satisfy len(set(s)) > 1 and np.std(s) > 0.
14. Radical Zero-Trust: Zero assumed verified code. Actively scan for dead code, corrupted state, silent fallbacks.
15. Neutral Prompting: State inputs, outputs, and symptoms only; never pre-diagnose bugs in subagent prompts.
16. Uncompressed Reports: Persist 100% of AST findings, line citations, diffs, and test evidence in physical report files.
