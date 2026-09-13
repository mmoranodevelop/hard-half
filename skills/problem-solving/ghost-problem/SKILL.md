---
name: ghost-problem
description: >-
  Find whether the stated problem is a ghost — a proxy metric, a war that
  already ended, a political artifact, a symptom whose parent would kill it,
  or an inherited slogan nobody can justify — and either prove the stated
  problem is load-bearing or name the problem whose death would make this one
  evaporate. Use when a fix shipped and nothing changed, the team has worked
  the same ticket for months, the "real problem" keeps sliding, they inherited
  a problem nobody can source, or they ask whether they are solving the wrong
  problem. NOT for issue-tree (that decomposes a governing question you already
  accept). NOT for jobs-to-be-done (customer hire/fire). NOT for
  first-principles (the objective is real; the mechanism is stuck). NOT for
  value-problem-solver (worth building). NOT a brainstorm of alternative
  framings: a ghost dies on a test or the stated problem stands.
license: MIT
---

# Ghost Problem

## The stated problem is the first suspect

The default agent solves the problem as typed. That is correct when the typed problem is load-bearing. It is how you burn a quarter when the ticket is a **ghost**: a problem whose perfect solution would not change anyone's Monday, or whose death is implied by solving something else.

The leading word is **ghost**. Nothing is implemented against the stated problem until the ghost either dies on a test or the stated problem stands. Reframing as a creative exercise is not the job. The job is a verdict with a kill test.

This is not `issue-tree`. That skill accepts a governing question and splits it. This one asks whether the governing question should exist. It is not `first-principles`: that attacks a real stuck objective. It is not `value-problem-solver`: that asks who pays. A ghost can be valuable to someone (a coalition, a dashboard) and still be the wrong problem to solve.

## When to stop

- The objective is real, stuck on a floor or mechanism → `first-principles`
- They have not even named a question, only a topic → `issue-tree` first, then come back if the question itself looks hollow
- Customer hire/fire, what to stop building → `jobs-to-be-done`
- Worth building / capture vs create → `value-problem-solver`
- One official unsolved claim to lock and verify → `verified-hard-problem`
- Every option on the table is the same option written differently → `missing-axis` (wrong *space*, not wrong problem)
- Implementation, debugging, or a known best practice
- Two load-bearing intake facts still blank after one ask → issues list, stop

## Mode

| Mode | When | Output |
|---|---|---|
| **Hunt** | Default. A named ticket, a sliding "real problem", a shipped fix that changed nothing | Ghost class + parent or load-bearing verdict + confirmation test + one ASK |
| **Confirm** | They already named a suspected parent / decoy | The test that would kill the suspicion, then the verdict |
| **Dissolve** | Origin check shows the war ended | Stop-work sentence. No new solution |

Infer. Ask only when Hunt and Confirm are equally live.

## Protocol

### 0. Intake — name the stated problem or stop

Load-bearing (two missing after one round → refuse):

1. The stated problem in their words, plus who owns the ticket
2. What already shipped against it, and what changed in someone's week (or "nothing" / "unknown")

Also collect: how long it has been open; who first asserted it; what "solved" currently means on the ticket.

Restate the stated problem **mechanism-free**. If you cannot delete the current solution and keep the sentence, you are still holding a solution, not a problem.

> **Done when:** the stated problem is one mechanism-free sentence, or you have refused.

### 1. Run the three displacement tests

A ghost is not a vibe. It fails at least one of these.

| Test | Question | Ghost signal |
|---|---|---|
| **Monday** | If we solved this perfectly on Friday, whose Monday changes — named person, named hour? | Nobody, or only the dashboard owner |
| **Parent** | Name a Y such that solving Y makes this evaporate | A cheaper or truer Y exists |
| **Origin** | Who asserted this, when, and what would they say now? | No source, or the source would withdraw it |

Read `references/ghost-classes.md` **now** if more than one signal is lit, or if the ticket is older than two cycles with no Monday change. It holds the five classes (proxy, dissolved, political, symptom, inherited) and the test that kills each.

Write which tests fired and which class is the best fit. Multiple classes may stack; pick the one whose death would do the most work.

> **Done when:** every test has a result (fired / clear / unknown), and one class is named or all three tests are clear.

### 2. Verdict

| Verdict | Meaning | What you write |
|---|---|---|
| **Load-bearing** | The stated problem stands | The Monday that would change, and the test that would *unseat* it later |
| **Displaced** | A parent (or a different problem) is the real one | The ghost, the parent, why the parent's death kills the ghost |
| **Dissolved** | The war ended | What ended it, who still tends the ritual, the stop-work sentence |

A load-bearing verdict without an unseat-test is a slogan. A displaced verdict without a named parent is a reframe. A dissolved verdict that proposes a new project has not dissolved anything.

If the parent is itself stuck on a floor, invoke `first-principles` on the parent — not on the ghost. If the parent is an official unsolved claim, invoke `verified-hard-problem`.

> **Done when:** one verdict is on the page, with the sentence that would falsify it.

### 3. Confirmation test and ASK

The cheapest observation that would confirm the verdict. What is seen, what result kills the verdict, cost, time. You do not invent the observation; you name where it would come from. Missing facts stay **unknown**.

ASK, exactly one: `confirm parent` / `kill ghost` / `keep stated` / `one interview` / `stop the ritual`. Owner, date.

Use `assets/one-pager.md` for the page.

Read `references/worked-examples.md` if the honest output wants to be a clever new framing, or if they asked you to "rethink the problem" with no ticket.

> **Done when:** the page has stated problem, three tests, class, verdict, unseat/confirm test, one ASK — and no solution was built against a ghost.

## Anti-patterns

- **Reframe-as-product.** Five alternative problem statements, no test, no verdict.
- **Solve-anyway.** The ghost is named in paragraph one; paragraph two designs the original ticket.
- **Parent-without-Monday.** A grander problem is declared; nobody's week is specified.
- **Issue-tree-in-disguise.** The governing question is accepted and split. That is a different skill.
- **Value-in-disguise.** "Is it worth it?" is not "is it the problem?"
- **Infinite suspicion.** Everything is a ghost. Load-bearing is a legal verdict; use it when the tests are clear.

## Bundled references

| File | Read it when |
|---|---|
| `references/ghost-classes.md` | More than one displacement test fired, or the ticket is older than two cycles with no Monday change |
| `references/worked-examples.md` | The run wants a clever reframe, or they asked to rethink the problem with no ticket |
| `assets/one-pager.md` | You are writing the deliverable |
