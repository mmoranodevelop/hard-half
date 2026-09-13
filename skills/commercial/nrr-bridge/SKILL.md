---
name: nrr-bridge
description: >-
  Use for a logo→NRR revenue bridge: beginning book, new, expansion,
  contraction, churn; one ASK. Not cohort-retention (cohort curves), not
  renewal-risk (one account), not book-of-business, not account-health.
license: MIT
---

# NRR Bridge

**ARR/MRR bridge one-pager** — beginning recurring revenue → + new logos → + expansion → − contraction → − churn → ending; GRR and NRR read off the same bridge; one ASK. Default: venture SaaS board pack; same spine for F500 subscription lines.

Method origin: Bessemer public Good/Better/Best NRR ladder + retention definition (existing-cohort view). ChartMogul / ProfitWell-public NRR definitions — NRR = (start + expansion − contraction − churn) / start; new logos excluded from NRR; GRR caps at 100% without expansion.

If they want a retention-metrics lecture: one paragraph then produce or stop.

## When to use

- Board / ELT needs the period bridge (new / expansion / contraction / churn), not a slogan NRR
- "Are we growing the book or buying logos?" must be visible on one page
- GRR vs NRR must reconcile from the same movements
- Forecast or fundraising pack needs a labelled bridge before narrative

## When not to use

- Logo vs GRR vs NRR by cohort age — [Cohort Retention](../../commercial/cohort-retention/SKILL.md)
- One named renewal in distress — [Renewal Risk](../../accounts/renewal-risk/SKILL.md)
- Book mix / coverage / capacity — [Book of Business](../../accounts/book-of-business/SKILL.md)
- Multi-signal health of one account — [Account Health](../../accounts/account-health/SKILL.md)
- One logo save plan — [Churn Save](../../accounts/churn-save/SKILL.md)
- Top-N revenue share — [Customer Concentration](../../strategy/customer-concentration/SKILL.md)

## Modes

| Mode | When | Output |
|---|---|---|
| **produce** | Default. Period + beginning $ known or HOLE | Bridge + GRR/NRR + one ASK |
| **redline** | They pasted blended NRR or "NRR 120%" without movements | Force the five lines; kill the blend |
| **refuse** | No period, no beginning book, and they want a benchmark NRR | Issues list. Stop |

## Hard rules

1. **One bridge, one period.** Name start date, end date, and currency. Constant-currency note if FX matters — or HOLE.
2. **Five movements.** Beginning → New → Expansion → Contraction → Churn → Ending. Arithmetic must tie or the gap is labelled.
3. **NRR excludes new logos.** ChartMogul/Bessemer: NRR is the existing cohort. New is on the bridge for ARR growth; it is not in the NRR numerator.
4. **GRR and NRR from the same bridge.** GRR = (start − contraction − churn) / start (≤100%). NRR = (start + expansion − contraction − churn) / start (can exceed 100%). Do not compute them from different cohorts.
5. **Logo count is optional but honest.** If logo adds/losses are shown, they do not replace $ movements.
6. **Do not invent NRR, GRR, or $.** Holes stay holes. Bessemer 100/110/120+ is context ladder, not a fake target on their page.
7. **Not a cohort age table.** Aged curves are [Cohort Retention](../../commercial/cohort-retention/SKILL.md).
8. **One ASK.** Accept bridge / investigate contraction / own churn driver — not "improve retention."

## Intake

If **period** and **beginning recurring $** are both missing after one round: issues list.

1. Period (start→end) and metric grain (ARR / MRR)
2. Beginning recurring revenue ($) — load-bearing
3. New / expansion / contraction / churn $ (or HOLE per line)
4. Definition of customer / logo and recurring boundary
5. Currency / constant-currency policy or HOLE
6. Audience (board / ELT / fundraising) + decide-by
7. Suspected driver (contraction vs logo churn vs weak expansion) or unknown

## Output shape

```
NRR BRIDGE  |  [ARR/MRR]  |  period: [start → end]  |  currency: [ ]
ASK: accept bridge | investigate [contraction/churn] | owner [ ] by [date]

| Line | $ | Notes |
| Beginning | [ ] | cohort freeze rule: [ ] |
| + New logos | [ ] | excluded from NRR |
| + Expansion | [ ] | upsell / seat / price / cross |
| − Contraction | [ ] | downgrade / seat loss |
| − Churn | [ ] | logo exit $ |
| Ending | [ ] | must tie: begin+new+exp−con−churn |

GRR = (begin − con − churn) / begin = [ ]% or HOLE
NRR = (begin + exp − con − churn) / begin = [ ]% or HOLE
Bessemer ladder (context): NRR 100 / 110 / 120+% — not a fake target.

LOGO (optional): start [n]  +new [ ]  −lost [ ]  end [ ]
NOT THIS PAGE: cohort age → cohort-retention | one renewal → renewal-risk | book mix → book-of-business | one account → account-health
HOLES: [ ]
```

## QA (must pass)

1. Period and grain named.
2. Five movement lines present; ending ties or gap labelled.
3. NRR formula excludes new; GRR excludes expansion.
4. No invented % or $.
5. One ASK + owner + date.
6. Not cohort-retention, renewal-risk, book-of-business, or account-health.
7. One page.

If 2, 3, 4, or 5 fail: do not ship.

## Escalate / stop

- Headline NRR with no bridge → refuse (redline to bridge).
- Expansion masking churn while GRR hidden → show both; if they refuse GRR, stop.
- One logo dominates the bridge → flag fragility; concentration math → [Customer Concentration](../../strategy/customer-concentration/SKILL.md).
- "Save this account" → [Churn Save](../../accounts/churn-save/SKILL.md) / [Renewal Risk](../../accounts/renewal-risk/SKILL.md).

## Related

- [Cohort Retention](../../commercial/cohort-retention/SKILL.md) — aged logo/GRR/NRR curves
- [Renewal Risk](../../accounts/renewal-risk/SKILL.md) — one renewal
- [Book of Business](../../accounts/book-of-business/SKILL.md) — book mix
- [Account Health](../../accounts/account-health/SKILL.md) — one account signals
- [Churn Save](../../accounts/churn-save/SKILL.md) — named logo save
- [Customer Concentration](../../strategy/customer-concentration/SKILL.md) — top-N share
- [Forecast Call](../../commercial/forecast-call/SKILL.md) — forward view using this bridge as input
