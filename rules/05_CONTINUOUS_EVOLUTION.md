---
description: Gauntlet review, dual-gate convergence, and two-layer /learn meta-learning.
trigger: always_on
---
# CONTINUOUS EVOLUTION & META-LEARNING

## 1. DUAL-GATE CONVERGENCE
- Gate A (Empirical): 100% test suite pass (exit code 0).
- Gate B (Adversarial): Red Team qualitative review (Q >= 9.0/10).
- Refinement cycles continue until score converges (delta Q < epsilon).

## 2. TWO-LAYER META-LEARNING (/learn)
- Layer 1 (Local Workspace): Project-specific rules/skills in `<workspace>/.agents/rules/` and `<workspace>/.agents/skills/`. Never pollute global core.
- Layer 2 (Global AGI Core): Universal invariants in `agi-antigravity-core`. Propose via `/learn` upon resolving non-trivial causal defects or major milestones.

