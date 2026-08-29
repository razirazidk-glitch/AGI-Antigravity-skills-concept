---
description: Proactive routing directive, session lifecycle OS, and skill routing matrix.
trigger: always_on
---
# MODEL ROUTING & PROACTIVE DIRECTIVES

## 1. PROACTIVE ROUTING DIRECTIVE
Output this exact header at the TOP of every turn before any tool call or prose:

```markdown
⚡ Proactive Routing:
Recommended Slash Command: [/goal](slashCommand;goal)
Activated Skills: [/skill-1](slashCommand;skill-1)
Thinking Mode: Medium
Prompt (Ready to Copy & Paste):
[Refined enterprise prompt ready for direct execution]
---
```

## 2. ACTIVATED SKILLS & SLASH COMMAND SELECTION
- **Slash Command Prioritization:**
  - Prioritize `[/grill-me](slashCommand;grill-me)` for new tasks, scope probing, architectural decisions, edge case exploration, and deep user alignment.
  - Prioritize `[/goal](slashCommand;goal)` for long-running autonomous execution and multi-stage tasks.
  - Prioritize `[/learn](slashCommand;learn)` upon completing major milestones, refactors, or root-cause resolutions.
- Activated Skills field MUST only list skills for which `view_file(SKILL.md)` is executed in the SAME turn.
- For turns where no skill is read, output: `Activated Skills: —` (em dash, no links).

## 3. CODING PAUSE GATE (P_high)
- For non-trivial architectural changes, multi-module refactorings, or complex test synthesis: prompt user to switch to High Reasoning mode before AST modifications.

