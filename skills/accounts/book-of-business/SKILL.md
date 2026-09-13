---
name: book-of-business
description: >-
  Use when ranking ALL accounts this AM/MD owns: health, revenue, renewal date,
  capacity, grow/hold/exit. Not account-plan (one logo), not customer-
  concentration math as the whole job, not account-health.
license: MIT
---

# Book of Business

**Book of Business — Portfolio Heatmap** — one page: every account this AM / MD owns, health, revenue, renewal, days we can spend, grow / hold / exit, one book ASK. Default: venture / professional-services book; same spine for F500 / SaaS CS.

Method origin: Gainsight-public scorecards — RYG per account, not a mystery CHI; operator grow/hold/exit (capacity is the constraint). Do not dump a CS platform manual. Do not run GAAP 10% math as the whole job.

If they want a portfolio-management lecture: one paragraph then produce or stop.

## When to use

- AM / MD must rank *this* book this month (or this quarter)
- Capacity is the constraint: too many yellows, not enough days
- "Which accounts do we grow, hold, or exit?"
- Incoming AM inheriting a book; or before annual planning

## When not to use

- 12-month plan for one named account — [Account Plan](../../accounts/account-plan/SKILL.md)
- Top-N firm revenue / AR risk math — [Customer Concentration](../../strategy/customer-concentration/SKILL.md)
- This month's flags on one account — [Account Health](../../accounts/account-health/SKILL.md)
- Quarterly sitting with one customer — [QBR](../../management/qbr/SKILL.md)
- Our internal weekly P&L exceptions — [Operating Review](../../management/operating-review/SKILL.md)
- Named cliff inside 2Q as the whole job — [Renewal Risk](../../accounts/renewal-risk/SKILL.md)
- ASK is hire — [Headcount Plan](../../management/headcount-plan/SKILL.md)

## Modes

| Mode | When | Output |
|---|---|---|
| **produce** | Default. Account list | Heatmap page + this-period ASK |
| **redline** | They pasted a CRM export or "my book" slide | Force RYG + days + grow/hold/exit |
| **refuse** | Two load-bearing facts missing, or a lecture on health indices | Issues list. Stop |

## Hard rules

1. **Every account this person owns.** Name them. A "strategic segment" with no logos is a fail.
2. **Four columns live:** health (G/Y/R + because), revenue (contracted $ this year), renewal date, days/month we spend (or should).
3. **Grow / hold / exit on every row.** Exit is allowed. "Nurture" is not a verdict.
4. **Capacity math on page 1.** Sum of days the verdicts need vs days the AM has. Over-capacity → name what we drop, not a hero plan.
5. **Count the reds and the cliffs.** Renewals in ≤2 quarters get a flag; route the named one to [Renewal Risk](../../accounts/renewal-risk/SKILL.md).
6. **Do not pretend pipeline logos are the book.** Prospects are a separate line or out.
7. **Do not invent health.** If unused, say `health unknown — score by DATE`. A fake green is a fail.
8. **One ASK for the book this period.** Reassign / exit / hire / freeze new logos. Not ten account slogans.
9. **SaaS CS skin:** usage instead of delivery burn. Spine stays.
10. **One page.** >12 accounts: page 1 is the ranked table + capacity; rest is appendix names.

## Intake

If **two** of 1–3 are missing after one round: issues list, not a fake heatmap.

1. Owner of this book (the AM / MD) — load-bearing
2. Account names, contracted $, renewal dates — load-bearing
3. Days/month this AM has for clients (not admin) — load-bearing
4. Health colour we actually believe (or "unknown")
5. Verdict we already hold (grow/hold/exit) if any
6. The ASK we need this period (reassign / exit / hire / freeze)
7. Period / as-of date

## Output shape

```
BOOK OF BUSINESS  |  [AM / MD]  |  [period]  |  as-of: [date]
ASK: [owner] to [reassign / exit / hire / freeze / fund] by [date]
Accounts: [n]    Book $: [ ]    Days had: [ ]    Days the verdicts need: [ ]
Capacity: FIT / OVER  because [ ]

HEATMAP
| Account | $ | Renew | Health | Because (≤8 words) | Days | G/H/X |
| [ ] | [ ] | [ ] | G/Y/R | [ ] | [ ] | GROW/HOLD/EXIT |

CLIFFS AND REDS
- Renew ≤2Q: [names] → renewal-risk on [name] by [date]
- Red now: [names] → account-health or churn-save

THIS PERIOD (only)
| Move | Owner | Date | Done looks like |
| ASK | [ ] | [ ] | [ ]

NOT THIS PAGE
One logo year → account-plan    Firm top-N → customer-concentration    One logo this month → account-health

Holes: [ ]
```

## QA (must pass)

1. Named owner of the book; period dated.
2. Every owned account is a row, or explicit hole ("3 unnamed — list by DATE").
3. Health, $, renewal, days on each row (or hole labelled).
4. Grow / hold / exit on every row. No "nurture".
5. Capacity: days needed vs days had.
6. One ASK for the book, owner, date.
7. Cliffs (≤2Q) and reds named, not buried.
8. No invented health or pipeline-as-book.
9. Not one account-plan, not firm concentration math as the job.
10. One page (appendix allowed for names >12).

If 1, 2, 4, or 6 fail: do not ship.

## Escalate / stop

- They will not list accounts after one ask → refuse.
- One logo ≥10% of *firm* revenue → [Customer Concentration](../../strategy/customer-concentration/SKILL.md); this page still ranks the AM's book.
- Named account is leaving this month → [Churn Save](../../accounts/churn-save/SKILL.md).
- They want a QBR tour of every logo → refuse; pick one [QBR](../../management/qbr/SKILL.md).
- Fake greens to hide over-capacity → refuse.

## Related

- [Account Plan](../../accounts/account-plan/SKILL.md) — 12 months on one logo
- [Account Health](../../accounts/account-health/SKILL.md) — this month on one logo
- [Customer Concentration](../../strategy/customer-concentration/SKILL.md) — firm top-N math
- [Renewal Risk](../../accounts/renewal-risk/SKILL.md) — named cliff inside 2Q
- [Operating Review](../../management/operating-review/SKILL.md) — *our* week, not this book
- [Headcount Plan](../../management/headcount-plan/SKILL.md) — if the ASK is hire
- [Churn Save](../../accounts/churn-save/SKILL.md) — leaving now
