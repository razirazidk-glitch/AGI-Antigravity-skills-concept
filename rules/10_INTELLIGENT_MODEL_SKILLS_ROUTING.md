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

## 2. ACTIVATED SKILLS CONTRACT
- Activated Skills field MUST only list skills for which view_file(SKILL.md) is executed in the SAME turn.
- For turns where no skill is read, output: `Activated Skills: —` (em dash, no links).

## 3. CODING PAUSE GATE (P_high)
- Pause and prompt user to switch to High Reasoning mode before editing code, AST refactoring, or authoring tests.
