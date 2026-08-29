---
name: swarm-legacy-archaeology
description: >-
  Swarm auditing of legacy repos, 100% node disassembly, and seam verification. Trigger on: legacy archaeology, codebase archaeology, legacy audit, AST analysis, repo excavation, sprint audit.
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

## 4. 🤖 DOMAIN-CLUSTER SWARM EXCAVATION PROTOCOL

To achieve 100% node coverage without API quota exhaustion (`HTTP 429`) or context fragmentation:

1. **Deterministic Batch Pre-Scan (Step 0):**
   - The Principal Agent executes a deterministic recursive scan (or AST extraction script) over the root target directory to map 100% of file paths, lines of code, and imports before spawning subagents.
   - Record the full inventory in `PROJECT_BRAIN.md`.

2. **Domain-Cluster Chunking:**
   - Group files by cohesive subsystem directories / packages (e.g. `Code/Bridge/mt5/` with all its 8 files analyzed in one cluster context).
   - **Strict Ban on 1:1 File Spawning:** Never spawn individual subagents for each isolated source file.

3. **Bounded Swarm Execution ($C_{\max} \le 2$):**
   - Dispatch workers for each subsystem cluster sequentially or in pools of 2:

```json
{
  "TypeName": "research",
  "Role": "Subsystem Cluster Archaeology Worker",
  "Prompt": "LEGACY ARCHAEOLOGY CLUSTER: Perform a complete semantic AST audit of cluster directory [TARGET_CLUSTER_DIR]. Inspect all files in this module together to trace internal state interactions, verify exported symbol contracts, extract call graphs, compute cyclomatic complexity, and detect dead branches or threshold asphyxiation. Deliver a structured 5-component handoff report."
}
```

4. **Gate of Full Coverage (Tribunal Firewall):**
   - Adversarial Red/Blue Team audits and refactoring proposals are **STRICTLY BLOCKED** until 100% of module clusters report complete inventory status in `PROJECT_BRAIN.md`.

---

## 5. 🔗 MANDATORY INTEGRATION SEAM VERIFICATION (CROSS-CLUSTER)

> **Production-Verified Failure:** Two workers each declared their individual cluster "correct" in isolation — `fluid_dynamics.py` math was verified, `singularity_arbiter.py` logic was verified — but NOBODY traced whether the output of one was actually wired into the input of the other. The integration seam was the actual failure point, invisible to both workers.

**This section is NON-OPTIONAL. It runs AFTER all cluster reports are received and BEFORE any tribunal.**

### 5.1 Cross-Cluster Seam Mapping Protocol

After all cluster workers return their reports, the Principal Agent MUST build the **Full Data Lineage DAG**:
```
[Ingestion Source] → [Transform A] → [Module B input] → [Transform B] → [Output Sink]
```
Map this graph across ALL cluster boundaries. Every inter-cluster edge is an explicit seam that must be verified.

**Per-seam verification checklist:**
```markdown
## Seam: [Cluster A output] → [Cluster B input]
- [ ] A's output type matches B's expected input type (empirically verified, not assumed)
- [ ] A's output is actually consumed by B (grep-confirmed, not assumed)
- [ ] The data transformation A→B produces values in B's expected range/domain
- [ ] An integration test exercises this seam end-to-end
- [ ] PROHIBITED: Marking VERIFIED based on A's unit tests or B's unit tests alone
```

### 5.2 Seam Failure Taxonomy

| Failure Type | Symptom | Detection Method |
|---|---|---|
| **Dead Output** | A produces data nobody reads | `grep` A's return value consumed by B |
| **Type Mismatch** | A outputs `float`, B expects `int` | AST type annotation cross-check |
| **Domain Violation** | A outputs normalized [0,1], B expects raw signal | Trace expected value ranges through transforms |
| **Phantom Connection** | Comment says "connected" but call graph shows no edge | Live call graph, not documentation trust |

### 5.3 Required Deliverable: `SEAM_REPORT.md`

Every archaeology mission delivers this before any refactoring begins:
```markdown
# SEAM REPORT — [PROJECT NAME] — [TIMESTAMP]

## ✅ Verified Seams (live connection confirmed)
| Seam | Output Type | Input Type | Consuming Call | Status |

## ❌ Broken Seams (disconnected or type-mismatched)
| Seam | Expected | Actual | Impact | Priority |

## ⚠️ Unknown Seams (requires investigation)
| Seam | Blocker | Next Step |
```
