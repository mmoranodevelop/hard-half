# Impossibility classes and how to attack each one

Read this whenever a theorem, physical law, or complexity result is offered as the reason something cannot be done. Getting the class right determines the entire attack; getting it wrong produces either crackpottery or premature surrender.

**Contents**
- [The six classes](#the-six-classes)
- [Class A — attacking the premise, not the theorem](#class-a--attacking-the-premise-not-the-theorem)
- [The premise-attack table](#the-premise-attack-table)
- [Walls with no door](#walls-with-no-door)
- [Class B — complexity bounds](#class-b--complexity-bounds)
- [Classes C through F](#classes-c-through-f)
- [Diagnostic questions](#diagnostic-questions)

---

## The six classes

| Class | Meaning | Signature phrase | Attack |
|---|---|---|---|
| **A — Proven** | Violates a theorem or conservation law | "thermodynamics forbids it", "CAP says you can't" | Find the premise your problem doesn't need |
| **B — Complexity-bounded** | Hard in the worst case | "it's NP-hard", "combinatorial explosion" | Worst case ≠ your case |
| **C — Empirically unachieved** | No proof, just nobody has done it | "nobody has ever managed it" | Full protocol; this is the target |
| **D — Economically unattractive** | Works, doesn't pay | "the numbers don't work" | Attack the cost stack, scale, buyer, bundling |
| **E — Institutionally blocked** | Rules, incentives, org shape | "compliance will never allow it" | The constraint has an owner — model the owner |
| **F — Definitionally impossible** | The words hide a contradiction | "make it fully secure" | Force an operational definition |

Most real problems are a **mixture**, and the mixture is the finding. A stalled program is typically one Class-A citation used as cover for a Class-D economics problem and a Class-E ownership problem. Separating those three is often the entire value of the analysis, because they have three different fixes and the organization has been buying only one.

---

## Class A — attacking the premise, not the theorem

A theorem is a conditional: *given premises P₁…Pₙ, conclusion C is impossible.* People remember C and forget P.

The attack is never "the theorem is wrong." It is:

> **That theorem forbids W under premises P. We do not need W — we need V. And premise Pₖ does not hold for us.**

If you can write that sentence honestly, the wall was never in front of you. If you cannot, the wall is real and you should go reshape the objective instead.

The three doors, in order of how often they work:

1. **You don't need the forbidden thing.** The theorem forbids something stronger than your objective requires. This is by far the most common case in enterprise contexts — the theorem is invoked against a goal it never addressed.
2. **A premise doesn't hold for you.** The theorem assumes a model (fully asynchronous, adversarial, arbitrary inputs, general programs) that your situation does not match.
3. **The bound is not the binding constraint.** The theorem's limit is real but orders of magnitude away from where you actually are, so it is not what is stopping you. Verify this numerically — it is remarkably common.

---

## The premise-attack table

Each row: what the theorem actually forbids, the premise most often false in practice, and the escape it enables.

### CAP (Gilbert & Lynch, 2002)

- **Forbids**: a linearizable read/write register that stays available on *every* non-failing node during a network partition.
- **Vulnerable premises**: that you need linearizability for *all* operations; that "available" means every node answers; that all data has one consistency class; that partitions are the common case.
- **Escapes**: per-operation consistency classes (strong where an invariant depends on it, causal or eventual elsewhere); quorum systems that sacrifice only the minority side; CRDTs and monotonic logic (**CALM theorem**: a program has a coordination-free consistent implementation exactly when it is monotonic); escrow and reservation patterns that convert a global invariant into independently checkable local ones; PACELC's observation that outside partitions the real trade is latency vs consistency, which is a tuning decision rather than a wall.
- **The sentence**: *CAP forbids linearizable-and-fully-available during a partition. We need bounded staleness plus preserved invariants, which CAP does not forbid.*

### FLP (Fischer, Lynch & Paterson, 1985)

- **Forbids**: a **deterministic** consensus protocol that **guarantees** termination in a **fully asynchronous** system with even one crash failure.
- **Vulnerable premises**: determinism; full asynchrony; guaranteed (rather than probability-1) termination.
- **Escapes**: randomization terminates with probability 1 (Ben-Or); partial synchrony (Dwork, Lynch & Stockmeyer) and failure detectors (Chandra & Toueg) restore termination; Paxos and Raft keep safety unconditionally and liveness under eventual synchrony. Every production consensus system lives inside this escape.
- **The sentence**: *FLP forbids deterministic guaranteed termination. We need safety always and liveness under normal conditions, which is achieved daily.*

### Arrow's impossibility theorem (1951)

- **Forbids**: a **ranked** voting rule over ≥3 alternatives satisfying unrestricted domain, Pareto, independence of irrelevant alternatives, and non-dictatorship.
- **Vulnerable premise**: that preferences are **ordinal only**. Arrow is a theorem about rankings.
- **Escapes**: cardinal or graded methods (approval, score) fall outside Arrow's scope entirely — though Gibbard–Satterthwaite still constrains strategyproofness, so check which property you actually need. Restricted domains also escape: single-peaked preferences give the median-voter result (Black).
- **Generalizes to**: any prioritization, scoring, or resource-allocation scheme built on ranked stakeholder preferences — a very common enterprise shape.

### Shannon capacity

- **Forbids**: error-free rate above `C = B·log₂(1 + S/N)` over a given channel.
- **Vulnerable premises**: fixed bandwidth, fixed SNR, one channel, and — most importantly — that those bits must be sent at all.
- **Escapes**: MIMO creates parallel spatial channels (it obeys Shannon, on a different channel); more bandwidth or better SNR; and the big one, **reduce the information that must cross the channel** — source coding, caching, prediction, sending the delta or the query result rather than the data.
- **The general lesson**: Shannon bounds bits over a channel. It says nothing about whether you need those bits.

### Carnot efficiency

- **Forbids**: a **heat engine** between reservoirs exceeding `η = 1 − Tc/Th`.
- **Vulnerable premise**: that your device is a heat engine.
- **Escapes**: fuel cells and photovoltaics convert chemical or radiant energy directly and are not Carnot-bounded. Heat pumps move heat rather than convert it, so COP > 1 is routine and not a violation. Within heat engines: raise Th, lower Tc, or cascade cycles.

### Landauer limit

- **Forbids**: erasing one bit for less than `kT ln 2` (≈2.8 zJ at 300 K).
- **Vulnerable premise**: that the operation is **logically irreversible**.
- **Escapes**: reversible computing (Bennett) has no such floor; adiabatic circuits approach it.
- **But check first**: current CMOS runs several orders of magnitude above Landauer. If someone cites it as the reason your compute cost cannot fall, they have cited a bound you are nowhere near. This is the canonical "not the binding constraint" case — verify with arithmetic before conceding.

### Halting problem and Rice's theorem

- **Forbids**: deciding, **for all programs**, whether one halts, or any non-trivial semantic property.
- **Vulnerable premise**: "for all programs."
- **Escapes**: restricted languages (total, terminating by construction); decidable fragments; bounded model checking; sound-but-incomplete analysis that answers yes / no / **don't know**. Working static analyzers exist because a three-valued answer was acceptable all along.

### NP-hardness

Treated as Class B below — it is the most commonly misused impossibility in business contexts.

### No-cloning theorem

- **Forbids**: an exact copy of an **arbitrary unknown** quantum state.
- **Vulnerable premises**: arbitrary, unknown, exact.
- **Escapes**: known states copy freely; approximate cloning is possible with bounded fidelity; teleportation relocates a state at the cost of destroying the original.

### Diffraction limit (Abbe)

- **Forbids**: resolving features below roughly `λ/2NA` in **conventional far-field linear** imaging.
- **Vulnerable premises**: far-field, linear response, no prior knowledge of the sample.
- **Escapes**: STED, PALM and STORM use nonlinearity or stochastic localization to beat it (Nobel Prize in Chemistry, 2014); near-field probing; immersion to raise NA; shorter wavelength.
- **Why it matters here**: this is the best example of a century-old "fundamental limit" that fell to a premise attack rather than better lenses.

### Amdahl's law

- **Forbids**: speedup beyond `1/s` for serial fraction `s`, at **fixed problem size**.
- **Escape**: Gustafson's observation that problem size usually scales with the machine, which changes the conclusion entirely.

### Nyquist–Shannon sampling

- **Forbids**: reconstruction below 2× bandwidth for a **general band-limited** signal.
- **Vulnerable premise**: generality. Compressed sensing exploits sparsity to reconstruct from far fewer samples.

### Gödel incompleteness

- **Forbids**: a consistent, effectively axiomatized system strong enough for arithmetic proving all its truths.
- **Reality check**: this almost never binds on an engineering problem. Weaker systems can be complete and decidable (Presburger arithmetic), and the statements you care about are generally provable. Treat a Gödel citation in a business context as a rhetorical move, not a constraint.

---

## Walls with no door

Calibration matters as much as ambition. These have no premise attack, and a candidate solution requiring one is simply wrong:

- **Conservation of energy.** No net energy from nothing. No over-unity device.
- **Second law of thermodynamics.** No isolated-system entropy decrease; no perpetual motion of the second kind; no free work from a single reservoir.
- **Conservation of momentum.** No reactionless drive.
- **Relativistic causality.** No superluminal signalling. (Entanglement transmits no information — the no-communication theorem is itself a Class-A wall.)
- **Information-theoretic security bounds.** No lossless compression of arbitrary data (counting argument); no key shorter than the message for perfect secrecy.

When you meet one, the correct move is not to circumvent it but to **relocate the objective**. Nobody needs energy from nothing; they need a lower cost per unit of delivered service. That objective is not blocked. Perform the relocation explicitly in Phase 0 and state what was traded away.

---

## Class B — complexity bounds

"It's NP-hard" is the most over-applied impossibility in enterprise work. The claim is precise and narrow: **no known algorithm solves the worst case exactly in polynomial time.** Four premises hide in there.

| Premise | Attack | What it looks like in practice |
|---|---|---|
| **Worst case** | Real instances carry structure | Industrial SAT instances with millions of variables solve in seconds; the hard instances are constructed, not encountered |
| **Exact optimum** | Approximation with a guarantee | A 5%-of-optimal answer in a second usually beats an exact answer in a week — confirm which the business needs |
| **General instances** | Parameterized complexity | Exponential in a parameter `k` that is small in your data, polynomial in `n` (FPT) |
| **Asymptotic** | Your `n` is fixed and finite | An `O(2ⁿ)` algorithm at `n = 30` runs fine; asymptotics describe growth, not your instance |

Before accepting an NP-hardness objection, ask: *what is the actual distribution of instances, what is the actual `n`, and does anyone need the true optimum — or do they need to beat the incumbent by a stated margin?* Answering those three questions dissolves most of these objections.

---

## Classes C through F

**Class C — empirically unachieved.** No proof forbids it; nobody has done it. The most valuable class, and where the rest of the protocol earns its keep. Key discipline: separate *nobody has succeeded* from *nobody has tried*. Search for failed attempts before concluding it is virgin territory — a graveyard of attempts is data about the constraint you have not yet modelled.

**Class D — economically unattractive.** Physically fine, does not pay at current prices and volumes. Ask: does it pay at a different scale? For a different buyer? As a byproduct of something already being done? If the input price trend continues five years? If the cost is amortized differently? Many Class-D problems are Class-D only at today's operating point, and the analysis is about identifying which operating point flips it.

**Class E — institutionally blocked.** Regulation, liability, standards bodies, procurement, incentives, org structure (Conway's law makes architecture follow communication structure). These constraints are genuinely binding, but unlike physics they have an **owner**, a **change process**, and a **cost**. Model those three. Note the common trap: an institutional constraint gets reported as a technical one because the technical framing is less politically costly to state.

**Class F — definitionally impossible.** "Fully secure", "bias-free", "provably correct AI", "eliminate all risk". These are unmeasurable as stated, so no solution can satisfy them and no effort can be shown to have helped. Force the operational definition: *secure against which adversary with which budget; fair by which of the mutually incompatible fairness criteria; correct with respect to which specification.* Sometimes the impossibility dissolves. More often it relocates onto a real, tractable, and now measurable question — which is still a large win.

---

## Diagnostic questions

Run these when the class is unclear:

1. **Is there a proof, or a track record?** A proof is Class A or B. A track record of failure is Class C — and worth reading carefully.
2. **Who benefits from this being impossible?** If someone does, suspect Class E dressed as Class A.
3. **At what price does it become possible?** If the answer is a number, it is Class D, not an impossibility.
4. **What exactly is forbidden — in one sentence, with quantities?** If nobody can state it, suspect Class F.
5. **When was the impossibility established, and what has changed since?** Constraints have expiry dates: a cost that fell 100×, a material that became available, a computational capability that did not exist.
6. **Does the objective actually require the forbidden thing?** The most productive question in this document, and the one asked least.
