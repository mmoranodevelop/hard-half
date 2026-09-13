---
name: sponsor-status
description: >-
  Use for the client-facing one-pager this period: on track / at risk / off,
  exceptions, one ASK. Not the internal operating review, not a RAID dump, not a
  steering pack.
license: MIT
---

# Sponsor Status

**Client-facing status one-pager** — this period, named sponsor: on track / at risk / off, exceptions only, one ASK. Default: weekly; same spine for F500.

Method origin: PRINCE2 highlight report (PM → board, manage by exception) + RAG one-pager craft. Not a WBR of *our* shop.

If they want a highlight-report lecture: one paragraph then produce or stop.

## When to use

- Weekly (default) or this-period update **to the client sponsor**
- Need on track / at risk / off, exceptions, one ASK — not a tour
- A 12-slide "status deck" must become one page the sponsor can fly

## When not to use

- Internal weekly exceptions of *our* P&L / program — [Operating Review](../../management/operating-review/SKILL.md)
- Steering sitting (up to 3 decisions, capacity) — [Steering Pack](../../project/steering-pack/SKILL.md)
- Living RAID — [RAID Register](../../management/raid-register/SKILL.md)
- Quarterly sitting with one named customer — [QBR](../../management/qbr/SKILL.md)
- First authorisation — [Project Charter](../../project/project-charter/SKILL.md)
- One named delta to the baseline — [Change Control](../../project/change-control/SKILL.md)
- Notes that need decisions extracted — [Meeting Notes to Decisions](../../writing/meeting-notes-to-decisions/SKILL.md)

## Modes

| Mode | When | Output |
|---|---|---|
| **produce** | Default | Filled one-pager + ASK |
| **redline** | They pasted a status deck / RAID dump | RAG first; exceptions only; list what you killed |
| **refuse** | Two load-bearing facts missing, or a workstream tour | Issues list. Stop |

## Hard rules

1. **Clock is this period.** A charter tour is not the page.
2. **One overall RAG.** On track / at risk / off. At risk = path to green with a named action. Off = cannot hit baseline without a decision. Do not hide off as at-risk. Do not invent RAG.
3. **Four lenses only:** scope, time, cost, residual risk. Each: RAG + one sentence. Green is seen, not discussed.
4. **Exceptions only (≤5).** Owner, date, verb that is not "monitor." Point at RAID; do not paste it.
5. **One ASK** the sponsor can close this period — or explicit "note only." Baseline move → [Change Control](../../project/change-control/SKILL.md) or [Steering Pack](../../project/steering-pack/SKILL.md). Last period's ASK on the page.
6. **Do not invent dates or spend.** Holes stay holes.

## Intake

If **two** of 1–3 are missing after one round: issues list, not a fake page.

1. Project + named client sponsor — load-bearing
2. Period ending [date]; cadence weekly default — load-bearing
3. Plan of record — end date, envelope, this period's promise — load-bearing
4. Actuals they have — dates, spend, deliverable state, or "unknown"
5. Exceptions — off-plan, or "we have not looked"
6. Last period's ASK — closed or not

## Output shape

```
SPONSOR STATUS  |  [project]  |  [client]  |  period ending: [date]
Sponsor: [name]     PM: [name]     Cadence: weekly (default)
Baseline: charter v[n] · end [date] · envelope [ ]

ASK: [sponsor] to [verb + object] by [date]. If none: "note only this period."

SCORE
[On track / At risk / Off] because [one cause]. Path: [action + owner + date / "needs a decision"].

LENSES
| Lens | RAG | Actual vs plan | So what |
| Scope | | | |
| Time | | | |
| Cost | | | |
| Risk residual | | | |

EXCEPTIONS (≤5)
1. [item] — [at risk/off] — Owner: [name] — Action: [verb] by [date] — RAID [id]

LAST PERIOD'S ASK
| Item | Owner | Due | Closed? |
| | | | |

DONE / NEXT (max 3 each)
Done: [ ]
Next: [ ]

NOT THIS PAGE
Our shop → operating-review    SteerCo → steering-pack    Living RAID → raid-register

Holes: [ ]
```

## QA (must pass)

1. Named sponsor + period date.
2. Overall RAG (on track / at risk / off).
3. ASK or explicit "note only."
4. Each exception has owner + date + verb.
5. Not a RAID dump or workstream tour.
6. Not a steering pack (3 decisions, capacity).
7. Not an internal operating review of *our* shop.
8. No invented numbers or a fake "green."
9. One page.

If 2, 3, 7, or 8 fail: do not ship.

## Escalate / stop

- They want every workstream, two minutes → refuse the tour.
- Internal MOR labelled "sponsor update" → [Operating Review](../../management/operating-review/SKILL.md).
- Three baseline decisions this sitting → [Steering Pack](../../project/steering-pack/SKILL.md).
- No plan of record → say so; do not fake RAG.
- Safety / legal / cyber off → escalate now; do not wait for Friday.

## Related

- [Operating Review](../../management/operating-review/SKILL.md) — *our* weekly exceptions
- [Steering Pack](../../project/steering-pack/SKILL.md) — committee sitting, decisions
- [RAID Register](../../management/raid-register/SKILL.md) — feeds exceptions; is not this page
- [Project Charter](../../project/project-charter/SKILL.md) — plan of record
- [Change Control](../../project/change-control/SKILL.md) — one baseline delta
- [QBR](../../management/qbr/SKILL.md) — quarterly, one named customer
