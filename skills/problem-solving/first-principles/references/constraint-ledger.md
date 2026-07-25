# The constraint ledger

Phase 2. The purpose is to make every constraint on the current solution explicit, classified, and priced — so that Phase 3 can compute a floor and Phase 4 knows which walls are actually made of paper.

The ledger is the single highest-value artifact in the protocol. Teams routinely discover that the constraint they had organized a decade of work around was written down by someone who left, for a reason that expired.

---

## The format

One row per constraint. Prose does not work here — the discipline comes from being forced to fill every column.

| # | Constraint (with quantities) | Asserted by | Class | Evidence | False if… | Cost to remove |
|---|---|---|---|---|---|---|
| 1 | Reconciliation must complete within the 6h overnight window | Ops runbook, 2019 | Habitual | None found; window predates the current settlement API | Settlement API supports intraday posting (it does since 2023) | ~0 — requires scheduling change only |
| 2 | Every transaction requires dual human approval above €10k | AML policy §4.2 | Regulatory | Written policy, external auditor sign-off | Regulator accepts model-based review with audit trail | 6–9 months, legal + regulator engagement |
| 3 | Separation energy ≥ 0.9 kWh/kg | Thermodynamics | Law | Gibbs free energy of mixing at this concentration | Never (at this concentration and temperature) | Immovable — change the concentration instead |

Three columns do the real work:

- **Quantities**, not adjectives. "Slow" is unusable. "Above 6 hours end-to-end" can be tested, bounded, and designed against. A ledger of adjectives cannot produce a floor, which makes the entire exercise decorative.
- **Asserted by**, because a constraint with no author is usually not a constraint. Tracing authorship is the cheapest way to discover that the "requirement" was one person's preference in a meeting.
- **False if…**, because it converts a wall into a testable proposition. This column is what makes Phase 6's kill experiments writable.

---

## The seven classes

Ordered from immovable to free.

| Class | Definition | Test | Movability |
|---|---|---|---|
| **Law** | Physics, chemistry, conservation | Would violating it violate a conservation law? | None. Design around it. |
| **Math** | Proved theorem | Is there a proof, and do its premises hold here? | None — but see the premise attack in `impossibility-classes.md` |
| **Regulatory** | Written rule with force | Can you cite the article? | Slow, expensive, has an owner and a process |
| **Economic** | Price- and volume-dependent | At what price does it stop binding? | Moves with scale, technology, and time |
| **State-of-the-art** | Best known today | Is there a proof it is optimal? Usually not. | Moves with effort — this is where R&D lives |
| **Organizational** | Structure, skills, incentives | Would a different org shape dissolve it? | Moves, painfully, on human timescales |
| **Habitual** | Nobody remembers why | Can anyone state the original reason? | Often free — and often load-bearing anyway |

Only **Law** and **Math** are walls. Everything else has a price, a timeline, and an owner. Writing them all as "constraints" is what makes problems look impossible: it flattens a $50k scheduling change and the second law of thermodynamics onto the same line.

Two classification errors to watch for, because both are systematic:

- **Upgrading.** Economic and Organizational constraints get reported as Law, because "physics forbids it" ends a conversation that "we chose this and it would be awkward to change" does not.
- **Downgrading.** Regulatory and Law constraints get dismissed as Habitual by someone enthusiastic about a reconstruction. This produces confident proposals that are illegal or impossible.

---

## Chesterton's fence

Before removing any constraint, find out why it is there.

> A fence across a field with no visible purpose should not be removed until you know why it was built.

Operationally, for each constraint you propose to remove:

1. **Find the origin.** Commit history, meeting notes, the policy's revision log, the person who wrote it. Timebox this — an hour is usually enough to find either the reason or the absence of one.
2. **Write the original reason down**, in the terms of the time. Constraints are usually rational responses to conditions that no longer hold.
3. **Test whether the condition still holds.** This is the actual question. A retry limit set when the downstream API had a 2 rps quota is not a constraint once the quota is 2000 rps — but it *is* still a constraint if nobody renegotiated the quota.
4. **If you cannot find the reason, that is a research task, not permission.** An unexplained constraint has roughly even odds of being scar tissue from an incident nobody documented. Removing it blindly is how the incident recurs.

The inverse failure is just as expensive: treating every fence as sacred means the ledger never moves, and the problem stays impossible for reasons nobody can defend. The standard is *reason found and evaluated*, not *reason exists*.

---

## Interrogation questions

Use these to surface constraints nobody wrote down. Unstated constraints are where the value is — stated ones have already been optimized against by everyone in the field.

**On the constraint itself**
- What exactly happens if this is violated? By how much, at what cost?
- Is this a hard threshold or a smooth penalty? Thresholds are usually policy; smooth penalties are usually physics.
- Who would notice if it changed by 10%? By 10×?
- When was it last checked against reality?

**On origin**
- Who decided this, and when?
- What was true then that may not be true now — prices, volumes, technology, regulation, team size?
- Was it derived, or copied from a prior system?
- Is it a constraint, or the residue of a solution to a different problem?

**On the boundary**
- Is this a constraint on the *problem*, or on the *current solution*? (The most useful question in the list. Most entries turn out to be the latter.)
- Would a different actor face this constraint? A different jurisdiction? A different scale?
- Does it apply to all cases, or has one case's constraint been generalized to all of them?

**On what is missing**
- What does everyone in this field assume that an outsider would question?
- What is never discussed because it is obvious? (Obvious assumptions are unexamined by definition.)
- What did the last three failed attempts have in common? That commonality is a constraint nobody listed.
- If a competitor with no legacy system entered tomorrow, which of these rows would they simply not have?

That last question is the fastest route to a good ledger. A greenfield entrant inherits none of the Habitual and Organizational rows, and enumerating what they would skip tells you precisely which constraints are self-imposed.

---

## Completeness check

The ledger is done when:

- [ ] Every row has quantities, not adjectives
- [ ] Every row has an asserting source, or is explicitly marked "no source found"
- [ ] Every row is classified, and the Law/Math rows have their premises checked against `impossibility-classes.md`
- [ ] At least one row is uncomfortable to challenge — if not, the ledger is incomplete and you have only questioned the cheap constraints
- [ ] Every constraint you intend to remove has its fence read
- [ ] The rows sum to something: you can now say what the solution costs *given* these constraints, which is the input to Phase 3
