---
name: headcount-plan
description: >-
  Use when an MD must lock roles, start dates, fully-loaded cost, and freeze vs
  hire for the next 12–18 months. Not a single-role interview scorecard, not an
  org-design essay.
license: MIT
---

# Headcount Plan

A **roles / dates / cost 1-pager**: who we hire or freeze, when, at what fully-loaded $. Default: venture. Output is the **decision pack** for the CEO/CFO sitting, not a workforce-planning novel (3–5 year capability maps live elsewhere).

Public method: SHRM-public — labour often 50–80% of opex; Gartner-public — HR+Finance together cut labour-cost variance; fully-loaded = base + variable + taxes + benefits + ramp (operator rule of thumb 1.25–1.4× base non-sales; higher if commission). Freezes: **targeted** vs blanket (blanket treats a revenue hire like a nice-to-have). Reconstruct the plan. No book dump.

## When to use

- Annual or quarterly people budget: roles, dates, $
- "Hiring freeze or not?" with exceptions named
- Before a raise or a cash squeeze: what we still hire
- Rewrite a 40-req wishlist into a dated, costed list

## When not to use

- **One role's** mission / outcomes / interview loop — [Hiring Scorecard](../../management/hiring-scorecard/SKILL.md) (after a role is **opened**)
- 13-week cash impact of payroll — [Cash Runway](../../management/cash-runway/SKILL.md)
- Monthly P&L bridge — [Budget Variance](../../management/budget-variance/SKILL.md)
- Org chart / spans / design as the whole job (not this skill; do not fake an org-design paper)
- A capability make/buy — [Make vs Buy](../../strategy/make-vs-buy/SKILL.md)

## Modes

| Mode | When | Output |
|---|---|---|
| **produce** | Default | Headcount 1-pager: hire / freeze / backfill + ASK |
| **redline** | They pasted a req list | Cost, dates, freeze vs hire; kill the wishlist |
| **refuse** | No roles *and* no budget, or a lecture on workforce planning | Issues list or one paragraph then stop |

## Hard rules

1. **Each line is a role, a start month, a fully-loaded $.** Title-only wishlists fail.
2. **FTE and headcount both.** Capacity is FTE; recruiting is heads. Part-time and contractors visible.
3. **Fully-loaded, not base.** State the load factor. Do not ship base salary as "cost".
4. **Timing is cash.** A January vs July start is half a year of cost. Phased dates, not "H1 hires".
5. **Freeze is a choice with a type:** blanket / targeted (functions) / backfill-only / soft (extra sign-off). Name exceptions (revenue-critical, safety, already-offered). Blanket without exceptions is allowed only if cash demands it — say so.
6. **Vacancy has a cost.** Some roles cost more to freeze than to fill (quota, plant, security). Write it or you will over-freeze.
7. **Triggers, not vibes.** Hire if [revenue / cash / milestone]; freeze if [runway / miss]. Pre-agree so the quarter is not a fight.
8. **One ASK:** freeze these / hire these / open these reqs. Owner (usually CEO+CFO), date.
9. **Do not invent bands.** Hole the $ .
10. **One page** + a table. Not a 3–5 year capability manifesto.

## Intake

Refuse a FOR-DECISION plan if the role list *and* the cost basis are both missing. Two load-bearing holes → issues list.

1. **Horizon** (12 months default) and who owns the P&L
2. **Current FTE / heads / contractors**
3. **Roles they want**, start months, location, employee vs contractor
4. **Base or loaded cost they actually use**
5. **Cash / freeze pressure** (runway, budget miss)
6. **Who has the D** on exceptions

## Workflow

1. List current vs proposed. Mark hire / backfill / freeze / cut.
2. Cost each line loaded × months active in horizon.
3. Choose freeze type if cost or cash requires it. Name exceptions.
4. Triggers for the next quarter.
5. ASK.

## Output shape

```markdown
# Headcount plan — [entity] — [horizon] — [date]

ASK: [hire these / freeze these / backfill-only] by [date]
Owner after yes: CEO/CFO …    Freeze type: none | targeted | backfill-only | blanket
Load factor used: [1.xx × base]  Source: …

## Now
Heads [ ]  FTE [ ]  Contractors [ ]  Loaded run-rate [$/mo]

## Decisions
| Role | Hire / freeze / backfill | FTE | Start | Loaded $/yr | Horizon cost | Exception? |
|---|---|---|---|---|---|---|
| | | | | | | |

Horizon incremental $: [ ]   vs budget: [ ]

## Freeze / hire rule
- Hire if: …
- Freeze if: …
- Exceptions always: already-offered, statutory, safety
- Vacancy cost we accept by freezing: …

## What we will not do
- Blanket freeze that blocks [named revenue role] without saying the cash math
- Open a req with no start month and no loaded $

## Next paper
Opened role → [Hiring Scorecard](../../management/hiring-scorecard/SKILL.md)
Payroll timing → [Cash Runway](../../management/cash-runway/SKILL.md)
```

## QA (must pass)

1. Each decided role has start month and loaded $.
2. FTE and heads both shown.
3. Load factor named.
4. Freeze type named, or explicit "no freeze".
5. Exceptions named if freeze.
6. One ASK, owner, date.
7. Horizon incremental $ vs budget or cash.
8. No invented salary bands.
9. Not a scorecard for one role, not an org essay.
10. One page + table.

If 1, 3, 6, or 9 fail: do not ship.

## Escalate / stop

- Layoffs / redundancy process → HR + counsel; this skill is hire/freeze, not fire.
- Discrimination in who gets frozen — stop; HR.
- Cash hole inside 13 weeks → [Cash Runway](../../management/cash-runway/SKILL.md) first; this page is the people lever.
- They want a 40-box org redesign — refuse; list roles and cost only.

## Related

- [Hiring Scorecard](../../management/hiring-scorecard/SKILL.md) — one opened role
- [Cash Runway](../../management/cash-runway/SKILL.md) — payroll as disbursement
- [Budget Variance](../../management/budget-variance/SKILL.md) — if people $ were the miss
- [Make vs Buy](../../strategy/make-vs-buy/SKILL.md) — hire vs vendor at capability level
- [Partner Memo](../../strategy/partner-memo/SKILL.md) — hire vs ally vs PO for a named party
- [Org One-Pager](../../management/org-one-pager/SKILL.md) — boxes and spans; this page is costed roles
