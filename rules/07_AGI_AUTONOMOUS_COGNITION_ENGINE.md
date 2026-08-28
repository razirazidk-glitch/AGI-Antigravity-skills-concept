---
description: Session state machine and autonomous action triggers.
trigger: always_on
---
# AUTONOMOUS COGNITION ENGINE

## 1. SESSION STATE MACHINE (S0-S7)
- S0 GENESIS: New mission -> generate SessionId, init `.sessions/active/CHECKLIST.md`.
- S1 ROUTING: Emit Proactive Directive at TOP, map skills, dynamic /grill-me.
- S2 PRE-FLIGHT: 3+ files -> 5 planning docs in `.planning/` before code.
- S3 RED TDD: Write minimal failing test first.
- S4 GREEN/REFACTOR: Minimal code to pass (exit code 0), clean AST refactor.
- S5 TELEMETRY: Terminal proof, CDP trace, optical verification.
- S6 TRIBUNAL: Red Team / Adversarial review (Q >= 9.0).
- S7 CLOSURE: Move checklist to archive, write RETROSPECTIVE.md, update PROJECT_BRAIN.md.

## 2. AUTONOMOUS ACTION TRIGGERS
- New request -> Emit Proactive Directive at TOP.
- Ambiguous/short prompt -> Offer /grill-me + `agi-prompt-refiner`.
- Coding task -> Pause and prompt user to switch to High Reasoning mode.
- 3+ files implementation -> Generate planning docs before editing code.
- Code modified -> Run test suite immediately (exit code 0).
- Deliverable complete -> Archive session and write Retrospective.

