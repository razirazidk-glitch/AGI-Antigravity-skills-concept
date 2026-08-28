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

## 3. POST-EDIT RESTART PROTOCOL
After ANY modification to a rule (`rules/*.md`) or skill (`skills/*/SKILL.md`):
1. Commit and push changes to git (see §4 GIT SYNC INVARIANT).
2. ALWAYS notify the user: "⚠️ Regra/skill atualizada. Reinicie o Antigravity IDE para que as mudanças entrem em vigor."
3. Do NOT assume the new behavior is active until user confirms restart.

## 4. GIT SYNC INVARIANT (Windows/PowerShell)
After modifying any file in `agi-antigravity-core`:
- REQUIRED: Execute immediately after edits (PowerShell syntax — `&&` is INVALID):
  ```powershell
  git add .; git commit -m "<type>: <summary>"; git push
  ```
- Commit message format: `learn: <description>` for /learn sessions, `fix: <description>` for bug fixes, `feat: <description>` for new additions.
- PROHIBITED: Leaving uncommitted changes without explicit user request.

