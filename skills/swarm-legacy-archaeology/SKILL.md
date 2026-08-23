---
name: swarm-legacy-archaeology
description: >-
  Consolidated protocol for multi-level parallel swarm auditing of legacy repositories, 100% node disassembly, AST 3-tier complexity classification, and sprint audit persistence. Trigger on mentions of: 'legacy archaeology', 'codebase archaeology', 'legacy audit', 'legacy repository scan', 'batch planning', 'coverage gate', 'repository excavation', 'audit tier', 'codebase audit', 'complexity classification', 'AST analysis', 'entropy scan', 'sprint audit', or when onboarding onto unfamiliar legacy code.
---

# 🏛️ UNIVERSAL CORPUS ARCHAEOLOGY & SEMANTIC DEPENDENCY MAPPER

> **Mandate**: Systematic, zero-guesswork excavation of legacy or unfamiliar repositories. Disassembles 100% of codebase nodes onto the mechanic's workbench without preconceived hypotheses, maps AST dependency graphs, extracts symbol contracts, classifies complexity tiers, and enforces formal coverage gates before refactoring.

---

## 1. 🔬 THE MECHANIC'S DISASSEMBLY INVARIANT (ZERO-PRECONCEPTION)

Never diagnose an unfamiliar system by "pointing at a tire". A true engineering audit disassembles all micro-components onto the workbench without bias:
- **Zero Premature Hypothesis:** Prohibit formulating a single culprit or inventing technical buzzwords before 100% of files are inventoried.
- **Exhaustive Scope ($\forall v \in \mathcal{V}$):** Every file is an individual component on the bench with its inputs, outputs, mutability, and callers mapped.

---

## 2. 🔍 4-PHASE ARCHAEOLOGY WORKFLOW

```
┌───────────────────────────┐
│ 1. Structural Discovery   │ ──> Recursive file tree scan, file sizes, extensions, LOC (100% of nodes).
└───────────────────────────┘
              │
              ▼
┌───────────────────────────┐
│ 2. AST & Symbol Graphing  │ ──> Extract exported classes, functions, types, and call graphs.
└───────────────────────────┘
              │
              ▼
┌───────────────────────────┐
│ 3. Complexity & Pathologies│ ──> Compute cyclomatic complexity, dead code, threshold asphyxiation.
└───────────────────────────┘
              │
              ▼
┌───────────────────────────┐
│ 4. Topological Coverage   │ ──> Generate semantic_coverage_proof.json & evidence-based tribunal.
└───────────────────────────┘
```

---

## 3. 📊 3-TIER COMPLEXITY CLASSIFICATION

Every module in the scanned codebase is assigned an audit tier:

| Tier | Classification | Cyclomatic Complexity ($M$) | Action Protocol |
|---|---|---|---|
| **Tier 1 (T1)** | **Critical Core** | $M \ge 15$ or Core State Engine | Deep formal review, 100% test coverage contract, invariant tree proofs. |
| **Tier 2 (T2)** | **Module Interface** | $5 \le M < 15$ or Boundary API | Type contract verification, mock elimination, cross-sector validation. |
| **Tier 3 (T3)** | **Utility & Data** | $M < 5$ or Pure Helpers | Unit test baseline, dead code removal, style refactoring. |

---

## 4. 🤖 SWARM DISPATCH & EXCAVATION PROTOCOL

When delegating legacy archaeology to research workers:
1. Enforce $C_{\max} \le 2$ concurrent workers.
2. Structure the dispatch payload with explicit bounding contracts:

```json
{
  "TypeName": "research",
  "Role": "Corpus Archaeology Worker",
  "Prompt": "LEGACY ARCHAEOLOGY: Perform a semantic AST scan of directory [TARGET_DIR]. Extract exported symbols, call graphs, external dependencies, cyclomatic complexity metrics, and identify dead code or unreferenced modules. Deliver a structured 5-component handoff report."
}
```

3. Collect the archaeology findings and feed them directly into `swarm-synthesis-protocol`.

