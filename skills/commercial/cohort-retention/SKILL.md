---
name: cohort-retention
description: >-
  Use to inspect logo vs GRR vs NRR by cohort age, not blended company NRR. NOT
  for customer-concentration, not churn-save, not unit-economics.
license: MIT
---

# Cohort Retention

**Cohort Retention — Logo vs GRR vs NRR by Age** — one page: each acquisition month/quarter as a row; columns at 3 / 6 / 12 / 24 months for logo %, GRR %, NRR %; one line on whether expansion is masking GRR; starting revenue and logo count per cohort. No top-N table. No single-account save. Default: venture SaaS; same spine for F500.

Method origin: Bessemer public Good/Better/Best (NRR 100/110/120+, logo >85/>90/95+) + Bessemer Scaling to $100M GRR vs NRR split + ChartMogul cohort definitions (logo ≠ GRR ≠ NRR; 5%/mo ≈ 46% annual logo loss).

If they want a retention-metrics lecture: one paragraph then produce or stop.

## When to use

- Leadership is quoting a blended NRR as if it were operating insight
- A young cohort is rotting while expansion on older logos prints "healthy" NRR
- Need logo vs GRR vs NRR on the same aged rows before a board or forecast conversation
- Month-3 drop vs month-12 annual-plan drop vs year-2 NRR decay must be separated

## When not to use

- Top-N revenue share — [Customer Concentration](../../strategy/customer-concentration/SKILL.md)
- One named account in distress — [Churn Save](../../accounts/churn-save/SKILL.md)
- Cost/payback of one more unit — [Unit Economics](../../strategy/unit-economics/SKILL.md)
- One renewal's save plan — [Renewal Risk](../../accounts/renewal-risk/SKILL.md)
- Quarterly account review — [QBR](../../management/qbr/SKILL.md)
- Burning a logo with a sloppy ask — [Reference Ask](../../commercial/reference-ask/SKILL.md)
- Book mix rather than aged retention — [Book of Business](../../accounts/book-of-business/SKILL.md)

## Modes

| Mode | When | Output |
|---|---|---|
| **produce** | Default. Cohorts definable; three metrics available or HOLE | Aged table + masking line + ASK |
| **redline** | They pasted a blended NRR slide or a "we are at 120%" board line | Force logo + GRR + NRR by age; kill the blend |
| **refuse** | Two load-bearing facts missing, or they want one company NRR as the page | Issues list. Stop |

## Hard rules

1. **Clock is cohort age, not a blended NRR.** A cohort = customers whose first paid start falls in period T. Do not add later logos to an old cohort (ChartMogul).
2. **Three columns, they diverge.** Logo / customer retention counts heads (cannot exceed 100%). GRR / GDR is revenue kept excluding expansion (cannot exceed 100%). NRR / NDR includes expansion and can exceed 100%. ChartMogul worked example: logo 75%, NRR 103.9%, GRR 81.8%.
3. **Expansion can mask churn.** "Net retention of 105% could be 90% GRR + 15% expansion or 70% GRR + 35% expansion." Without GRR you cannot tell. Never report Bessemer-best 120%+ NRR while hiding <85% GRR or a young cohort falling apart at month 3.
4. **Starting n and $ are on the page.** A 120% NRR on five customers is visible as fragile.
5. **Age views:** month 3 = onboarding/acquisition (not "CS failed at month 18"); month 12 = logo vs GRR vs NRR vs Bessemer ladders; month 24 = NRR decay (ChartMogul: year-1 expanders do not repeat). ChartMogul also flags a drop at months 11–12 (annual-plan churn).
6. **Bessemer ladders are two ladders, not one.** Typical Series B/C enterprise: NRR 100 / 110 / 120+%; logo >85 / >90 / 95+%. A company can clear "best" NRR with logo stuck at "good" — that is expansion concentration, not health. GRR typically 85–90% across ARR scale (Bessemer Scaling to $100M); SMB exception they name: HubSpot pre-IPO 70–80% GRR. Segment matters: Mindbody 109% NRR on ~$2K ACVs vs Okta 123% on $50K+.
7. **Act on the worst aged cohort**, not the blended number. One-account saves are [Churn Save](../../accounts/churn-save/SKILL.md). Top-N share is [Customer Concentration](../../strategy/customer-concentration/SKILL.md).
8. **5% monthly logo churn ≈ 46% of a cohort gone in a year** (ChartMogul). Treat that as the logo clock, not a slogan.
9. **Do not invent NRR, GRR, or logo %.** Holes stay holes. Do not borrow McKinsey 113/98 — that page was not fetched.

## Intake

If **two** of 1–4 are missing after one round: issues list, not a fake table.

1. Cohort definition (start month/quarter of first paid contract) — load-bearing
2. Logo **and** GRR **and** NRR as three columns — load-bearing
3. Age (at least a 12-month view; year-2 if it exists) — load-bearing
4. Starting revenue and logo count of each cohort — load-bearing
5. Motion / ACV band (SMB vs enterprise — Bessemer Mindbody vs Okta)
6. Worst aged cohort already suspected, or "unknown"
7. Board / forecast date this page must land before

## Output shape

```
COHORT RETENTION — LOGO vs GRR vs NRR BY AGE  |  as-of: [date]  |  motion: [SMB / MM / ENT]
Cohort = first paid start in period T. Later logos do not join old cohorts.

| Cohort (start) | Start logos | Start $ | Logo 3 / 6 / 12 / 24 | GRR 3 / 6 / 12 / 24 | NRR 3 / 6 / 12 / 24 |
| [YYYY-MM] | [n] | [$] | [%] | [%] | [%] |

MASKING LINE: expansion is / is not hiding GRR. Worst case on this page: NRR [ ] = GRR [ ] + expansion [ ].
Worst aged cohort: [T] because [logo / GRR / NRR cell]. Action is the cohort, not the blend.

BESSEMER LADDERS (context, not a fake target): NRR 100/110/120+%    logo >85/>90/95+    GRR typically 85–90% (SMB may print lower).
ChartMogul clock: 5%/mo logo ≈ 46% annual loss. Month-3 drop = onboarding. Months 11–12 = annual-plan. Year-2 = NRR decay.

NOT THIS PAGE
Top-N share → customer-concentration    One account save → churn-save    CAC/LTV of one more unit → unit-economics    One renewal → renewal-risk

ASK: [D] accepts the aged table (not the blended NRR) by [date]. Worst cohort owner: [name] by [date].
Holes: [ ]
```

## QA (must pass)

1. Cohort definition is first-paid start, not "all customers this year."
2. Logo, GRR, and NRR are three columns. NRR alone is a fail.
3. Starting n and $ are on every row.
4. At least a 12-month view, or the hole is labelled.
5. Masking line is a sentence with numbers, not "retention is healthy."
6. ASK + owner + date.
7. Not a top-N concentration table, not a save plan, not a CAC/LTV page.
8. No invented percentages. No McKinsey 113/98. No blended NRR as the headline.
9. One page.

If 2, 5, 6, or 8 fail: do not ship.

## Escalate / stop

- Report 120% NRR while hiding <85% GRR or a month-3 collapse → refuse (ChartMogul: expansion masking churn).
- Average all cohorts into one NRR and call it operating insight → refuse.
- One logo is the NRR → show it as fragility on this page, then route the concentration math to [Customer Concentration](../../strategy/customer-concentration/SKILL.md).
- "Save this account" as the job → [Churn Save](../../accounts/churn-save/SKILL.md).

## Related

- [Customer Concentration](../../strategy/customer-concentration/SKILL.md) — top-N share; this page may *reveal* that one logo is the NRR
- [Churn Save](../../accounts/churn-save/SKILL.md) — one named account
- [Unit Economics](../../strategy/unit-economics/SKILL.md) — cost/payback of one more unit
- [Renewal Risk](../../accounts/renewal-risk/SKILL.md) — one renewal
- [QBR](../../management/qbr/SKILL.md) — quarterly account review
- [Book of Business](../../accounts/book-of-business/SKILL.md) — book mix, not aged retention
- [Reference Ask](../../commercial/reference-ask/SKILL.md) — do not burn a referenceable logo; that is a cohort event
