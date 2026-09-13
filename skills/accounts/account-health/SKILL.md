---
name: account-health
description: >-
  Use when scoring ONE named account this month: usage/delivery, relationship,
  commercial flags, one ASK. NOT for qbr (quarterly sitting), not book-of-
  business, not renewal-risk, not churn-save.
license: MIT
---

# Account Health

**Account Health — This Month, One Named Account** — one page: delivery (or usage), relationship, commercial — each RYG with a because — overall = worst material flag, one ASK this month. Default: venture / professional-services book; same spine for F500 / SaaS CS.

Method origin: Gainsight/Totango-public health — several dimensions roll to RYG; a stale score is a hole; colour without a because is theatre. Do not invent a house CHI formula.

If they want a health-score lecture: one paragraph then produce or stop.

## When to use

- Named account this month: is it green, and what do we do
- CRM health colour is stale or unexplained
- Before a QBR, so the sitting is not a colour argument
- A yellow just flipped, or a champion went quiet

## When not to use

- Quarterly sitting with the customer — [QBR](../../management/qbr/SKILL.md)
- Heatmap of all accounts this AM owns — [Book of Business](../../accounts/book-of-business/SKILL.md)
- 12-month plan — [Account Plan](../../accounts/account-plan/SKILL.md)
- Named renewal inside 2 quarters as the whole job — [Renewal Risk](../../accounts/renewal-risk/SKILL.md)
- They are leaving now — [Churn Save](../../accounts/churn-save/SKILL.md)
- Promised vs delivered value this period — [Value Realization](../../accounts/value-realization/SKILL.md)
- Angry client this week — [Client Escalation](../../accounts/client-escalation/SKILL.md)

## Modes

| Mode | When | Output |
|---|---|---|
| **produce** | Default. Named account | This-month health page + ASK |
| **redline** | They pasted a dashboard or CRM colour | Force because + ASK; kill the mystery index |
| **refuse** | Two load-bearing facts missing, or "explain CHI" | Issues list. Stop |
| **diagnose** | Colour flipped with no because | Name the stale flag; still ship the page or issues list |

## Hard rules

1. **One named account. This month.** Not a year tour.
2. **Three flags, always:** delivery (PS: milestone / burn / quality; SaaS: usage), relationship (buyer + champion last contact), commercial (AR / renewal / scope).
3. **Each flag is G/Y/R + because (≤12 words) + evidence date.** Colour without because is a fail.
4. **Overall is the worst material flag**, not an average that hides a red.
5. **Stale >30 days is not green.** Hole it.
6. **One ASK this month.** Call / recover / resource / intro / stop. Owner, date.
7. **Do not invent NPS, usage, or ROI.** Hole: `[not measured — proxy by DATE]`.
8. **Single-threaded relationship is at best yellow.**
9. **Not a QBR pack.** Last-quarter goals appear only as evidence for a flag.
10. **One page.**

## Intake

If **two** of 1–3 are missing after one round: issues list, not a fake colour.

1. Named account, our owner, period (this month) — load-bearing
2. Delivery / usage we actually have — load-bearing
3. Last contact with economic buyer and with champion — load-bearing
4. Commercial: AR, renewal date, scope fight
5. The ASK this month
6. What flipped if a colour moved
7. As-of date of the evidence (or "stale")

## Output shape

```
ACCOUNT HEALTH  |  [ACCOUNT]  |  [month]  |  as-of: [date]
ASK: [owner] to [call / recover / resource / intro / stop] by [date]
Our owner: [ ]    Economic buyer last contact: [date or never]
Champion last contact: [date or never]    Single-threaded: yes/no
Overall: G / Y / R  because [worst material flag]

FLAGS
| Flag | RYG | Because (≤12 words) | Evidence date | If we do nothing |
| Delivery / usage | [ ] | [ ] | [ ] | [ ]
| Relationship | [ ] | [ ] | [ ] | [ ]
| Commercial | [ ] | [ ] | [ ] | [ ]

THIS MONTH
| Move | Owner | Date | Done looks like |
| ASK | [ ] | [ ] | [ ]

NOT THIS PAGE
Quarterly sitting → qbr    Whole book → book-of-business    Leaving now → churn-save    Named cliff → renewal-risk

Holes: [ ]
```

## QA (must pass)

1. Named account, month, our owner.
2. Three flags, each with because and evidence date (or hole).
3. Overall = worst material flag, not a smoothing average.
4. Stale >30 days not scored green.
5. One ASK, owner, date.
6. Single-thread flagged.
7. No invented NPS / usage / ROI.
8. Not a QBR sitting pack, not a book heatmap, not a 12-month plan.
9. One page.

If 1, 2, 5, or 7 fail: do not ship.

## Escalate / stop

- Colour is red *and* they said they are leaving → [Churn Save](../../accounts/churn-save/SKILL.md).
- Renewal inside 2Q is the live fight → [Renewal Risk](../../accounts/renewal-risk/SKILL.md).
- They want the whole book coloured → [Book of Business](../../accounts/book-of-business/SKILL.md).
- No account name after one ask → refuse.
- They insist on a house CHI formula with no because → refuse the theatre.

## Related

- [QBR](../../management/qbr/SKILL.md) — the quarterly sitting this page may feed
- [Book of Business](../../accounts/book-of-business/SKILL.md) — all logos this AM owns
- [Account Plan](../../accounts/account-plan/SKILL.md) — the year
- [Value Realization](../../accounts/value-realization/SKILL.md) — promised vs delivered evidence
- [Renewal Risk](../../accounts/renewal-risk/SKILL.md) — named cliff inside 2Q
- [Churn Save](../../accounts/churn-save/SKILL.md) — leaving now
- [Client Escalation](../../accounts/client-escalation/SKILL.md) — angry this week
