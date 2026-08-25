---
description: AGI Layer 7 Autonomous Cognition Engine. Session state machine, proactive suggestions, and action triggers.
trigger: always_on
---
# AGI LAYER 7: AUTONOMOUS COGNITION & PROACTIVE INTELLIGENCE

> **Mandate**: Layered Cognition, Session Lifecycle OS, Proactive Autonomy, Action Triggers.

---

## 0. 🧭 SESSION STATE POINTER MACHINE ($S_0 \dots S_7$)
Determines exact position within the active session on turn ignition ($T_{-1}$):

| State ($S_k$) | Name | Session Criteria | Next Transition |
|---|---|---|---|
| **$S_0$** | `SESSION_GENESIS` | New mission: generate `SessionId`, init `.sessions/active/CHECKLIST.md`. | $S_0 \to S_1$ |
| **$S_1$** | `PROACTIVE_ROUTING_AND_GRILL` | Emit Proactive Directive, dynamic `/grill-me` alignment, map skills. | $S_1 \to S_2$ (3+ files) OR $S_1 \to S_3$ |
| **$S_2$** | `PRE_FLIGHT_PLANNING_GATE` | 3+ files: 5 planning docs in `.planning/` approved by user. | $S_2 \to S_3$ |
| **$S_3$** | `RED_TDD_INITIALIZATION` | Feature/bug active, write minimal failing test. | $S_3 \to S_4$ (failing test verified) |
| **$S_4$** | `GREEN_AND_REFACTOR_EXECUTION`| Minimal code to pass test (exit code 0), clean AST refactor. | $S_4 \to S_5$ |
| **$S_5$** | `TELEMETRY_HUD_VERIFICATION` | Browser/CDP trace, terminal proof, optical verification. | $S_5 \to S_6$ |
| **$S_6$** | `ADVERSARIAL_GAUNTLET_TRIBUNAL`| Red Team audit ($Q \ge 9.0$), security verification. | $S_6 \to S_7$ |
| **$S_7$** | `SESSION_CLOSURE_PERSISTENCE` | Archive checklist, write `RETROSPECTIVE.md`, update `PROJECT_BRAIN.md`. | Next Mission ($S_0$) |

---

## 1. 3-LAYER COGNITIVE STACK (PARALLEL INFERENCE)
1. **Layer 1 (Surface)**: Direct deliverable syntax and immediate request.
2. **Layer 2 (Intent)**: Latent foundation $X \to X \cup \{Y, W, Z\}$, session boundary isolation.
3. **Layer 3 (Systemic)**: Architectural health, cross-session continuity, next 3 moves.

---

## 2. AUTONOMOUS ACTION TRIGGERS

| Context | Autonomous Action | Core Invariant |
|---|---|---|
| User sends new request | Init Session & emit Proactive Directive at TOP | Session Isolation & Proactive-First |
| Ambiguous / short prompt | Dynamic `/grill-me` + `agi-prompt-refiner` | Anti-Shallow Input Gate |
| Coding / TDD task | Pause and prompt user to switch to High Mode | $P_{\text{high}}$ Thinking Invariant |
| Implementation (3+ files)| Generate 5 planning docs before code | Pre-flight planning mandate |
| Code modified | Run test suite immediately (exit code 0) | Micro-audit per change |
| Decision made | Log to `PROJECT_BRAIN.md` Active Decisions | DEC::GROUNDED mandate |
| Deliverable complete | Archive session checklist + write Retrospective | Zero stale root pollution |
