---
name: autonomous-workspace-orchestration
description: >-
  Git worktree and isolated workspace lifecycle manager for safe sandboxing and experimental refactoring. Trigger on: sandbox, experimental branch, test safely, isolated branch, worktree, safe refactor, parallel test, branch workspace, git worktree, destructive testing.
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

---

## 4. 🏆 THE GOLDEN REFERENCE ENGINE & HIGH-FIDELITY SANDBOX REPLICATION

When testing experimental algorithms, new trading strategies, physics simulations, or major architectural pivots:

### 1. Identify the Golden Reference Core (Ground Truth)
- Check `PROJECT_BRAIN.md` under `## 🏆 GOLDEN REFERENCE CORE`.
- Determine the canonical stable files:
  - **Execution Engine:** The proven production core.
  - **Backtest / Benchmark Harness:** The real validation runner and historical datasets.
  - **Data Ingestion Pipeline:** The authentic input feeds.

### 2. High-Fidelity Sandbox Isolation (Zero Mocks)
- **Invariant:** Never modify the golden reference engine in-place to test an experimental hypothesis.
- Spawn an isolated workspace (`Workspace: "branch"` or `git worktree add ../sandbox-experiment -b task/experiment`).
- **Zero-Synthetic Mandate:** The sandbox MUST inherit and replay the exact execution harness, input feeds, and backtest suite of the Golden Core. Synthetic mocks, simplified stubs, or fake proxy math are strictly prohibited.

### 3. Differential A/B Benchmarking
- Run the experiment and baseline against the **exact same real dataset**:
  $$\Delta_{\text{metric}} = \text{Score}(\text{Experimental}) - \text{Score}(\text{Golden Baseline})$$
- Record metrics in `.sessions/active/SANDBOX_BENCHMARK.md` (e.g. latency, throughput, Sharpe ratio, drawdown, precision, memory envelope).

### 4. Promotion & Consensus Gate
- Merge is permitted only if:
  1. The experimental logic preserves 100% of mathematical invariants and contract types.
  2. All baseline regression tests pass with `Exit Code 0`.
  3. $\Delta_{\text{metric}} \ge 0$ (demonstrated parity or superiority over Golden Baseline).

