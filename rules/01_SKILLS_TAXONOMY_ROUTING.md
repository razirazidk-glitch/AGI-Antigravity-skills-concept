---
description: Skills taxonomy, T0 forcing function, and trigger routing.
trigger: always_on
---
# SKILLS TAXONOMY & ROUTING

## 1. T0 FORCING FUNCTION
- Invariant: First tool call(s) in non-trivial technical turns MUST execute parallel `view_file` on `skills/<name>/SKILL.md` for ALL activated skills before output or code edits.

## 2. STRICT 2-LAYER TAXONOMY & SCOPE PARTITIONING
- **Layer 2: Universal AGI Core (`agi-antigravity-core`)**:
  - Scope: 100% Domain-Agnostic & Stack-Agnostic System 2 meta-cognition, formal verification, strict TDD, 4-phase debugging, AST refactoring, swarm governance, and cognitive defenses.
  - Invariance Gate: Must hold true across ANY engineering domain (from medical robotics to automotive mechanics, quantum physics to game engines).
  - Prohibited: Vertical industry terms, niche domain ontologies, specific client schemas, or local project workflows.
- **Layer 1: Niche Workspace Scope (`<workspace>/.agents/`)**:
  - Scope: Vertical domain rules (e.g. Healthcare/HIPAA/FHIR vs Automotive/OBD-II/CAN-bus), project-specific frameworks, database models, internal APIs, and bespoke runbooks.
  - Invariant: Strictly quarantined to the active project repository. NEVER leaked to the global core.

## 3. WORKFLOW PRESETS (UNIVERSAL CORE)
- Architectural Alignment & Scope Probing: grill-me-layered + deep-planning-protocol + systemic-insight-engine
- Frontend / Web UI: modern-web-guidance + visual-synthesis-engine + a11y-debugging + interactive-kinetic-media-engine
- Code Change / Bug Fix: test-driven-development + systematic-debugging
- Multi-Module Refactor: master-refactoring-pipeline + cross-sector-integration + project-neural-map
- Math / Physics / Tensor: test-driven-development + popperian-invariance-testing
- Subagent Delegation: corporate-swarm-os
- Reverse Engineering & Codebase Archaeology: reverse-engineering-pipeline + master-refactoring-pipeline + project-neural-map + systematic-debugging
- Milestone Release Gate: gauntlet-loop + adversarial-tribunal + permissioned-github

## 4. DOMAIN-SPECIFIC WORKSPACE ROUTING
- When operating in a specialized domain (e.g., Medicine, Automotive, FinTech, Legal, Robotics):
  - Load and prioritize local rules from `<workspace>/.agents/rules/` and local skills from `<workspace>/.agents/skills/`.
  - Never import or propose global skills containing niche vertical dependencies.
