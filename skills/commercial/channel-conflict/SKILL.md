---
name: channel-conflict
description: >-
  Use when two partners (or partner plus direct) are on the same account this
  week: timestamp the evidence, name one referee, assign one pursuer, and give
  the buyer one price. NOT for a partner-memo and NOT for a vendor-sow.
license: MIT
---

# Channel Conflict

**Channel Conflict — Two Partners, One Account, One Quote** — account, partner A (evidence + timestamp), partner B (evidence + timestamp), direct involved Y/N, registration status, named referee, one assigned pursuer, one price to the buyer, protection window, what the other party gets, customer communication (one quote). Default: venture; same spine for F500.

Method origin: HubSpot horizontal channel conflict (same-level partners, same customers, same-price discipline) + Magentrix/Track360 deal-registration operating rules (timestamp, exclusivity window, one quote).

If they want a partner-program lecture: one paragraph then produce or stop.

## When to use

- Two named parties (two partners, or partner + direct) on one named account *this week*
- Two quotes, two registrations, or two active pursuits on the same buyer
- Customer has already seen competing prices
- A registration was approved and direct is about to close around it

## When not to use

- How to work with **one** named partner — [Partner Memo](../../strategy/partner-memo/SKILL.md)
- Delivery scope with one vendor — [Vendor SOW](../../management/vendor-sow/SKILL.md)
- Two inherited price lists post-M&A — [Packaging Collision](../../ma/packaging-collision/SKILL.md)
- One named discount vs list — [Discount Exception](../../strategy/discount-exception/SKILL.md)
- Non-standard terms package on the surviving quote — [Deal Desk](../../commercial/deal-desk/SKILL.md)
- This week's Commit number — [Forecast Call](../../commercial/forecast-call/SKILL.md)

## Modes

| Mode | When | Output |
|---|---|---|
| **produce** | Default. Two parties + one account | One owner, one price, one quote + ASK |
| **redline** | They pasted "let the customer pick" or dual quotes | Freeze the second quote; force a referee |
| **refuse** | Two load-bearing facts missing, or they want both to quote | Issues list. Stop |

## Hard rules

1. **Clock is this week: two parties, one account.** Unresolved conflict is two quotes — the customer-visible failure (Magentrix; HubSpot discount conflict). Salesforce 6th ed.: 89% of sales teams already use partner sales. Conflict is the default once two routes can quote the same buyer.
2. **Freeze additional quotes** the same day you detect overlap.
3. **Named referee** with authority to pick one owner. "Let the customer decide" is not a rule.
4. **One price to the buyer.** HubSpot/Magentrix: competing prices *are* the conflict. Harry's public example: same price regardless of channel. If both created value, name a co-sell split *internally*; the buyer still sees one quote and one price.
5. **Apply the published rule, not who discounted first.** First *valid* registration, or documented active direct engagement, or evidence of who created demand. Magentrix: unenforced rules are worse than none. Track360: first valid registration wins unless direct already has *active* engagement — then decline *with explanation*.
6. **Pay the registered partner.** Track360: the fastest way to destroy a partner program is to approve a deal registration and then close the deal through direct without paying. One incident poisons the channel.
7. **Tell the loser the rule and the evidence the same day.** Protection window on the page (Magentrix 30–90 days; Track360 90–180 as public operating ranges — use *your* published window, or HOLE).
8. **Repeat collisions in one territory** = over-recruitment or bad boundaries (HubSpot) — still not a [Partner Memo](../../strategy/partner-memo/SKILL.md) for a single counterparty.
9. **Do not invent timestamps, prices, or registration IDs.** Holes stay holes.

## Intake

If **two** of 1–4 are missing after one round: issues list, not a fake resolution.

1. Two named parties (two partners, or partner + direct) on one named account — load-bearing
2. Evidence of overlap (two quotes, two registrations, or two active pursuits) — load-bearing
3. Named referee with authority to pick one owner — load-bearing
4. One-price rule (or "no published rule — hole") — load-bearing
5. Registration timestamps / IDs, or "no registration system"
6. Direct involved? Y/N — and whether direct had *active* engagement before the registration
7. What the other party is owed (co-sell credit / decline with reasons / commission if direct closes)

## Output shape

```
CHANNEL CONFLICT — TWO PARTIES, ONE ACCOUNT, ONE QUOTE  |  [account]  |  as-of: [date]
Partner A: [name]     Evidence: [quote / reg / pursuit]     Timestamp: [ ] or HOLE
Partner B: [name]     Evidence: [quote / reg / pursuit]     Timestamp: [ ] or HOLE
Direct involved: Y/N     Active direct engagement before registration: Y/N / n/a
Registration status: [valid A / valid B / duplicate / none]

REFEREE: [name]     Published rule: [first valid reg / active direct / demand-created]
FREEZE additional quotes: done [date] / NOT DONE

DECISION
One assigned pursuer: [name — A / B / direct]
One price to the buyer: [$]     Buyer sees: ONE quote
Protection window: [your published days] or HOLE
Other party gets: [co-sell split internally / decline with reasons / commission if direct closes]
Told the loser (same day): owner [ ]  date [ ]  evidence cited [ ]

NOT THIS PAGE
One partner operating memo → partner-memo    One vendor delivery → vendor-sow    Two inherited lists → packaging-collision

ASK: [referee] assigns one pursuer and one price by [today]. Second quote does not go out.
Holes: [ ]
```

## QA (must pass)

1. Two named parties + one named account.
2. Evidence of overlap is dated (or HOLE, not a vibe).
3. Named referee.
4. One pursuer, one price, one quote to the buyer.
5. Loser is told the same day, with the rule and the evidence.
6. ASK + owner + date this week.
7. Not a one-partner memo, not a vendor SOW.
8. No invented timestamps or prices.
9. One page.

If 1, 4, 6, or 8 fail: do not ship.

## Escalate / stop

- "Let both quote; the best one will win" → refuse. That is two quotes — the failure this skill exists to stop.
- Honor a registration then steal the deal direct without paying → refuse (Track360: one incident poisons the channel).
- No published rule and they want a one-off handshake → issues list; Magentrix: unenforced rules are worse than none.
- How to work with one partner going forward → [Partner Memo](../../strategy/partner-memo/SKILL.md).

## Related

- [Partner Memo](../../strategy/partner-memo/SKILL.md) — one named counterparty; conflict needs two parties and a referee
- [Vendor SOW](../../management/vendor-sow/SKILL.md) — delivery scope, not route-to-market collision
- [Packaging Collision](../../ma/packaging-collision/SKILL.md) — two inherited price lists, structural
- [Discount Exception](../../strategy/discount-exception/SKILL.md) — one named discount vs list
- [Deal Desk](../../commercial/deal-desk/SKILL.md) — non-standard terms on the surviving quote
- [Forecast Call](../../commercial/forecast-call/SKILL.md) — this period's Commit; dual quotes are not two Commits
- [Pricing One-Pager](../../strategy/pricing-one-pager/SKILL.md) — list architecture, not this week's collision
