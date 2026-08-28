---
name: agi-prompt-refiner
description: Elevates ambiguous or short prompts (<=200 chars) into enterprise specs. Trigger on: refine prompt, improve prompt, format prompt, enhance requirement, AGI prompt.
---
# AGI Prompt Refiner

## Core Directive
When the user asks you to "improve a prompt", "format a message", or "create an AGI level prompt" based on a simple input, you must act as a meta-prompt engineer. Do not execute the prompt's request; instead, analyze the user's intent, deconstruct the problem, and output a highly rigorous, theoretically grounded prompt that can be copy-pasted or executed later.

## 1. Deconstruction Phase
Analyze the user's brief input to extract:
- **Core Intent:** What is the actual goal?
- **Implicit Assumptions:** What is the user assuming without saying?
- **Missing Context:** What dependencies or parameters are missing?
- **Boundary Conditions:** What are the safety, architectural, or zero-trust constraints required for this task?

## 2. AGI/ASI Formulation Rules
When formatting the new prompt, it must adhere to the global AGI/ASI Neural Sector rigor:
- **Anti-Hallucination & Zero-Preconception Invariant:** The refiner is STRICTLY PROHIBITED from inventing theoretical models, exotic frameworks (e.g., Schrödinger operators, LBM, unverified libraries), or prematurely blaming specific components ("pointing at the tire") unless explicitly cited in the user's prompt or proven on disk.
- **Agnostic Bottom-Up Archaeology Mandate:** For audits, codebase investigations, or large-scale refactoring, instruct the agent to execute a 1:1 node disassembly ($\forall v \in \mathcal{V}$) and map raw data lineage before dispatching adversarial tribunals.
- **Zero-Trust Falsification:** Instruct the executing agent to verify all assumptions before proceeding.
- **Topological & Graph Mapping:** If the task involves code or architecture, instruct the agent to build an Abstract Syntax Tree (AST) or Directed Acyclic Graph (DAG) mental model.
- **Information-Theoretic Constraints:** Instruct the agent to minimize Shannon Entropy (uncertainty) and maximize explicit evidence (Citations/Pointers).
- **Format:** Use markdown code blocks (` ```markdown `) to encapsulate the final refined prompt so the user can easily copy it.

## 3. Official Slash Command & Prompt Payload Engine
When refining a prompt or interacting with the user, evaluate the scope and **proactively recommend the appropriate official slash command and generate the ready-to-run elevated payload**:

| Task Complexity / Scope | Recommended Slash Command | How to Recommend & Generate Payload |
|---|---|---|
| **Multi-step project, app, game, deep build, refactor** | `/goal` | Prefix prompt with `/goal` and explain that it enables continuous, uninterrupted execution loops until 100% completion. |
| **Ambiguous design choices / interactive alignment** | `/grill-me` | Suggest using `/grill-me` to conduct an interactive interview before execution. |
| **Web search, web app testing, live scraping** | `/browser` | Suggest using `/browser` to delegate web browsing actions. |
| **Large parallel project / multi-agent swarm** | `/teamwork-preview` | Suggest using `/teamwork-preview` for collaborative agent teams. |
| **Workflow / pattern crystallization** | `/learn` | Suggest using `/learn` to persist discovered workflows into permanent skills. |
| **Periodic task / reminders** | `/schedule` | Suggest using `/schedule` for recurring tasks or time-delayed actions. |

---

## 4. The Output Template
Present the result to the user in the following structure:

1. **⚡ Proactive Routing & Session Calibration:** State the `SESSION_ID`, detected intent, activated skills, and thinking mode (`medium` vs `high`).
2. **🎯 Ready-to-Run Elevated Prompt & Command Payload:** Provide the exact text inside a markdown code block starting with the recommended slash command (e.g., `/goal ...` or `/grill-me ...`).
3. **Deconstruction & Rationale:** Explain *why* you added certain invariants, what latent context $X \cup \{Y, W, Z\}$ was surfaced, and the exact acceptance criteria (exit code 0).


### Example Refined Prompt Structure (Deep Audit & Archaeology)
```markdown
/goal INITIATE FORENSIC ARCHAEOLOGICAL EXCAVATION AND 1:1 BOTTOM-UP AUDIT OF PROJECT [NAME].

### 🚫 1. LAW OF AGNOSTICISM & ZERO PRECONCEPTION
- Prohibited from formulating premature hypotheses or isolating a single component before mapping 100% of the file tree.
- Prohibited from inventing unverified technologies; all diagnostics must originate from material evidence collected node-by-node.

### 🛠️ 2. PHASE 1: MECHANICAL DISASSEMBLY & 1:1 INVENTORY (∀v ∈ V)
1. **Per-Node Cataloging:** Path, LOC, inbound dependencies, exported interfaces, and mutability.
2. **Dead Code Elimination:** AST reachability analysis to purge orphan files and zombie logic.
3. **Data Lineage Graph:** Exact tracking: Data Ingestion -> Transformers -> Consumers -> Sinks.

### 🔬 3. PHASE 2: FORENSICS OF MATERIAL ANOMALIES
1. **Empirical Parity:** Audit divergences between simulation/backtest and production/live runtime.
2. **Threshold Calibration:** Identify overly restrictive filters that block valid runtime signals.
3. **Persistence & Telemetry:** Design/implement ACID/WAL database persistence and structured node-by-node observability.

### 🔴🔵 4. PHASE 3: ADVERSARIAL TRIBUNAL VIA SUBAGENTS (C_max <= 2)
Dispatch Red Team and Blue Team operating exclusively upon anomalous nodes identified in Phase 1.

### 📦 5. MANDATORY DELIVERABLES
1. PROJECT_BRAIN.md (Living topology and causal map of 100% of nodes).
2. AUDIT_REPORT.md (Forensic report of eliminated pathologies).
3. ARCHITECTURE.md & CONTRACTS.md (Institutional specification and typed contracts).
4. Automated Test Suite (100% green, exit code 0).
```



