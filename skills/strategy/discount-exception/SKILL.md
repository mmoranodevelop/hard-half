---
name: discount-exception
description: >-
  Use for a yes/no on a named discount versus list: fence, expiry, give-get,
  pocket impact. NOT for price architecture (that's pricing-one-pager). Not
  unit-economics.
license: MIT
---

# Discount Exception

**Discount-exception one-pager** — yes / no / yes-with-fence on a **named deal**, vs list, with expiry and pocket impact. Default: venture; same spine for F500 deal desk.

Public method. Nagle public (Inc 1995 + pocket-price craft): list is not what you keep; **pocket price** is. Discounts without **fences** leak. A one-off that never expires becomes the new list. Approval without a give-get is a gift. This is **one exception**, not a re-architecture — that is [Pricing One-Pager](../../strategy/pricing-one-pager/SKILL.md). Do not clone a McKinsey waterfall exhibit.

If they want a pricing lecture, one paragraph then produce or stop.

## When to use

- Sales (or you) wants off-list on a **named** customer / deal
- "Strategic discount" / "just this once" / matching a competitor quote
- Deal desk / founder / CRO must yes-or-no this week
- A prior exception is still live past its expiry

## When not to use

- Designing **list, metric, GBB, policy** — [Pricing One-Pager](../../strategy/pricing-one-pager/SKILL.md)
- Whether the unit makes money — [Unit Economics](../../strategy/unit-economics/SKILL.md) (use it as the floor)
- The whole book of exceptions (that's a policy rewrite → pricing-one-pager)
- Illegal price-fixing, collusion, RPM — stop
- Procurement cost-out on inputs (make-vs-buy / purchasing)

## Modes

| Mode | When | Output |
|---|---|---|
| **produce** | Default. Named deal | Yes / no / yes-with-fence + expiry |
| **redline** | They pasted a discount request or a quote | Fail missing fence/expiry/pocket; rewrite the ASK |
| **refuse** | No list, no named deal, or they want a standing off-list with no end | Issues list. Stop |

## Hard rules

1. **Named deal.** Customer, SKU/offer, quantity, term. "Our enterprise segment needs 20% off" is a policy request → pricing-one-pager.
2. **List and pocket on the page.** List → this discount → other already-promised leak (rebate, freight, extra months, services) → pocket. If pocket is unknown, that is a hole, not a yes.
3. **Floor from unit-economics.** Contribution after this pocket. If you cannot say it, you may still no; you may not yes.
4. **Fence or no.** What they **give up** to get the lower price (term, volume, SLA, features, public reference, prepay). A cheaper price with Best outcomes is not a fence.
5. **Expiry or no.** Date the exception dies and the deal returns to list / to a named band. "Until they churn" is a fail.
6. **Give-get is written.** If they get 15% off, we get [multi-year / case study / mix / prepay]. Empty get = gift. Write it.
7. **Who may approve** this depth (rep / manager / you / board). If the asker is marking their own homework, say so.
8. **Do not invent competitor quotes or WTP.** A "they have a cheaper bid" without paper is a story.

## Intake

If **the deal** and **list price** are both missing after one round: issues list.

1. Customer, offer, quantity, term (the named deal)
2. List price and the discount asked (%, $)
3. Other leaks already in the quote (rebate, freight, free months)
4. Contribution / floor (or "unknown")
5. What they will give (fence / get) and expiry you can live with
6. Approver of record; competitor paper if any
7. Venture or F500 (venture default)

## Output shape

```
DISCOUNT EXCEPTION  |  [customer]  |  [offer]  |  [date]
Deal: [qty / term]    Approver of record: [ ]
List: [ ]    Asked: [ % or $ ]    Other leaks already in quote: [ ]

VERDICT: YES | YES WITH FENCE | NO
ASK: approve this exception through [expiry] | refuse | send back for give-get
Owner: [ ]    Decide-by: [ ]

POCKET
List → on-invoice discount → off-invoice / freight / extra months → pocket [ ]
Contribution at this pocket: [known / hole]    Floor: [ ]

FENCE (what they give up)
- [term / volume / SLA / features / reference / prepay]
If empty: verdict cannot be YES

GIVE-GET
They get: [ ]    We get: [ ]

EXPIRY
Dies on [date]. Then: back to list / to band [ ]. Who watches: [ ]

WHY THIS DEAL (one sentence, or "no reason that survives expiry")
Competitor paper: attached / story only / none

IF NO
What we offer instead: [list / smaller fence / walk]

HOLES
- [ ]
```

## QA (must pass)

1. Named deal, not a segment slogan.
2. List and asked discount both stated.
3. Pocket attempted; other leaks listed or hole.
4. Fence non-empty if verdict is YES.
5. Expiry date if verdict is YES.
6. Give-get written or verdict is NO.
7. Contribution floor used or labelled hole — no silent yes below unknown floor.
8. Not a price-architecture rewrite.
9. No invented competitor quotes.
10. One page.

If 1, 4, 5, or 9 fail: do not ship a YES.

## Escalate / stop

- They want a permanent off-list for a logo → refuse; that is a fence in the architecture (pricing-one-pager) or a NO.
- They insist cost-plus "so finance can approve" → floor is a hurdle, not the exception.
- Collusion / matching a competitor because you **met** them → stop.
- Pocket unknown and they still want YES → NO, or hole + "return when pocket is computed".
- This is "should we even sell this unit" → unit-economics.

## Related

- [Pricing One-Pager](../../strategy/pricing-one-pager/SKILL.md) — architecture and standing policy
- [Unit Economics](../../strategy/unit-economics/SKILL.md) — floor / contribution
- [Business Case](../../strategy/business-case/SKILL.md) — if this exception is actually a capital bet
- [Margin Bridge](../../strategy/margin-bridge/SKILL.md) — after the fact, why margin moved
