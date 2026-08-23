---
description: Core Engineering Standards, TDD Red-Green-Refactor, and 12 Iron Laws of Cognitive Immunity
trigger: always_on
---
# AGI LAYER 2: ENGINEERING, TDD & REFACTORING STANDARDS

> **Scope**: Layer 2 Specialized Operational Rule for `agi-antigravity-core`.
> **Mandate**: True Red-Green-Refactor TDD, Zero Guesswork, Causal Bug Isolation, Zero Placeholders.

---

## 1. ⚡ THE RED-GREEN-REFACTOR TDD INVARIANT
Every software implementation task must follow the strict 3-phase TDD discipline:

```
[Intent / Feature Request]
          │
          ▼
┌──────────────────┐
│  1. RED PHASE    │ ──> Write failing unit/integration test suite.
└──────────────────┘     Verify test executes and fails for the expected reason.
          │
          ▼
┌──────────────────┐
│  2. GREEN PHASE  │ ──> Implement the minimal production logic to pass tests.
└──────────────────┘     Verify test suite passes cleanly with exit code 0.
          │
          ▼
┌──────────────────┐
│ 3. REFACTOR PHASE│ ──> Optimize AST, enforce strict types, eliminate redundancy.
└──────────────────┘     Assert 100% test pass rate preserved (zero regression).
```

---

## 2. 🔍 4-PHASE CAUSAL ROOT-CAUSE DEBUGGING PROTOCOL
When encountering defects, crashes, or test failures, trial-and-error shotgun edits are strictly forbidden. The agent must execute:

1. **Phase 1 (Reproduce):** Construct a minimal deterministic failing test or reproduction script that isolates the exact failure symptom.
2. **Phase 2 (Isolate):** Trace the data flow backwards from the failure point along the causal DAG to locate state corruption.
3. **Phase 3 (Diagnose):** Formulate a single falsifiable hypothesis explaining why the invariant broke.
4. **Phase 4 (Verify):** Apply the atomic fix and verify that the reproduction script and all surrounding test suites pass cleanly.

---

## 3. 🏛️ MASTER REFACTORING & DEEP ICEBERG LAWS
- **Zero-Placeholder Mandate:** All code files must be 100% complete and fully executable. Never introduce `// TODO`, mock data stubs, or placeholder functions.
- **Deep Iceberg Mandate ($X \to X \cup \{Y, W, Z\}$):** Expose latent state machines, failure recovery, idempotency, telemetry logs, and Popperian boundary stress tests.
- **Pre-Flight Verification:** Never edit a file without first viewing its contents via `view_file`.

---

## 4. 🔬 AGNOSTIC BOTTOM-UP EXCAVATION PROTOCOL (THE MECHANIC'S DISASSEMBLY LAW)

When auditing, refactoring, or investigating unfamiliar systems or broad behavioral anomalies:
1. **Zero Premature Hypothesis ("Proibição de Olhar no Pneu"):** Never guess the root cause or isolate a single component before inspecting the full repository tree ($\forall v \in \mathcal{V}$).
2. **Phase 0 Disassembly (1:1 Node Inventory):** Read and catalog 100% of files, extracting symbols, imports, data inputs, and outputs into a structural inventory.
3. **Causal Data Lineage & Dead-Code Elimination:** Map the live data pipeline from ingestion to sink; identify and quarantine unreferenced or dead AST branches.
4. **Parameter & Threshold Asphyxiation Audit:** Scan all conditional barriers and threshold filters to detect overly restrictive tolerances or normalization bugs that block valid runtime signals.
5. **Empirical Parity Verification:** Compare simulated/backtest invariants against real production/live execution (slippage, floating spread, async latency, floating-point rounding).
6. **Evidence-Driven Subagent Tribunal:** Dispatch Red/Blue subagents only after the empirical node inventory is complete, targeting verified bottlenecks.

---

## 5. 🛑 3-FAILURE ESCALATION PROTOCOL
When diagnosing or attempting to fix a defect or failing test:
1. **Consecutive Failure Limit:** If 3 consecutive fix attempts fail to resolve the defect or cause regression, halt all trial-and-error edits immediately.
2. **Causal State Re-Grounding:** Re-read and re-ground the full causal state from disk (`view_file`), resetting any assumptions or corrupted context.
3. **DAG Re-Verification:** Trace the causal dataflow backwards from the failure symptom to root cause along the DAG, formulate a fresh falsifiable hypothesis, and escalate or re-plan before attempting further modifications.

---

## 6. 🚫 NON-EXPLORATORY CODING INVARIANT & ZERO-SYNTHETIC DATA BAN
- **Non-Exploratory Coding Invariant:** Speculative or trial-and-error coding during implementation is strictly forbidden. Every edit must be preceded by pre-flight file inspection and clear contract definitions.
- **Zero-Synthetic Data Ban:** Never inject hardcoded fake datasets, synthetic mock arrays (`const MOCK_DATA = [...]`), or dummy fallback stubs into production code paths. All implementations must maintain genuine state and connect to real data pipelines and schemas.

