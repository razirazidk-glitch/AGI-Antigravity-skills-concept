---
name: meta-skill-synthesis
description: >-
  AGI Machine Self-Learning protocol for synthesizing durable, new skill files directly on disk from session insights (/learn workflow) and dual-loop self-improvement without model collapse. Trigger on mentions of: 'meta skill', 'synthesize skill', 'create skill', 'self-learning agent', 'new skill generation', 'persist capability', 'skill synthesis', '/learn', 'extract insights', 'save lesson', 'learn from session', 'persist rule', 'dual loop optimizer', 'self-improvement', 'prevent model collapse', or when teaching the agent new permanent workflows.
---
# 🧠 META-SKILL SYNTHESIS (Dual-Scope Machine Self-Learning)

**CENTRAL DOGMA:** An AGI/ASI engineering intelligence never repeats the same architectural struggle twice. Upon conquering a new complexity frontier or resolving non-trivial causal pathologies, the system synthesizes and categorizes the discovered heuristic across two strictly isolated layers to prevent **Overfitting / Benchmaxing**.

---

## 1. 🧭 Synthesis Scope Bifurcation (The 2 Learning Layers)

Before persisting any lesson or crystallized rule, rigorously classify the target scope layer:

### Layer 1: Niche / Local Scope (Workspace & Project Specific)
- **Criteria:** Local stack conventions (e.g., Next.js, Django, Rust, Tailwind), customer-specific database schemas, repository-specific build/CI workflows, local migration scripts, or bespoke domain business rules.
- **Canonical Paths:**
  - Local Rules: `<workspace_root>/.agents/rules/<rule-name>.md`
  - Local Skills: `<workspace_root>/.agents/skills/<skill-name>/SKILL.md`
- **Isolation:** Strictly confined within the active workspace. **NEVER** pollute the global core plugin.

### Layer 2: Universal AGI/ASI Scope (Global Plugin `agi-antigravity-core`)
- **Criteria:** First-principle invariant laws, System 2 reasoning methodologies, epistemic grounding, anti-hallucination cognitive defenses, universal TDD protocols, or heuristics applicable to ANY daily engineering domain.
- **Canonical Paths:**
  - Master Rules: `~/.gemini/config/plugins/agi-antigravity-core/rules/<rule-name>.md`
  - Master Skills: `~/.gemini/config/plugins/agi-antigravity-core/skills/<skill-name>/SKILL.md`
- **Registration:** Synchronize updates in `rules/AGENTS.md` and `rules/01_SKILLS_TAXONOMY_ROUTING.md`.

---

## 2. 🛡️ Anti-Overfitting & Anti-Benchmaxing Distillation Filter

The greatest failure mode of machine self-learning is **overfitting**, where a hyper-specific heuristic learned in one domain (e.g., "always structure websites using component X") is injected globally and rigidly applied out of context.

### The Universal Invariance Test:
When proposing a synthesis for **Layer 2 (Global Scope)**, the agent must subject the candidate heuristic to 3 elimination filters:
1. **Stack Independence Filter:** Does this principle hold true across C++, Python, Rust, TypeScript, Verilog, and Distributed Systems? (If dependent on a specific framework $\to$ Layer 1 Local).
2. **Non-Prescriptive Heuristic Filter:** Does the learning impose a rigid pattern, or does it prescribe an adaptive System 2 reasoning heuristic? (If prescribing rigid fixed templates $\to$ reject or refactor into an adaptive heuristic).
3. **Cross-Domain Resilience Filter:** Would applying this rule in a completely divergent technical domain (e.g., quantum simulation vs frontend animation) cause destructive interference? (If yes $\to$ Layer 1 Local).

---

## 3. ⚡ Post-Milestone Proactive Recommendation Trigger

Upon completing:
1. A major architectural milestone (e.g., massive 10+ node refactoring);
2. The resolution of a complex causal root-cause defect;
3. The correction of a cognitive bias identified by the user;

The agent **MUST** formally recommend `/learn` to the user with a pre-drafted 2-layer classification:
> *"We have conquered this critical challenge. I recommend running `/learn` to persist this insight cleanly to Layer 1 (Local Workspace) or Layer 2 (Global AGI Core) without risk of overfitting."*

---

## 4. 🛠️ Operational Protocol for `/learn` Execution

1. **Proposal Draft:** Generate artifact `learning_proposal.md` with explicit Layer 1 vs Layer 2 classification and diff specifications.
2. **Mandatory Rule Frontmatter Structure:**
   ```markdown
   ---
   description: Concise summary of the rule and operational scope.
   trigger: always_on # Options: always_on | model_decision | glob
   globs: "*.ts,*.py" # Mandatory if trigger is glob
   ---
   ```
3. **Validation & Confirmation:** Obtain explicit user confirmation before writing changes to disk.
4. **Regression Verification:** Run validation test suites via `pytest` to certify Exit Code `0`.
