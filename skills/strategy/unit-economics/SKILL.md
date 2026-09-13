---
name: unit-economics
description: >-
  Use when an MD must defend whether one more unit (customer, order, SKU,
  subscription) creates or destroys cash: contribution, payback, cohort vs
  blended. CAC/LTV only if a repeating customer and real numbers. Not a three-
  statement model or a business case.
license: MIT
---

# Unit Economics

**Unit-economics 1-pager** — named unit, contribution waterfall, payback, cohort vs blended, linchpin, ASK. An MD can defend scale / freeze / kill / price from it. Default: venture.

Method origin: contribution margin (OpenStax) + marketplace take vs GMV (a16z) + payback/cohort (Skok, Gurley). If they ask to be taught LTV: one paragraph, then produce or stop. Do not invent a house Rule of 40.

## When to use

- "Do unit economics work?" / "Should we scale this channel / SKU / geo?"
- Pricing, mix, or subsidy that hangs on contribution
- Diligence on a venture or an F500 line that behaves like a product
- Someone handed GMV, bookings, or downloads as if they were profit

## When not to use

- Investment case with options and capital — [Business Case](../../strategy/business-case/SKILL.md)
- 13-week cash / runway — [Cash Runway](../../management/cash-runway/SKILL.md)
- Weekly KPI review — [Operating Review](../../management/operating-review/SKILL.md)
- Price architecture (metric, fences, GBB) — [Pricing One-Pager](../../strategy/pricing-one-pager/SKILL.md) (this page supplies the floor)
- One-off custom project with no repeating unit — [Vendor SOW](../../management/vendor-sow/SKILL.md); refuse CAC/LTV
- The email that carries this page — [Pyramid Principle](../../writing/pyramid-principle/SKILL.md)

## Modes

| Mode | When | Output |
|---|---|---|
| **produce** | Default | Filled 1-pager + ASK |
| **redline** | They pasted GMV / blended LTV / a "growth story" | Fail QA; name the lie; rewrite the waterfall |
| **refuse** | No unit, or project book dressed as SaaS | Issues list. Stop |

## Hard rules

1. Name the unit in one noun before any ratio. "The business" is not a unit.
2. CM$ = revenue kept minus variable costs of that unit. List in/out. GAAP gross is not CM if variable serving is omitted.
3. Negative contribution is a stop. Do not recommend scale.
4. GMV is not revenue. Bookings are not revenue. Downloads are vanity. GMV may sit as size context next to take — never as the headline.
5. CAC/LTV only if a repeating acquired customer, actuals or labelled assumptions, full CAC, paid vs blended named, contribution not revenue in LTV. Else omit LTV and say why.
6. Payback over LTV:CAC when life is a guess. Payback months = CAC / monthly CM. Observable. Cohort over blended: at least two vintages or write "blended only — confidence low".
7. Do not invent numbers. Services/project: utilisation, realisation, project CM — sentence **this book is not unit-economic**.

Type to primary metrics: product-LOB = CM and mix. SaaS = CM, payback, GRR/NRR, cohort. Marketplace = take rate, CM per completed take. Services = project CM, utilisation — no CAC. Hybrid = split the page.

## Intake

If **two** of 1–3 are blank after one round: issues list, not a fake 3x.

1. Unit (one noun) and type (product-LOB / SaaS / marketplace / services / hybrid) — load-bearing
2. Revenue you keep vs GMV/bookings — last 12 months actuals — load-bearing
3. Decision (scale / freeze / kill / price) — load-bearing
4. Variable cost list (what moves with the unit)
5. Cuts they have (channel, SKU, vintage)
6. If subscription/marketplace: S&M, new customers, expansion, gross and net churn, cohort table

## Output shape

```
UNIT ECONOMICS  |  [entity / LOB]  |  [date]  |  Decision: [scale / freeze / kill / price]

ASK: [owner] to [verb] [unit/channel] by [date]
Governing thought: [complete sentence — CM and payback]. Cost of delay: [ ]

UNIT AND WATERFALL (actuals, date, source)
Activity (GMV/TCV if any): [ ]   <- not revenue
Revenue kept: [ ]   Take / price: [ ]
Variable costs in CM: [list]
Contribution: [$ / unit] ([%])   vs last period: [ ] or [HOLE]

PAYBACK AND CAC  (omit if not a repeating acquired customer — say why)
CAC paid / blended: [ ]  Definition: [what's in]
Payback: [n] months  (formula + GM used)
LTV: [12m observed / 24m observed / not shown — reason]
LTV:CAC: [ ]  <- secondary; assumptions: [churn, life]

COHORT VS BLENDED
Blended CM% or NRR: [ ]  Why it misleads: [ ]
Vintage A / B at M12: still-active [ ]  CM [ ]
Gross churn [ ]  Net revenue churn [ ]  (net hides losses)

LINCHPIN
If [assumption] is false, reverse. Watch [indicator] by [date].

NOT THIS PAGE
Invest/kill with options → business-case    13-week cash → cash-runway    Price architecture → pricing-one-pager

Holes: [ ]
```

## QA (must pass)

1. ASK + owner + date. Unit is a noun; type classified.
2. Governing thought is a disagreeable complete sentence (scale / freeze / kill / not-a-unit-business).
3. Waterfall shows revenue kept and CM. GMV is not the headline. In/out of CM listed.
4. If CAC/LTV appears: repeating customer, paid vs blended, contribution not revenue, cohort not only blend. Payback present whenever CAC is.
5. At least one cut, or "blended only — confidence low".
6. Linchpin named. No invented numbers; holes labelled.
7. Services/project books carry the flag, not a fake 3x.
8. One page.

If 1, 3, or 6 fail: do not ship.

## Escalate / stop

- No unit after one ask → issues list.
- Project book dressed as SaaS CAC/LTV → refuse; utilisation / realisation / project CM only.
- They insist GMV is the headline → refuse the vanity.
- They want a three-statement model / NPV options → [Business Case](../../strategy/business-case/SKILL.md).
- Cash this week, not unit CM → [Cash Runway](../../management/cash-runway/SKILL.md).

## Related

- [Business Case](../../strategy/business-case/SKILL.md) — invest/kill with options; this is the unit exhibit
- [Pricing One-Pager](../../strategy/pricing-one-pager/SKILL.md) — architecture; this is the floor
- [Cash Runway](../../management/cash-runway/SKILL.md) — 13-week cash; unit CM does not pay payroll if DSO is long
- [Operating Review](../../management/operating-review/SKILL.md) — weekly; this designs the engine
- [Vendor SOW](../../management/vendor-sow/SKILL.md) — one-off custom work is not a repeating unit
- [Pyramid Principle](../../writing/pyramid-principle/SKILL.md) — the email that carries this page
