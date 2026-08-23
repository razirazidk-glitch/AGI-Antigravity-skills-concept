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
