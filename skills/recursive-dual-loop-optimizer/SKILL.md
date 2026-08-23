---
name: recursive-dual-loop-optimizer
description: >-
  AGI Recursive Self-Improvement engine implementing a Dual-Loop architecture to rewrite system prompts and skills without Model Collapse. Trigger on mentions of: 'dual loop optimizer', 'self-improvement', 'prevent model collapse', 'prompt optimization', 'skill optimization', 'recursive optimization', 'meta prompt tuning', or when refining core agent prompts.
---

# 🔄 RECURSIVE DUAL-LOOP OPTIMIZER & SELF-IMPROVEMENT ENGINE

> **Mandate**: Governs safe, autonomous self-mutation of skills and operational rules on disk. Implements an Inner/Outer Loop feedback cycle that eliminates cognitive inertia while mathematically preventing Model Collapse.

---

## 1. 🏗️ DUAL-LOOP ARCHITECTURAL TOPOLOGY

```
┌────────────────────────────────────────────────────────┐
│  INNER LOOP (Task Execution & Empirical Performance)  │
│  - Executes user requests, compiles code, runs tests   │
└──────────────────────────┬─────────────────────────────┘
                           │ Task Failures / Friction Logs
                           ▼
┌────────────────────────────────────────────────────────┐
│  OUTER LOOP (Meta-Optimization & Skill Mutation)       │
│  - Analyzes cognitive bottlenecks in SKILL.md/Rules    │
│  - Synthesizes improved instructions & trigger words   │
│  - Validates mutation against Gold Standard Benchmarks │
└──────────────────────────┬─────────────────────────────┘
                           │ Atomic Commit (if Q >= 9.0)
                           ▼
               [Updated Durable Platform]
```

---

## 2. 🛡️ ANTI-MODEL COLLAPSE INVARIANTS

To prevent self-referential degradation or circular prompt drift:
1. **Information Entropy Preservation:** Mutations must increase density and concrete actionable heuristics without adding vague conversational fluff.
2. **Gold Standard Benchmark Guard:** Any proposed skill or rule mutation must run against the full suite (`python test_plugin.py` and `python -m unittest discover -s tests`). If even a single regression or tie occurs, the mutation is immediately aborted.
3. **Immutable Core Laws:** The fundamental axioms in `rules/AGENTS.md` (Constitutional Sovereignty, Axiom of Invisible, Zero-Placeholders, Concurrency $C_{\max} \le 2$) cannot be removed or weakened by autonomous optimization.

---

## 3. 🛠️ MUTATION WORKFLOW RUNBOOK

When refining or synthesizing a skill:
1. **Step 1 (Isolate):** Copy the target `SKILL.md` to a temporary sandbox.
2. **Step 2 (Mutate):** Refactor the YAML frontmatter and markdown body with crisp triggers and operational runbooks.
3. **Step 3 (Validate):** Execute all static schema, tool binding, placeholder, and link resolution tests:
   ```bash
   python test_plugin.py
   ```
4. **Step 4 (Atomic Commit):** Overwrite the target skill file only upon 100% test pass (`exit code 0`).
