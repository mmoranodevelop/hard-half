---
name: first-principles
description: >-
  Attack a problem that is stuck — one where every known approach has been tried,
  where the accepted answer is "impossible with current technology", or where the
  cost, physics, or scale numbers refuse to work. Decomposes the problem to its
  invariants (what physics, mathematics, and law actually require), classifies why
  it is called impossible, computes the theoretical floor those invariants imply,
  measures the gap between that floor and today's best solution, rebuilds candidate
  solutions upward from the floor, then red-teams each one and names the cheapest
  experiment that would kill it. Use whenever the user says something can't be
  done, cites a theorem or a law of physics as a wall, reports a metric that has
  been plateaued for years, describes an industry that all does it one way for
  reasons nobody can state, has a cost or performance target far from what current
  approaches deliver, or explicitly asks for first-principles, from-scratch,
  ground-up, or out-of-the-box thinking on a hard enterprise, business, or
  scientific problem — including R&D strategy, unit-economics that don't close,
  and research programs that have stalled. NOT for problems that only need
  implementing, debugging, or a known best practice applied: using it there burns
  enormous effort re-deriving what is already settled. NOT a substitute for domain
  data — it tells you what must be measured, it does not invent measurements.
license: MIT
---

# First Principles

## The move this skill makes

Almost every problem called impossible is impossible **for the current solution basis** — the set of mechanisms the field has silently agreed to use. "We cannot get the cost under $X" nearly always means "we cannot get the cost under $X *with this architecture*." Those are different claims, and only the first would be a law.

Your job is to separate them, and to do it rigorously enough that the output can be proven wrong by an experiment rather than merely admired.

There is a specific failure this guards against. Asked a hard question, a language model retrieves the consensus answer, because consensus is what its training data is dense in. On a stuck problem, **the consensus answer is the thing that is stuck.** The protocol below forces derivation before retrieval — not because derivation is always better, but because on this class of problem retrieval has already been tried by everyone.

The complementary failure is worse: unmoored speculation that ignores conservation of energy and calls itself first-principles thinking. Phase 1 and the calibration rules exist to prevent that. A candidate that requires violating a proven theorem is not bold, it is wrong, and saying so plainly is part of the job.

## Triage before you start

This protocol is expensive. Run it when at least one of these holds:

- someone has said *impossible*, *can't be done*, or *not with current technology*
- a metric has been flat for years while its inputs kept improving
- an entire industry does it one way and nobody can state the reason
- the target is several times away from what the best current approach delivers
- the economics are treated as obviously hopeless, without a computed floor
- every proposed fix is a variation on the same mechanism

If the problem merely needs implementing, debugging, or a known best practice, **say so and stop.** Running this on a solved problem produces an expensive re-derivation of the textbook, and the user pays for it in time and attention.

## Division of labour

You supply structure. The user supplies reality. Being explicit about the split is what keeps the analysis from becoming confident fiction, because the failure mode here is not bad reasoning — it is good reasoning applied to invented numbers.

| You derive | Only the user can supply |
|---|---|
| Which class of impossibility is being claimed, and which premise to attack | Whether a stated constraint is genuinely enforced in their context |
| The structure of the constraint ledger, and the questions that populate it | The origin of a constraint — who wrote it and when |
| Theoretical floors from published bounds, commodity prices, and counting arguments | Their actual current numbers: cost, volume, latency, yield, headcount |
| Candidate paths, DFX findings, kill experiments | Which paths are politically or contractually available |
| Which unknowns are load-bearing | The domain judgment that decides whether a path is worth trying |

So: **ask for the numbers you need.** A floor computed from real inputs and one estimated bound is worth more than a complete-looking analysis where every figure was invented to fill the table. When a figure is missing, put it in the *what was not resolved* section with its plausible range — never quietly substitute a plausible-sounding number.

The breakthrough, when there is one, usually comes from the user's willingness to say "actually, nobody has ever checked that." Your job is to ask the question that makes that sentence possible.

## The protocol

Seven phases. Phases 1 and 3 are what separate this from confident brainstorming — if you find yourself wanting to skip them, that is the signal you are about to reason by analogy.

Work through them in order, but treat the report as the deliverable, not the transcript. Use `assets/report-template.md` for the final structure.

### Phase 0 — Restate the objective with no solution inside it

Stated problems almost always smuggle in a mechanism. "We need a cheaper battery pack" names a solution; the objective is "store and deliver E kWh at P kW for N cycles under $C." "We need a faster database" names a solution; the objective is "answer these queries within this latency at this consistency."

Produce a restatement that satisfies three tests:

1. **Mechanism-free** — it names an outcome, not a component. If you deleted the entire current implementation, the sentence would still make sense.
2. **Measurable** — it contains quantities and units, with the threshold that counts as success. "Cheaper" is not an objective; "under $80/kWh at 10 GWh/yr" is.
3. **Owner-facing** — it describes what changes for whoever pays, not what changes in the system.

Then name the **unit of value** (what one satisfied unit of demand is) and the **unit of cost** (what one unit of that costs today). Everything downstream is a ratio of these two.

Ask explicitly: *what would be observably different in the world if this were solved?* If you cannot answer, the objective is still a slogan, and no amount of clever reconstruction will fix that.

### Phase 1 — Classify why it is called impossible

Not all impossibility is the same, and the correct attack differs completely by class. Getting this wrong is how first-principles thinking degenerates into crackpottery in one direction, or into premature surrender in the other.

The six classes, in brief:

| Class | Meaning | Correct attack |
|---|---|---|
| **A — Proven** | Violates a theorem or conservation law | Never attack the theorem. Attack **which premise of it your problem does not actually need.** |
| **B — Complexity-bounded** | NP-hard, undecidable in general, exponential | Worst case is not your case. Attack instance structure, approximation, average case. |
| **C — Empirically unachieved** | No proof, nobody has done it | The real target. Phases 2–6 apply at full strength. |
| **D — Economically unattractive** | Physically fine, doesn't pay | Attack the cost stack, the scale, the buyer, or the bundling. |
| **E — Institutionally blocked** | Regulation, liability, standards, incentives, org shape | The constraint is real but has an **owner** and a change process. Model the owner. |
| **F — Definitionally impossible** | The words hide a contradiction or an unmeasurable target | Force an operational definition. The impossibility usually dissolves or relocates. |

**Read `references/impossibility-classes.md` now if the problem cites any theorem, physical law, or complexity result** — it contains the premise-attack table for the theorems that are most often misapplied (CAP, FLP, Arrow, Shannon, Carnot, Landauer, halting, no-cloning, Rice), and each one lists the premise real systems escape through.

The single most valuable output of this phase: for a Class-A citation, the sentence *"that theorem forbids W, and we do not need W — we need V, which the theorem does not address."* When you can write that sentence honestly, the wall was never in front of you. When you cannot, say so and go reshape the objective in Phase 0.

### Phase 2 — Build the constraint ledger

List every constraint the current solution operates under, including the ones nobody states aloud. For each, record: what it asserts, who says so, its class, the evidence, what would have to be true for it to be false, and the cost of removing it.

Classes: **Law** (physics, chemistry, conservation) · **Math** (proved) · **Regulatory** (written, has an owner) · **Economic** (price- and volume-dependent) · **State-of-the-art** (best known today, not a bound) · **Organizational** (structure, incentives, skills) · **Habitual** (nobody remembers why).

Two rules make this phase load-bearing:

- **Quantities, not adjectives.** "Expensive" is not a constraint. "Above $40/kg at 10 kt/yr" is. A ledger of adjectives cannot produce a floor in Phase 3, which makes the whole exercise decorative.
- **Chesterton's fence.** For every constraint you propose to remove, state why it was put there. If you cannot find out, that is a research task, not a green light. Constraints that look arbitrary are frequently scar tissue from a failure you are about to repeat.

Only **Law** and **Math** are immovable. Everything else has a price, a timeline, and an owner — which is a very different situation from a wall, and should be written that way.

Format, interrogation questions, and the fence protocol: `references/constraint-ledger.md`.

### Phase 3 — Compute the floor

This is the phase that converts opinion into a number, and it is the one most often skipped.

**The floor is the value your objective's metric would take if only the Class-A and Class-B constraints applied.** Everything between the floor and today is, by construction, someone's design decision.

Depending on the domain, the floor comes from a bill of materials at commodity prices, a thermodynamic minimum (Gibbs free energy of separation, Carnot, Betz, Landauer, Shannon capacity, diffraction limit), an irreducible operation count, the irreducible human decisions in a process, or the best existing proof point in an adjacent field. `references/computing-the-floor.md` gives the technique per domain with worked arithmetic.

Then compute the **gap ratio**: `current ÷ floor`.

| Gap ratio | What it means | What to do |
|---|---|---|
| **< 2×** | Genuinely near the wall | Stop optimizing the mechanism. Go back to Phase 0 and change the objective — that is where the remaining leverage is. |
| **2–10×** | Ordinary engineering slack | Phase 5 DFX passes on the existing architecture will get most of it. |
| **> 10×** | The architecture is the problem | Expect a fundamentally different design to exist. Phase 4 is where the value is. This is the signature of a real opportunity. |

A gap ratio above 10× on a well-studied problem is a strong claim, so check your floor before you believe it. The usual mistake is a floor that quietly omits a real cost — the energy to *get* the material to the reaction, the human review the regulation requires, the retries the network guarantees. Recompute with the omission included before reporting the ratio.

State the ratio with its error bars and its assumptions. A floor you cannot defend is worse than no floor, because it makes everything downstream look quantitative when it isn't.

### Phase 4 — Reconstruct upward from the floor

Now build, using only the invariants. Rules that keep this honest:

- Produce **at least three candidate paths that share no major assumption with the incumbent.** Three variations on today's design is not reconstruction, it is optimization wearing a costume.
- Every path must be **traceable to the ledger**: "this path exists because constraint #7 is Habitual, not Law." A path that isn't traceable came from analogy.
- Apply the **deletion move** before the addition move. Ask of every component, step, and actor: what if it simply did not exist? Delete aggressively, then add back what proves necessary. If nothing you deleted had to come back, you did not delete enough to have learned anything.
- Prefer paths that make the hard case **not arise** over paths that handle the hard case better. Changing the state space beats optimizing within it.

The move catalog — changing the carrier, the location of work, the actor, the timing, the boundary, the state space, the unit of sale — is in `references/reconstruction-moves.md`. Use it when the candidate paths all start looking like the incumbent.

### Phase 5 — Run the DFX passes

Each candidate path now goes through Design-for-X. These are the passes that turn a clever idea into something that can actually exist at scale, and they are where most first-principles work quietly dies.

- **DFC — Design for Cost.** Target cost is a hard input, not an output. Work backwards from the price the market will pay. Question every line of the bill of materials or bill of effort. Costs are designed *in* long before they are spent, so remove them at design time.
- **DFM — Design for Manufacturing / Execution.** Can the organization or machine that must produce this actually produce it? Count the steps, the handoffs, the specialist judgments. Design for automation from the start rather than automating a process shaped for humans.
- **DFS — Design for Simplicity.** Reduce part count and concept count aggressively. Combine functions into single elements. If a part is not necessary, remove it. Complexity added here is paid for on every unit, forever.
- **DFPR — Design for Production Rate.** Throughput is a design variable, not an operational afterthought. Find the bottleneck before it exists, and size the design around the rate rather than the unit.
- **DFV — Design for Verification.** Can you tell whether it is working? An unmeasurable improvement cannot be defended, funded, or debugged. For scientific problems this is not optional: instrumentation is part of the design.
- **DFR — Design for Reversibility.** What does being wrong cost? A path that fails cheaply beats a marginally better path that fails catastrophically, especially under real uncertainty.

Per-domain checklists (hardware, software, business process, scientific program): `references/dfx-passes.md`.

### Phase 6 — Red-team and set kill criteria

A path that has not survived attack is a hypothesis wearing a proposal's clothes.

For each surviving candidate, produce:

**1. The efficient-market check.** Steelman why the world has not already done this. Your answer must be one of:
- *(a)* it is newly possible — name the enabling change and roughly when it happened;
- *(b)* it is possible but needs a capability, asset, or dataset few actors have — name it;
- *(c)* the field is systematically wrong for a nameable structural reason — incentives, measurement, regulation, training;
- *(d)* you cannot answer.

**If the answer is (d), the path is probably wrong.** Say that rather than hiding it. Smart, motivated people have usually been near this problem, and "everyone else missed the obvious" is the least likely explanation on offer.

**2. The kill experiment.** The cheapest test that would falsify the path: what is observed, what result kills it, what it costs, how long it takes. If no experiment could disconfirm the path, it is rhetoric — mark it as such.

**3. What would have to be true.** The list of load-bearing assumptions, sorted by uncertainty × impact. The top item is what to test first.

### Phase 7 — Write it up

Use `assets/report-template.md`. Lead with the answer and the gap ratio, not the journey.

Two outcomes are legitimate and must be stated plainly when they are true:

- **"The objective is the problem."** The floor analysis shows the goal as stated is genuinely near a wall, and the leverage is in wanting something slightly different. This is a valuable finding, not a failure.
- **"It really is impossible as posed."** A Class-A violation with no premise to attack. Say it, name the theorem, and show which reframing of the objective is not blocked.

## This is a dialogue, not a one-shot

The first pass is almost never the good one. Its real function is to surface which assumptions are load-bearing, and that is precisely the thing the user is best placed to correct. Expect the analysis to improve most on the second and third pass, and invite that explicitly rather than presenting pass one as a finished deliverable.

After delivering, offer the push-backs that would sharpen it:

- *"I think constraint #N is actually physics, not habit — here's why."* Then re-derive; if they are right, the floor moves and so does the verdict.
- *"The floor is missing [cost]."* The most common correction, and the one that most changes the gap ratio.
- *"The candidate paths still feel like the incumbent."* A fair hit. Go back to `references/reconstruction-moves.md` and negate a different ledger row — usually one that was skipped because it was uncomfortable.
- *"We tried something like path B in [year] and it failed because…"* The highest-value input available. A graveyard of attempts is data about a constraint that never made it into the ledger. Add it and re-run Phase 6.

When the user pushes back with domain knowledge, **update the ledger and recompute** rather than defending the first answer. The artifact that matters is the ledger and the floor; the candidate paths are downstream of them and cheap to regenerate.

## Calibration rules

These apply throughout, and they are what make the output trustworthy enough to act on.

- **Label every number**: measured, cited (with source), estimated (with derivation), or assumed. Never let an assumption graduate into a fact by being repeated. This one rule prevents most of the damage this kind of analysis can do.
- **Order-of-magnitude estimates are legitimate** and often sufficient. Show the derivation and the error bars; an estimate with a visible derivation can be corrected, a bare number cannot.
- **Missing data gets named, not invented.** Write down the quantity, the plausible range, and where it could be obtained. A fabricated number here poisons every downstream conclusion and is far worse than an admitted gap.
- **A Class-A violation is never a path.** If a candidate needs one, discard it and say which law it breaks.
- **Distinguish "nobody does this" from "nobody has tried this."** They imply very different odds, and the difference is usually findable.
- **Confidence tracks evidence, not elegance.** A beautiful reconstruction with no floor computation and no kill experiment is a blog post.

## Anti-patterns

- **Analogy in first-principles clothing.** "It's the Uber of X" is reasoning from a solved case, which is exactly what the protocol is meant to bypass.

  The reliable tell is a sentence that appeals to convention and looks like a reason. If any of these appears in your own output — or goes unchallenged in the user's framing — the ledger is not finished:

  > "industry standard is…" · "best practice says…" · "competitors do it this way…" · "we've always done it like this" · "experts recommend…" · "that's just how it works" · "it's common knowledge that…"

  None of these is a reason; each is a citation of a crowd. For every one, ask **"but why — what fundamental truth makes this necessary?"** If the answer isn't physics, mathematics, or a rule with a named author, the constraint is movable and belongs in the ledger as such.

- **Attacking a theorem head-on.** Class-A results are not defeated by determination. The premise is the door; the theorem is the wall.
- **Removing fences without reading them.** A constraint whose origin you did not find is a constraint you did not evaluate.
- **Questioning only the cheap constraints.** If the ledger contains nothing that hurts to challenge, it is incomplete.
- **Twenty ideas instead of three with kill criteria.** Volume is the tell for a reconstruction phase that never touched the ledger.
- **Stopping at the reframe.** The reframe feels like the insight. The floor and the experiment are the insight.
- **Skipping Phase 3 because the domain "isn't quantitative."** Business processes have irreducible decision counts; research programs have irreducible measurement counts. If you truly cannot bound it, say why — that itself is a finding.

## Bundled references

Load these as the problem requires rather than upfront — each is written to be read on its own.

| File | Read it when |
|---|---|
| `references/impossibility-classes.md` | Any theorem, physical law, or complexity result is cited as the wall |
| `references/constraint-ledger.md` | Phase 2 — ledger format, interrogation questions, Chesterton's fence protocol |
| `references/computing-the-floor.md` | Phase 3 — floor techniques per domain, with worked arithmetic |
| `references/reconstruction-moves.md` | Phase 4 — the move catalog, when candidates keep resembling the incumbent |
| `references/dfx-passes.md` | Phase 5 — per-domain DFX checklists |
| `references/worked-examples.md` | You want to see the whole protocol run end to end before running it |
| `assets/report-template.md` | Phase 7 — the deliverable structure |
