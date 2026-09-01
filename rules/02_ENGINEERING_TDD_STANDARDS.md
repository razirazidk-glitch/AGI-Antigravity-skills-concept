---
description: Engineering, TDD standards, causal root-cause debugging, and strict data contracts.
trigger: always_on
---
# ENGINEERING & TDD STANDARDS

## 1. RED-GREEN-REFACTOR
1. RED: Minimal failing test first. Verify deterministic failure for expected cause.
2. GREEN: Minimal production code to pass test (exit code 0).
3. REFACTOR: Clean AST, strict typing, zero redundancy, zero regressions.

## 2. 4-PHASE CAUSAL DEBUGGING
- Prohibited: Trial-and-error edits and speculative guesses.
1. Reproduce: Minimal deterministic test.
2. Isolate: Backward trace from symptom to root cause.
3. Diagnose: Single falsifiable hypothesis.
4. Verify: Atomic fix + 100% test pass (exit code 0).

## 3. STRICT DATA CONTRACTS
- Prohibited: Mock data, synthetic proxy arrays, np.sin proxies in production/test pipelines.
- Prohibited: dict.get(key, default) for decision/physics/ML pipelines.
- Required: Strict typed dataclasses or functions raising DataLineageMissingError on missing keys.

## 4. CIRCUIT BREAKER & CLEANUP
- Halt edits after 3 consecutive failed fixes; re-read target files from disk.
- Configure socket LINGER=0 on teardown. Bounded thread/listener teardown (<=0.5s).

## 5. THE DUAL-POLE ISOMORPHISM LAW (DIGITAL TWIN PARITY)
- Invariant: Zero behavioral divergence between Simulation/Sandbox/Staging pole ($P_{sim}$) and Production/Live pole ($P_{prod}$).
- Synchronous Mirroring: Any mechanic, filter, state machine, or configuration modified in one pole MUST be simultaneously implemented and verified with identical causal behavior in the other pole.
- Pre-Release Parity Gate: No component or engine upgrade may be deployed to Production without passing the identical benchmark in Simulation with exit code 0.

## 6. THE MECHANIC'S DISASSEMBLY LAW (ZERO BLIND REFACTORING)
- Before altering or modernizing existing subsystems: catalog 100% of symbols and establish minimal reproducible baseline test probes to capture prior behavior before modifying AST.
