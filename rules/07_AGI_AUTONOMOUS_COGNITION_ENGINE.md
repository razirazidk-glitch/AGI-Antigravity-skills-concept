---
description: Session state machine and autonomous action triggers.
trigger: always_on
---
# AUTONOMOUS COGNITION ENGINE

## 1. SESSION STATE MACHINE
- S0 GENESIS: New mission -> generate SessionId, init `.sessions/active/CHECKLIST.md`.
- S1 ROUTING: Emit Proactive Directive at top, map skills.
- S2 PRE-FLIGHT: 3+ files -> create 5 planning docs in `.planning/` before code.
- S3 RED TDD: Write minimal failing test first.
- S4 GREEN/REFACTOR: Minimal code to pass (exit code 0), clean AST refactor.
- S5 TELEMETRY: Terminal proof, trace, optical verification.
- S6 TRIBUNAL: Adversarial review (Q >= 9.0).
- S7 CLOSURE: Archive checklist, write RETROSPECTIVE.md, update PROJECT_BRAIN.md.

## 2. AUTONOMOUS ACTION TRIGGERS
- New request -> Emit Proactive Directive at top.
- Coding task -> Pause and prompt user to switch to High Reasoning mode.
- Code modified -> Run test suite immediately (exit code 0).
- Deliverable complete -> Archive session and retrospective.
