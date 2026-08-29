---
name: meta-skill-synthesis
description: >-
  Self-learning protocol for synthesizing new skills/rules on disk (/learn). Trigger on: learn, /learn, save rule, create skill, learn from mistake, persist learning, remember this, extract insights, save lesson, persist rule, meta skill, synthesize skill.
---
# 🧠 META-SKILL SYNTHESIS (Dual-Scope Machine Self-Learning)

**CENTRAL DOGMA:** An AGI/ASI engineering intelligence never repeats the same architectural struggle twice. Upon conquering a new complexity frontier or resolving non-trivial causal pathologies, the system synthesizes and categorizes the discovered heuristic across two strictly isolated layers to prevent **Overfitting / Benchmaxing**.

---

## 1. 🧭 Synthesis Scope Bifurcation (The 2 Learning Layers)

Before persisting any lesson or crystallized rule, rigorously classify the target scope layer:

### Layer 1: Niche / Local Scope (Workspace & Project Specific)
- **Criteria:** Domain-specific vertical knowledge, industry standards, specialized taxonomies (e.g. Healthcare/HIPAA/FHIR/CID-10 vs Automotive/OBD-II/CAN-bus), client business rules, database schemas, local CI/build scripts, and framework-specific conventions (e.g., Next.js 15 App Router, Django ORM).
- **The Domain Specialization Invariant:** Rules/skills relevant only to one specific industry (e.g., medical diagnostics, auto shop management, dental software, legal contracts) **MUST NEVER** be placed in the global plugin. A medical skill must never pollute an auto repair workspace.
- **Canonical Paths:**
  - Local Rules: `<workspace_root>/.agents/rules/<rule-name>.md`
  - Local Skills: `<workspace_root>/.agents/skills/<skill-name>/SKILL.md`
- **Isolation:** Strictly confined within the active workspace and versioned in the project repository. **NEVER** pollute the global core plugin.

### Layer 2: Universal AGI/ASI Scope (Global Plugin `agi-antigravity-core`)
- **Criteria:** First-principle invariant laws, System 2 reasoning methodologies, epistemic grounding, anti-hallucination cognitive defenses, universal TDD protocols, 4-phase causal debugging, AST refactoring, or heuristics applicable to ANY daily engineering domain.
- **Canonical Paths:**
  - Master Rules: `~/.gemini/config/plugins/agi-antigravity-core/rules/<rule-name>.md`
  - Master Skills: `~/.gemini/config/plugins/agi-antigravity-core/skills/<skill-name>/SKILL.md`
- **Registration:** Synchronize updates in `rules/AGENTS.md` and `rules/01_SKILLS_TAXONOMY_ROUTING.md`.

---

## 2. 🛡️ Anti-Overfitting & Domain Invariance Distillation Filter

The greatest failure mode of machine self-learning is **overfitting and domain leakage**, where a hyper-specific heuristic or vertical niche ontology learned in one project is injected globally and rigidly applied out of context.

### The Universal Invariance Test (The Medical vs. Workshop Proof):
When proposing a synthesis for **Layer 2 (Global Scope)**, the agent must subject the candidate heuristic to 5 elimination filters:
1. **The Medical vs. Workshop Test (Cross-Domain Invariance):** If this rule was created during a medical project, would it be completely absurd or obstructive in an automotive repair workshop project? If YES $\to$ **Layer 1 (Local Workspace)**. Only rules that are universally true in BOTH (e.g., deterministic verification, root-cause isolation, AST integrity) qualify for Layer 2.
2. **Stack Independence Filter:** Does this principle hold true across C++, Python, Rust, TypeScript, Verilog, and Distributed Systems? (If dependent on a specific framework/library $\to$ Layer 1 Local).
3. **Non-Prescriptive Heuristic Filter:** Does the learning impose a rigid operational pattern (e.g. fixed folder trees, rigid multi-tier subagent spawning per file), or does it prescribe an adaptive System 2 reasoning heuristic? (If prescribing rigid static topologies $\to$ reject or refactor into an adaptive principle).
4. **Epistemic Invariance vs Structural Topology Filter:** Universal laws capture fundamental epistemics (e.g. "Mechanic's Disassembly Law: Mandate 100% node inventory $\forall v \in \mathcal{V}$ prior to causal diagnosis or refactoring"), NEVER prescriptive subagent topologies or local file paths.
5. **Cross-Domain Resilience Filter:** Would applying this rule in a completely divergent technical domain (e.g., quantum simulation vs frontend animation) cause destructive interference or quota exhaustion? (If yes $\to$ Layer 1 Local).


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

---

## 5. 🚨 CAPABILITY GAP AUTO-GENESIS PROTOCOL

When the system encounters a novel problem class where zero existing skills provide an adequate playbook:
1. **Detect Gap:** Identify that current toolings/playbooks lack deterministic guidance.
2. **Draft Capability Specification:** Draft a `SKILL.md` defining triggers, invariants, and step-by-step execution protocol.
3. **Propose Skill Genesis:** Present `learning_proposal.md` to user classifying whether it is Layer 1 (workspace) or Layer 2 (global core).
4. **Persist & Register:** Write the new skill and register it in `01_SKILLS_TAXONOMY_ROUTING.md`.

---

## 6. 🎯 DUAL-BAND NATURAL SEMANTIC TRIGGER LAW (Anti-Hermetic Standard)

When authoring or modifying the `description` and `Trigger on:` of any skill:
1. **Ban on Synthetic Compound Jargon:** Strictly prohibit artificial, academic compound phrases that developers never say in daily conversation (e.g., `legacy refactor`, `codebase archaeology`, `quarantine spec`, `topological boundary`, `refine prompt`).
2. **Mandatory Dual-Band Semantic Structure:**
   - **Band 1 (Plain Everyday Language & Atomic Verbs):** Include common, raw, direct actions and objects (`refactor`, `clean up`, `audit`, `debug`, `find bug`, `integrate`, `connect API`, `improve prompt`, `sound`, `3D model`, `slow page`, `write test`).
   - **Band 2 (Technical Concepts & Formal Tokens):** Include standard formal domain keywords (`AST`, `CDP`, `WebGL`, `Three.js`, `TDD`, `WCAG`, `Git worktree`).
3. **Universality Filter:** The skill MUST activate smoothly for both ultra-short informal user prompts and long-form enterprise specifications.


