---
name: budget-variance
description: >-
  Use when an MD must explain this period vs last vs plan with three drivers and
  one reallocation ASK. Flexible-budget / price-volume-mix craft. NOT for cash-
  runway, not operating-review, not margin-bridge as the whole P&L.
license: MIT
---

# Budget Variance

**Budget Variance — This vs Last vs Plan** — one page: three named drivers, labelled remainder, one-offs out of run-rate, one reallocation ASK (owner, amount, date). Default: venture P&L the MD owns; same spine for F500.

Method origin: AFP-public variance — master (static) vs flexible budget; price / volume / mix (PVM) for revenue; spending vs volume for cost. Operator page, not a standard-costing textbook.

If they want a PVM lecture: one paragraph then produce or stop.

## When to use

- Monthly or quarterly: actual vs budget vs prior
- "Why did we miss (or beat) plan?" that must end in a move of money or activity
- Rewrite a 40-line variance dump into three drivers
- Reallocate: freeze a bucket, fund another, change forecast

## When not to use

- 13-week cash / payroll — [Cash Runway](../../management/cash-runway/SKILL.md)
- Weekly exception ops — [Operating Review](../../management/operating-review/SKILL.md)
- Unit contribution of one SKU — [Unit Economics](../../strategy/unit-economics/SKILL.md)
- Headcount as the whole plan — [Headcount Plan](../../management/headcount-plan/SKILL.md)
- Gross/contribution this vs last only — [Margin Bridge](../../strategy/margin-bridge/SKILL.md)
- Covering email — [Pyramid Principle](../../writing/pyramid-principle/SKILL.md)

## Modes

| Mode | When | Output |
|---|---|---|
| **produce** | Default. Plan + actuals | Variance page + reallocation ASK |
| **redline** | They pasted a P&L pack | Three drivers; kill the 40 lines; one ASK |
| **refuse** | Two load-bearing facts missing, or a PVM lecture | Issues list. Stop |

## Hard rules

1. **Three columns:** this period, last period, plan (or forecast). A single actual is noise.
2. **Three drivers, not thirty lines.** Typical: price, volume, mix for revenue; volume vs spend for cost; FX / timing / one-off as a labelled remainder. Remainder must be small or named.
3. **Flexible vs static.** If volume moved, do not praise "cost underspend" that is just fewer units. Say which view the ASK uses.
4. **Favourable / unfavourable is not the ASK.** The ASK is a reallocation or a forecast change: move $X from A to B, or cut, or accept.
5. **One ASK.** Owner, date, amount.
6. **One-offs named.** Do not let a true-up hide the run-rate.
7. **Do not invent mix math** if you lack units. Hole: `[units missing — cannot split price/volume]`.
8. **Controller numbers or stop.** Do not ship a page that disagrees with the close.
9. **Not cash.** Accrual variance can look fine while the bank dies — flag, route [Cash Runway](../../management/cash-runway/SKILL.md).
10. **One page.** Line-item appendix for the sceptic.

## Intake

If **two** of 1–3 are missing after one round: issues list, not a fake bridge.

1. Entity, period, P&L owner — load-bearing
2. This / last / plan (or forecast) for the lines that matter — load-bearing
3. Who has the D on reallocation — load-bearing
4. Units if revenue (or hole)
5. Known one-offs
6. The move they want (or "we need you to recommend")
7. As-of / close date

## Output shape

```
BUDGET VARIANCE  |  [entity]  |  [period]  |  as-of: [date]
ASK: [reallocate $X from A → B / cut / accept] by [date]     Owner: [ ]
View: static vs plan | flexible at actual volume

HEADLINE
[Beat / miss] plan by [$ / %]. vs last: [$]. Run-rate vs one-off: [ ]

BRIDGE
| | Last | Plan | Actual | Δ vs plan | Δ vs last |
| Revenue | [ ] | [ ] | [ ] | [ ] | [ ]
| Gross profit | [ ] | [ ] | [ ] | [ ] | [ ]
| Opex | [ ] | [ ] | [ ] | [ ] | [ ]
| EBITDA / contribution | [ ] | [ ] | [ ] | [ ] | [ ]

THREE DRIVERS
1. [Price / rate] — [$]
2. [Volume] — [$]
3. [Mix / spend / FX / timing] — [$]
Remainder: [$] because [ ]

ONE-OFFS (exclude from run-rate)
- [ ]

REALLOCATION
| From (cut / delay) | To (fund) | $ | Effect if we do nothing |
| [ ] | [ ] | [ ] | [ ]

NOT THIS PAGE
13-week cash → cash-runway    Weekly ops → operating-review    This vs last margin only → margin-bridge

Holes: [ ]
```

## QA (must pass)

1. This vs last vs plan on the page.
2. Exactly three drivers + labelled remainder.
3. Flexible vs static named if volume moved.
4. One-offs separated.
5. One ASK with $, owner, date (or explicit accept).
6. No invented units.
7. Matches controller or flagged.
8. Not a cash strip, not a weekly OR.
9. Remainder is explained or small.
10. One page.

If 1, 2, 5, or 6 fail: do not ship.

## Escalate / stop

- No plan *and* no actuals after one ask → refuse. Do not invent a plan.
- Bank vs accrual conflict → [Cash Runway](../../management/cash-runway/SKILL.md) first.
- They want 200 lines explained equally → refuse; three drivers.
- Forecast replacing the annual plan as a stealth budget — say so; that is a re-plan, still one ASK.
- Headcount is the only driver → [Headcount Plan](../../management/headcount-plan/SKILL.md) as the move.

## Related

- [Cash Runway](../../management/cash-runway/SKILL.md) — liquidity; this is accrual vs plan
- [Operating Review](../../management/operating-review/SKILL.md) — weekly exceptions
- [Headcount Plan](../../management/headcount-plan/SKILL.md) — if people are the reallocation
- [Unit Economics](../../strategy/unit-economics/SKILL.md) — if mix/price is a unit problem
- [Margin Bridge](../../strategy/margin-bridge/SKILL.md) — gross/contribution this vs last only
- [Pyramid Principle](../../writing/pyramid-principle/SKILL.md) — the email
