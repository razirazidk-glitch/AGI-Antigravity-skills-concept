---
description: Gauntlet review, dual-gate convergence, and two-layer /learn meta-learning.
trigger: always_on
---
# CONTINUOUS EVOLUTION & META-LEARNING

## 1. DUAL-GATE CONVERGENCE
- Gate A (Empirical): 100% test suite pass (exit code 0).
- Gate B (Adversarial): Red Team qualitative review (Q >= 9.0/10).

## 2. TWO-LAYER META-LEARNING (/learn)
- Layer 1 (Local Workspace): Project-specific rules/skills in `<workspace>/.agents/`.
- Layer 2 (Global AGI Core): Universal invariants in `agi-antigravity-core`.

## 3. POST-EDIT PROTOCOL & GIT SYNC
- After rule/skill edit, notify user: "Regra/skill atualizada. Reinicie o Antigravity IDE para que as mudanças entrem em vigor."
- Execute immediately after edits in PowerShell:
  git add .; git commit -m "<type>: <summary>"; git push
- Types: learn, fix, feat. Uncommitted changes prohibited.
