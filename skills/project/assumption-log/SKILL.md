---
name: assumption-log
description: >-
  Use when load-bearing project assumptions need owners, validate/kill dates,
  and status — not the mixed RAID page, not a pre-mortem, not a kill-criteria
  card for one bet.
license: MIT
---

# Assumption Log

**Load-bearing assumption log — one page** — only the premises the plan is betting on: statement, owner, validate-by / kill-by, status, if-false. One ASK. Default: venture client program; same spine for F500.

Method origin: PMI / PMBOK assumption-log craft (charter → living log; assumption ≠ risk) + PS assumption-register practice (owner, validation method, date, status; invalidated → risk/issue). Reconstruct the operator page. Do not invent validation results.

If they want a PMBOK / RAID lecture: one paragraph then produce or stop.

## When to use

- Plan rests on unproven premises and nobody owns the tests
- Kickoff / charter assumptions were filed once and never reviewed
- Steering asks "what are we still betting on?" before a gate
- Invalidated premise must become a risk/issue with a dated action — not a vibe

## When not to use

- Imagined failure of a plan about to launch — [Pre-mortem](../../management/pre-mortem/SKILL.md) (feeds this log)
- Mixed ≤12 R/A/I/D page for this period — [RAID Register](../../management/raid-register/SKILL.md)
- NPV / invest case that embeds premises — [Business Case](../../strategy/business-case/SKILL.md)
- Cheap test design for one named bet + next cheque — [Kill Criteria](../../strategy/kill-criteria/SKILL.md)
- Hypothesis for a growth experiment — [Experiment Brief](../../strategy/experiment-brief/SKILL.md)

If they cannot name **any** load-bearing premise after one round, stop.

## Modes

| Mode | When | Output |
|---|---|---|
| **produce** | Default. Premises exist or must be written | One-page log + ASK |
| **redline** | They pasted a charter dump or 40-row sheet | Cut to load-bearing; force owner + date + if-false |
| **refuse** | Two load-bearing facts missing, or they want a lecture | Issues list. Stop |

## Hard rules

1. **Load-bearing only.** If false would not change scope, date, cost, or go/no-go — cut it. Page 1 is not a diary of hopes.
2. **Assumption ≠ risk ≠ issue.** Treated as true without proof → here. Uncertain future event → RAID risk. Already happening → issue. Do not list twice.
3. **Falsifiable sentence.** "Client will be cooperative" fails. Name who / what / by when.
4. **Owner is a person**, not "PMO" / "the team". Owner validates or escalates.
5. **Validate-by or kill-by is a calendar date.** "Ongoing" fails. Past-due unvalidated = stale → ASK.
6. **If-false is on the row:** become risk / change plan / CR / kill / stop gate — a verb path, not "monitor".
7. **Status is one of:** open / validating / validated / invalidated / escalated. Do not invent "mostly true".
8. **Never invent** evidence, pass counts, or impact $. Holes stay holes.
9. **One ASK** — named D / PM to validate, escalate, or kill named rows by date.
10. **One page.** Rest is backlog count + next cut date.

## Intake

If **two** of 1–4 are missing after one round: issues list, not a fake log.

1. Program / outcome the premises serve — load-bearing
2. The load-bearing premises they already know (even guesses — label them) — load-bearing
3. Who can own validation — named people — load-bearing
4. Next gate / date the log must be honest for — load-bearing
5. What already failed or looks shaky
6. Linked RAID / charter / SOW if any

## Output shape

```
ASSUMPTION LOG  |  [program]  |  as-of [date]  |  next gate [date]  |  D: [sponsor]  |  PM: [name]
ASK: [D/PM] to [validate / escalate / kill] [IDs] by [date]
Page 1: premises that change scope, date, cost, or go/no-go if false.
Backlog: [n] low-impact, owner [PM], next cut [date].

| ID | We are treating as true (falsifiable) | Owner | Validate-by / Kill-by | Method | If false | Status |
| A1 | [ ] | [name] | [date] | call / doc / PoC / sign-off | risk / CR / kill / stop gate | open/validating/validated/invalidated/escalated |

INVALIDATED THIS PERIOD → RAID / change-control
- [ID]: [what failed] → [risk ID / CR / decision]

NOT THIS PAGE
Pre-launch failure hunt → pre-mortem    Mixed R/A/I/D → raid-register
NPV case → business-case    One-bet kill tests → kill-criteria    Growth hyp → experiment-brief

Holes: [ ]
```

## QA (must pass)

1. Only load-bearing rows on page 1.
2. Every row: falsifiable statement, named owner, calendar date, if-false verb path, status.
3. No duplicates that belong on RAID as risks/issues.
4. One ASK with owner, verb, date — or explicit "note only this period".
5. No invented evidence or impact numbers.
6. One page (+ backlog pointer).

If 1, 2, 4, or 5 fail: do not ship.

## Escalate / stop

- Safety / legal / licence premise invalidated → escalate now; do not wait for validate-by.
- They want p=0.37 confidence → H/M/L impact-if-false or stop.
- Premises are actually kill tests for one funded bet → [Kill Criteria](../../strategy/kill-criteria/SKILL.md).
- They want the mixed period RAID → [RAID Register](../../management/raid-register/SKILL.md).

## Related

- [RAID Register](../../management/raid-register/SKILL.md) — mixed page; invalidated assumptions land as risks/issues
- [Pre-mortem](../../management/pre-mortem/SKILL.md) — harvests failure reasons that become rows here
- [Kill Criteria](../../strategy/kill-criteria/SKILL.md) — one bet, dated kill tests + next cheque
- [Business Case](../../strategy/business-case/SKILL.md) — money model; attach this log as the premise exhibit
- [Experiment Brief](../../strategy/experiment-brief/SKILL.md) — growth hypothesis, not delivery premises
