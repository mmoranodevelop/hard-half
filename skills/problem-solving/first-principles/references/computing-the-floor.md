# Computing the floor

Phase 3. The floor is **the value your objective's metric would take if only the Law and Math constraints applied.** Everything between the floor and today's number is a design decision someone made, which means it can be unmade.

This phase converts the analysis from opinion into arithmetic. It is the most skipped phase and the one that produces the finding.

**Contents**
- [The procedure](#the-procedure)
- [Floor techniques by domain](#floor-techniques-by-domain)
- [The gap ratio](#the-gap-ratio)
- [Worked micro-examples](#worked-micro-examples)
- [How floors go wrong](#how-floors-go-wrong)

---

## The procedure

1. **State the metric and its units.** From Phase 0. `$/kWh`, `€/reconciled transaction`, `hours to result`, `kg CO₂/tonne`, `FTE-days/release`.
2. **List what is irreducibly required** to produce one unit of value, using only Law and Math rows from the ledger. Materials, energy, information, operations, human decisions.
3. **Price each at its commodity or theoretical value** — the cost if you bought or performed it at scale with no markup, no process inefficiency, no organizational overhead.
4. **Sum.** That is the floor.
5. **Divide today's number by it.** That is the gap ratio.
6. **Label every input**: measured / cited / estimated / assumed. An unlabelled floor cannot be defended, and a floor that cannot be defended makes everything downstream look quantitative when it is not.

The floor is deliberately unachievable. It is not a target — it is a **measuring instrument** for how much of the current cost is physics and how much is choice.

---

## Floor techniques by domain

### Physical products and manufacturing

**Bill of materials at commodity prices.** Weigh the finished object, decompose it into materials, price each at spot commodity rates, and sum. This ratio — finished price over raw material price — is often called the **idiot index**, and a high value means you are paying for process, not for substance.

Also available: the theoretical **bill of energy** (thermodynamic minimum to effect the transformation), and the **minimum operation count** (how many irreducible shaping, joining, and inspection steps the geometry requires).

### Chemistry, energy, and materials

Use the actual bounds:

- **Gibbs free energy** of the reaction or separation — the true minimum work, which for separations depends strongly on concentration (dilute streams are punishing, and that dependence is often the finding).
- **Carnot** for heat engines; note that fuel cells and photovoltaics are not heat engines and are not bounded by it.
- **Betz limit** (59.3%) for a wind actuator disc in free stream.
- **Shockley–Queisser** (~33%) for a single-junction solar cell; multi-junction cells exceed it because the premise is single-junction.
- **Enthalpy of vaporization / fusion** for phase-change processes.

The characteristic result: current industrial processes run at 5–30% of thermodynamic efficiency, so the floor is far below the current number and the gap is process, not physics.

### Information and computation

- **Shannon capacity** bounds bits over a channel — but ask first whether the bits must be sent at all. Caching, prediction, delta encoding, and moving computation to the data all reduce the numerator rather than fighting the bound.
- **Counting and entropy arguments** bound storage and comparison-based sorting.
- **Landauer** bounds irreversible bit erasure at ~2.8 zJ (300 K). Current CMOS runs orders of magnitude above it, so it is rarely the binding constraint — check the arithmetic before conceding to it.
- **Irreducible operation count**: how many operations does the problem's information content actually require? Compare against what is executed.
- **Minimum data movement**: bytes that must cross a boundary, versus bytes that do. In distributed systems this gap is frequently 100× or more.

### Business processes and operations

The floor here is the **irreducible human decision count** plus the **irreducible data movement**.

For each unit of work, ask: how many decisions genuinely require human judgment — a judgment where a rule cannot be written, an accountability that regulation assigns to a person, or a genuinely novel situation? Everything else is transport, transcription, checking, chasing, and waiting.

Floor = (irreducible decisions × loaded cost of the decider's time) + (regulatorily mandated steps) + (unavoidable capital).

Typical result on a mature back-office process: the floor is 5–20% of current cost, and the remainder is handoffs and rework. A process with 40 steps and 3 real decisions is telling you something quantitative.

Complementary technique: **the theoretical cycle time** — the sum of the steps' actual work time, ignoring all queueing. Real cycle time over theoretical is usually 20–100×, and the ratio is entirely waiting.

### Scientific and R&D programs

The metric is usually **cost or time per unit of knowledge gained** — per hypothesis discriminated, per candidate screened, per parameter constrained.

Floor techniques:
- **Information-theoretic**: how many bits does deciding between the hypotheses require, and what is the cheapest measurement yielding those bits? Programs frequently run experiments that cannot discriminate, which is a floor violation of a different kind.
- **Minimum measurement count**: how many measurements does the design of experiments actually require, given the effect size and the acceptable error rates? Compare with how many are performed.
- **Best-in-adjacent-field**: another discipline that solved a structurally similar measurement problem, and its cost per data point. Cross-field ratios of 100× are common and are usually the highest-value finding available.
- **Nature's proof point**: if a biological or geological system performs the transformation, the conditions it does so under bound what is possible — biological nitrogen fixation at ambient temperature and pressure being the standard example against the Haber–Bosch process's conditions.

### Software delivery

- Floor for a change: the time to write the genuinely novel logic plus the time to verify it. Everything else — environment setup, waiting for review, waiting for CI, coordination, rework from unclear requirements — is above the floor.
- Floor for a query: the bytes that must be read given the data layout and the selectivity. Compare to bytes actually read.

---

## The gap ratio

`gap ratio = current ÷ floor`

| Ratio | Reading | Action |
|---|---|---|
| **< 2×** | Genuinely near the wall | Stop optimizing the mechanism. The leverage is in changing the objective — go back to Phase 0. Further engineering here has poor returns and everyone before you has already tried it. |
| **2–10×** | Ordinary engineering slack | The architecture is roughly right. Phase 5 DFX passes will recover most of it. Expect incremental, compounding wins. |
| **> 10×** | The architecture is the problem | A fundamentally different design almost certainly exists. Phase 4 is where the value is. This is the signature of a real opportunity. |
| **> 100×** | Check the floor again | Either a historic opportunity or, far more often, a floor that omits a real cost. Re-derive before believing it. |

The ratio is a diagnostic, not a promise: nobody reaches the floor. Its use is telling you **which phase to spend your effort in**, which is a decision teams otherwise make by temperament.

---

## Worked micro-examples

**Manufactured assembly.** A device sells for $4,800. Mass 12 kg: 7 kg steel (~$0.8/kg), 3 kg aluminium (~$2.5/kg), 1.5 kg copper (~$9/kg), 0.5 kg electronics (~$60/kg). Materials ≈ $5.6 + $7.5 + $13.5 + $30 = **$56.6**. Gap ratio ≈ **85×**. Reading: the price is almost entirely process, tooling amortization, and margin — not substance. A different manufacturing architecture is very likely to exist. *(All figures estimated at illustrative spot prices; recompute with real quotes.)*

**Back-office process.** Reconciliation costs €14.20 per transaction fully loaded. Decomposition: 31 process steps, of which 3 require genuine human judgment (exception classification, write-off approval, regulatory attestation), averaging 90 seconds each at €55/h loaded → €2.06. Mandated archival ≈ €0.15. Floor ≈ **€2.21**. Gap ratio ≈ **6.4×**. Reading: mid-range — the process shape is salvageable, the 28 non-decision steps are the target. Note this is a Phase 5 problem, not a Phase 4 one, and that is a useful thing to know before commissioning a rewrite.

**Data pipeline.** A nightly job reads 4.2 TB to produce a 90 MB report. Given the filters, the rows that can affect the output total ~38 GB. Gap ratio on data movement ≈ **110×**. Reading: check the floor — and it holds, because the filter is applied after the scan. The finding is predicate pushdown and layout, not a bigger cluster. This is the common case where the floor computation names the fix directly.

---

## How floors go wrong

- **Omitting a real cost.** The energy to transport the material to the reaction. The human review the regulation requires. The retries the network guarantees. The most common source of an implausible ratio.
- **Pricing at retail instead of commodity.** The floor asks what the input costs at scale with no markup, not what you currently pay your supplier.
- **Using today's process to define what is irreducible.** If your step list came from the current runbook, you have computed a floor for the current design, not for the problem. Derive the requirement from the objective.
- **Assuming away the hard part.** A floor that ignores the constraint that actually binds produces a large, meaningless ratio.
- **Confusing a bound with a target.** The floor is not achievable and nobody should be held to it. Its job is to size the opportunity.
- **Precision theatre.** €2.2137 per transaction implies measurement you do not have. Give a range and its basis; order-of-magnitude honesty is more useful than false precision and survives scrutiny better.
