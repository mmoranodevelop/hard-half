---
name: portfolio-stage-gate
description: >-
  Use when an MD must Go / Kill / Hold / Recycle one internal bet: one-page gate
  paper with evidence bar, kill criteria, named resources, one ASK. Gates commit
  resources. Not a status review, not a business case, not a first charter.
license: MIT
---

# Portfolio Stage-Gate

**Gate Paper — Go / Kill / Hold / Recycle** — one page for one named bet: evidence vs bar written last gate, assumptions converted, resource commit (names, money, next-gate date), one ASK. Portfolio table only when the MD holds several this sitting. Default: venture; same spine for F500.

Method origin: Stage-Gate public (Go/Kill/Hold/Recycle, hollow gates) + sequential investment. Trademark; not a licensed SOP.

If they want a Cooper lecture: one paragraph then produce or stop.

## When to use

- Continue or stop one named internal bet
- "We never kill anything" / hollow Go (approved, unfunded)
- A status review is pretending to be a gate

## When not to use

- In-flight exceptions — [Operating Review](../../management/operating-review/SKILL.md)
- Writing the money model — [Business Case](../../strategy/business-case/SKILL.md) (Gate 2 *uses* it)
- First authorisation — [Program Charter](../../management/program-charter/SKILL.md)
- Living assumptions — [RAID Register](../../management/raid-register/SKILL.md)
- Who has the D at the gate — [Decision Rights](../../management/decision-rights/SKILL.md)
- Dated kill tests for one venture, not the sitting — [Kill Criteria](../../strategy/kill-criteria/SKILL.md)

If nobody can kill, it is an operating review.

## Modes

| Mode | When | Output |
|---|---|---|
| **produce** | Default. One bet at a gate | Gate paper + ASK |
| **redline** | They pasted a status deck labelled "gate" | Force Go/Kill/Hold/Recycle; kill hollow Go |
| **refuse** | Two load-bearing facts missing, or "just Go it" | Issues list. Stop |

## Hard rules

1. **A gate is a resource decision**, not a status meeting.
2. **One bet per paper.** Outcomes are only Go / Kill / Hold / Recycle. "Continue pending alignment" is Hold.
3. **Kill criteria were written last gate.** Moving the bar to save a pet is a fail. Missing bar → Recycle (write tests), not a free Go.
4. **Go without names, money, and a next-gate date is Hold** (hollow).
5. **Sunk cost is not a criterion.** Next-stage value given what we now know.
6. **Evidence bar rises with spend.** Do not invent pilots.
7. **Right-size.** A two-week experiment is not five stages. Gatekeepers are resource owners of the next stage.
8. **Cannot say what would make them Kill** → refuse a live gate.

## Intake

If **two** of 1, 3, 6, 7 are missing after one round: issues list, not a fake Go.

1. The bet, one sentence — load-bearing
2. Which gate and what the last gate committed
3. Kill criteria already written — load-bearing
4. Evidence they actually have
5. Ask: Go / Kill / Hold / Recycle
6. Money and named people for the next stage — load-bearing
7. D / gatekeepers (resource owners of the next stage) — load-bearing

## Output shape

```
GATE PAPER  |  [bet]  |  Gate [n]  |  as-of: [date]
D / gatekeepers: [resource owners]     R: [lead]
Last gate committed: [resources / tests / date]
ASK: [D] to Go with [cash/FTE] through [next gate date] / Kill / Hold until [evidence] / Recycle to [stage] by [date]

RECOMMENDATION (one sentence)
[Kill / Go / Hold / Recycle] because [ ]. Sunk cost ignored.

EVIDENCE VS BAR
| Criterion | Bar (written last gate) | Evidence we actually have | Pass? |
| Strategic fit | [ ] | [ ] | Y/N/HOLE |
| Customer / user | [ ] | [ ] | Y/N/HOLE |
| Technical / operational | [ ] | [ ] | Y/N/HOLE |
| Resourcing | [ ] | [ ] | Y/N/HOLE |
| Residual vs appetite | [ ] | [ ] | Y/N/HOLE |

ASSUMPTIONS THIS STAGE WAS TO CONVERT
| Assumption | Test | Result | If false we said we would |
| [ ] | [ ] | hold / fail / untested | kill / recycle / pivot |

IF GO — RESOURCE COMMIT (not hollow)
Money: [ ]    People (names/FTE): [ ]    Deliverables: [ ]    Next gate: [date]
Next-gate kill tests: 1. [ ]  2. [ ]

PORTFOLIO (only if several this sitting)
| Bet | Gate | Rec | People/cash next | Residual / correlation |
| [ ] | [ ] | Go/Kill/Hold/Recycle | [ ] | [ ]

NOT THIS PAGE
Status tour → operating-review    Money model → business-case    First auth → program-charter

Holes: [ ]
```

## QA (must pass)

1. Outcome is one of Go / Kill / Hold / Recycle.
2. Go has names, money, next-gate date, next success tests — or the rec is Hold.
3. ASK + D + date.
4. Kill criteria pre-written, or the paper is Recycle-to-design.
5. No invented pilots; sunk cost is not the reason to continue.
6. Not a status tour of twelve bets with no kill.
7. One page (portfolio table only if needed).

If 1, 2, 3, or 5 fail: do not ship.

## Escalate / stop

- "Just Go it" / never-kill → refuse hollow Go; Hold or Kill.
- Type 1 (safety, plant, public) with failed tests → Kill or Recycle.
- Twelve bets, no kill → [Operating Review](../../management/operating-review/SKILL.md).
- Business case missing at Gate 2 full-rigor → Recycle; [Business Case](../../strategy/business-case/SKILL.md).

## Related

- [Program Charter](../../management/program-charter/SKILL.md) — first authorisation and first gate date
- [Kill Criteria](../../strategy/kill-criteria/SKILL.md) — dated tests for one venture
- [Business Case](../../strategy/business-case/SKILL.md) — money exhibit a Gate 2 uses
- [Operating Review](../../management/operating-review/SKILL.md) — in-flight stage; not a substitute gate
- [Decision Rights](../../management/decision-rights/SKILL.md) — who has the D at the gate
- [RAID Register](../../management/raid-register/SKILL.md) — assumptions and residuals
