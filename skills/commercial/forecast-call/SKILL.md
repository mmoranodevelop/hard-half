---
name: forecast-call
description: >-
  Use when this week's Commit / Best Case / Slip is the period number. Not QBR,
  not book-of-business, not account-health, not renewal-risk.
license: MIT
---

# Forecast Call

**Weekly Forecast Call — Commit / Best Case / Slip** — one page: this-period quota, owner Commit $, Best Case $ and what would have to be true, named Commit deals, named slips since last week, in-period qualified coverage vs quota using *this motion's* win rate. Default: venture; same spine for F500.

Method origin: Salesforce Collaborative Forecasts (Commit / Best Case / Pipeline / Closed; weekly submissions; cumulative vs single) + HubSpot hygiene + Gartner 2020 forecast-confidence survey.

If they want a forecasting lecture: one paragraph then produce or stop.

## When to use

- This week's Commit must be a number leadership can staff to
- Owner submissions are due and the call inspects evidence, not mood
- Close dates walked, or Pipeline is sitting in Commit
- Coverage vs quota needs *this motion's* win rate, not a slogan

## When not to use

- Quarterly account / portfolio review — [QBR](../../management/qbr/SKILL.md)
- Book composition, not this-period Commit — [Book of Business](../../accounts/book-of-business/SKILL.md)
- One account's health score — [Account Health](../../accounts/account-health/SKILL.md)
- One renewal's save plan — [Renewal Risk](../../accounts/renewal-risk/SKILL.md)
- One account already leaving — [Churn Save](../../accounts/churn-save/SKILL.md)
- Named exec meeting as Commit evidence — [Exec Sponsor Live](../../commercial/exec-sponsor-live/SKILL.md)
- Non-standard terms on a Commit deal — [Deal Desk](../../commercial/deal-desk/SKILL.md)

## Modes

| Mode | When | Output |
|---|---|---|
| **produce** | Default. Named deals + a period | Commit / Best Case / Slip page + ASK |
| **redline** | They pasted a CRM export or a "we will hit it" deck | Force named Commit lines; kill water and sandbag |
| **refuse** | Two load-bearing facts missing, or Pipeline relabelled Commit | Issues list. Stop |

## Hard rules

1. **Clock is weekly.** A period label (Q1, "this quarter") is not the call. Salesforce Forecast Submissions exist so the owner submits *this period's* Commit — inspect that, not a stage-weighted sum.
2. **Commit is evidence, not a picklist.** Last buyer evidence + paper-process (MEDDPICC) + close date. Pipeline in Commit is water. A verbal-yes held in Best Case until week 12 is sandbag.
3. **Name the deals.** A rolled-up $ is not a Commit. Each line: account, amount, close date, last buyer evidence.
4. **Slip is a reason.** Close-date move since last week needs a reason (HubSpot: probability jump >15 pts needs notes). Repeat slips leave Commit.
5. **Coverage is arithmetic, not 3x.** In-period qualified pipeline / quota vs 1÷trailing win rate on the *same qualified definition*. If win rate is unknown, say so — do not invent 3x.
6. **Cumulative vs single.** Cumulative: Commit Forecast = Commit + Closed; Best Case Forecast = Best Case + Most Likely + Commit + Closed. Mixing them is water.
7. **Commit that always equals quota is political.** Gartner: only 45% of sales leaders/sellers have high forecast-accuracy confidence. Salesforce 6th ed.: 67% of reps do not expect to meet quota this year. Do not force Commit = quota.
8. **Accuracy is Commit-that-closed**, not "we were close if you count Best Case."
9. **Do not invent amounts or close dates.** Holes stay holes.

## Intake

If **two** of 1–4 are missing after one round: issues list, not a fake call.

1. Named Commit deals for *this period* (account, $, close date) — load-bearing
2. Weekly owner-submitted Commit, distinct from stage-weighted pipeline — load-bearing
3. Slip list: deals that moved out of period since last week, with reason — load-bearing
4. In-period coverage vs quota, with the win rate used (or "win rate unknown") — load-bearing
5. This-period quota and Best Case $ (what would have to be true)
6. Who owns the call (forecast D) and as-of date
7. Last week's Commit vs this week's (or "first call this period")

## Output shape

```
WEEKLY FORECAST CALL  |  [period]  |  as-of: [date]  |  owner: [name]
Quota this period: [$]     Submitted Commit: [$]     Best Case: [$]
Win rate used: [%] or HOLE     Coverage: [in-period qualified $ / quota] vs 1÷win rate

COMMIT (evidence this period — not Pipeline)
| Account | $ | Close | Last buyer evidence | Paper process | Slip risk |
| [ ] | [ ] | [ ] | [ ] | [ ] | L/M/H |

BEST CASE (what would have to be true)
| Account | $ | Must be true this period | Why not Commit |
| [ ] | [ ] | [ ] | [ ]

SLIPS SINCE LAST WEEK
| Account | Was $ / date | Now $ / date | Reason | Leaves Commit? |
| [ ] | [ ] | [ ] | [ ] | Y/N |

WATER / SANDBAG FLAGS
- Water: [Pipeline or Best Case sitting in Commit — name them]
- Sandbag: [real Commit held in Best Case — name them]

NOT THIS PAGE
QBR → qbr    Book mix → book-of-business    One account → account-health    One renewal save → renewal-risk

ASK: [forecast D] signs Commit $ [n] by [this week]. Slips named. Coverage hole: [or none].
Holes: [ ]
```

## QA (must pass)

1. Period + as-of date + named forecast D.
2. Commit is named deals, not a roll-up speech.
3. No Pipeline line in Commit without a downgrade.
4. Each slip has a reason and a new date.
5. Coverage uses this motion's win rate, or the page says "win rate unknown — cannot compute coverage." No invented 3x.
6. ASK + owner + date this week.
7. Not a QBR, not a book mix, not an account-health score.
8. No invented amounts.
9. One page.

If 2, 5, 6, or 8 fail: do not ship.

## Escalate / stop

- Relabel Pipeline as Commit because coverage looks thin → refuse (water). Gartner: bogus Commit drives bogus discounts and bogus spend.
- Hold a verbal-yes out of Commit to sandbag next period → refuse.
- They want a quarterly narrative instead of this week's deals → [QBR](../../management/qbr/SKILL.md).
- Win rate unknown and they insist on "3x coverage" → refuse the slogan; coverage is 1÷win rate or a hole.

## Related

- [QBR](../../management/qbr/SKILL.md) — quarterly review; this is weekly Commit
- [Book of Business](../../accounts/book-of-business/SKILL.md) — book mix, not this period
- [Account Health](../../accounts/account-health/SKILL.md) — one account
- [Renewal Risk](../../accounts/renewal-risk/SKILL.md) — a renewal may appear as a Commit line; the save plan is that skill
- [Exec Sponsor Live](../../commercial/exec-sponsor-live/SKILL.md) — named exec meeting is Commit evidence, not a silent logo
- [Deal Desk](../../commercial/deal-desk/SKILL.md) — non-standard terms on a Commit deal
- [Bid No-Bid](../../commercial/bid-no-bid/SKILL.md) — whether to pursue; this page is in-period $
