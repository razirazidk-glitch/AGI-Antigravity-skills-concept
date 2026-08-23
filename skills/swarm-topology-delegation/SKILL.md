---
name: swarm-topology-delegation
description: >-
  Governs multi-level parallel chat swarms, programmatic subagent teams, and worker role classification. Trigger on mentions of: 'swarm topology', 'topology delegation', 'subagent delegation', 'swarm map', 'worker role classification', 'CEO direct swarm', 'team orchestration', or when designing multi-agent topologies.
---

# 🐝 DYNAMIC MULTI-AGENT TOPOLOGY & TASK GRAPH ORCHESTRATION

> **Mandate**: Models multi-agent task execution as an acyclic dependency graph $G = (V, E)$. Governs node classifications, role specializations, Byzantine fault tolerance, and strict concurrency pacing ($C_{\max} \le 2$).

---

## 1. 🏗️ MULTI-AGENT TOPOLOGY ARCHITECTURES

```
[1. Hierarchical Tree]          [2. Paced Parallel Workers]         [3. Blind Critic Loop]
        ┌─────┐                         ┌─────┐                            ┌────────┐
        │ CEO │                         │ Lead│                            │Builder │
        └──┬──┘                         └──┬──┘                            └───┬────┘
      ┌────┴────┐                     ┌────┴────┐                              │ (Candidate)
      ▼         ▼                     ▼         ▼                              ▼
  ┌──────┐   ┌──────┐             ┌───────┐ ┌───────┐                      ┌────────┐
  │Lead A│   │Lead B│             │Worker1│ │Worker2│                      │ Critic │
  └──────┘   └──────┘             └───────┘ └───────┘                      └────────┘
                                 (Max 2 Concurrent)                        (Q >= 9.0)
```

---

## 2. 📊 NODE CLASSIFICATION MATRIX

| Node Class | Execution Model | Memory Isolation | Concurrency Policy | Best Used For |
|---|---|---|---|---|
| **Class $\alpha$ (Inline)** | Current Context Turn | Shared Context | Single Agent | Quick file reads, small patches, prompt elevation. |
| **Class $\beta$ (Programmatic Worker)** | `invoke_subagent` (`self` / `research`) | Isolated Thread | Max 2 Concurrent | Deep multi-file research, isolated tests, archaeology. |
| **Class $\gamma$ (Sub-Orchestrator)** | Hierarchical Lead Agent | Branched Workspace | Sequential Pacing | Large multi-sector features, corporate OS modules. |

---

## 3. 🛡️ BYZANTINE FAULT TOLERANCE & DRIFT CONTROL

1. **Anti-Hallucination Barrier:** Every subagent result must be backed by file line numbers, test execution outputs, or direct citations. Pure assertions without evidence are rejected.
2. **Semantic Drift Sentinel:** If worker outputs diverge from the mission contract by $\Delta > 0.15$, trigger an immediate rollback to the latest state checkpoint.
3. **Reactive Wakeup Invariant:** After dispatching workers via `invoke_subagent`, the supervisor must yield execution immediately and await system notifications. Busy-loop polling is strictly forbidden.
