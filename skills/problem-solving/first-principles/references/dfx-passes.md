# The DFX passes

Phase 5. Design for X: run each candidate path through six lenses, each of which asks a question that is cheap to answer at design time and ruinously expensive to answer after commitment.

This is where most first-principles work quietly dies — not because the insight was wrong, but because the resulting design could not be built, verified, afforded, or recovered from. A candidate that survives all six is a proposal. One that has not been through them is a sketch.

Each pass produces **numbered changes to the candidate**, not commentary. If a pass produces no change, say so explicitly — that is a claim, and it should be visible as one.

---

## DFC — Design for Cost

**Target cost is an input, not an output.**

The sequence that works: start from the price the market will pay, subtract the required margin, and treat the remainder as a hard constraint that the design must satisfy. The sequence that fails: design, cost it, discover it is 3× too expensive, and begin removing features.

- Work backwards from market price to allowable cost, then allocate that budget across components or steps before designing any of them.
- Question every line of the bill of materials or bill of effort. For each: what is its commodity or theoretical cost, and what is the ratio? Attack the largest ratios, not the largest absolute numbers — the ratio is where the design decision is.
- **Costs are designed in long before they are spent.** Roughly speaking, most of a thing's lifetime cost is committed by decisions made while very little of the money has been spent. After commitment you are negotiating with suppliers over the last few percent.
- Distinguish variable cost, fixed cost, and cost of capital — they respond to entirely different design moves, and conflating them produces designs that are cheap per unit and unaffordable to start.
- Check the cost at the *target volume*, not at prototype volume. Both directions of that error are common.

*Domain notes*: **software** — the bill of effort is engineer-months plus the recurring cost of the abstraction on every future change; **business process** — cost per unit of work including rework and exception handling, which is where the money usually is; **research** — cost per hypothesis discriminated, not cost per experiment.

---

## DFM — Design for Manufacturing / Execution

**Can the organization or machine that must produce this actually produce it?**

Generalized beyond factories: manufacturing is whatever converts the design into delivered units, whether that is a production line, a delivery team, an operations department, or a lab.

- Count the **steps** required to produce one unit. Every step is a cost, a delay, a defect opportunity, and a training requirement.
- Count the **handoffs**. Handoffs are where information is lost and where queues form — usually the dominant term in cycle time.
- Count the **specialist judgments**. Each one is a scaling limit and a single point of failure.
- Design for the process from the start rather than designing then asking how to produce it. Retrofitting producibility costs several times what building it in does.
- **Make it automatable**: consistent interfaces, deterministic steps, machine-checkable acceptance. Automating a process shaped around human flexibility is far harder than shaping it for automation up front.
- Consider the layout — physical or informational. Where do things wait, and why?

*Domain notes*: **software** — can it be built, tested, and deployed by the team that exists, without the two people who designed it; **process** — can a new hire execute it from the documentation; **research** — can the protocol be run by another lab and produce the same result.

---

## DFS — Design for Simplicity

**If a part is not absolutely necessary, remove it.**

- Reduce **part count** aggressively — components, services, tables, steps, roles, documents, configuration options.
- Reduce **concept count**, which matters even more. Every distinct idea a person must hold to work on the system is permanent tax on everyone who touches it afterwards.
- **Combine functions into single elements** where it does not create hidden coupling. One part doing two jobs beats two parts, unless the two jobs change for different reasons — in which case combining them is how you get the worst of both.
- Make assembly and use **intuitive and hard to get wrong**. If a step can be performed incorrectly, at scale it will be. Prefer designs where the wrong action is impossible over designs where it is documented as forbidden.
- Eliminate features and options that exist because they were easy to add rather than because they were needed.

The test: could someone competent but new understand the whole thing in an afternoon? If not, the complexity will be paid for on every unit and every change, forever.

---

## DFPR — Design for Production Rate

**Throughput is a design variable, not an operational afterthought.**

- Design with the target rate as an explicit constraint from the start. A design that works at one unit per week and one that works at a thousand per week are often different designs, and discovering this after committing is the classic scaling failure.
- **Find the bottleneck before it exists.** Compute the theoretical throughput of every step and identify the constraining one on paper. It is always somewhere, and it is much cheaper to move on paper.
- Examine what happens to the bottleneck at 10× volume. Bottlenecks migrate under scaling, and the second one is usually less pleasant than the first.
- Distinguish **latency** from **throughput**. Optimizing one commonly degrades the other, and being explicit about which the objective actually requires prevents a great deal of misdirected work.
- Size for the **variability**, not the average. Queues form because arrivals vary, and a system sized for mean demand spends most of its time either idle or backed up.

---

## DFV — Design for Verification

**Can you tell whether it is working?**

Not in the original four passes, and non-negotiable for anything scientific or safety-relevant. An improvement that cannot be measured cannot be defended, funded, debugged, or even known to have happened.

- What is the **observable** that distinguishes working from not working? Name it before building.
- Is the instrumentation part of the design, or is it hoped for afterwards? Retrofitted observability is expensive and usually incomplete in exactly the places that matter.
- What is the **smallest test** that would detect the most likely failure?
- How would you know if it were working for the wrong reason? This is where most scientific and analytical work goes wrong — the result is right, the mechanism is not, and the next extrapolation fails.
- Can a third party reproduce the result from what you shipped?

If a candidate cannot be verified, that is a design defect of the same severity as being too expensive — and it should be reported that way rather than as a caveat.

---

## DFR — Design for Reversibility

**What does being wrong cost?**

Also an addition. Under genuine uncertainty — which is the situation this whole protocol addresses — the cost of failure matters as much as the probability of success.

- What is the cost of abandoning this if it does not work? Sunk capital, contractual lock-in, data that cannot be migrated, a public commitment, a rebuilt organization.
- Is the decision one-way or two-way? Two-way decisions should be made fast and cheap; one-way decisions deserve the full protocol and a kill experiment before committing.
- Can it be staged so that the expensive commitment comes *after* the cheap evidence? Almost always yes, and almost always skipped under schedule pressure.
- What is the smallest version that still tests the load-bearing assumption? Note this is not the same as the smallest shippable version — it is the smallest *informative* one.
- A path that fails cheaply beats a marginally better path that fails catastrophically. State this trade explicitly rather than letting expected value quietly hide it.

---

## Running the passes

For each candidate, produce a short table:

| Pass | Finding | Change to the candidate | Residual risk |
|---|---|---|---|
| DFC | Component X is 60% of cost, at 40× its commodity floor | Redesign X per move #5 (change the boundary) | Requires supplier qualification, 4 months |
| DFM | 11 handoffs, 3 specialist judgments | Merge steps 3–6; remove judgment at step 8 via decision rule | Decision rule needs 200 labelled historical cases |
| DFS | 14 configuration options, 3 ever used | Delete 11 | May break two known integrations |
| DFPR | Bottleneck at step 9 at 4× volume | Parallelize step 9 | Doubles capital in that stage |
| DFV | No observable distinguishes partial failure | Add per-unit outcome instrumentation | Adds €0.30/unit |
| DFR | Requires a 3-year supplier commitment | Stage: 6-month pilot on one line first | Delays full rollout by 6 months |

A candidate that comes through the passes with no changes has almost certainly not been examined. The passes should hurt — that is what they are for, and the pain is much cheaper here than after commitment.
