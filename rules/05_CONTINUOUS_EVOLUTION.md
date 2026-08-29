---
description: Gauntlet review, dual-gate convergence, and two-layer /learn meta-learning.
trigger: always_on
---
# CONTINUOUS EVOLUTION & META-LEARNING

## 1. DUAL-GATE CONVERGENCE
- Gate A (Empirical): 100% test suite pass (exit code 0).
- Gate B (Adversarial): Red Team qualitative review (Q >= 9.0/10).

## 2. TWO-LAYER META-LEARNING (/learn) & DOMAIN QUARANTINE
- **Layer 1 (Local Workspace - `<workspace>/.agents/`):**
  - Destination for ALL niche domain knowledge, vertical business rules, industry standards (e.g., Medical/FHIR vs Automotive/OBD-II), project schemas, and framework specifics.
  - Quarantined strictly to repository version control.
- **Layer 2 (Global AGI Core - `agi-antigravity-core`):**
  - Restricted EXCLUSIVELY to universal, domain-agnostic meta-invariants, System 2 reasoning protocols, epistemics, and cross-paradigm engineering standards.
  - **Universal Invariance Filter**: Must be 100% transposable across any technical domain without semantic or cognitive friction.

## 3. POST-EDIT PROTOCOL & GIT SYNC
- After rule/skill edit, notify user: "Regra/skill atualizada. Reinicie o Antigravity IDE para que as mudanças entrem em vigor."
- Execute immediately after edits in PowerShell:
  git add .; git commit -m "<type>: <summary>"; git push
- Types: learn, fix, feat. Uncommitted changes prohibited.
