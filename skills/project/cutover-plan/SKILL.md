---
name: cutover-plan
description: >-
  Use for the hour-by-hour cutover of a named go-live: sequence, owners, freeze,
  rollback trigger. NOT for the go/no-go gate, not the 100 days after.
license: MIT
---

# Cutover Plan

**Hour-by-hour cutover runbook** — named window: sequence, owners, freeze, rollback trigger, point of no return. Default: venture go-live; same spine for F500.

Method origin: public cutover-runbook craft (freeze, timed sequence, validation, rollback trigger, point of no return). Operator cut.

If they want a cutover / runbook lecture: one paragraph then produce or stop.

## When to use

- A named go-live window needs the hours (who does what, in order)
- Freeze, rollback trigger, or point of no return is missing
- A "cutover approach" slide must become a timed sequence

## When not to use

- Go / no-go gate — [Go-Live Readiness](../../project/go-live-readiness/SKILL.md) (this runbook assumes a Go, or is evidence the gate needs)
- First 100 days after — [Integration 100](../../management/integration-100/SKILL.md)
- Behaviours after — [Change Adoption](../../management/change-adoption/SKILL.md)
- Client UAT / accept the product — [Acceptance Signoff](../../project/acceptance-signoff/SKILL.md)
- Steering sitting — [Steering Pack](../../project/steering-pack/SKILL.md)
- Imagined failure before the window — [Pre-mortem](../../management/pre-mortem/SKILL.md)

Cutover ≠ go-live-readiness ≠ integration-100. Gate decides. This page runs the hours.

## Modes

| Mode | When | Output |
|---|---|---|
| **produce** | Default. Window dated | Timed runbook + ASK |
| **redline** | They pasted a day-level plan or a 12-tab spreadsheet | Force hours, owners, freeze, rollback; list what you killed |
| **refuse** | No window, no owners, or a strategy essay | Issues list. Stop |

## Hard rules

1. **Sequence is time-ordered.** Each row: time, step, one named owner, observable validation, rollback now? (Y/N). Day-level rows fail — split to hours (or 15-min where it matters).
2. **Freeze** is a time + a test (write fails / banner sent). Communicate it. No freeze = the old path keeps moving while you cut.
3. **Rollback trigger** is observable and pre-agreed. Owner of the rollback call is named (D or cutover lead with a written rule). Time to reverse is a number they gave — do not invent minutes.
4. **Point of no return** is a clock time. After it, fix-forward. The in-window go/no-go sits before that point.
5. **Comms rows are real steps** (who tells whom, channel). Silent cutover fails.
6. **ASK:** named D or cutover lead approves this runbook and freeze by a date before the window. Do not re-litigate the gate here.
7. **Do not invent times or owners.** Holes stay holes.

## Intake

If **two** of 1, 3, 5 are missing after one round: issues list, not a fake run.

1. Window — start–end, timezone, what switches — load-bearing
2. Go / no-go status — already called, or this is a draft for the gate
3. Steps they know — messy list is fine — load-bearing
4. Freeze — from when, what cannot change
5. Rollback trigger + owner — or "none yet" — load-bearing
6. Point of no return — or "unknown"
7. Command names — cutover lead, comms, tech, business validator

## Output shape

```
CUTOVER RUN  |  [what switches]  |  [client]
Window: [start–end] [timezone]     Freeze from: [time]     Point of no return: [time]
Cutover lead: [name]     D (rollback call): [name]     Comms: [name]
Go/no-go: [called Go date / draft for gate]

ASK: [D or cutover lead] to approve this runbook + freeze by [date], [n] hours before window.

FREEZE
From [time]: [what cannot change]. Test: [write fails / banner]. Told: [who, channel].

ROLLBACK
Trigger: [observable]. Call by: [name] within [n min]. Time to reverse: [ ]. After point of no return: fix-forward only.

SEQUENCE
| Time | Step | Owner | Validation | Rollback now? |
| [ ] | [ ] | [one name] | [observable] | Y/N |

IN-WINDOW GATES
| Time | Gate | D | If no |
| [ ] | go/no-go before point of no return | [ ] | rollback / abort |

COMMS
| Time | Message | From → to | Channel |
| [ ] | freeze start / live / rollback | [ ] | [ ]

NOT THIS PAGE
Go/no-go criteria → go-live-readiness    Day 1–100 → integration-100
Holes: [ ]
```

Also `assets/cutover-run.md`.

## QA (must pass)

1. Window: start–end + timezone.
2. Every step has a time and a named owner.
3. Freeze time + test present.
4. Rollback trigger and rollback D named.
5. Point of no return is a clock time.
6. Sequence is not day-level ("Saturday: migrate").
7. ASK: approve runbook by a date before the window.
8. Not a go/no-go essay or a 100-day plan. No invented times.

If 1, 2, 4, or 7 fail: do not ship.

## Escalate / stop

- No names after one ask → stop.
- "Agile, we'll improvise on the night" → refuse; this is the hours.
- Gate not called and they want to skip it → produce as **draft**; route the call to [Go-Live Readiness](../../project/go-live-readiness/SKILL.md).
- Friday afternoon window with no rollback owner → name the residual; do not hide it.
- Data-residency / regulated cutover → counsel; still write the hours as holes.

## Related

- [Go-Live Readiness](../../project/go-live-readiness/SKILL.md) — the gate this runbook executes
- [Integration 100](../../management/integration-100/SKILL.md) — 100 days after
- [Change Adoption](../../management/change-adoption/SKILL.md) — behaviours after
- [Acceptance Signoff](../../project/acceptance-signoff/SKILL.md) — product accepted before the window
- [RAID Register](../../management/raid-register/SKILL.md) — residuals this night can still hit
- [After Action Review](../../management/after-action-review/SKILL.md) — after the window
