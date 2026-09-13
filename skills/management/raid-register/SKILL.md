---
name: raid-register
description: >-
  Use when building an MD-readable RAID (Risks, Assumptions, Issues,
  Dependencies): owner, date, trigger, residual, one ASK. Kill 100-row theatre.
  Not an AAR, not a pre-mortem, not a status tour.
license: MIT
---

# RAID Register

**MD RAID One-Pager** — ≤12 items this period: Risks, Assumptions, Issues, Dependencies. Every page-1 row has a named person, date, trigger/test, residual, verb treatment. One ASK. Default: venture program; same spine for F500.

Method origin: ISO 31000 residual risk + operator RAID craft. Letters here are not Actions or Decisions.

If they want an ISO / 5×5 lecture: one paragraph then produce page 1 or stop.

## When to use

- Stand up or cut a RAID an MD will read
- Separate risks from assumptions, issues, and dependencies
- 100-row register must become ≤12 with owners and dates

## When not to use

- After the event — [After Action Review](../../management/after-action-review/SKILL.md)
- Before launch, imagined failure — [Pre-mortem](../../management/pre-mortem/SKILL.md)
- Period exceptions — [Operating Review](../../management/operating-review/SKILL.md)
- Unstructured problem — [Issue Tree](../../strategy/issue-tree/SKILL.md)
- Someone must choose — [Decision Rights](../../management/decision-rights/SKILL.md)
- First authorisation / kill-test pointer — [Program Charter](../../management/program-charter/SKILL.md)
- Gate using failed assumptions — [Portfolio Stage-Gate](../../management/portfolio-stage-gate/SKILL.md)

AAR ≠ RAID ≠ pre-mortem.

## Modes

| Mode | When | Output |
|---|---|---|
| **produce** | Default | One-page RAID + backlog pointer + ASK |
| **redline** | They pasted 100 rows | Page 1 of ≤12, each typed R/A/I/D |
| **refuse** | Two load-bearing facts missing, or they want the heat-map poster | Issues list. Stop |

## Hard rules

1. **An MD reads a page, not a database.** ≤12 on page 1. Rest is backlog (count, owner, next cut).
2. **Four different things.** Risk = uncertain future. Assumption = treated as true without proof. Issue = already happening. Dependency = waiting on a named other party.
3. **Owner, date, trigger, residual** — or it is theatre. Owner is a person, not PMO. Date is not "ongoing".
4. **Treatment is a verb:** avoid / take / remove / change / share / retain / contain. "Mitigate" / "monitor closely" fails.
5. **A materialised risk moves to Issues.** Do not list twice. Assumptions have tests and if-false.
6. **Dependencies have two owners** (ours and theirs), need-by, if-late.
7. **Do not invent likelihood decimals.** H/M/L or HOLE.

## Intake

If **two** of 1, 3, 5 are missing after one round: issues list, not a fake register.

1. Program / outcome this RAID serves — load-bearing
2. Appetite — residual the D will accept (even one sentence)
3. Items they already know — load-bearing
4. Period — this week / this month
5. Who can own — named people — load-bearing
6. Already happening vs feared vs unproven vs waiting on others

## Output shape

```
RAID  |  [program]  |  period ending [date]  |  D: [sponsor]  |  PM: [name]
Appetite (one line): [ ]
Page 1: items that change a decision this period, or residual outside appetite.
Backlog: [n] items, owner [PM], next cut [date]. Max 12 on this page.
ASK: [D] to decide / accept residual / escalate [item] by [date]. If none: note only this period.

RISKS
| ID | Event → effect on [objective] | L | I | Treatment (verb) | Trigger | Residual vs appetite | Owner | Date |
| R1 | [ ] | H/M/L | H/M/L | avoid/take/remove/change/share/retain | [ ] | inside/outside/unknown | [ ] | [ ]

ASSUMPTIONS
| ID | We are treating as true | Test | If false | Owner | Test-by |
| A1 | [ ] | [ ] | become risk / change plan / kill | [ ] | [ ]

ISSUES (already happening)
| ID | What is happening | Impact now | Containment | Residual | Owner | Resolve-by | Escalate-to |
| I1 | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ]

DEPENDENCIES
| ID | We need [what] from [counterparty] | Need-by | Our owner | Their owner | Status | If late |
| D1 | [ ] | [ ] | [ ] | [ ] | [ ] | [ ]

DECISIONS THIS RAID IS FORCING (not RAID)
- [decision sentence] → RAPID / memo / gate

NOT THIS PAGE
After → after-action-review    Before launch → pre-mortem    Period tour → operating-review
Holes: [ ]
```

## QA (must pass)

1. ≤12 items on page 1.
2. Every item typed; no duplicates across R/A/I/D.
3. Every page-1 row has a named person and a date.
4. ASK or explicit "note only".
5. Treatment is a verb, not "mitigate/monitor".
6. Issues are already happening; resolve-by is not "ongoing".
7. Dependencies have a counterparty owner.
8. No heat-map poster, invented decimals. One page.

If 1, 3, 4, or 8 fail: do not ship.

## Escalate / stop

- Safety / legal / cyber residual outside appetite → do not bury; named D.
- 100 rows for "completeness" → refuse as the MD pack.
- They want p=0.37 → H/M/L or stop.
- The row is actually a decision → [Decision Rights](../../management/decision-rights/SKILL.md).
- Problem unstructured → [Issue Tree](../../strategy/issue-tree/SKILL.md).

## Related

- [After Action Review](../../management/after-action-review/SKILL.md) — after; AAR actions may become rows
- [Pre-mortem](../../management/pre-mortem/SKILL.md) — before; surviving reasons land here
- [Operating Review](../../management/operating-review/SKILL.md) — period exceptions; RAID feeds reds
- [Program Charter](../../management/program-charter/SKILL.md) — kill test and top risks as pointers
- [Portfolio Stage-Gate](../../management/portfolio-stage-gate/SKILL.md) — failed assumption tests are kill criteria
- [Decision Rights](../../management/decision-rights/SKILL.md) — when the row is actually a decision
