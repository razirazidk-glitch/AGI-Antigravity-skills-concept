---
description: Corporate Swarm Governance, Subagent Concurrency (C_max <= 2), and Reactive Wakeup
trigger: always_on
---
# AGI LAYER 3: SWARM COGNITION & MULTI-AGENT GOVERNANCE

> **Scope**: Layer 3 Specialized Operational Rule for `agi-antigravity-core`.
> **Mandate**: Strict Concurrency Limit ($C_{\max} \le 2$), Reactive Wakeup, Corporate OS Hierarchy, Theory of Mind.

---

## 1. 🐝 SWARM CONCURRENCY & ZERO-POLLING INVARIANTS
- **Concurrency Boundary ($C_{\max} \le 2$):** Never spawn more than 2 subagents concurrently to avoid context degradation, token churn, and 429 quota exhaustion.
- **Zero-Polling Mandate:** Never poll or check subagent/task status in a busy loop (`manage_task(status)`, `manage_subagents(list)`). Dispatch tasks/subagents and immediately yield the turn to let the platform wake the agent reactively.

---

## 2. 🏛️ CORPORATE SWARM OS & ROLE DELEGATION
- **Autonomous Hierarchy:** Orchestrate multi-agent teams following CEO $\to$ C-Level $\to$ Specialized Workers structure.
- **Artifact Governance:** Generate `BRIEF.md` for team-level contracts and `PROJECT_BRAIN.md` for recursive cross-module state tracking.
- **Theory of Mind & Markov Blankets:** Maintain explicit context boundaries around worker subagent memory to prevent swarm hallucination.

---

## 3. 📦 5-COMPONENT STRUCTURED SUBAGENT HANDOFF
Every inter-agent task handoff must adhere to the 5-part protocol:
1. **Observation:** Empirical summary of what was discovered or executed.
2. **Logic Chain:** Step-by-step causal chain leading to the conclusion.
3. **Caveats:** Edge cases, unverified assumptions, or boundary conditions.
4. **Conclusion:** Concrete actionable finding or artifact generated.
5. **Verification Method:** Deterministic command or test to verify the handoff output.
