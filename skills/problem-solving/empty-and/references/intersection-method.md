# Intersection method

A constraint enters the AND only as a **set of allowed values**. Slogans stay out until they are sets.

## Writing a set

A set has a **space** (what kind of thing is being chosen) and a **cut** (which of those things are allowed).

| Slogan | Not a set | A set |
|---|---|---|
| Fast | — | P95 latency on workload W < 200ms |
| Cheap | — | Fully-loaded monthly cost ≤ €X at volume V |
| Compliant | — | Satisfies control C as audited by party P this year |
| Custom | — | Per-tenant schema allowed to diverge |
| Realtime | — | End-to-end delay < 50ms including the slowest dependency |

If two constraints live in different spaces, you must say how they meet (they share a resource, a lock, a person, a legal entity, a time window). Unrelated sets do not AND until you name the shared world they inhabit. The shared world is often "one shipped system, one budget, one night of cutover."

Unlocked = excluded from the AND. Write it on the page so nobody pretends it was checked.

## Pairwise then n-way

For n constraints, pairwise is n(n-1)/2 checks. Do them. Most emptiness is a pair.

Then check for **three-way (and higher) emptiness**: every pair nonempty, the triple empty. Classic shape: three designs each pairwise compatible on a shared resource whose capacity holds two but not three.

You do not need a formal proof assistant. You need a reason the intersection has no element: a conservation law, a mutex, a legal exclusivity, a budget identity, a single-threaded person, a spectrum that cannot be split, a consistency requirement that forbids the combination.

If you cannot name the reason, you do not yet have emptiness — you have a suspicion. Either find the reason or exhibit a point.

## What counts as an exhibited point

One concrete world: named values for every constraint's space, each value inside that constraint's set, all at the same time (or in the sequenced windows you claim).

A toy world counts. "System S with two tenants, P95 180ms on W, cost €X, control C held by P" is a point. "A balanced approach" is not.

The point may be ugly. Ugliness is not emptiness.

## Sequence vs coexistence

If emptiness holds only when the constraints are simultaneous, sequence can reopen sets. Write the windows. In each window, name what is *false*. If after all windows some pair is still never co-true, say so — that pair is still empty in the project's life, just not in a single instant.

Do not label a sequence "we get all of it."
