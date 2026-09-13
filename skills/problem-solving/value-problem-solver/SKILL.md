---
name: value-problem-solver
description: >-
  Run a product idea, feature, decision, project, PRD, vendor proposal, company
  initiative, or agent task through seven value filters — real problem, efficacy,
  validation, communication, access, sustainability, integrity — and produce
  either an Audit verdict on something that already exists or a Design walk
  before anyone writes a PRD or starts building. Infers Audit vs Design from
  context; asks only when genuinely ambiguous. Use when the user asks whether
  something is worth building, whether an idea creates real value, to
  pressure-test a feature or vendor proposal, to audit a PRD, or says the
  solution is looking for a problem, nobody will switch, or we are capturing
  value we did not create. NOT for problems declared impossible or stuck on a
  physics or cost floor (use first-principles). NOT for diagnosing why a metric
  is down (use issue-tree). NOT for writing the PRD itself (use prd-spec) — this
  is the filter pass before or against it. NOT a cash business case, and NOT
  kill-criteria for the next funding tranche.
license: MIT
---

# Value Problem Solver

## The filter is the whole skill

Value is not a property of the thing. It is a relation: **someone**, a **state change** that matters to them, and everything that change **costs anyone**.

> Value = a real improvement in someone's life, minus everything that improvement costs anyone, measured over time.

The leading word is **filter**. Seven filters, not seven phases. A candidate passes through all of them; excellence on one does not rescue a zero on another. Relevance × efficacy × adoption are **multiplicative** — if one term is zero, net value is zero. The seven **guardrails** are vetoes, not weights: a failed guardrail stops the run.

Three distinctions every run keeps on the page:

| Distinction | If you collapse it |
|---|---|
| **Potential vs realized** | A drawer-solution is scored as if someone already lives differently |
| **Gross vs net** | Concentrated, visible, immediate benefit hides diffuse, invisible, future cost |
| **Created vs captured** | Rent, lock-in, and manipulation read as "success" |

Communication is not marketing pasted on afterwards. It is the channel that turns potential into realized. A solution nobody can see, understand, or reach has the same potential and near-zero realized value.

You supply the filter structure. The user supplies who hurts and what they already do. Missing facts stay labelled **unknown** — they are not filled with a plausible story.

## When to stop

Say so and hand off. Forcing the filters onto the wrong job produces a value essay that nobody asked for.

- The problem is called impossible, or a physics / cost floor will not move → `first-principles`
- The room has not agreed *what the problem is* → `issue-tree` first; come back when there is a governing question
- They want the builder spec written → `prd-spec` *after* this pass (or instead, if a signed value verdict already exists)
- They want only the customer job and a stop-building list → `jobs-to-be-done` (that is filter 1's interview method, not the seven)
- Cash flows, NPV, options → `business-case`
- Dated kill tests for the next tranche of one bet → `kill-criteria`
- One experiment already scoped → `experiment-brief`
- One official unsolved *claim* (millennial, prize-grade, safety/legal-grade) to attack and verify → `verified-hard-problem`
- The "who hurts" keeps sliding, or a shipped fix changed nobody's week → `ghost-problem`
- About to ship a KPI / bonus / agent reward and need the post-game state → `cobra-equilibrium`
- Implementation, debugging, or a known best practice

If two load-bearing facts in step 0 are still blank after one ask, produce an issues list and stop. A fake filter pass is worse than a refusal.

## Mode

Infer. Ask only when both readings are equally live.

| Mode | When | Output |
|---|---|---|
| **Audit** | They named or pasted a thing that exists — live feature, PRD, vendor proposal, initiative, agent task already specified | Verdict + weakest filter + cheapest kill experiment |
| **Design** | They are about to build, write a PRD, or start something, and the filters must run *first* | What to test smallest, what not to build yet, one-sentence promise |

Do not mix them. An Audit that quietly redesigns the product has not audited it. A Design that scores a fantasy as if it were shipped has not designed it.

## Protocol

### 0. Name before you filter

Write four sentences. If you cannot, you do not have a candidate yet.

1. **Who** — a nameable segment, not "everyone" or "users"
2. **State change** — from what, to what, in their life (mechanism-free)
3. **Today** — the workaround they already pay for (time, money, effort), or "none observed"
4. **Beat** — the best alternative already available, including doing nothing

Label every later claim **verified**, **assumed**, or **unknown**. An unlabelled claim is a defect: it lets an assumption graduate into a fact.

> **Done when:** the four sentences exist, two of them are load-bearing and not blank, and you have named Audit or Design.

### 1. Run the seven filters

For each filter: the question, pass / fail / unknown, the evidence (or the hole), and the typical failure if it is failing. A fail or unknown on a multiplicative term (1, 2, 5) makes net value **zero or unknown** — say that; do not average.

| # | Filter | The question |
|---|---|---|
| 1 | Real problem | Does it exist for real people, and hurt enough that they already spend around it? |
| 2 | Efficacy | Does the solution change that state, measurably, better than the alternative they have? |
| 3 | Validation | Have 1 and 2 been checked with real people, or does the team merely believe them? |
| 4 | Communication | Can the right people see it, understand the promise in ten seconds, and trust it enough to try? |
| 5 | Access | Can they actually obtain and use it — price, practicality, habit-change cost? |
| 6 | Sustainability | Can it keep existing in three years, and at 100×? |
| 7 | Integrity | Who pays costs that are not on our books? Do we earn when they are better off? |

Read `references/seven-filters.md` **now** if a filter is the deciding one, if the user is pushing back on a fail, or if you are about to mark a multiplicative filter "pass" on belief alone. It holds the indicators, the honest-cause-vs-symptom test, the millennial-problem suspicion, and the written checklist.

A millennial unsolved problem is *more* suspicious, not less: either people will not change, or cost has always beaten benefit, or prior attempts failed for a reason you do not yet know. Validation is how you find out which, before you burn years.

> **Done when:** all seven have a status, every fail names its typical failure, and any zero on filters 1, 2, or 5 is reflected in the verdict as zero or unknown — not as a weighted score.

### 2. Apply the formula as an instrument, not a number

```
                 Relevance × Efficacy × Adoption
Net value     =  ──────────────────────────────  −  Direct costs  −  Externalities
                         (1 + Friction)

              …integrated over years, not a quarter
```

Three properties, which are the reason to write it down:

1. The first three terms **multiply**. They do not compensate.
2. Externalities **subtract** and are often delayed. Read the integral, not the point.
3. Friction (communication, access, habit change) **divides**. It rarely zeros the value; it can make an identical solution worth a tenth.

If you do not have numbers, do not invent them. State which term is zero, unknown, or load-bearing, and what measurement would pin it. A labelled hole is worth more than a filled-in score.

> **Done when:** the three properties have been applied to *this* candidate, and every quantity (or hole) is labelled.

### 3. Guardrails — veto, not weight

Apply these **before** optimizing anything else. A violation is a stop, not a deduction you make up elsewhere.

1. No hidden harm — if the value depends on someone not knowing what you are doing, it is not value
2. Real consent — whoever bears a cost knows and accepted it freely; unread terms do not count
3. Reversibility — prefer what you can undo; irreversible harm needs certainty you almost never have
4. Aligned incentives — you earn when the user is better off, not when they are worse or trapped
5. Headline test — if the capture mechanism ran on the front page, described accurately, would it be a problem?
6. Time test — in ten years, improvement or tolerated-until-the-cost-showed?
7. Truth in the metric — a proxy that no longer tracks the wellbeing it stood for is not a target

Read `references/guardrails-and-antipatterns.md` **now** if filter 7 is in play, if the business model might earn on user harm, or if the candidate matches an anti-pattern (lock-in, subsidized growth, engagement-as-wellbeing, Goodhart). It holds the recognition table.

> **Done when:** every guardrail is pass / fail / not-applicable, and any fail has stopped the run or forced a redesign that removes the violation — not a note in the appendix.

### 4. Deliver

Use `assets/report-template.md` for the page. Lead with the verdict.

**Audit** produces one of:

| Verdict | Meaning |
|---|---|
| **Creates** | Realized net value, or a clear path from potential to realized with evidence |
| **Transfers** | Benefit here is cost somewhere else that was not on the page |
| **Extracts** | Capture without creation (lock-in, rent, hidden harm) |
| **Hypothesis** | Potential only — the load-bearing assumption is unnamed or untested |
| **Refuse** | Cannot name who / state change / today's workaround after one ask |

Name the **weakest filter**, the **cheapest experiment** that would kill the load-bearing assumption (behavior, not opinions), and **when** you will remeasure — value is an integral; a thing that created value can start extracting later.

**Design** produces:

- the smallest thing that tests the load-bearing assumption
- what you will **not** build until that test speaks
- a one-sentence promise a person with the problem recognizes instantly
- the same filter table, scored as *intended*, with every pass marked assumed until evidence exists

Do not write the PRD. If they want it next, say so and stop, or invoke `prd-spec` only after they accept the verdict.

Read `references/worked-examples.md` if the honest answer wants to be "yes" out of politeness, or if you have never seen a run that refuses. One of the examples is a no.

> **Done when:** the page has a named verdict, a weakest filter, a kill experiment or an explicit refusal to invent one, claim labels on every assertion, and no PRD.

## Anti-patterns

- **Scoring belief.** Team enthusiasm, friend feedback, or investor excitement marked as validation.
- **Averaging a zero.** A dazzling filter 2 used to excuse a missing problem or a switching cost nobody will pay.
- **Gross as net.** The benefit is on slide one; the off-books cost is a footnote or is absent.
- **Potential as realized.** The demo works; nobody has changed a weekly habit.
- **Capture as creation.** Users stay because leaving hurts, and that gets written down as value.
- **Redesign-during-audit.** The existing thing is quietly replaced with a better one so the verdict can be kind.
- **Guardrail as deduction.** "We lose a few points on integrity but the efficacy is huge."

## Bundled references

| File | Read it when |
|---|---|
| `references/seven-filters.md` | A filter is deciding the verdict, the user disputes a fail, or you are about to pass a multiplicative filter on belief |
| `references/guardrails-and-antipatterns.md` | Filter 7 is live, the model may earn on harm, or the candidate looks like an anti-pattern |
| `references/worked-examples.md` | You need a full Audit-no, an Audit-hypothesis, or a Design walk — including a refusal |
| `assets/report-template.md` | You are writing the deliverable |
