---
name: popperian-invariance-testing
description: >-
  Metamorphic invariance testing and stress-testing critical algorithms against scale limits and boundaries. Trigger on: stress test, edge cases, boundary test, break code, scale limits, heavy load, property test, invariant test, test limits, robustness, popperian testing, metamorphic testing.
---
# SKILL: Popperian Invariance Testing

> *"A theory that cannot be refuted by any conceivable empirical or logical event is non-scientific. A rule that holds only in a single calibration regime is an artifact."*

## 1. Epistemic Foundations

Every hypothesis, solver, or algorithm must undergo rigorous scientific stress-testing prior to promotion to core architecture.

1. **Popperian Falsification Protocol:**
   A hypothesis \(H\) is scientifically valid if and only if there exists a non-empty set of potential falsifiers \(\mathcal{F}\) such that:
   \[
   \exists e \in \mathcal{F} \quad \text{where} \quad \text{Evaluate}(H, e) = \text{FALSE}
   \]
   If \(\mathcal{F} = \emptyset\), \(H\) is dogmatic and REJECTED immediately.

2. **Metamorphic Invariance Transformations:**
   A valid system property \(P\) must satisfy metamorphic relations under transformation \(\mathcal{T}\):
   \[
   P(x) \equiv P(\mathcal{T}(x))
   \]
   Transformations cover four universal axes:
   - **Scale Invariance:** System behavioral equivalence under scaling of input dimensions, concurrency, or payload volumes.
   - **Temporal Invariance:** Performance and accuracy stability across disjoint temporal windows (\(\text{drift} < \delta_{\text{max}}\), where \(\delta_{\text{max}}\) is derived from system variance bounds).
   - **Regime Invariance:** Invariance across operational states (Nominal, Extreme Burst, Degraded Fault), or explicit scope restriction (`DOES_NOT_APPLY_WHEN`).
   - **Topological Invariance:** Structural equivalence under isomorphic transformations of the underlying execution network or data structure.

---

## 2. AGI Execution Engine

### Step 1: Formal Falsifier Declaration
- State hypothesis \(H\) with quantitative tolerance bounds.
- Define Falsifier \(F\): `"H is FALSE if [Measurable Condition C holds within time T]."`
- **MANDATORY EXECUTION & CANONICAL HARNESS:** \(F\) MUST be backed by an executable test runner command (`pytest`, `npm test`, etc.) executing directly against the CANONICAL architecture/engine. Writing standalone "toy" scripts or mock runners to simulate algorithms is FORBIDDEN. Comparative hypotheses must enforce differential A/B testing on frozen canonical pipelines.

### Step 2: Automated Metamorphic Battery & Subagent Dispatch
Subject \(H\) to the metamorphic transformation matrix:
1. **Scale Transform:** \(\mathcal{T}_{\text{scale}}(x, \lambda)\) where \(\lambda \in [10^{-1}, 10^3]\). Output must scale within theoretical complexity bounds \(O(f(n))\).
2. **Temporal Transform:** Evaluate across out-of-sample data or simulated time windows. Compute distribution drift via Kullback-Leibler divergence \(D_{KL}(P \parallel Q) < \delta\).
3. **Regime Shift:** Perturb operating conditions (inject latency, fault spikes, parameter saturation). Verify regime bounds.
4. **Visual/UI Invariance:** If the test touches UI or 3D rendering, use Puppeteer MCP (`puppeteer_screenshot(width: 1920, height: 1080)`) + `view_file` to visually inspect state transitions.
5. **Subagent Falsifier Dispatch:** Invoke subagent falsifier to aggressively construct metamorphic edge cases:
   ```json
   {
     "TypeName": "self",
     "Role": "Popperian Falsifier",
     "Prompt": "FALSIFICATION RUN: Execute metamorphic invariance tests against module [NAME]. Test edge regimes, scale transformations (10x, 100x), noise injection, and verify whether physical/mathematical invariants survive. Return a formal falsification report and command exit codes."
   }
   ```

### Step 3: Falsification Verdict Matrix
- **`VERDICT::NOT_FALSIFIED`:** All metamorphic invariants hold with zero-exit-code command proof. Promote claim to `DEC::GROUNDED`.
- **`VERDICT::STRONGLY_FALSIFIED`:** Fails temporal stability or regime tests. Downgrade to `DEC::SPECULATIVE`. Must fix underlying code — narrowing scope to bypass a failed test is STRICTLY FORBIDDEN (`VERDICT::SCOPED` is abolished).
- **`VERDICT::FATALLY_FALSIFIED`:** Violates fundamental physical invariants, mathematical identities, or safety bounds. Reclassify to `DEC::UNKNOWN` and quarantine module.

### Step 4: Cognitive Memory Hypothesis Watchlist
All active hypotheses are indexed in the system cognitive memory graph.
Required fields per hypothesis:
`[ID | Title | Falsifier Contract | Scope Bounds (APPLIES_WHEN / DOES_NOT_APPLY_WHEN) | Test History | Current DEC Level]`

---

## 3. Verification Gate
- [ ] Falsifier explicitly defined as executable assertion.
- [ ] Scale, Temporal, Regime, and Topological transformations executed.
- [ ] Drift measured against statistical variance bounds (no arbitrary magic numbers).
- [ ] Epistemic DEC status updated in system memory graph.

---

## 4. The 4-Layer Ground Truth Forensic Protocol

When evaluating any predictive, heuristic, or autonomous decision system, black-box output metrics (e.g. cumulative win-rate, total loss score) are insufficient. The system must generate a 4-Layer Ground Truth Forensic Visual and Telemetric Audit:

1. **Layer 1: Raw Empirical Reality ($D_{\text{raw}}$):** The unmodified real-world sensory, telemetry, or time-series data streams.
2. **Layer 2: Ground Truth Oracle Benchmark ($O_{\text{ideal}}$):** The theoretical or a posteriori optimal action calculated with full hindsight (the optimal target).
3. **Layer 3: Model Latent Physical State ($\Phi_{\text{latent}}$):** Internal hidden variables, potential fields, probability densities, or phase synchrony metrics.
4. **Layer 4: Machine Action & Precision Delta ($\Delta_{\text{error}}$):** The discrete actions executed by the agent measured against the Oracle benchmark in latency, accuracy, and magnitude dispersion.

