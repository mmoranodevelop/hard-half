# Worked examples

Three runs of the protocol, at decreasing length. The first is enterprise software and shows a Class-A premise attack. The second is scientific/industrial and shows a floor computation that relocates the whole problem. The third shows the protocol correctly returning **no** — which is a real outcome and must be reported as cleanly as a yes.

All figures are illustrative and labelled as the protocol requires. Recompute with your own data.

---

## Example 1 — "Global inventory without overselling is impossible, CAP says so"

**Presented problem.** A retail platform runs in four regions. Product availability must be correct globally: no overselling of the last unit. Latency budget is 100 ms at the edge. Two vendors and the internal architecture team have concluded that global strong consistency at that latency is impossible, citing CAP.

### Phase 0 — Objective with no solution in it

The stated problem contains a mechanism ("global strong consistency"). Restated:

> For each SKU, the number of units promised to customers must never exceed the number of units that exist, and an availability answer must return within 100 ms at p99 from any region.

Unit of value: one correct availability answer. Unit of cost: current p99 is 340 ms with a cross-region read, and the business absorbs ~0.4% oversell.

Observable difference if solved: oversell incidents go to zero *and* p99 falls under 100 ms. Note these are two objectives that were being traded against each other, and nobody had written them as separate requirements.

### Phase 1 — Impossibility class

**Class A cited: CAP.** Check the premises (`impossibility-classes.md`).

CAP forbids a linearizable register that remains available on every non-failing node during a partition. Two premises fail here:

1. **The objective is not linearizability.** The requirement is an *invariant* — promised ≤ existing — not a total order on reads. An invariant of the form "a counter never goes below zero" is preservable without consensus on every operation.
2. **The objective is not full availability during partition.** The business can tolerate a partitioned minority region degrading to "check back" on the last few units of a SKU, which is a tiny fraction of requests.

**The sentence**: *CAP forbids linearizable-and-fully-available during a partition. We need a preserved inventory invariant plus bounded staleness, which CAP does not forbid.*

Real class: **C (empirically unachieved here) + D (nobody costed the alternative)**. The Class-A citation was cover.

### Phase 2 — Constraint ledger (abridged)

| # | Constraint | Asserted by | Class | False if… |
|---|---|---|---|---|
| 1 | Availability must be exact for every SKU | Product spec, 2021 | Habitual | Exactness only matters near zero stock — 96% of SKUs are never within 10 units of zero *(measured)* |
| 2 | All reads cross to the primary region | Architecture, 2019 | State-of-the-art | Regional replicas can answer if the invariant is enforced elsewhere |
| 3 | Inventory is one global number per SKU | Inherited from the ERP | Habitual | Nothing requires a single counter; it is a modelling choice |
| 4 | Oversell has unbounded cost | Finance | Economic | Actual cost measured at €18/incident, ~2,100 incidents/yr = €38k *(measured)* |
| 5 | Speed of light: 40 ms round trip between the two furthest regions | Physics | **Law** | Never |

Fence check on #3: the single global counter came from the ERP's data model, not from a business rule. The ERP constraint is real for settlement, not for the availability path.

Row #5 is the only wall, and it says something precise: any design requiring a cross-region round trip on the read path cannot meet 100 ms with headroom. That kills the "just make it faster" family entirely — a useful thing to establish in one line.

### Phase 3 — The floor

Metric: p99 latency for an availability answer, and oversell incidents per year.

Floor for latency: a read served from the requesting region — no cross-region hop — is bounded by local storage and network, ≈ **4 ms** *(estimated from current same-region p99)*. Current: 340 ms. **Gap ratio ≈ 85×.**

Floor for oversell: with any regional autonomy, the irreducible oversell is bounded by how much stock is delegated to a region that cannot currently be reconciled. That is a *design parameter*, not a constant — and this is the finding. Zero is achievable by delegating zero, at the cost of latency; the two objectives are connected by a dial nobody had drawn.

Gap ratio of 85× on latency means the architecture is the problem, not the tuning. Phase 4.

### Phase 4 — Reconstruction

Ledger rows negated: #1, #2, #3.

**Path A — Escrow / reservation partitioning.** Split each SKU's count into per-region escrows. A region sells freely from its escrow with a purely local read and a local decrement — the invariant holds by construction because no region can sell stock it does not hold. Rebalancing happens asynchronously. When a region's escrow nears zero, and only then, it falls back to a coordinated path. *Traces to row #3: the single global counter was a modelling choice.* Move #6 — change the state space so the hard case does not arise.

**Path B — Monotonic modelling (CALM).** Model availability as a monotonically growing set of allocations rather than a mutable count. Monotonic programs have coordination-free consistent implementations, so the coordination requirement disappears rather than being optimized. Higher modelling cost; strong theoretical footing.

**Path C — Tiered by risk.** 96% of SKUs are never near zero *(measured)*. Serve those from a stale regional replica with no coordination at all; apply Path A only to the 4% that approach zero. *Traces to row #1.* This is the "50% of the target at 5% of the complexity" candidate — and it turns out to be more like 96% of the target.

All three share no assumption with the incumbent. All respect row #5 by removing the cross-region hop from the read path entirely rather than shortening it.

### Phase 5 — DFX (abridged, Path A + C combined)

| Pass | Finding | Change |
|---|---|---|
| DFC | Rebalancing traffic is the only new recurring cost, ≈ €900/mo *(estimated)*, against €38k/yr oversell | Proceed |
| DFM | Escrow rebalancing needs an on-call runbook; new failure mode is stranded stock in a partitioned region | Add stranded-stock alarm and a manual release path |
| DFS | Two mechanisms (escrow + tiering) instead of one | Accept: tiering keeps escrow off 96% of SKUs, which is a net reduction in moving parts |
| DFPR | Rebalancer is the bottleneck at 10× SKU count | Shard the rebalancer by SKU hash |
| DFV | Need to observe invariant violations directly, not infer them from complaints | Add a continuous global reconciliation check that alarms on promised > existing |
| DFR | Reversible — escrow can be set to 100% in one region, restoring current behaviour | Ship behind a per-SKU flag |

### Phase 6 — Red team

**Efficient-market check**: answer **(a) + (c)**. Escrow patterns are well known in the distributed systems literature and have been for decades; this organization did not apply them because the ERP's data model was treated as the domain model. That is a nameable structural reason, and it is embarrassing rather than mysterious — which is exactly what a credible (c) looks like.

**Kill experiment**: shadow-run escrow accounting on production traffic for one week without serving from it. Cost: ~3 engineer-days. **Kills the path if**: more than 0.1% of transactions would have hit an escrow-empty fallback, which would mean the latency win does not materialize where it matters.

**What would have to be true**, by uncertainty × impact:
1. Demand per SKU per region is predictable enough that escrows do not empty constantly *(highest uncertainty — the shadow run tests exactly this)*
2. Stranded stock in a partition is recoverable within the fulfilment SLA
3. Finance accepts a bounded, chosen oversell rate instead of a nominal zero that is currently 0.4% anyway

**Outcome**: the impossibility was a Class-A citation applied to an objective the theorem does not address, resting on a Habitual data-modelling constraint. The gap ratio was 85×.

---

## Example 2 — "Direct air capture below $100/tonne is thermodynamically impossible"

**Compressed run.** Illustrates a floor computation that relocates the entire problem.

**Phase 0.** Objective: remove one tonne of CO₂ from ambient air and deliver it in concentrated form, for under $100, at megatonne scale.

**Phase 1.** Class A cited: the thermodynamic minimum work of separation. This is genuine physics — no premise attack on the second law. So compute it rather than argue with it.

**Phase 3 (run early, because the Class-A claim is quantitative).** Minimum work to separate CO₂ from air at ~420 ppm:

`W = RT·ln(1/x) = 8.314 × 298 × ln(1/0.00042) ≈ 19.3 kJ/mol` *(derived)*

Per tonne: `19.3 kJ/mol × (10⁶ g ÷ 44 g/mol) ≈ 439 MJ ≈ 122 kWh/tonne` *(derived)*.

At $0.03/kWh: **≈ $3.70/tonne** of irreducible separation energy *(estimated at illustrative renewable pricing)*.

Operating plants report roughly 1,500–2,500 kWh/tonne *(cited, order of magnitude)* and costs in the $400–1,000/tonne range *(cited)*.

**Gap ratio on energy ≈ 12–20×. Gap ratio on cost ≈ 100–270×.**

**The finding.** The thermodynamic wall is real and is nowhere near $100/tonne — it is near $4/tonne. **The cited impossibility is not the binding constraint.** The binding constraints are sorbent cycling energy (the parasitic heat to release the CO₂, far above the separation minimum), capital amortization, and air-contacting throughput. Those are Class C and Class D, not Class A.

The problem is therefore not "beat thermodynamics" but "close a 15× gap between actual and minimum separation energy, and amortize contactor capital across far more air." Those are engineering and finance problems with a known shape, and the reframing is what makes them attackable.

**Phase 4 pointers**: move #4 (change when — continuous passive contacting versus forced-draft cycling), move #8 (change the scale — capital per tonne falls with contactor area, not with plant count), move #7 (change the unit of sale — the buyer of removal credits is not the buyer of CO₂).

**Lesson**: when a Class-A claim is quantitative, compute it immediately. A cited law that turns out to sit two orders of magnitude below the current operating point is not a wall — it is a measurement of how much room exists.

---

## Example 3 — "Zero false positives and zero false negatives in automated compliance screening"

**Compressed run.** Illustrates the protocol returning a correct no.

**Phase 0.** Restated: classify every transaction as reportable or not, with no missed reports and no incorrect reports, without human review.

**Phase 1.** **Class F, and underneath it Class A.** The requirement is definitionally unachievable unless the two classes are perfectly separable by the available features — which is an empirical property of the data, and here it is false: identical feature vectors appear in both classes *(measured on 18 months of history)*. Given overlapping distributions, no classifier of any kind achieves both zero false positives and zero false negatives. This is not a limitation of the model; it is a property of the data.

**The honest answer**: *impossible as posed*, and no amount of modelling effort changes it. Reporting this early saves the entire program.

**The relocation.** The objective was never really "zero and zero" — it was "no regulatory finding, at acceptable cost." That reframes to a constrained optimization with an explicit, defensible operating point:

> Minimize human review volume subject to false-negative rate below the threshold the regulator will accept, with a documented, auditable basis for the threshold.

Which is achievable, measurable, and — critically — *negotiable with the regulator*, moving the binding constraint from Class A to Class E where it actually lives.

**Phase 3 on the reframed objective.** Floor = the irreducible human reviews implied by the genuinely ambiguous region of the feature space: ≈ 2% of volume *(estimated from the overlap region)*. Current: 100% of flagged volume, ≈ 31%. **Gap ratio ≈ 15×**, which is an ordinary and very fundable engineering problem.

**Lesson**: "impossible as posed" is a finding, not a failure — and it is usually accompanied by a nearby objective with a large gap ratio. Deliver both together. The team asked for the impossible thing because nobody had written down the achievable one.
