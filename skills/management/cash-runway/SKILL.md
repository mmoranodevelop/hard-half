---
name: cash-runway
description: >-
  Use when an MD (default: ventures) must see near-term cash: 13-week strip plus
  one-page ask — receipts, disbursements, net burn, runway, collections,
  payables. Direct-method liquidity. Not a three-statement model, not a business
  case, not a P&L review.
license: MIT
---

# Cash Runway

**13-week cash strip + one-page ask** — receipts, disbursements, net burn, runway, collect / delay / draw / cut (owner, date). Default: venture; same spine for F500 (covenants and revolver on page 1).

Method origin: direct-method 13-week cash (TWCF) + net burn / runway. One line, not a model novel.

If they want a CCC / 13-week lecture: one paragraph then produce or stop.

## When to use

- "How much runway?" / "Can we make payroll / the coupon / the vendor?"
- Before a hire, campaign, or vendor commit that spends cash inside 13 weeks
- Collections or payables are the constraint

## When not to use

- Three-statement / IC model — stop; not this skill
- Unit contribution / CAC payback — [Unit Economics](../../strategy/unit-economics/SKILL.md)
- Invest / NPV / options — [Business Case](../../strategy/business-case/SKILL.md)
- Weekly ops KPIs with no cash — [Operating Review](../../management/operating-review/SKILL.md)
- The vendor contract itself — [Vendor SOW](../../management/vendor-sow/SKILL.md)
- Going-concern board paper — [Executive Board Memo](../../management/executive-board-memo/SKILL.md)
- This month's DSO / DIO / DPO / CCC — [Working Capital](../../finance/working-capital/SKILL.md)
- This vs last vs plan on the P&L — [Budget Variance](../../management/budget-variance/SKILL.md)

Accrual P&L "we're profitable" is not the bank. Footnote cash vs EBITDA; do not build IS/BS/CF here.

## Modes

| Mode | When | Output |
|---|---|---|
| **produce** | Default | One-pager + 13-week strip + one ASK |
| **redline** | They pasted a forecast or a P&L labelled "cash" | Rebuild **direct**; variance vs bank; list invented receipts you killed |
| **refuse** | No bank balance, no burn basis, or they want the annual plan | Issues list. Stop |

## Hard rules

1. **Direct method.** Opening cash → receipts → disbursements → net → financing → closing. Closing is next opening. Flag any week below the floor.
2. **Receipts from AR + collection curve (history),** not pipeline or LOIs. Unbilled "sure things" need a name you will defend — or cut them.
3. **Disbursements from payroll, AP, contracts.** Payroll, tax, and debt are not "DPO optimisation."
4. **Net burn from recent actuals** (not the budget). Runway months ≈ (cash or net cash) / monthly net burn. Net cash ≈ cash + AR − AP when material. If net burn ≤ 0, say cash-flow positive; still show weekly timing.
5. **One ASK, ordered:** collect this week → delay named non-critical AP → draw → cut spend. Do not "monitor closely."
6. **Rolling.** Always a new week 13. Variance vs last week's forecast vs bank.
7. **Pasted P&L is not cash.** Do not start from net income.
8. **Do not invent receipts.** Holes stay holes.

## Intake

If **two** of 1, 3, 4 are missing after one round: issues list, not a fake forecast.

1. Entity and bank cash today (accounts, FX, as-of date) — load-bearing
2. Floor — covenant, or 4–6 weeks of opex if none
3. AR aging (or "none / pre-revenue") — load-bearing
4. AP + payroll / tax / debt dates in the next 13 weeks — load-bearing
5. Known one-offs — draw, capex, earn-out, escrow
6. The decision — hire, campaign, vendor, freeze, lender call

Venture is the default skin. F500/PE: covenants and revolver availability on page 1. Distress: minimum cash and draw timing on page 1.

## Output shape

```
CASH / RUNWAY  |  [entity]  |  as-of: [date]  |  CLASS: liquidity
ASK: [owner] to [collect / delay / draw / cut] [amount] by [date].

BLUF
[Claim.] We [make / miss] the floor in week [n]. Runway ~[x] months at net burn [$/mo].

CASH AND FLOOR
Cash today: [ ]  (accounts, FX)
Floor: [ ]  Source: [covenant / 4–6 wks opex]
Minimum closing in 13w: [ ] in week [ ]  Headroom: [ ]

BURN AND RUNWAY
Gross burn: [ ]   Net burn: [ ]   Basis: [last n weeks actual]
Runway: [ ] months  (cash [or net cash = cash+AR−AP] / net burn)
Burn trend: [up / flat / down]  Why: [ ]

COLLECTIONS
DSO: [ ]  Overdue >[n]d: [ ]  Top names / disputes: [ ]
This week's collect list: [name, amount, owner]

PAYABLES
DPO: [ ]  Payroll / tax / debt dates: [ ]
Stretch: [named, amount]  Will not stretch: [payroll, critical, statutory]
Supplier risk if we stretch: [ ]

LINCHPIN
If [receipt / customer / draw] slips, week [n] breaks.

NOT THIS PAGE
CCC this month → working-capital    P&L vs plan → budget-variance    Invest → business-case

Holes: [ ]
```

13-week strip: `assets/thirteen-week.md`.

## QA (must pass)

1. Direct method; not a restated P&L.
2. ASK with owner, verb, amount, date.
3. Floor named; any week below it flagged.
4. Receipts trace to AR/history, or labelled hole.
5. Payroll / tax / debt visible in disbursements.
6. Cash today, net burn, runway as numbers or "unknown".
7. No invented inflows.
8. Strip exists; not an essay.
9. One page + strip.

If 2, 6, or 7 fail: do not ship.

## Escalate / stop

- Bank balance unknown → refuse.
- Going-concern / covenant breach / missed payroll → this page is the exhibit; principal + CFO + counsel.
- They want the 13-week to *be* the annual plan → refuse.
- Stretch statutory/payroll as "working capital excellence" → refuse.
- FX / debt / tax treatment → specialist; flag, do not advise.

## Related

- [Working Capital](../../finance/working-capital/SKILL.md) — CCC this month; this is the bank
- [Budget Variance](../../management/budget-variance/SKILL.md) — accrual vs plan
- [Unit Economics](../../strategy/unit-economics/SKILL.md) — whether a unit should make money
- [Business Case](../../strategy/business-case/SKILL.md) — invest; this is liquidity to survive the invest
- [Vendor SOW](../../management/vendor-sow/SKILL.md) — a commit that becomes a disbursement
- [Operating Review](../../management/operating-review/SKILL.md) — cash is a line, not the whole review
- [Executive Board Memo](../../management/executive-board-memo/SKILL.md) — viability / going concern
