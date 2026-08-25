---
description: Master Engineering, TDD Standards, Causal Root-Cause Debugging, and Deep Iceberg Laws.
trigger: always_on
---
# AGI LAYER 2: ENGINEERING, TDD & REFACTORING STANDARDS

> **Mandate**: True Red-Green-Refactor TDD, Zero Guesswork, Causal Bug Isolation, Zero Placeholders.

---

## 1. ⚡ RED-GREEN-REFACTOR TDD INVARIANT
Every implementation follows 3 strict phases:
1. **RED**: Write failing test first. Verify it fails for expected reason.
2. **GREEN**: Implement minimal production logic to pass test. Exit code `0`.
3. **REFACTOR**: Optimize AST, enforce types, eliminate redundancy. Zero regressions.

---

## 2. 🔍 4-PHASE CAUSAL ROOT-CAUSE DEBUGGING
Trial-and-error shotgun edits strictly forbidden:
1. **Reproduce**: Minimal deterministic failing test isolating symptom.
2. **Isolate**: Trace data flow backwards along causal DAG to corrupted state.
3. **Diagnose**: Single falsifiable hypothesis explaining invariant breach.
4. **Verify**: Atomic fix + full test suite passes (exit code `0`).

---

## 3. 🏛️ MASTER REFACTORING & DEEP ICEBERG LAWS
- **Zero-Placeholder Mandate:** 100% complete executable files. No `// TODO`, mocks, or stubs.
- **Deep Iceberg Mandate ($X \to X \cup \{Y, W, Z\}$):** Expose state machines, failure recovery, idempotency, Popperian tests.
- **Pre-Flight Verification:** Read target files via `view_file` before editing.

---

## 4. 🔬 AGNOSTIC BOTTOM-UP EXCAVATION PROTOCOL
Auditing unfamiliar systems:
1. **Zero Premature Hypothesis:** Inspect full repo ($\forall v \in \mathcal{V}$) before guessing root cause.
2. **1:1 Node Inventory:** Catalog 100% of files — symbols, imports, inputs, outputs.
3. **Causal Data Lineage:** Map live pipeline from ingestion to sink; quarantine dead AST branches.
4. **Threshold Audit:** Scan conditional barriers for restrictive tolerances or normalization bugs.
5. **Empirical Parity:** Compare simulated vs live execution (latency, rounding, spread).
6. **Domain-Cluster Processing:** Group in clusters ($C_{\max} \le 2$); tribunal only after 100% node inventory in `PROJECT_BRAIN.md`.

---

## 5. 🛑 3-FAILURE ESCALATION PROTOCOL
1. After 3 consecutive failed fix attempts: halt edits immediately.
2. Re-read target files from disk (`view_file`), reset assumptions.
3. Re-trace causal DAG, formulate new hypothesis. Write to `FAILURE_REGISTRY.md`.

---

## 6. 🚫 NON-EXPLORATORY CODING & ZERO-SYNTHETIC DATA
- Speculative trial-and-error coding forbidden.
- Never inject fake datasets or dummy stubs in production paths. Connect to real schemas.

---

## 7. 🔌 SOCKET LINGER-0 TEARDOWN
For all sockets, threads, WebSockets, gRPC, TCP:
1. Configure `socket.setsockopt(LINGER, 0)` and `socket.close(linger=0)` before termination.
2. Test teardown hooks join threads with bounded timeouts ($\le 0.5\text{s}$).
