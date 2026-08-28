---
name: grill-me-layered
description: 12-topic deep alignment interview via /grill-me. Trigger on: /grill-me, grill me, requirement interview, architectural alignment, deep questioning, scope probing, contract debate.
---
# 🔥 GRILL-ME LAYERED — 12-Topic / 4-Layer Deep Alignment Interview

> 🔴 **MANDATE:** Every `/grill-me` alignment interview for complex projects MUST follow this 4-layer protocol. Each layer commences ONLY AFTER the preceding layer is 100% resolved. Skipping layers is STRICTLY PROHIBITED. Batching multiple questions into a single turn is PROHIBITED. Ask one question at a time, providing an explicit technical recommendation for the preferred option.

---

## ACTIVATION TRIGGERS

- The user explicitly invokes `/grill-me`
- A project spans 5+ implementation files or multiple interconnected subsystems
- The agent detects critical architectural ambiguities that prevent safe planning
- Naive or underspecified requirements where multiple contradictory implementations could be considered "correct"

---

## FACILITATION PROTOCOL

**Golden Rules:**
1. **One question at a time** — never group multiple topics in a single turn.
2. **Always provide a recommendation** — present the option the agent believes is technically optimal, supported by formal rationale.
3. **Use `ask_question` with structured options** — avoid unbounded, unstructured open questions.
4. **Log all decisions** — upon completion, generate `.planning/GRILL_RESULTS.md` documenting every decision.
5. **Challenge weak answers** — if a user answer appears superficial or contradicts earlier constraints, probe deeper before advancing.

---

## LAYER 1 — SCOPE & INTENT (Topics 1-3)

> **Objective:** Uncover what the user truly needs, not merely what was literally stated. Resolve scope ambiguities before engaging in technical analysis.

### T1: True Underlying Intent
**Root Question:** "What core business/engineering outcome are you fundamentally trying to achieve with this project?"
- Identify the underlying root problem, not just the requested surface feature.
- Distinguish between "what was requested" and "what solves the problem".
- Probe if a simpler, more robust architecture exists that was not considered.

**Resolution Checklist:**
- [ ] Business/engineering problem clearly articulated.
- [ ] Measurable definition of success established.
- [ ] Validation that proposed approach directly solves the core problem.

### T2: Success Scope & Acceptance Bar
**Root Question:** "What objective criteria define that this project was delivered with production-grade excellence?"
- Establish objective, measurable success metrics.
- Identify the primary inspection path the user will test first.
- Clarify the dominant priority dimension: raw performance? Visual elegance? Algorithmic correctness? Scalability?

**Resolution Checklist:**
- [ ] Definition of "DONE" is objective and testable (not subjective "feels good").
- [ ] Multi-dimensional quality criteria established (functional, visual, architectural).
- [ ] Concrete acceptance test suite defined that can be executed deterministically.

### T3: Anti-Scope (What NOT to Build)
**Root Question:** "What is explicitly OUT OF SCOPE and must not be implemented in this iteration?"
- Guard against feature creep and gold-plating.
- Identify external dependencies or downstream integrations deferred to future phases.
- Establish explicit boundaries between MVP and future enhancements.

**Resolution Checklist:**
- [ ] Explicit anti-scope blacklist documented.
- [ ] MVP boundaries segregated from future roadmap items.
- [ ] External dependencies cataloged (existing vs required).

---

## LAYER 2 — ARCHITECTURE & ANTI-HALLUCINATION (Topics 4-6)

> **Objective:** Eliminate hazardous assumptions and verify that the technical architecture is anchored in disk-verified facts and physical constraints.

### T4: Hard Technical Constraints
**Root Question:** "What non-negotiable technical constraints must the architecture strictly obey?"
- Technology stack (languages, frameworks, datastores — with exact versions).
- Execution environment (target OS, hardware envelopes, cloud/edge topology).
- Legacy integrations and locked interfaces that cannot be mutated.
- Licensing, regulatory compliance, and security policies.

**Resolution Checklist:**
- [ ] Tech stack defined with exact semver specifications.
- [ ] Target deployment runtime formalized.
- [ ] Legacy boundaries mapped with immutable interfaces.
- [ ] Resource boundaries defined (CPU/memory envelope, maximum latency budget).

### T5: Anti-Hallucination — Assumption Verification
**Root Question:** "What assumptions is the agent currently making that COULD be invalid?"
- The agent explicitly enumerates all latent assumptions regarding the system.
- The user reviews and verifies or corrects each assumption.
- Purge all `DEC::SPECULATIVE` tags prior to committing architecture.

**Format:**
```
The agent is assuming:
1. [Assumption A] — Confirmed / Corrected?
2. [Assumption B] — Confirmed / Corrected?
3. [Assumption C] — Confirmed / Corrected?
```

**Resolution Checklist:**
- [ ] All agent assumptions listed explicitly with zero hand-waving.
- [ ] User verified every assumption.
- [ ] Zero `DEC::SPECULATIVE` items remaining in critical paths.

### T6: Authentic Data Sources & Schemas
**Root Question:** "What real data will the system consume, and what is its authoritative source?"
- Available production APIs (with credentials and schemas).
- Authentic datasets vs synthetic prototypes.
- Expected data volumes (throughput, payload size, concurrency).
- Strict policy that synthetic mocks are banned in production code paths.

**Resolution Checklist:**
- [ ] Real data sources identified with access specifications.
- [ ] Expected operational volumes estimated with numeric boundaries.
- [ ] Data validation and schema migration strategies defined.

---

## LAYER 3 — DEBATE & FALSIFICATION (Topics 7-9)

> **Objective:** Force critical System 2 debate, explore alternative paradigms, and identify failure modes prior to implementation.

### T7: Comparative Alternatives Debate
**Root Question:** "What are the 3 viable architectural approaches to this problem, and why should we choose this specific one?"
- Present 3 genuine architectural alternatives with rigorous pros and cons.
- Justify the recommended approach with technical and algorithmic evidence.
- Provide trade-off visibility for the user's decision.

**Format:**
```markdown
Alternative A: [Name]
✅ Pros: [list]
❌ Cons: [list]
📊 Ideal Regime: [context]

Alternative B: [Name]
✅ Pros: [list]
❌ Cons: [list]

Alternative C: [Name]
...

🏆 Recommendation: Alternative A because [precise technical rationale].
```

**Resolution Checklist:**
- [ ] 3 genuine architectural alternatives evaluated (no straw men).
- [ ] Objective trade-offs documented.
- [ ] Selection justified with physical/algorithmic proofs.

### T8: Failure Modes & Fault Tree Analysis
**Root Question:** "What could go critically wrong? What are the top 3 catastrophic failure vectors?"
- Adversarial review of the selected architecture.
- Identify: performance bottlenecks, single points of failure (SPOF), dangerous concurrency regimes.
- Establish concrete deterministic mitigations for each failure mode.

**Format:**
```markdown
RISK-01: [Concrete failure description]
- Likelihood: High / Medium / Low
- Impact: Critical / High / Medium
- Mitigation: [Deterministic countermeasure]
- Plan B: [Contingency protocol if mitigation fails]
```

**Resolution Checklist:**
- [ ] Top 3 critical risks identified with likelihood and impact.
- [ ] Actionable mitigations defined.
- [ ] Step-by-step contingency Plan B formulated for highest severity risk.

### T9: Empirical Falsification Criteria
**Root Question:** "How will we empirically know if the architecture fails? What is the falsification threshold?"
- Formulate quantitative metrics defining failure.
- Establish numeric thresholds (P99 latency, error rates, dropped frames).
- Define how and when empirical falsification benchmarks will be executed.

**Format:**
```markdown
The solution is falsified (REJECTED) if:
- [ ] P99 Latency > [X] ms under standard load
- [ ] Error rate > [Y]% over 24-hour runtime
- [ ] [Metric] breaches [Threshold] for longer than [Duration]

Verification Protocol:
- Phase: [Project phase]
- Tooling: [Benchmark harness / Profiler]
- Lead Role: [QA Engineer / Red Team Adversary]
```

**Resolution Checklist:**
- [ ] Falsification criteria are quantitative and measurable.
- [ ] Numeric thresholds defined.
- [ ] Deterministic testing protocol documented.

---

## LAYER 4 — CONTRACTS & RELEASE (Topics 10-12)

> **Objective:** Formalize delivery contracts, define domain-specific Q ≥ 9.0 criteria, and plan lifecycle sustainment.

### T10: Formal Deliverables Registry
**Root Question:** "Enumerate EXACTLY what physical artifacts must be delivered upon project completion."
- Exhaustive inventory of files, modules, documents, APIs, and schemas.
- File formats and locations.
- Target deployment artifacts.

**Format:**
```markdown
MANDATORY DELIVERABLES:
- [ ] `src/core/engine.py` — Core engine implemented with unit tests
- [ ] `docs/API.md` — Complete endpoint specification
- [ ] `tests/` — Test suite with ≥ 90% code coverage
- [ ] `docker-compose.yml` — One-command deployment configuration
- [ ] `PROJECT_BRAIN.md` — Neural memory map of the project
```

**Resolution Checklist:**
- [ ] Deliverables inventory is exhaustive and unambiguous.
- [ ] Schema and format for every deliverable specified.
- [ ] Storage and deployment paths formalized.

### T11: Acceptance Gate Criteria (Project-Specific Q ≥ 9.0)
**Root Question:** "What concrete dimensions define Quality Score Q ≥ 9.0 for THIS specific project?"
- Domain-tailored quality standards.
- Phase-by-phase quality gates.
- Explicit criteria for final acceptance.

**Format:**
```markdown
Q = 9.0 for [Project Name] requires:
- Functional: [Specific behavioral guarantees]
- Performance: [Numeric latency/throughput bounds]
- Visual/UX: [WCAG 2.2 AA / responsive / 60fps]
- Security: [Zero-trust auth / zero injection vulnerabilities]
- Documentation: [Comprehensive typed specs]
- Test Suite: [100% passing, exit code 0]
```

**Resolution Checklist:**
- [ ] Q ≥ 9.0 criteria customized to the domain.
- [ ] Phased quality gates established.
- [ ] Objective evaluation protocol defined.

### T12: Post-Delivery Sustainment & Handoff
**Root Question:** "What is the operational lifecycle post-delivery? Who maintains, monitors, and evolves this system?"
- Target operators and user onboarding pathways.
- Maintenance ownership and runbooks.
- Modularity and extension roadmap.
- Comprehensive handoff documentation.

**Resolution Checklist:**
- [ ] Target operators identified.
- [ ] Operational runbooks planned.
- [ ] Handoff documentation structured.

---

## FINAL ARTIFACT: GRILL_RESULTS.md

Upon completing all 12 topics, the agent synthesizes the results to `.planning/GRILL_RESULTS.md`:

```markdown
# GRILL_RESULTS.md — [Project Name]
> Session: [timestamp] | Resolved Topics: 12/12

## LAYER 1 — Scope & Intent
- True Intent: [Validated core outcome]
- Success Scope: [Measurable criteria]
- Anti-Scope: [Explicit exclusions]

## LAYER 2 — Architecture & Facts
- Tech Stack: [Complete specification]
- Validated Assumptions: [Enumerated list]
- Authoritative Data Sources: [Details]

## LAYER 3 — Debate & Falsification
- Selected Architecture: [Name + Rationale]
- Top 3 Critical Risks: [Mitigations & Plan B]
- Falsification Thresholds: [Numeric metrics]

## LAYER 4 — Contracts & Quality
- Deliverables: [Exhaustive list]
- Q ≥ 9.0 Specification: [Custom criteria]
- Post-Delivery Lifecycle: [Plan]

## NEXT ACTIONS
→ Activate `deep-planning-protocol` (Generate 5 pre-flight documents)
→ Activate `project-neural-map` (Initialize PROJECT_BRAIN.md)
→ Activate `corporate-swarm-os` (Instantiate multi-agent hierarchy)
```

This artifact is saved in `.planning/GRILL_RESULTS.md` and linked in `PROJECT_BRAIN.md`.
