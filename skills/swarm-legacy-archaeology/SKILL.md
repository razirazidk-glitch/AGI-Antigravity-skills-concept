---
name: swarm-legacy-archaeology
description: >-
  Consolidated protocol for multi-level parallel swarm auditing of legacy repositories, directory mapping, and tier classification. Trigger on mentions of: 'legacy archaeology', 'codebase archaeology', 'legacy audit', 'legacy repository scan', 'batch planning', 'coverage gate', 'repository excavation', or when onboarding onto unfamiliar legacy code.
---

# 🏛️ UNIVERSAL CORPUS ARCHAEOLOGY & SEMANTIC DEPENDENCY MAPPER

> **Mandate**: Systematic, zero-guesswork excavation of legacy or unfamiliar repositories. Maps AST dependency graphs, extracts symbol contracts, classifies complexity tiers, and enforces formal coverage gates before refactoring.

---

## 1. 🔍 4-PHASE ARCHAEOLOGY WORKFLOW

```
┌───────────────────────────┐
│ 1. Structural Discovery   │ ──> Recursive file tree scan, file sizes, extensions, LOC.
└───────────────────────────┘
              │
              ▼
┌───────────────────────────┐
│ 2. AST & Symbol Graphing  │ ──> Extract exported classes, functions, types, and call graphs.
└───────────────────────────┘
              │
              ▼
┌───────────────────────────┐
│ 3. Complexity Tiering     │ ──> Compute cyclomatic complexity & entropy to assign T1/T2/T3 tiers.
└───────────────────────────┘
              │
              ▼
┌───────────────────────────┐
│ 4. Topological Coverage   │ ──> Generate semantic_coverage_proof.json before touching code.
└───────────────────────────┘
```

---

## 2. 📊 3-TIER COMPLEXITY CLASSIFICATION

Every module in the scanned codebase is assigned an audit tier:

| Tier | Classification | Cyclomatic Complexity ($M$) | Action Protocol |
|---|---|---|---|
| **Tier 1 (T1)** | **Critical Core** | $M \ge 15$ or Core State Engine | Deep formal review, 100% test coverage contract, invariant tree proofs. |
| **Tier 2 (T2)** | **Module Interface** | $5 \le M < 15$ or Boundary API | Type contract verification, mock elimination, cross-sector validation. |
| **Tier 3 (T3)** | **Utility & Data** | $M < 5$ or Pure Helpers | Unit test baseline, dead code removal, style refactoring. |

---

## 3. 🤖 SWARM DISPATCH & EXCAVATION PROTOCOL

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
