---
name: program-charter
description: >-
  Use when writing the one-page authorisation for a program: outcome, in/out of
  scope, benefits, constraints, D, success tests, first 90 days. Not a business
  case, not a 40-page PID, not a later Go/Kill gate.
license: MIT
---

# Program Charter

**One-Page Program Charter + 90-Day Tranche** — sponsor can sign: outcome, in/out of scope, benefits with line owners, constraints, named D, pass/kill tests, first 90 days with envelope. Authorises resources. Does not plan the work. Default: venture program; same spine for F500.

Method origin: PMI program charter + MSP programme brief, operator cut.

If they want an MSP / PID lecture: one paragraph then produce or stop.

## When to use

- Starting, reframing, or killing-and-rebooting a program
- Extracting a one-pager from a 40-page PID
- Naming outcome, fence, benefits, constraints, D, success tests, first 90 days

## When not to use

- Economics, options, do-nothing — [Business Case](../../strategy/business-case/SKILL.md)
- Later Go/Kill of a live bet — [Portfolio Stage-Gate](../../management/portfolio-stage-gate/SKILL.md)
- One client project (not a program) — [Project Charter](../../project/project-charter/SKILL.md)
- Status of a live program — [Operating Review](../../management/operating-review/SKILL.md)
- Board paper to minute the start — [Executive Board Memo](../../management/executive-board-memo/SKILL.md)
- Living RAID after authorisation — [RAID Register](../../management/raid-register/SKILL.md)
- RAPID for the next stuck call — [Decision Rights](../../management/decision-rights/SKILL.md)

If they want 40 pages, refuse.

## Modes

| Mode | When | Output |
|---|---|---|
| **produce** | Default. New program | One-page charter + 90-day card + ASK |
| **redline** | They pasted a PID / live charter whose fence moved | Seven fields extracted; rest cut |
| **refuse** | Two load-bearing facts missing, or they insist on the binder | Issues list. Stop |

## Hard rules

1. **One page is the default.** If it needs a table of contents, it is a definition document.
2. **Authorisation, not a plan.** ASK: authorise this program through the first gate under these constraints.
3. **Outcome, not a ticket list.** End-state of the organisation. Multiple components with a benefits architecture = program; one project → [Project Charter](../../project/project-charter/SKILL.md).
4. **In and out of scope, both written.**
5. **Benefits are hypotheses with line owners**, not PMO slogans. 3–5, measured.
6. **One D.** Named sponsor. Program manager is R and P unless D was pushed down in writing.
7. **Kill test before happy tests.** First 90 days: definition + first observable + named resources. Hollow authorisation fails.
8. **Do not invent envelope numbers.** Point at the business case; do not paste NPV.

## Intake

If **two** of 1, 4, 6 are missing after one round: issues list, not a fake charter.

1. Outcome — what will be true of the organisation when we stop — load-bearing
2. In scope / out of scope — both
3. Benefits — who gains what, measure, line owner
4. D — named sponsor — load-bearing
5. Constraints — money envelope, time, must-not-break, regulatory
6. Success tests + kill test — load-bearing
7. First 90 days — what must be true; first gate date; 90-day envelope

## Output shape

```
PROGRAM CHARTER  |  [name]  |  as-of: [date]  |  D: [sponsor]  |  P: [PM]
First gate: [date]     CLASS: FOR AUTHORISATION
ASK: [D] to authorise [program] through [first gate date] with [90-day envelope].

OUTCOME
When we stop, [organisation] will [observable end-state], so that [benefit in one line].
Why now: [complication]. Desirable because: [one line; case lives elsewhere].

IN SCOPE: [ ]
OUT OF SCOPE (explicit): [ ]

BENEFITS (3–5)
| Benefit | Measure | Baseline → target (date) | Operational owner (line, not PMO) |
| [ ] | [ ] | [ ] or HOLE | [ ]

CONSTRAINTS
Money envelope: [amount / unknown — 90-day definition envelope is X]
Time: [end or first-tranche date]     Must not break: [ ]     Regulatory: [ ]

D: [name] starts / redirects / kills. PM recommends and performs.
SUCCESS: Pass [observable]. Pass [observable]. Kill: [evidence that would stop us].

FIRST 90 DAYS
By [date] we will have: [definition + first outcome].
Resources: [cash / FTE / names]. Next look by D: [date] — Go / Kill / Hold / Recycle.

SIGN: D ________  P ________  Money owner (if different) ________
NOT THIS PAGE
NPV → business-case    Later gate → portfolio-stage-gate    One project → project-charter
Holes: [ ]
```

## QA (must pass)

1. ASK (D, authorise, date, envelope).
2. Outcome is an organisational end-state, not a ticket list.
3. Out of scope is written.
4. Each benefit has a measure and a line owner.
5. Named D. Kill test present.
6. First 90 days have a date and resources.
7. Not a business case, PID, or Gantt.
8. No invented envelope. One page.

If 1, 2, 5, or 6 fail: do not ship.

## Escalate / stop

- They insist on 40 pages → extract seven fields or stop.
- No D after one ask → stop.
- Benefits owned by the PMO → send back to line leaders.
- They want economics modelled → [Business Case](../../strategy/business-case/SKILL.md).
- This is one project → [Project Charter](../../project/project-charter/SKILL.md).

## Related

- [Project Charter](../../project/project-charter/SKILL.md) — one project, not a program
- [Business Case](../../strategy/business-case/SKILL.md) — whether the money is worth it
- [Portfolio Stage-Gate](../../management/portfolio-stage-gate/SKILL.md) — later Go/Kill
- [Decision Rights](../../management/decision-rights/SKILL.md) — RAPID for the next stuck call
- [RAID Register](../../management/raid-register/SKILL.md) — living list after authorisation
- [Operating Review](../../management/operating-review/SKILL.md) — inspects the period against this charter
