---
description: Proactive routing directive, session lifecycle OS, and skill routing matrix.
trigger: always_on
---
# MODEL ROUTING & SESSION OS

## 1. PROACTIVE ROUTING DIRECTIVE
Output this exact header at the TOP of every turn before any tool call or prose:

```markdown
⚡ Proactive Routing:
Recommended Slash Command: [/goal](slashCommand;goal)
Activated Skills: [/skill-1](slashCommand;skill-1) [/skill-2](slashCommand;skill-2)
Thinking Mode: Medium
Prompt (Ready to Copy & Paste):
[Refined enterprise prompt ready for direct execution]
---
```

### ACTIVATED SKILLS CONTRACT (INVARIANT)
`Activated Skills:` field MUST only list skills for which `view_file(SKILL.md)` is
executed in that SAME turn. Listing a skill without reading it is PROHIBITED.
For conversational/meta turns where no skill is read, the field MUST be:
`Activated Skills: —` (em dash, no links).

## 2. SESSION LIFECYCLE OS
1. Genesis: On new objective, create `.sessions/active/CHECKLIST.md` with ID `SES-[TIMESTAMP]-[SLUG]`.
2. Execution: All tasks, tests, and subagents execute strictly within session boundaries.
3. Closure: When deliverable passes all tests (exit code 0):
   - Move `.sessions/active/CHECKLIST.md` -> `.sessions/archive/[SESSION_ID]/CHECKLIST.md`.
   - Write `.sessions/archive/[SESSION_ID]/RETROSPECTIVE.md`.
   - Update `PROJECT_BRAIN.md`. Clear `.sessions/active/`.

## 3. CODING PAUSE GATE (P_high)
For code generation, AST refactoring, bug patching, or test authoring:
- PAUSE before editing source files.
- Prompt user to switch model to High Reasoning (Gemini Flash High / Claude Thinking / Gemini Pro).

## 4. SKILL CLUSTERS & ROUTING
- C1 Inception: `agi-prompt-refiner`, `grill-me-layered`, `deep-planning-protocol` (/grill-me, /goal)
- C1 Prospecting: `technological-prospecting`, `systemic-insight-engine` (/browser)
- C2 TDD & Code: `test-driven-development`, `master-refactoring-pipeline` (/goal - HIGH)
- C3 Debug & Leaks: `systematic-debugging`, `memory-leak-debugging`, `popperian-invariance-testing` (/goal - HIGH)
- C4 Tribunal & Gates: `adversarial-tribunal`, `adversarial-sector-validation`, `permissioned-github` (/teamwork-preview)
- C5 UI & A11y: `modern-web-guidance`, `visual-synthesis-engine`, `a11y-debugging`, `interactive-kinetic-media-engine` (/browser)
- C6 CDP & DevTools: `chrome-devtools`, `puppeteer-browser-automation`, `debug-optimize-lcp`, `chrome-extensions` (/browser)
- C7 Multimodal: `omni-multimodal-spatial-engine`, `youtube-audio-prospecting`, `gemini-omni-video-generation` (/browser)
- C8 Swarm & Memory: `corporate-swarm-os`, `project-neural-map`, `meta-skill-synthesis`, `agy-customizations` (/teamwork-preview, /learn)

## 5. STARTUP SKILL VERIFICATION PROTOCOL
Se o contexto `<skills>` parecer incompleto (menos de 30 skills visíveis do `agi-antigravity-core`):
1. Informar o usuário: skills podem não ter sido indexadas na inicialização.
2. Solução: Reiniciar o Antigravity IDE.
3. Verificação pós-restart: Perguntar "quais skills você tem disponíveis?" — deve retornar 36 skills.
4. DISTINGUIR de context drift: bug de startup → presente desde a 1ª mensagem. Drift → progressivo em conversas longas.
