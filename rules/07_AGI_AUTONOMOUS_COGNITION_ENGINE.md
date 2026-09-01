---
description: Session state machine and autonomous action triggers.
trigger: always_on
---
# AUTONOMOUS COGNITION ENGINE

## 1. EXECUTIVE SESSION STATE MACHINE
- S0 GENESIS & BOARD CONVOCATION: New mission -> generate SessionId, initialize `.sessions/active/CHECKLIST.md` and Board Strategy Mandate.
- S1 OODA ORIENTATION & MEMORY REHYDRATION: Observe operational theater, Orient via AST/codebase scan, emit Proactive Directive at top, map master skills. **Auto-Rehydrate:** Read `PROJECT_BRAIN.md`, target `<module_dir>/NODE.md`, and latest `.sessions/archive/*/RETROSPECTIVE.md`. Verify module lock state (pause if `🔴 CHANGING`). If requirements are open-ended or require deep alignment/extra insights -> recommend `[/grill-me]`.
- S2 PRE-FLIGHT & WRAP DELIBERATION: >=3 files -> generate 5 planning docs in `.planning/` + Cartesian Matrix + WRAP options analysis before code (utilize `grill-me-layered` to solidify contracts).
- S3 RED TDD & FORMAL PROOF: Minimal failing test first. Enforce domain invariants and mathematical/contract guarantees.
- S4 GREEN/REFACTOR: Minimal production code to pass test (exit code 0), followed by clean AST refactor and zero dead paths.
- S5 EMPIRICAL TELEMETRY: Terminal execution proof, performance benchmarks, boundary stress tests, memory envelope verification.
- S6 ADVERSARIAL BOARD TRIBUNAL: Red Team audit against top-tier industry benchmarks (Q >= 9.0).
- S7 STRATEGIC CLOSURE & MEMORY PERSISTENCE: Archive checklist to `.sessions/archive/[SESSION_ID]/`, author comprehensive `RETROSPECTIVE.md`, update `PROJECT_BRAIN.md` module registry (transition target to `✅ DONE`) + `DEC::GROUNDED` decision log, and trigger `/learn` for continuous evolution.

## 2. AUTONOMOUS ACTION & EXECUTIVE ACCOUNTABILITY TRIGGERS
- New request / Architecture inception -> Emit Proactive Directive at top; rehydrate memory; prioritize `[/grill-me]` for high-frequency alignment, probing edge cases and extracting strategic insights.
- Coding task -> Pause and prompt user to switch to High Reasoning mode before AST modifications.
- Strategic / Architecture pivot -> Run WRAP framework filter to eliminate bias and widen options; log to `DEC::GROUNDED`.
- Code / Model modified -> Run deterministic test suite immediately (exit code 0, 100% test pass).
- Deliverable complete -> Archive session, update neural map, and trigger continuous evolution.
