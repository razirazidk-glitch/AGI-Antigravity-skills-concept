---
description: Swarm Cognition, Concurrency Boundaries, Corporate OS Governance, and Declarative Subagent Registration.
trigger: always_on
---
# AGI LAYER 3: SWARM COGNITION & MULTI-AGENT GOVERNANCE

> **Mandate**: Strict Concurrency Limit ($C_{\max} \le 2$), Reactive Wakeup, Corporate OS Hierarchy, Theory of Mind.

---

## 1. 🐝 SWARM CONCURRENCY & ZERO-POLLING
- **Concurrency Limit ($C_{\max} \le 2$):** Max 2 concurrent subagents to prevent context degradation and 429 quota exhaustion.
- **Zero-Polling Mandate:** Never poll `manage_task(status)` or `manage_subagents(list)`. Dispatch and yield turn to wake reactively.

---

## 2. 🏛️ CORPORATE SWARM OS & ROLE DELEGATION
- **Autonomous Hierarchy:** Orchestrate multi-agent teams following CEO $\to$ C-Level $\to$ Specialized Workers structure.
- **Artifact Governance:** Generate `BRIEF.md` for team contracts and `PROJECT_BRAIN.md` for cross-module state tracking.
- **Theory of Mind:** Maintain explicit context boundaries around worker subagent memory.

---

## 3. 📦 5-COMPONENT STRUCTURED SUBAGENT HANDOFF
Every inter-agent transfer report must contain:
1. **Observation:** Empirical summary of what was discovered/executed (files, lines, logs).
2. **Logic Chain:** Deductive step-by-step reasoning leading to conclusion.
3. **Caveats:** Edge cases, unverified assumptions, or boundary conditions.
4. **Conclusion:** Concrete actionable finding or artifact generated.
5. **Verification Method:** Deterministic command or test to verify handoff output.

---

## 4. ⚙️ DECLARATIVE SUBAGENT REGISTRATION
To prevent executor construction errors:
- **Built-in Compliance:** If invoking without custom definition, `TypeName` MUST strictly be `"self"` or `"research"`.
- **Pre-Registration (`define_subagent`):** Custom `TypeName` MUST be registered via `define_subagent` BEFORE calling `invoke_subagent`.
- **Declarative Contracts:** Provide full config: `name`, `description`, `system_prompt`, `enable_write_tools`, `enable_mcp_tools`, `enable_subagent_tools`.

---

## 5. 🌐 DOMAIN-CLUSTER DELEGATION LAW
- **Zero 1:1 File-to-Agent Spawning:** Never spawn individual subagents per single file.
- **Domain-Cluster Allocation:** Delegate subagents by cohesive functional clusters or subsystem directories.
- **Bounded Pool:** Maintain $C_{\max} \le 2$ concurrent workers processed sequentially or via bounded queue pool.
