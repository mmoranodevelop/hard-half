---
name: project-charter
description: >-
  Use when writing the one-page authorisation for one client project: outcome,
  in/out, sponsor, dates, budget envelope, success tests. Not a program charter,
  not a PID, not a kickoff pack.
license: MIT
---

# Project Charter

**One-Page Project Charter** — sponsor can sign for one named project: outcome, in/out, named D, calendar dates, budget envelope, pass/kill tests. Authorises resources. Not a program. Not a kickoff. Default: venture client project; same spine for F500.

Method origin: PMI project charter (sponsor issues; PM may apply resources) + PRINCE2 project brief, operator cut. Refuse the PID.

If they want a PID / PMBOK lecture: one paragraph then produce or stop.

## When to use

- Starting, reframing, or killing-and-rebooting one client project
- Extracting a one-pager from a 40-page PID or SOW dump
- Naming outcome, fence, sponsor, dates, envelope, success tests

## When not to use

- Outcomes + multiple components / benefits architecture — [Program Charter](../../management/program-charter/SKILL.md)
- First session after signature — [Kickoff Pack](../../project/kickoff-pack/SKILL.md)
- Economics — [Business Case](../../strategy/business-case/SKILL.md)
- Later Go/Kill of a live bet — [Portfolio Stage-Gate](../../management/portfolio-stage-gate/SKILL.md)
- Status of a live project — [Sponsor Status](../../project/sponsor-status/SKILL.md)
- Scope/cost/time change against a signed baseline — [Change Control](../../project/change-control/SKILL.md)
- Who does the work — [RACI Delivery](../../project/raci-delivery/SKILL.md)

If they want 40 pages, refuse.

## Modes

| Mode | When | Output |
|---|---|---|
| **produce** | Default. New project | One-page charter + ASK |
| **redline** | They pasted a PID / SOW | Six fields extracted; rest cut |
| **refuse** | Two load-bearing facts missing, or they insist on the binder | Issues list. Stop |

## Hard rules

1. **One project, one page.** Multiple components with a benefits architecture is a program.
2. **Authorisation, not a plan.** ASK the sponsor to authorise under these constraints.
3. **Outcome, not a ticket list.** In and out of scope, both written.
4. **Named sponsor (D).** "Steering committee" with no person fails. PM is P; does not silently hold the D.
5. **Dates are calendar dates.** "Q3" is a hole. Envelope is a number or explicit unknown plus a definition envelope.
6. **Kill test before happy tests.**
7. **Signatures mean resource commitment.** Cut Gantt, RACI wallpaper, NPV. Do not invent amounts.

## Intake

If **two** of 1, 3, 4 are missing after one round: issues list, not a fake charter.

1. Outcome — what will be true when this project stops — load-bearing
2. In scope / out of scope — both
3. Sponsor (D) — named person — load-bearing
4. Dates — start and end (or first gate) — load-bearing
5. Budget envelope — cash / fees / unknown with definition envelope
6. Success tests + kill test
7. Project manager (P) and client name

## Output shape

```
PROJECT CHARTER  |  [project]  |  client: [name]  |  as-of: [date]
Sponsor / D: [name]     PM (P): [name]
Start: [date]     End / first gate: [date]     CLASS: FOR AUTHORISATION
ASK: [D] to authorise [project] from [start] to [end] with envelope [amount or HOLE].

OUTCOME
When we stop, [client / organisation] will [observable end-state], so that [one-line why].
Why now: [complication].

IN SCOPE: [ ]
OUT OF SCOPE (explicit): [ ]

CONSTRAINTS
Budget envelope: [amount / unknown — definition envelope is X]
Time: [end date]     Must not break: [ ]     Regulatory: [ ]

D: [name] starts / redirects / kills. PM recommends and performs.
SUCCESS: Pass [observable]. Pass [observable]. Kill: [evidence that would stop us].

SIGN: D ________  P ________  Money owner (if different) ________
NOT THIS PAGE
Program → program-charter    First sitting → kickoff-pack    Later delta → change-control
Holes: [ ]
```

## QA (must pass)

1. ASK (D, authorise, dates, envelope).
2. Outcome is an end-state, not a ticket list.
3. Out of scope is written. Named D.
4. Dates are days, not "Q3".
5. Kill test present.
6. Not a program charter, PID, Gantt, or kickoff agenda.
7. No invented amounts. One page.

If 1, 3, 4, or 6 fail: do not ship.

## Escalate / stop

- They insist on 40 pages → extract six fields or stop.
- This is actually a program → [Program Charter](../../management/program-charter/SKILL.md).
- Charter already signed; they want the first session → [Kickoff Pack](../../project/kickoff-pack/SKILL.md).
- They want economics modelled → [Business Case](../../strategy/business-case/SKILL.md).

## Related

- [Program Charter](../../management/program-charter/SKILL.md) — program authorisation
- [Kickoff Pack](../../project/kickoff-pack/SKILL.md) — first session after this is signed
- [Change Control](../../project/change-control/SKILL.md) — later deltas against this baseline
- [RACI Delivery](../../project/raci-delivery/SKILL.md) — who does the work
- [Sponsor Status](../../project/sponsor-status/SKILL.md) — inspects this period against this charter
- [Project Close](../../project/project-close/SKILL.md) — scores this charter at the end
