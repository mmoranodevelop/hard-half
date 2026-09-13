---
name: recovery-plan
description: >-
  Use when a project is red and needs a 14-day recovery pack: stop-doing,
  critical-path protect, resource, stakeholder message, one ASK. Not a health
  RAG, not a pre-mortem, not an AAR, not a crisis holding statement.
license: MIT
---

# Recovery Plan

**14-day recovery pack + one ASK** — stop-doing list, critical path protected, resource moves, stakeholder message, reset success test. Stabilize then reset baseline. Default: venture / client delivery; same spine for F500.

Method origin: PMI / industry troubled-project recovery (assess → stabilize → root cause → recovery plan → new baseline) + PRINCE2 management by exception (tolerance breach → exception plan as new stage plan) + operator 14-day pack. Reconstruct the operator board. Do not invent % complete or new end dates without a named source.

If they want a turnaround lecture: one paragraph then produce or stop.

## When to use

- Project is red / will breach tolerance and the room wants a recovery plan, not hope
- Sponsor asks "what do we stop, protect, and ask for in the next 14 days?"
- Health check said recover; need the pack, not another RAG
- Critical path is unprotected; scope still growing

## When not to use

- Routine RAG / traffic light — [Project Health](../../project/project-health/SKILL.md)
- Imagine failure before launch — [Pre-mortem](../../management/pre-mortem/SKILL.md)
- Learn after an event — [After Action Review](../../management/after-action-review/SKILL.md)
- First-hour holding statement — [Crisis Holding](../../writing/crisis-holding/SKILL.md)
- SteerCo decision pack (up to 3 decisions) — [Steering Pack](../../project/steering-pack/SKILL.md)
- Kill the bet at portfolio — [Portfolio Stage-Gate](../../management/portfolio-stage-gate/SKILL.md)

## Modes

| Mode | When | Output |
|---|---|---|
| **produce** | Default. Red/amber-escalating; facts exist | 14-day pack + ASK |
| **redline** | They pasted "work harder" or a new fantasy end date | Force stop-doing + protected path; kill invented dates |
| **refuse** | No evidence of breach, or they want to hide red as green | Issues list. Stop |

## Hard rules

1. **Horizon is 14 days** for the pack. Reset baseline may extend beyond; label it.
2. **Stop-doing is mandatory.** If nothing stops, it is not recovery.
3. **Protect the critical path** — named activities, owners, what is ring-fenced.
4. **Resource moves are named** (people / $ / vendor) or HOLE — do not invent headcount.
5. **Stakeholder message** is one short true paragraph (state, stop-doing, ask, next update).
6. **Success test for "out of recovery"** — written before the 14 days end.
7. **One ASK** — named sponsor / D to approve stop-doing + resource + new baseline (or kill) by date.
8. **Never invent** % complete, remaining €, or end dates. Holes stay holes. RAG without evidence is refuse.
9. **One page.**

## Intake

If **two** of 1–4 are missing after one round: issues list, not a fake recovery.

1. Project name, charter outcome, named sponsor / PM — load-bearing
2. Why red (breach: time / cost / scope / quality / benefit) with evidence — load-bearing
3. Current critical path (or honest "unknown") — load-bearing
4. What can be stopped or deferred this fortnight — load-bearing
5. Resource options already real (bench, vendor, overtime policy)
6. Who must hear the stakeholder message
7. As-of date; 14-day end date

## Output shape

```
RECOVERY PLAN (14 DAYS)  |  [project]  |  as-of: [date]  |  sponsor: [name]
ASK: [sponsor] to [approve stop-doing + resource move / reset baseline / kill] by [date]

BLUF
Red because [breach + evidence]. In 14 days we [stabilize / reset / recommend kill]. Out-of-recovery test: [ ].

STOP-DOING (mandatory)
| Item | Why stop | Owner | Effective |
|  |  |  |  |

CRITICAL PATH PROTECT
Path: [named activities or HOLE]
Ring-fence: [people / time / decision rights]
Will not touch: [ ]

RESOURCE
Add / move: [named, or HOLE]   Cost/authority: [or HOLE]
Vendor / overtime: [policy fact, not wish]

STAKEHOLDER MESSAGE (send)
[One short paragraph: state · stop-doing · ask · next update clock]

RESET / SUCCESS TEST
New baseline (if approved): [scope/date/cost — sourced or HOLE]
Out of recovery when: [measurable test]

NOT THIS PAGE
RAG only → project-health    Before launch → pre-mortem    After event → after-action-review
First hour → crisis-holding    SteerCo 3 decisions → steering-pack

Holes: [ ]
```

Annex: `assets/fourteen-day.md`.

## QA (must pass)

1. 14-day horizon stated with as-of and end date.
2. Stop-doing list non-empty.
3. Critical path protect named or HOLE (not invented).
4. Stakeholder message present (true, short).
5. Out-of-recovery test written.
6. One ASK with owner, verb, date.
7. No invented % / € / end date.
8. Not health RAG, pre-mortem, AAR, or holding statement.
9. One page.

If 2, 6, or 7 fail: do not ship.

## Escalate / stop

- Breach is going-concern / legal / safety → principal + counsel; this page is the exhibit.
- Sponsor refuses stop-doing → refuse to ship a "recovery" that only adds work.
- Kill is the honest option → route to [Portfolio Stage-Gate](../../management/portfolio-stage-gate/SKILL.md) / sponsor kill; pack can recommend.
- Live external incident in the first hour → [Crisis Holding](../../writing/crisis-holding/SKILL.md) first.

## Related

- [Project Health](../../project/project-health/SKILL.md) — detects red; this recovers
- [Pre-mortem](../../management/pre-mortem/SKILL.md) — before launch
- [After Action Review](../../management/after-action-review/SKILL.md) — after the recovery window
- [Crisis Holding](../../writing/crisis-holding/SKILL.md) — first hour comms
- [Steering Pack](../../project/steering-pack/SKILL.md) — room that approves the ASK
