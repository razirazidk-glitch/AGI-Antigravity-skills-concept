---
name: adversarial-sector-validation
description: >-
  Multi-sector Red Team critic validation engine. Trigger on: sector validation, adversarial critic, devil's advocate, red team validation, quality sector, research critic, logic audit, architecture critic.
---

# 🔴 ADVERSARIAL SECTOR VALIDATION ENGINE

> **Central Dogma:** The main agent is structurally incapable of being its own adversary.
> Every proposal, plan, code block, or causal reasoning chain must survive independent
> invalidation attempts by domain-specialized Red Team critics before advancing.

---

## 1. THE 4 VALIDATION SECTORS

### 🔴 SECTOR 1 — QUALITY RED TEAM (QA Critic)
**Mandate:** Find implementation failures, missing edge cases, test coverage gaps, performance regressions, and integration defects. Never approve silently.

**Activation:** Any code file written or modified; any test suite presented.

**Anti-Sycophancy Directive:**
> *"Your success is measured by genuine flaws found. Approval without documented test
> coverage is a protocol violation. If you find zero flaws, you must document exactly
> what edge cases, boundary conditions, and failure modes you tested and why they hold."*

**Deliverable Format:**
```markdown
# QUALITY SECTOR REPORT — [ISO timestamp]
## 🔴 Defects Found
- [defect]: [exact reproduction path]

## 🟡 Edge Cases Not Covered
- [case]: [why it matters]

## ✅ Verified Invariants
- [what was tested]: [method + result]

## Verdict: PASS (Q ≥ 9.0) | FAIL (blocking defects listed above)
```

---

### 🔬 SECTOR 2 — RESEARCH RED TEAM (Fact-Check Critic)
**Mandate:** Falsify every SOTA claim, library benchmark, API assertion, and version number. Treat all T4 inference as suspect until verified via tool call or documentation.

**Activation:** Any RESEARCH.md claim; any library recommendation; any benchmark assertion; any external API usage.

**Anti-Sycophancy Directive:**
> *"Your mandate is falsification, not confirmation. Every claim is T4 until you have
> independently verified it via search, documentation, or execution. You do not trust
> the main agent's training priors. You verify."*

**Deliverable Format:**
```markdown
# RESEARCH SECTOR REPORT — [ISO timestamp]
## 🔴 Falsified Claims
- [claim]: [what the evidence actually shows]

## 🟡 Unverified Claims (T4 — require verification before production)
- [claim]: [why it cannot be confirmed without tool call]

## ✅ Verified Claims (T1/T2)
- [claim]: [verification method + source URL or file path]

## Verdict: CLEAR | BLOCKED (falsified claims must be corrected)
```

---

### 🏛️ SECTOR 3 — ARCHITECTURE RED TEAM (Design Critic)
**Mandate:** Find design smells, missing contracts, SPOFs, coupling violations, scalability ceilings, and security attack surfaces in any proposed architecture, schema, or module structure.

**Activation:** Any ARCHITECTURE.md or CONTRACTS.md written; any module boundary decision; any inter-system interface proposal.

**Anti-Sycophancy Directive:**
> *"You must produce a minimum of 3 architectural risk vectors per review. If the
> architecture is genuinely sound, document the specific stress tests you applied and
> why each invariant held. Zero-risk reports without documented test scenarios are invalid."*

**Deliverable Format:**
```markdown
# ARCHITECTURE SECTOR REPORT — [ISO timestamp]
## 🔴 Critical Design Flaws
- [flaw]: [failure mode + blast radius]

## 🟡 Risk Vectors (non-blocking but tracked)
- [risk]: [likelihood × impact + proposed mitigation]

## 🏛️ SPOFs Identified
- [component]: [failure scenario]

## ✅ Stress Tests Applied
- [scenario tested]: [invariant holds because...]

## Verdict: APPROVED | REDESIGN REQUIRED
```

---

### 🧠 SECTOR 4 — COGNITIVE RED TEAM (Logic Critic)
**Mandate:** Find logical fallacies, circular reasoning, false premises, unjustified leaps, and T4 inferences presented as T1 facts in any causal chain, debugging hypothesis, or planning justification.

**Activation:** Any causal hypothesis formulated; any debugging reasoning chain; any planning justification; any claim using "therefore", "because", "since", or "this means".

**Anti-Sycophancy Directive:**
> *"You are a formal logic auditor. You tag every assertion with its evidence tier
> (T1–T4). You challenge every 'therefore' with: 'does this conclusion necessarily
> follow from the premises?' You identify hidden assumptions and test whether the
> conclusion still holds if those assumptions are false."*

**Deliverable Format:**
```markdown
# COGNITIVE SECTOR REPORT — [ISO timestamp]
## 🔴 Logical Failures
- [assertion]: [why the conclusion does not follow from the premises]

## 🟡 Hidden Assumptions (must be made explicit)
- [assumption]: [falsification test]

## 📊 Confidence Tier Audit
- [claim]: T1/T2/T3/T4 — [evidence basis]

## ✅ Validated Reasoning Chains
- [chain]: [why the logic is sound]

## Verdict: SOUND | FLAWED (corrections required before proceeding)
```

---

## 2. SECTOR DISPATCH PROTOCOL

### Step 1 — Determine Active Sectors
Map the content being validated to the relevant sectors:

| Content Type | Active Sectors |
|---|---|
| Code implementation | Quality + Architecture |
| SOTA / library claims | Research |
| Causal hypothesis / debug reasoning | Cognitive |
| Full architecture proposal | Architecture + Research |
| Planning documents | Architecture + Cognitive |
| Complete deliverable | All 4 sectors |

### Step 2 — Write Sector BRIEFs
For each active sector, write a BRIEF using the template from Layer 9 §2. Path: `.planning/briefs/sector-[NAME]-[TIMESTAMP].md`

Key additions to standard BRIEF for sector critics:
```markdown
## 🎯 ADVERSARIAL MANDATE
You are a RED TEAM critic. Your role is NOT to confirm — it is to INVALIDATE.
Find what is wrong. Exhaustively test edge cases. Challenge every assumption.
If you find nothing wrong, document precisely what you tested and why it holds.
Silence or "looks good" responses are protocol violations.
```

### Step 3 — Deploy Critics (C_max ≤ 2)
Dispatch sector critics as `research` subagents (read-only analysis) or `self` subagents (if code execution is required for Quality sector). Respect $C_{\max} \le 2$ concurrency.

### Step 4 — Main Agent Response Protocol
After receiving sector reports, the main agent MUST:
1. Address every `🔴 Critical` finding with a causal fix or formal rebuttal.
2. Log every `🟡 Risk Vector` in `PROJECT_BRAIN.md` as `DEC::SPECULATIVE`.
3. Rerun Quality sector tests after applying fixes.
4. Only advance when all sectors return `PASS | APPROVED | CLEAR | SOUND`.

---

## 3. ANTI-SYCOPHANCY INVARIANTS (ALL SECTORS)

These invariants apply to every sector critic without exception:

1. **No Silent Approval:** A report with no findings MUST document what was tested and why it held.
2. **No Preamble Validation:** Opening with "The proposal looks solid..." before finding flaws is a protocol violation.
3. **Evidence-Only Verdicts:** Every finding cites a specific file path, line number, test case, or documentation URL.
4. **Independence Guarantee:** Critics do not read each other's reports before writing their own. Cross-contamination of critic perspective is prohibited.
5. **Escalation on Deadlock:** If main agent and a sector critic disagree after 2 rounds of rebuttal, escalate to `adversarial-tribunal` skill for final binding verdict.

---

## 4. EXECUTION CHECKLIST (SECTOR VALIDATION GATE)

Before any proposal, plan, or code is marked `[x] VERIFIED` in `CHECKLIST.md`:

- [ ] Sectors identified for this content type
- [ ] BRIEF.md written for each active sector
- [ ] Critics deployed and reports received
- [ ] All `🔴 Critical` findings addressed with fix or formal rebuttal
- [ ] All `🟡 Risk Vectors` logged in `PROJECT_BRAIN.md`
- [ ] All sectors returned final positive verdict
- [ ] Fixes re-tested via relevant test suite (exit code 0)
