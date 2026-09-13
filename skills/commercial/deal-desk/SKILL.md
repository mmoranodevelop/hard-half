---
name: deal-desk
description: >-
  Use for a pre-quote yes/no on non-standard price + legal + delivery as one
  package. NOT for discount-exception, not pricing-one-pager, not packaging-
  collision.
license: MIT
---

# Deal Desk

**Deal Desk Decision — Non-Standard Terms (Price + Legal + Delivery)** — one page: account, ACV, what is non-standard (price *and* legal *and* delivery/SLA), margin impact, delivery feasibility (named owner), legal risk, decision yes / no / counter, authority used, expiry of the exception, precedent note. Default: venture; same spine for F500.

Method origin: Salesforce Deal Desk (non-standard quote-to-cash; finance + legal + product on one request; standard deals bypass) + Salesforce zone-based price management (inspect the ~10%).

If they want a deal-desk lecture: one paragraph then produce or stop.

## When to use

- A live deal needs a non-standard package *before* the customer sees the quote
- Price, legal language, and delivery/SLA are moving together
- Standard band / CPQ would auto-approve, but this deal is outside the zone
- Reps are chasing finance, legal, and product as four separate errands

## When not to use

- One named discount vs list, legal and delivery standard — [Discount Exception](../../strategy/discount-exception/SKILL.md)
- Offer architecture / list design — [Pricing One-Pager](../../strategy/pricing-one-pager/SKILL.md)
- Two inherited price lists post-M&A — [Packaging Collision](../../ma/packaging-collision/SKILL.md)
- Delivery scope with one vendor — [Vendor SOW](../../management/vendor-sow/SKILL.md)
- Whether to pursue at all — [Bid No-Bid](../../commercial/bid-no-bid/SKILL.md)
- This week's Commit number — [Forecast Call](../../commercial/forecast-call/SKILL.md)

## Modes

| Mode | When | Output |
|---|---|---|
| **produce** | Default. Package named; authority known | Yes / no / counter page + ASK |
| **redline** | They pasted a discount email or a redlined MSA | Force the three-way package; kill hallway "we'll make it work" |
| **refuse** | Two load-bearing facts missing, or they want a lone extra 5 points off list | Issues list. Stop. Route discount-only to discount-exception |

## Hard rules

1. **Clock is pre-quote.** Standard deals bypass the desk (Salesforce + zone-based approvals). Leadership inspects the ~10% that are truly non-standard *before* the customer sees the quote.
2. **Three together.** Price *and* legal *and* delivery/SLA. A lone extra 5 points off list is [Discount Exception](../../strategy/discount-exception/SKILL.md), not this skill. Salesforce: sales cannot silently change SLA / liability / discount together.
3. **Four seats on one request:** Finance (price, discount, revenue impact), Product (feasibility of custom), Sales (negotiation), Legal (compliance, contract terms, risk). Not four errands.
4. **Named authority vs escalate.** Desk has defined authority inside a published matrix; above threshold, escalate. Clear rules prevent delay *and* cowboy terms.
5. **Delivery must sign.** If product cannot deliver, or CS cannot support, the desk's own warning is churn plus word-of-mouth damage. Undocumented terms are how CS inherits a lie.
6. **Output is yes / no / counter.** Counters are tradable (discount for shorter liability tail) — never silent. File the concession; next similar deal is faster; it does not become silent policy.
7. **Published SLA in hours**, not "when legal gets to it." Salesforce State of Sales 6th ed.: 10% of a rep week is already quotes + approvals; 47% say number of approvers is more of a challenge than a year ago. The desk collapses that into one package decision.
8. **Exception expires.** Undated yes becomes the new list.
9. **Do not invent margin, liability caps, or SLA numbers.** Holes stay holes.

## Intake

If **two** of 1–4 are missing after one round: issues list, not a fake yes.

1. The non-standard package (price *and* legal terms *and* delivery/SLA) — load-bearing
2. Named authority (desk vs escalate) against a published matrix — load-bearing
3. Named delivery/product sign-off that the SLA/scope is deliverable — load-bearing
4. A response SLA and a written decision (yes/no/counter) — load-bearing
5. Account, ACV, list vs requested, margin impact (or "unknown — hole")
6. Legal flags already seen (liability, MFN, payment, termination) or "none named"
7. Expiry of the exception and whether a similar concession is already on file

## Output shape

```
DEAL DESK DECISION  |  [account]  |  ACV: [$]  |  as-of: [date]
What is non-standard: PRICE [ ]  +  LEGAL [ ]  +  DELIVERY/SLA [ ]
Authority used: desk / escalate to [name]     Response SLA: [hours]     Expiry: [date]

MARGIN / PRICE
List: [$]     Requested: [$ / % off]     Pocket / margin impact: [$ / %] or HOLE

LEGAL RISK
Liability / MFN / payment / termination: [flags or "standard"]     Counsel: [name]

DELIVERY
Scope / SLA asked: [ ]     Deliverable? Y/N     Named delivery owner: [ ]     CS can support? Y/N

DECISION: YES / NO / COUNTER
Counter (tradable, not silent): [e.g. discount for shorter liability tail]
Precedent file: [similar concession / first of kind]
Handoff to CS / implementation (in writing): [owner + date]

NOT THIS PAGE
Lone discount vs list → discount-exception    Offer architecture → pricing-one-pager    Two price lists post-M&A → packaging-collision

ASK: [desk D] issues yes / no / counter by [hours SLA]. Customer does not see the quote before this page.
Holes: [ ]
```

## QA (must pass)

1. All three of price + legal + delivery are named, or the page routes to discount-exception.
2. Named authority (desk vs escalate).
3. Named delivery owner; deliverable is Y/N, not "we'll make it work."
4. Decision is yes / no / counter. Counter is written.
5. Exception has an expiry date.
6. ASK + owner + SLA hours.
7. Not a discount-only page, not a price-list architecture, not a post-M&A collision map.
8. No invented margin or liability numbers.
9. One page.

If 1, 3, 6, or 8 fail: do not ship.

## Escalate / stop

- Rep already sent a redlined MSA + discount + custom SLA before the desk saw the three → refuse; that is the silent change the desk exists to stop.
- Lone extra points off list, legal and delivery standard → [Discount Exception](../../strategy/discount-exception/SKILL.md).
- Standard deal sent to the desk → refuse; standard bypasses (CPQ / zone).
- Quarter-end "just approve it" with no delivery sign-off → refuse.

## Related

- [Discount Exception](../../strategy/discount-exception/SKILL.md) — one named discount vs list
- [Pricing One-Pager](../../strategy/pricing-one-pager/SKILL.md) — offer architecture; desk consumes it
- [Packaging Collision](../../ma/packaging-collision/SKILL.md) — two inherited lists, structural
- [Vendor SOW](../../management/vendor-sow/SKILL.md) — delivery scope with one vendor
- [Bid No-Bid](../../commercial/bid-no-bid/SKILL.md) — whether to pursue at all
- [Forecast Call](../../commercial/forecast-call/SKILL.md) — this period's Commit
- [Exec Sponsor Live](../../commercial/exec-sponsor-live/SKILL.md) — exec must not commit price/SLA/dates; those land here
