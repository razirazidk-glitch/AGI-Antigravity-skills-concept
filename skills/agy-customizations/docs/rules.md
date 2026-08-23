# Workspace Rules

Rules are guidelines and constraints that the agent must follow when operating
within specific directories. They are useful for enforcing coding styles, API
usage restrictions, or safety protocols.

## Rule Locations

The system automatically discovers and applies rules from the following
locations:

*   **Directory-Based Rules (`GEMINI.md` / `AGENTS.md`)**: Placed directly in
    any directory. The system walks up from the current working directory to the
    repository root and loads these files. They apply to the directory they
    reside in and all its subdirectories.

## Rule Format & Frontmatter Specification

Rules are written in Markdown and should include YAML Frontmatter to declare their
activation trigger and semantic scope:

```markdown
---
description: Brief summary of the rule's mandate and scope.
trigger: always_on # Options: always_on | model_decision | glob
globs: "*.ts,*.py" # Required only when trigger is 'glob'
---
# Rule Title
Guidelines, invariants, and constraints.
```

### Trigger Types:
* **`always_on`**: Unconditionally injected into the system prompt for all turns.
* **`model_decision`**: Contextually activated when user intent matches `description`.
* **`glob`**: Activated when the agent interacts with files matching `globs` patterns.

## Rule Merging and Deduplication

*   Rules are automatically deduplicated. Even if a rule is discovered via
    multiple paths (e.g., inherited from parent directories), it is only applied
    once per conversation.
*   If a rule is defined in a plugin, it is loaded when the plugin is enabled.
