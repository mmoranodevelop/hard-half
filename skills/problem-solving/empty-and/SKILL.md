---
name: empty-and
description: >-
  Prove or kill the claim that several locally-working solutions can coexist:
  write each constraint as a set of allowed values, find the empty AND — the
  smallest pair or n-tuple whose intersection is empty — and name which
  constraint must be dropped, relaxed, or sequenced in time. Use when every
  workstream is green but the whole cannot ship, requirements contradict after
  pairwise review, they want it fast AND cheap AND custom AND compliant, or two
  successful designs cannot share a resource. NOT first-principles (one floor
  on one objective). NOT interdependency-map (schedule couplings across
  projects). NOT issue-tree (why is X down). NOT make-vs-buy. NOT a
  requirements brainstorm: the output is the empty intersection, or an
  exhibited point that proves the AND is nonempty.
license: MIT
---

# Empty And

## The greens can be impossible together

The default agent solves workstreams in parallel and staples the status. Each constraint is locally satisfiable. The **AND** of them is empty: there is no single world in which they are all true at once.

The leading word is **AND**. The work is to exhibit emptiness — the smallest set of constraints with empty intersection — or to exhibit one point in the intersection. "These might conflict" is the default. A named empty tuple, and a drop / relax / sequence, is not.

This is not `first-principles`. That computes a floor for one objective. This asks whether N successful local solutions can be true in the same world. It is not `interdependency-map`: that owns schedule couplings and unblocks. An empty AND can have a perfect Gantt and still be a logical or physical contradiction. It is not `issue-tree`: that diagnoses a down metric.

## When to stop

- One stuck objective, physics or cost floor → `first-principles`
- Cross-project dates and owners, not logical emptiness → `interdependency-map`
- Why is X down → `issue-tree`
- Build vs buy a capability → `make-vs-buy`
- The stated bundle of requirements may itself be a ghost ticket → `ghost-problem`
- Adaptive opponent, not incompatible constraints → `red-queen`
- Implementation of an already-compatible design
- Two load-bearing intake facts still blank after one ask → issues list, stop

## Mode

| Mode | When | Output |
|---|---|---|
| **Prove-empty** | Default. Greens that cannot ship together, or an AND-list of requirements | Empty tuple + drop/relax/sequence + one ASK |
| **Prove-nonempty** | They claim coexistence; you must exhibit a point | One concrete point in the intersection, or the empty tuple you found instead |
| **Sequence** | Emptiness is only simultaneous; time can reopen the set | The order, what is false in each window, what never becomes jointly true |

Infer. Ask only when Prove-empty and Sequence are equally live.

## Protocol

### 0. Intake — write constraints as sets

Load-bearing (two missing after one round → refuse):

1. The list of constraints they want jointly true (names they actually use)
2. For each, what values are **allowed** — a set, not a slogan ("fast" is not a set; "P95 < 200ms on workload W" is)

Also collect: which are already "green" locally; whether they must hold at the same time or may be sequenced; the resource that might be shared (budget, team, spectrum, lock, API, legal entity).

If a constraint cannot be written as a set after one ask, mark it **unlocked** and it cannot enter an AND. Unlocked slogans are how emptiness hides.

Read `references/intersection-method.md` **now** if there are more than four constraints, if any is still a slogan, or if they already said "we can do all of it." It holds how to write sets, pairwise vs n-way, and what counts as an exhibited point.

> **Done when:** every constraint in the AND is a set or is marked unlocked-and-excluded.

### 1. Intersect

Pairwise first. Then any n-way the pairs did not catch (three-way emptiness is real: A∩B, B∩C, A∩C nonempty, A∩B∩C empty).

Name the **smallest empty tuple** — the fewest constraints whose AND is empty. Larger lists that contain it are not additional findings; they are the same emptiness with decorations.

If every intersection you can compute is nonempty, you are not done: exhibit **one point** (a toy world is enough) that sits in all the sets at once. "Looks compatible" is not a point.

> **Done when:** either a smallest empty tuple is named, or one exhibited point is on the page.

### 2. Drop, relax, or sequence

Only these exits, and only on members of the empty tuple:

| Exit | Honest form |
|---|---|
| **Drop** | Constraint X is out. Who loses, what they will do |
| **Relax** | X's set enlarges by a named amount. Who pays the enlargement |
| **Sequence** | Not simultaneous. Window 1: these true, that false. Window 2: the reverse. What remains forever empty |

Fighting for the full AND after emptiness is exhibited is how programs stay green until the cutover.

If you sequenced, say what never becomes jointly true. Sequencing is not magic coexistence; it is taking turns.

> **Done when:** every member of the empty tuple has drop, relax, or sequence — or you exhibited a point and the AND stands.

### 3. ASK

Exactly one: `drop X` / `relax Y by Z` / `sequence A then B` / `exhibit a point` / `keep fighting` (allowed only if you name the empty tuple on the same line — eyes open). Owner, date.

Use `assets/one-pager.md` for the page.

Read `references/worked-examples.md` if they want a both-and, or if every workstream is green.

> **Done when:** the page has sets, the empty tuple or an exhibited point, one exit per member of the tuple (or nonempty proof), one ASK — and no stapled greens.

## Anti-patterns

- **Slogan-AND.** "Fast, cheap, good" with no sets.
- **Pairwise-only.** Missed a three-way empty.
- **Gantt-as-proof.** A schedule of impossible things is still empty.
- **Decorated tuple.** Eight constraints listed; the empty pair is buried.
- **Fake point.** A world that violates one set, labelled "compromise."
- **Floor-mix-up.** Computing how cheap one objective could be, not whether N can coexist.

## Bundled references

| File | Read it when |
|---|---|
| `references/intersection-method.md` | More than four constraints, slogans still on the list, or they said they can do all of it |
| `references/worked-examples.md` | They want a both-and, or every workstream is green |
| `assets/one-pager.md` | You are writing the deliverable |
