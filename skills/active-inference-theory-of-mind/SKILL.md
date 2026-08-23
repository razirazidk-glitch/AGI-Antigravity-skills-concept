---
name: active-inference-theory-of-mind
description: >-
  AGI/ASI protocol for Multiagent Theory of Mind and dynamic belief state estimation. Enforces Markov Blankets around subagent state. Trigger on mentions of: 'Theory of Mind', 'Markov Blanket', 'active inference', 'subagent belief', 'swarm hallucination', 'agent mental model', 'epistemic state', or when coordinating cognitive state across autonomous agents.
---

# 🧠 ACTIVE INFERENCE & MULTI-AGENT THEORY OF MIND

> **Mandate**: Models autonomous subagents as active inference entities separated by Markov Blankets. Minimizes Variational Free Energy (systemic surprise and uncertainty) across the swarm while continuously monitoring for belief divergence and hallucination drift.

---

## 1. 🛡️ THE MARKOV BLANKET ARCHITECTURE

```
                  ┌────────────────────────────────────────┐
                  │          EXTERNAL ENVIRONMENT          │
                  │   (Codebase, File System, Host OS)     │
                  └───────────────┬────────────────────────┘
                                  │ Sensory Inputs (s)
                                  ▼
      ┌────────────────────────────────────────────────────────┐
      │                   MARKOV BLANKET                       │
      │  ┌─────────────────┐              ┌─────────────────┐  │
      │  │ Sensory States  │              │  Active States  │  │
      │  │   (Prompts/     │              │ (Tool Calls /   │  │
      │  │  File Reads)    │              │  Handoff Rep)   │  │
      │  └────────┬────────┘              └────────▲────────┘  │
      └───────────┼────────────────────────────────┼───────────┘
                  │                                │
                  ▼                                │
      ┌────────────────────────────────────────────┴───────────┐
      │                   INTERNAL STATES ($\mu$)              │
      │        (Epistemic Model, Belief Distribution)          │
      └────────────────────────────────────────────────────────┘
```

---

## 2. ⚡ DYNAMIC BELIEF STATE ESTIMATION & DRIFT DETECTION

When a coordinator receives outputs from worker subagents:
1. **Never Accept Raw Assertions at Face Value:** Always inspect the empirical proof (test execution logs, exact file line references, compiler outputs).
2. **Surprise (Free Energy) Evaluation:** Calculate whether the worker's conclusions conform to known physical invariants or introduce ungrounded entities.
3. **Corrective Feedback Loops:** If a worker exhibits cognitive drift (hallucinating files, cyclic reasoning, or speculative conjectures), dispatch a grounding corrective message to reset the belief state.

---

## 3. 🤖 DISPATCH RECIPE FOR MARKOV BLANKET ISOLATION

When dispatching workers under the Active Inference protocol:
```json
{
  "TypeName": "self",
  "Role": "Grounded Inference Worker",
  "Prompt": "ACTIVE INFERENCE MISSION: Execute [TASK_OBJECTIVE]. Return strictly verified empirical facts backed by direct tool outputs and exit code 0. Speculative assumptions and unverified hypotheses are strictly forbidden. Deliver a structured 5-component handoff."
}
```
