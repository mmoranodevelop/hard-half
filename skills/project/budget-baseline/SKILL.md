---
name: budget-baseline
description: >-
  Use when locking or reviewing the signed cost baseline: buckets, approved
  total, as-of, variance drivers vs actuals this period (NOT EAC forecast). One
  ASK re-baseline or hold. NOT for eac-pulse, not budget-variance (P&L), not
  cash-runway, not business-case, not change-control.
license: MIT
---

# Budget Baseline

**Signed cost baseline — one page** — buckets, approved total, as-of, this-period variance vs actuals, one ASK to re-baseline or hold. Default: client / program cost baseline mid-flight; same spine for internal builds. **Not** an EAC forecast.

Method origin: PMI cost baseline / performance measurement baseline (PMB) — approved time-phased budget (work packages + contingency; **excludes** management reserve) changed only via formal change control; actuals compare to baseline, not to last week's wish.

If they want a PMB / EVMS lecture: one paragraph then produce or stop.

## When to use

- "What is the signed cost baseline?" — buckets and total must be on one page
- This period's actuals vs baseline need drivers, not a full EAC story
- Before a re-baseline ASK (hold vs open CR)
- New PM inherits a muddy "budget" and needs the approved number

## When not to use

- EAC / ETC / VAC forecast — [EAC Pulse](../../project/eac-pulse/SKILL.md)
- Company P&L this vs plan (price/volume/mix) — [Budget Variance](../../management/budget-variance/SKILL.md)
- Bank 13-week liquidity — [Cash Runway](../../management/cash-runway/SKILL.md)
- Invest / NPV decision — [Business Case](../../strategy/business-case/SKILL.md)
- Formal CR to change the baseline — [Change Control](../../project/change-control/SKILL.md) (this page may feed it)
- Risk money buffer governance — [Contingency Reserve](../../project/contingency-reserve/SKILL.md)

## Modes

| Mode | When | Output |
|---|---|---|
| **produce** | Default. Signed baseline + period actuals | Baseline page + ASK |
| **redline** | They pasted a "budget" that mixes hope and actuals | Force approved total, version, as-of; kill vibes |
| **refuse** | No approved total and no owner of D, or invent variance | Issues list. Stop |

## Hard rules

1. **Approved total + version + as-of + approver.** Missing → HOLE. Do not call a draft the baseline.
2. **Buckets** (labour / vendor / other / contingency-in-baseline) sum to approved total — or hole the gap.
3. **Management reserve is NOT in the cost baseline.** Show it as outside if material; do not bury it in BAC.
4. **This period:** actuals vs baseline for the period (or cumulative to date). Drivers ≤3. Not EAC.
5. **Variance is money + because**, not adjectives.
6. **One ASK** — hold baseline / open re-baseline CR / transfer contingency / freeze spend. Owner, date.
7. **Never invent** approved totals, actuals, or bucket splits. Holes stay holes.
8. **One page.** Baseline board, not a forecast model.

## Intake

If **two** of 1–4 are missing after one round: issues list, not a fake baseline.

1. Named project + approved cost baseline total — load-bearing
2. Version / CR that set it + approver + as-of — load-bearing
3. Bucket split (or "single pot") — load-bearing
4. Actuals this period / to date (source) — load-bearing
5. Contingency inside baseline vs management reserve outside
6. Who has D on re-baseline
7. Period label

## Output shape

```
BUDGET BASELINE  |  [PROJECT]  |  as-of: [date]  |  Period: [ ]
Currency: [ ]    Version: [charter / CR v]    Approver: [ ]
ASK: [D] to [hold / re-baseline CR / draw contingency / freeze] by [date]

APPROVED BASELINE (PMB)
| Bucket | Baseline $ | Notes |
| Labour |  |  |
| Vendor / third party |  |  |
| Other direct |  |  |
| Contingency (in baseline) |  | known risks |
| TOTAL (cost baseline) |  | excludes Mgmt Reserve |
Mgmt Reserve (outside baseline): [ ] / HOLE

THIS PERIOD VS BASELINE
|  | Baseline (period or cum) | Actual | Var $ | Var % |
|  |  |  |  |  |

DRIVERS (≤3)
| # | Driver | $ | Owner | Action |
| 1 |  |  |  |  |

NOT THIS PAGE
EAC/ETC → eac-pulse    P&L shop variance → budget-variance
Cash → cash-runway    Invest case → business-case
Formal CR → change-control    Reserve draws → contingency-reserve

Holes: [ ]
```

Annex: `assets/baseline-buckets.md`.

## QA (must pass)

1. Approved total + version + as-of (or explicit HOLE).
2. Buckets sum or gap labelled.
3. Mgmt reserve not silently inside baseline.
4. Period actuals vs baseline with ≤3 drivers (or holes).
5. One ASK with owner, verb, date.
6. Not EAC, not P&L variance, not cash. No invented numbers. One page.

If 1, 5, or 6 fail: do not ship.

## Escalate / stop

- No approved total after one ask → refuse; do not invent a baseline.
- Re-baseline required → this page is the exhibit; [Change Control](../../project/change-control/SKILL.md) owns the CR.
- They want EAC/ETC as the page → [EAC Pulse](../../project/eac-pulse/SKILL.md).
- Contingency draw is the decision → [Contingency Reserve](../../project/contingency-reserve/SKILL.md).

## Related

- [EAC Pulse](../../project/eac-pulse/SKILL.md) — forecast at complete
- [Budget Variance](../../management/budget-variance/SKILL.md) — shop P&L vs plan
- [Cash Runway](../../management/cash-runway/SKILL.md) — bank liquidity
- [Business Case](../../strategy/business-case/SKILL.md) — invest decision
- [Change Control](../../project/change-control/SKILL.md) — formal baseline change
- [Contingency Reserve](../../project/contingency-reserve/SKILL.md) — risk money buffer
- [Estimate Confidence](../../project/estimate-confidence/SKILL.md) — pre-commit band
