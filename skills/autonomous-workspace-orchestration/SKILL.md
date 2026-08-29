---
name: autonomous-workspace-orchestration
description: >-
  Git worktree and isolated workspace lifecycle manager for safe sandboxing and experimental refactoring. Trigger on: git worktree, isolated workspace, branch workspace, clean refactor branch, destructive testing, isolated sandbox, experimental refactor, safe parallel testing.
---

# 🌳 AUTONOMOUS WORKSPACE ORCHESTRATION

> **Central Law**: The primary repository state and main working directory must remain pristine and unpolluted during invasive architectural refactoring, destructive experiments, or deep migrations. Use native Git Worktrees and isolated subagent workspace modes.

---

## 1. 🏗️ WORKTREE LIFECYCLE STATE MACHINE

```
┌─────────────────┐       git worktree add       ┌─────────────────────┐
│ Main Repository │ ───────────────────────────> │ Isolated Worktree   │
│ (Pristine Main) │                              │ (Sandbox Workspace) │
└─────────────────┘                              └─────────────────────┘
         ▲                                                  │
         │          Integration Consensus Gate              │
         └──────────────────────────────────────────────────┘
                      (Fast-Forward / Rebase)
```

---

## 2. ⚡ WORKSPACE MODES IN SUBAGENT DELEGATION

When invoking subagents via `invoke_subagent`, explicitly choose the appropriate `Workspace` parameter:

| Mode | Isolation Level | File System Behavior | Best Used For |
|---|---|---|---|
| `Workspace: "inherit"` | Zero Isolation | Uses the exact same directory as parent agent. | Quick file inspection, small atomic edits, shared tasks. |
| `Workspace: "share"` | Shared Object DB | Shares the underlying Git repository directory (like `git worktree`), allowing independent branching without duplicating storage. | Medium refactoring, parallel exploration of alternative architectures. |
| `Workspace: "branch"` | Complete Isolation | Creates a newly isolated workspace branched/cloned from the parent. | Destructive migrations, high-risk package updates, invasive stress tests. |

---

## 3. 🛠️ CLI WORKTREE OPERATIONS RUNBOOK

### Creating an Isolated Refactoring Worktree:
```bash
# Create isolated worktree with a dedicated refactoring branch
git worktree add ../refactor-isolated-sandbox -b task/isolated-refactor

# Verify worktree status
git worktree list
```

### Executing Work in the Sandbox:
- Direct all file edits, test executions, and dependency installations exclusively within `../refactor-isolated-sandbox`.
- Run validation test suites locally within the isolated workspace.

### Merging and Consensus Integration:
Once the work passes the Tri-Gate Firewall ($Q \ge 9.0$ and exit code 0):
```bash
# In main repo:
git merge --ff-only task/isolated-refactor

# Cleanup worktree and branch
git worktree remove ../refactor-isolated-sandbox
git branch -d task/isolated-refactor
```

### Abort & Safe Purge:
If an experiment fails or is discarded:
```bash
git worktree remove --force ../refactor-isolated-sandbox
git branch -D task/isolated-refactor
```
