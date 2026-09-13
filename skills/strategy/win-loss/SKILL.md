---
name: win-loss
description: >-
  Use when a named deal just closed won or lost and an MD needs why, from the
  buyer, plus stop/start/continue this quarter. Not a competitive teardown, not
  a customer QBR, not an after-action of our process.
license: MIT
---

# Win Loss

**Named-deal 1-pager** — why we won or lost, what we stop / start / continue, one ASK. Default: venture or mid-market B2B deal.

Method origin: Clozd / Salesforce-public — CRM "lost reason" is usually wrong; the buyer is the source of truth; interviews beat surveys and beat the dropdown. Reconstruct the operator card. Do not dump a win-loss textbook.

If they want a method lecture: one paragraph then produce or stop.

## When to use

- A **named** opportunity just closed-won or closed-lost (or no-decision)
- "Why did we lose [Account]?" / "Why did we actually win?"
- Convert a CRM dropdown into a decision: pricing, qualification, product, process
- After a strategic win: lock what to **continue**, not a victory lap

## When not to use

- Tear down a **named rival's system** — [Competitive Teardown](../../strategy/competitive-teardown/SKILL.md)
- Quarterly review **with** that customer after they bought — [QBR](../../management/qbr/SKILL.md)
- Internal event learning (launch, incident) — [After Action Review](../../management/after-action-review/SKILL.md)
- Weekly pipeline theatre — [Operating Review](../../management/operating-review/SKILL.md)
- Forecast this period's Commit — [Forecast Call](../../commercial/forecast-call/SKILL.md)
- The email that forwards this page — [Pyramid Principle](../../writing/pyramid-principle/SKILL.md)

If they will not name the deal, you do not have a win/loss.

## Modes

| Mode | When | Output |
|---|---|---|
| **produce** | Default. Deal closed | Named-deal 1-pager + stop/start/continue |
| **redline** | They pasted a CRM note or "loss recap" | Same facts; buyer-truth first; kill the dropdown |
| **refuse** | No deal name, or they want a lecture on "how to do win-loss" | Issues list. Stop |

## Hard rules

1. **Name the deal.** Account, amount, close date, competitor or no-decision. Anonymous "we lose on price" is not this skill.
2. **Buyer before rep.** Label every cause **buyer-said / rep-said / inferred**. Inferred cannot carry the ASK.
3. **The AE on the deal does not interview the buyer.** Neutral party (founder, RevOps, CS, third party).
4. **Wins count.** Skipping wins means you will keep claiming differentiators marketing invented.
5. **Stop / start / continue, dated.** Owner + date. "Monitor pricing" is not a continue.
6. **One ASK.** Change qualification, price, product, or process — named owner, this quarter.
7. **Do not invent quotes.** Hole: `[buyer not interviewed — by DATE]`. CRM reason is a hypothesis. No-decision is a result, not a loss to a competitor.

## Intake

Refuse a FOR-SENDING page if the deal is unnamed **and** there is no buyer or CRM evidence.

1. Deal: account, $, won / lost / no-decision, date — load-bearing
2. Who decided (economic buyer) and who we can still ask
3. What the CRM says (reason, competitor)
4. What the buyer said (interview, email, call) — or "not yet"
5. What we will change this quarter if the finding holds
6. Who owns the ASK

## Output shape

```
WIN / LOSS  |  [Won | Lost | No-decision]  |  [ACCOUNT]  |  [date]

ASK: [owner] to [stop / start / change X] by [date]
Primary cause (buyer): [ ]
CRM said: [ ]   Competitor / alternative: [ ]

WHY
[Complete-sentence claim. Buyer evidence in quotes or labelled inferred.]

DECISION PROCESS WE ACTUALLY FACED
- Economic buyer: [ ]
- Criteria they used: [ ]
- When it was really decided: [ ]

STOP / START / CONTINUE (this quarter)
| | Action | Owner | Date |
| Stop | | | |
| Start | | | |
| Continue | | | |

WHAT WE WILL NOT DO
- [price cut / feature / blame] because [ ]

NOT THIS PAGE
Rival system → competitive-teardown    After they bought → qbr    Our event → after-action-review

Holes: [buyer not interviewed — by DATE]
```

## QA (must pass)

1. Named account, amount, date, result.
2. Primary cause is a complete sentence the buyer would recognise.
3. Every load-bearing cause labelled buyer / rep / inferred.
4. CRM reason is not treated as fact.
5. Stop, start, **and** continue present; owners and dates.
6. One ASK, this quarter.
7. No invented quotes.
8. Not a teardown, not a QBR, not an AAR of our sprint.
9. One page.
10. If the buyer was not heard, the hole is on the page and the ASK is "interview by DATE" or the page is issues-only.

If 1, 2, 5, or 6 fail: do not ship.

## Escalate / stop

- They want a method essay → one paragraph, then produce or stop.
- They want the AE to "just ping the buyer" → refuse the interviewer; offer a neutral.
- They want to fire someone from a single deal with no buyer evidence → stop; this page is not HR.
- Pattern across many deals → this skill still does **one** deal; aggregate later.
- Legal / NDA / disparagement of a named competitor in a sendable memo → counsel; keep the page internal.

## Related

- [Competitive Teardown](../../strategy/competitive-teardown/SKILL.md) — rival system; this is one deal's decision
- [QBR](../../management/qbr/SKILL.md) — after they are a customer
- [After Action Review](../../management/after-action-review/SKILL.md) — our event, participants in the room
- [Operating Review](../../management/operating-review/SKILL.md) — internal weekly exceptions
- [Forecast Call](../../commercial/forecast-call/SKILL.md) — this period's Commit, not why a deal closed
- [Pyramid Principle](../../writing/pyramid-principle/SKILL.md) — the email that forwards this page
