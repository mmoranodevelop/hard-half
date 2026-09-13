---
name: reforecast
description: >-
  Use when the remaining fiscal year must be rewritten vs the original plan
  (actuals occupy closed months; open months are re-assumed). NOT for budget-
  variance (past period), not scenario-planning (3–4 worlds), not operating-
  review.
license: MIT
---

# Reforecast

**This-year reforecast** — one page: original plan FY vs actuals to date vs reforecast FY, three drivers of the *year* change, year-end cash (venture) or remaining-year EBIT (F500), one ASK (reallocate / freeze / hire slip / raise / accept). Default: venture remaining-year burn + year-end cash. Same spine for F500 (say if bonuses still sit on the original budget).

Method origin: AFP public — remaining-year reforecast vs the **snowplow** (misses loaded into later months); **73%** reforecast at least quarterly (n = 606, 2017).

If they want a forecasting lecture: one paragraph then produce or stop.

## When to use

- Closed months exist (or a labelled flash) and the rest of *this* FY is still the old plan
- Board / lender asked “what do we now expect this year”
- Last reforecast drifted and nobody named the year-move

## When not to use

- Why **this period** missed vs last vs plan — [Budget Variance](../../management/budget-variance/SKILL.md)
- 3–4 worlds under uncertainty — [Scenario Planning](../../strategy/scenario-planning/SKILL.md)
- Weekly / monthly exception tour — [Operating Review](../../management/operating-review/SKILL.md)
- Invest / NPV / options — [Business Case](../../strategy/business-case/SKILL.md)
- 13-week bank — [Cash Runway](../../management/cash-runway/SKILL.md) (year-end cash *feeds* it)
- This month’s CCC — [Working Capital](../../finance/working-capital/SKILL.md)
- Named BD lock — [Close Calendar](../../finance/close-calendar/SKILL.md)
- Headcount as the *move* — [Headcount Plan](../../management/headcount-plan/SKILL.md) (this page still holds the year)

## Modes

| Mode | When | Output |
|---|---|---|
| **produce** | Default. Original plan FY + as-of / remaining months exist | Year-now page + one ASK |
| **redline** | They pasted a P&L or quietly rewrote Q4 | Kill snowplow; three year-drivers; keep original plan as baseline |
| **refuse** | No plan *and* no remaining-year view; or they want worlds / this-period variance | Issues list. Stop |

## Hard rules

1. Clock is **remaining FY**. Horizon **shrinks**. A rolling 12–18 month forecast is a cousin (Grove FP, vendor — label); it is not this page.
2. Actuals occupy closed months. Open months are re-assumed. Original plan date **does not move** unless the board re-bases.
3. Budget and forecast are supposed to be **distanced** so the forecast can be honest (AFP: 20% still cite budget as primary compensation basis). Say which number bonuses use.
4. **Snowplow is a fail:** missed months loaded into the rest of the year while the original plan is still treated as the forecast.
5. Three drivers of the **year** change — not 40 lines. Remainder labelled.
6. Do not build a three-statement model. Driver-based remaining-year P&L + cash implication + one ASK. Full IC model → [Business Case](../../strategy/business-case/SKILL.md).
7. Do not ship a reforecast that disagrees with the close (or unlabelled flash).
8. Cadence: quarterly minimum (AFP); monthly in a venture / PE skin.
9. Do not invent remaining-year numbers. Holes stay holes.

## Intake

If **original plan FY** and **as-of (closed vs open months)** are both missing after one round: issues list, not a fake page.

1. Entity; FY; as-of — closed months vs open months (load-bearing)
2. Original plan FY: revenue, GP, opex, EBITDA/burn, year-end cash (load-bearing)
3. Actuals to date on the same lines
4. Last reforecast date and numbers — or hole
5. Three suspected year-drivers, or “derive from the pack”
6. Who has D on accept / freeze / hire slip / raise
7. Compensation still on original plan? Y/N / “board may re-base”

## Output shape

```
THIS-YEAR REFORECAST  |  [entity]  |  FY[ ]  |  as-of: [date]
Closed months: [ ]     Open months: [ ]     Original plan date: [ ] (does not move)
Last reforecast: [date] or HOLE     D: [name]     Bonuses sit on: [plan / other]

| Line | Original plan FY | Actuals to date | Reforecast FY | Δ vs plan | Δ vs last RF |
| Revenue | [ ] | [ ] | [ ] | [ ] | [ ] |
| Gross profit | [ ] | [ ] | [ ] | [ ] | [ ] |
| Opex | [ ] | [ ] | [ ] | [ ] | [ ] |
| EBITDA / burn | [ ] | [ ] | [ ] | [ ] | [ ] |
| Year-end cash | [ ] | [ ] | [ ] | [ ] | [ ] |

YEAR BRIDGE (three drivers of the year — not 40 lines)
1. [driver]: $[ ]    2. [driver]: $[ ]    3. [driver]: $[ ]
Remainder labelled: $[ ]
SNOWPLOW CHECK: Q[ ] miss stays a miss. Remaining months have new evidence, not loaded hope.

NOT THIS PAGE: this-period why → budget-variance; 3–4 worlds → scenario-planning; 13-week bank → cash-runway

ASK: [reallocate / freeze / hire slip / raise / accept the year]
Owner: [ ]  Date: [ ]  $: [ ]
Holes: [ ]
```

## QA (must pass)

1. Closed vs open months named. Original plan date present.
2. Reforecast FY is remaining months rewritten + full-year implied — not a period variance.
3. Three year-drivers; remainder labelled.
4. Snowplow check is explicit.
5. ASK + named D + date + $.
6. No invented remaining-year dollars. Agrees with close or labelled flash.
7. Not worlds, not a 13-week strip, not an exec tour.
8. One page.

If 1, 2, 5, or 6 fail: do not ship.

## Escalate / stop

- This period vs last vs plan **without** rewriting the year → [Budget Variance](../../management/budget-variance/SKILL.md).
- Base / upside / downside as a business case → [Business Case](../../strategy/business-case/SKILL.md).
- Quietly snowplowing misses into Q4 → redline or refuse.
- Reforecast disagrees with the close → do not ship.

## Related

- [Close Calendar](../../finance/close-calendar/SKILL.md) — lock (or flash) first
- [Budget Variance](../../management/budget-variance/SKILL.md) — the past; this page is the rest of the year
- [Cash Runway](../../management/cash-runway/SKILL.md) — 13-week bank; year-end cash feeds it
- [Working Capital](../../finance/working-capital/SKILL.md) — this month’s cycle, not the year
- [Scenario Planning](../../strategy/scenario-planning/SKILL.md) / [Operating Review](../../management/operating-review/SKILL.md) / [Business Case](../../strategy/business-case/SKILL.md)
- [Decision Debt](../../finance/decision-debt/SKILL.md) — aged D on freeze / hire slip / raise
