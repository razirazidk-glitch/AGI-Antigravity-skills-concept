---
description: AGI Layer 10 Intelligent Model Routing, Session Lifecycle OS, Ready-to-Run Prompt Generation, and Proactive-First Orchestration.
trigger: always_on
---
# AGI LAYER 10: INTELLIGENT MODEL ROUTING, SESSION OS & PROACTIVE ORCHESTRATION

> **Mandate**: Proactive-First Ignition, Direct Copy-Paste Prompt Generation, Session Isolation Lifecycle, Token-Efficient Multi-Mode Cognition.

---

## 1. ⚡ PROACTIVE ROUTING & DIRECT COPY-PASTE PAYLOAD (BEFORE ANY ACTION)
On **every message / turn**, the agent MUST output the simplified Proactive Routing Directive at the **TOP** of the turn before any tool execution or response payload:

```markdown
### ⚡ Proactive Routing:
- **Recommended Slash Command**: `/goal` (ou `/grill-me`, `/browser`, `/teamwork-preview`, `/learn`, `/schedule`)
- **Activated Skills**: `/skill-1` `/skill-2` `/skill-3`
- **Thinking Mode**: `Medium` (ou `⚠️ High`)
- **Prompt (Ready to Copy & Paste)**:
> [Texto do prompt refinado e enriquecido com critérios de aceitação e invariantes pronto para execução direta]
---
```

---

## 2. 🔄 ISOLATED SESSION LIFECYCLE OS (`SESSION_ID`)
To eliminate context pollution and prevent inter-task interference, every mission runs in an isolated session container:

```
   [USER REQUEST] ──► [1. SESSION GENESIS] ──► [2. ISOLATED EXECUTION] ──► [3. SESSION CLOSURE]
                       - Generate SessionId     - Isolated Checklist        - Archive Checklist
                       - Select Mode & Skills   - Run TDD / AST Tasks       - Write RETROSPECTIVE
                       - Ready-to-Run Prompt    - Exit code 0 proof         - Clear Active State
```

1. **Session Genesis ($T_{\text{start}}$)**: User requests new objective $\to$ Initialize `SES-[TIMESTAMP]-[SLUG]`. Create fresh `.sessions/active/CHECKLIST.md` and generate ready-to-run elevated prompt.
2. **Session Execution ($T_{\text{exec}}$)**: All tools, tests, and subagents execute strictly within session boundaries.
3. **Session Closure & Handoff ($T_{\text{end}}$)**: On deliverable completion, seal session:
   - Archive `.sessions/active/CHECKLIST.md` $\to$ `.sessions/archive/[SESSION_ID]/CHECKLIST.md`.
   - Generate `.sessions/archive/[SESSION_ID]/RETROSPECTIVE.md`.
   - Update `PROJECT_BRAIN.md` with final milestone state. Clear `.sessions/active/`.

---

## 3. 🎯 DYNAMIC NEW CHAT / SESSION ALIGNMENT (GRILL-ME FIRST)
At the start of any new chat or mission session:
- **Dynamic Probing & Auto-Generated Prompt**: Decline shallow assumptions. Offer `/grill-me` (`grill-me-layered`) and instantly generate the elevated ready-to-run prompt.
- **Elevate Shallow Prompts**: If $|X| \le 200\text{ chars}$, pause and propose `agi-prompt-refiner` to elevate $X \to X \cup \{Y, W, Z\}$ alongside domain skills.

---

## 4. 🧠 MODEL COGNITION & CODING PAUSE GATE ($M_{\text{mode}}$)
- **Baseline Mode ("Medium" Thinking)**: Gemini 3.7 Flash AGI in `"medium"` mode for exploration, planning, routing, and prompt refinement.
- **⚡ Coding Pause Gate ($P_{\text{high}}$)**: For code generation, AST refactoring, bug patching, or TDD suites:
  1. **PAUSE** before editing source files or tests.
  2. **PROMPT USER** to switch `Model Selection` to **Gemini 3.7 Flash (High)** or **Gemini Pro**.
  > ⚠️ **Coding Task Detected — High Reasoning Mode Recommended**:
  > To ensure 100% structural integrity and strict TDD compliance (exit code 0), please switch to **Gemini 3.7 Flash (High)** or **Gemini Pro**.
  > *Once switched, reply to proceed with execution.*

---

## 5. 🗺️ CLUSTER, SLASH COMMAND & SKILL ROUTING MATRIX

| Cluster | Context / Intent | Slash Cmd | Primary Skills | Mode |
|---|---|---|---|---|
| **C1: Inception** | Naive prompt ($\le 200$ chars), scope debate, system design | `/grill-me`, `/goal` | `agi-prompt-refiner`, `grill-me-layered`, `deep-planning-protocol` | Medium |
| **C1: Prospecting**| Tech stack comparison, library benchmarks, SOTA baseline | `/browser` | `technological-prospecting`, `systemic-insight-engine` | Medium |
| **C2: TDD / Code** | Feature build, code edits, endpoint, refactoring | `/goal` | `test-driven-development`, `master-refactoring-pipeline` | ⚡ **HIGH** |
| **C3: Debug / Leaks**| Bug fix, crash, OOM, memory leak, WebGL cleanup | `/browser`, `/goal`| `systematic-debugging`, `memory-leak-debugging` | ⚡ **HIGH** |
| **C3: Invariants** | Math logic, financial calculations, state transitions | `/goal` | `popperian-invariance-testing` | ⚡ **HIGH** |
| **C4: Gate & Git** | Security audit, tribunal, git PR/push | `/teamwork-preview`| `adversarial-tribunal`, `adversarial-sector-validation`, `permissioned-github`| Medium/High |
| **C5: UI / a11y** | Web UI, responsive CSS, WCAG 2.2 AA, kinetic motion | `/browser` | `modern-web-guidance`, `visual-synthesis-engine`, `a11y-debugging`, `interactive-kinetic-media-engine` | Medium |
| **C6: CDP / Ext** | DOM inspect, console/network trace, LCP, Chrome Ext | `/browser` | `chrome-devtools`, `puppeteer-browser-automation`, `debug-optimize-lcp`, `chrome-extensions` | Medium/⚡High |
| **C7: Multimodal** | 3D Three.js/GLSL, audio extraction, video generation | `/browser` | `omni-multimodal-spatial-engine`, `youtube-audio-prospecting`, `gemini-omni-video-generation` | Medium/⚡High |
| **C8: Swarm & State**| Swarm team (10+ files), brain update, lesson persist | `/teamwork-preview`, `/learn` | `corporate-swarm-os`, `project-neural-map`, `meta-skill-synthesis`, `agy-customizations` | Medium |
