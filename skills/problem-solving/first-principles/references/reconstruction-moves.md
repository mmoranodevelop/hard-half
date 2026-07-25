# Reconstruction moves

Phase 4. You have a floor and a ledger. Now build candidate solutions upward using only the invariants.

Use this catalog when the candidates keep coming out looking like the incumbent — which is the normal failure, because the incumbent design is the most available pattern in anyone's head, including yours.

**The rule that governs all of them:** every move must be traceable to a specific ledger row. "This path exists because constraint #7 is Habitual, not Law." A move you cannot trace came from analogy, and analogy is what the protocol exists to bypass.

---

## The deletion move — do this first

Before adding anything, remove. Deletion is the only move that improves cost, complexity, throughput, and reliability simultaneously, which is why it comes first and why it is under-used: it produces no artifact to point at.

Ask of every component, step, actor, approval, field, and report: **what if this simply did not exist?**

The discipline that makes it work:

1. Delete aggressively — past the point of comfort.
2. Add back only what proves necessary, and only when its absence causes an observed failure rather than an imagined one.
3. **If nothing you deleted had to come back, you did not delete enough to have learned anything.** The purpose is to find the true boundary of necessity, and you only find it by crossing it.

Watch for the requirement that exists because a *person* asked for it. Requirements arrive without an owner and are then treated as physics. Every requirement should have a name attached to it, and that name should be askable.

The related move: **question the requirement before optimizing the thing that satisfies it.** Enormous effort goes into efficiently satisfying requirements that should not exist. A perfectly optimized unnecessary step is still waste.

---

## The substitution moves

Each changes one dimension of the current design while holding the objective fixed. Run them in order; they are roughly ordered by how often they produce something.

### 1. Change the carrier

Matter → energy → information, in any direction.

Can the thing be moved as information rather than matter? Manufactured at the point of use rather than shipped? Computed rather than measured? Measured rather than computed? Stored as a rule instead of as data?

*Signals it applies*: a large fraction of cost is transport, storage, or duplication.

### 2. Change where the work happens

Centralize, distribute, push to the edge, pull to the core, move it into the supplier, move it into the customer.

The same operation has wildly different costs depending on where it runs — because the cost of getting the inputs there differs, not the operation. Ask where the inputs already are, and move the work to them.

*Signals it applies*: data or material moves a long way to meet a process that could have met it.

### 3. Change who does it

Human → machine, expert → novice with a better tool, employee → customer, internal → supplier, one specialist → many generalists.

Not automation for its own sake: the question is whether the task requires the judgment of whoever performs it. A task done by an expert because it was *once* hard is a common and expensive residue.

*Signals it applies*: the floor computation shows few irreducible decisions but many expensive people.

### 4. Change when it happens

Batch ↔ continuous. Precompute ↔ compute on demand. Synchronous ↔ asynchronous. Just-in-time ↔ just-in-case. Prevent ↔ detect and repair.

Timing changes cost structure more than almost anything else, because it changes what must be held ready — inventory, capacity, buffers, staff, capital.

*Signals it applies*: large buffers, idle capacity sized for peaks, long queues, or the theoretical-cycle-time ratio being enormous.

### 5. Change the boundary

Integrate two steps into one and the interface between them disappears. Split one into two and each can be optimized independently, or bought from someone who is better at it.

Vertical integration is the classic version: if the input's price is dominated by a supplier's margin or a supplier's own inefficiency, and the volume justifies it, the make-versus-buy line moves. The floor computation tells you whether it does.

*Signals it applies*: a large gap ratio concentrated in one purchased input, or a handoff that generates most of the defects.

### 6. Change the state space

**Make the hard case not arise**, rather than handling it better.

This is the highest-leverage move in the catalog and the least intuitive, because it does not look like work on the problem. Restructure so the expensive situation is unreachable: make the invalid state unrepresentable, make the conflict impossible by construction, choose a data layout where the slow query has no reason to exist, define the contract so the ambiguous case cannot be submitted.

*Signals it applies*: substantial machinery exists to handle a case that a different structure would not produce.

### 7. Change the unit of sale or the unit of value

Sell the outcome instead of the artifact. Charge per use instead of per unit. Sell the capability, the availability, the result.

This changes who bears which cost and which risk, and therefore changes which design is optimal. A Class-D "economics don't work" verdict is frequently a verdict about the *current* unit of sale rather than about the technology.

*Signals it applies*: the technology works, the buyer will not pay, and the value is real but lands on someone other than the payer.

### 8. Change the scale

Both directions. Some floors are only reachable at volume — capital amortization, dedicated process, purpose-built supply. Others are only reachable when small — no coordination overhead, no shared infrastructure, no compliance regime that triggers above a threshold.

*Signals it applies*: a cost stack dominated by fixed costs (go bigger) or by coordination and compliance (go smaller).

### 9. Change the specification tolerance

Which requirements are thresholds and which are smooth? Thresholds are almost always policy, and policy has an author. A tolerance loosened by 10% sometimes removes an entire process stage; a tolerance tightened by 10% sometimes removes an entire inspection regime downstream.

*Signals it applies*: a single specification drives a disproportionate share of the cost stack — which the floor computation will have made visible.

### 10. Exploit the newly possible

Something changed recently that the incumbent design predates: a cost curve that fell an order of magnitude, a material that became available, a capability that did not exist, a regulation that opened.

Designs encode the constraints of their birth year and rarely get re-derived. Ask explicitly: *what would this look like if designed today, knowing nothing about how it is done now?* Then ask what specifically changed, and when — because that date is the answer to the Phase 6 efficient-market check.

*Signals it applies*: the architecture is more than a few years old and its era's binding constraint has since relaxed.

---

## Generating genuinely distinct paths

Three candidates that share the incumbent's core assumption are one candidate. To force real distinctness:

- Pick the **three most load-bearing rows** in the ledger. Build one path that negates each. If negating a row produces nothing, that row was not load-bearing and the ledger needs another look.
- Build one path that **an entrant with no legacy** would build. They inherit no Habitual or Organizational rows — write down what they simply would not have.
- Build one path that **optimizes a different one of the objective's terms**, in case the current framing has been optimizing the wrong one all along.
- Build one path that reaches only **50% of the target but at 5% of the complexity.** Frequently the actual answer, and almost never generated unless explicitly requested.

Then check: if two paths would fail for the same reason, they are the same path. Replace one.

---

## Before leaving Phase 4

For each candidate:

- [ ] Traceable to specific ledger rows
- [ ] Violates no Law or Math row (check against `impossibility-classes.md`)
- [ ] Its position relative to the floor is stated — how much of the gap does it actually close?
- [ ] It differs from the incumbent in an assumption, not merely in parameters
- [ ] Its own new constraints are written down; every architecture buys relief in one place by paying somewhere else, and the payment is what Phase 5 and Phase 6 will interrogate
