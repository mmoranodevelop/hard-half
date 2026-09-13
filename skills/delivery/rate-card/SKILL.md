---
name: rate-card
description: >-
  Use when the team needs the frozen list they may quote until a dated review.
  Not a pricing one-pager, not a discount exception, not a packaging collision.
license: MIT
---

# Rate Card

**Rate card freeze** — the list the team may quote: role (or service line) × geography × unit × currency, effective date, owner, who may exception. Frozen until a **dated** review. Default: venture shop; same spine for F500.

Method origin: Frozen commercial list (GSA GSAR 552.238-81 operator lesson: the catalog is a controlled object) + SPI HPO discount discipline. Same clock as [Packaging Collision](../../ma/packaging-collision/SKILL.md): **do not reprice in the incident week.**

If they want a pricing-strategy lecture: one paragraph then produce or stop. SPI 2026: HPOs discount **6.0%** vs **9.6%** for the rest — and win more bids. Magnetic: realization is **pricing integrity**. Birdview: the rate card on the project must be the rate card finance invoices. A "pricing review" with no date is a license for every seller to invent a rate.

## When to use

- Two people can quote the same role at two rates tomorrow
- Rescue / angry-client week and someone wants to reprice live work
- Blend or invoice does not match the list the team thinks is current

## When not to use

- Architecture of one offer (metric, GBB, fences) — [Pricing One-Pager](../../strategy/pricing-one-pager/SKILL.md)
- Yes/no on one named discount — [Discount Exception](../../strategy/discount-exception/SKILL.md)
- Two price lists after close; grandfather — [Packaging Collision](../../ma/packaging-collision/SKILL.md)
- This program's onshore / contractor / vendor mix — [Staffing Mix](../../delivery/staffing-mix/SKILL.md)
- Hours eaten without billing — [Unbilled Leakage](../../delivery/unbilled-leakage/SKILL.md)
- Pre-quote yes/no on price + legal + delivery as one package — [Deal Desk](../../commercial/deal-desk/SKILL.md)

## Modes

| Mode | When | Output |
|---|---|---|
| **produce** | Default. A list (or "we cannot find the list") exists | Freeze card + exception owner + ASK |
| **redline** | They pasted "pricing review this week" or a live reprice | Force freeze; kill the review-as-message |
| **refuse** | Incident-week reprice; inventing list prices; two load-bearing missing | Issues list. Stop |

## Hard rules

1. **One current card.** Role (or service line) × geography × unit (hour/day) × currency. Effective date. Owner (usually finance + delivery lead). Who may exception: a **name**.
2. **Quote week: frozen.** A deal that cannot clear the card goes to [Discount Exception](../../strategy/discount-exception/SKILL.md), not a silent new rate.
3. **Incident / rescue / angry-client week: do not reprice.** Do not announce a "pricing review." Dated change at the next review, or nothing. Levers this week: [Unbilled Leakage](../../delivery/unbilled-leakage/SKILL.md) and [Staffing Mix](../../delivery/staffing-mix/SKILL.md).
4. **Dated review (quarterly / annual) is the only legal moment to change the list.** Then freeze again. GSA lesson: revising the commercial catalog is an event, not a chat.
5. **Blend sits on top of the card** ([Staffing Mix](../../delivery/staffing-mix/SKILL.md)). Do not average your way to a new list in a live week.
6. **Do not invent list prices.** Hole stays hole.
7. **Realization is the test** that the card on the project is the card on the invoice.

## Intake

If **the current list (or "no list exists")** and **who owns it** are both missing after one round: issues list, not a fake freeze.

1. Shop / geography / currency (load-bearing)
2. Current card, or "we cannot find the list" (load-bearing)
3. Effective date + next dated review — or HOLE
4. Who owns the card; who may exception (a name)
5. Live deals that would break if the list moved this week
6. Discount already in the wild vs SPI HPO 6.0% / rest 9.6% — or "not pulled"
7. Why they want a change *this* week (rescue / RFP / annual) or "no change, freeze only"

## Output shape

```
RATE CARD FREEZE  |  [shop / geo / currency]  |  effective: [date]  |  freeze until: [dated review]
D (list): [finance + delivery]     Who may exception: [name]     Vehicle: hour / day

WEEK RULE: do not reprice. Do not announce a "pricing review." Incident week → leakage + mix, not a new list.

| Role / service line | Geo | Unit | List rate | Currency | In force? | Notes (fences, min) |
| [ ] | [ ] | hour/day | [ ] or HOLE | [ ] | Y/N | [ ] |

Next dated review: [date]     Change at review: [what, or "none"]
Live deals that must not move this week: [names]
Exception path: one named discount → discount-exception     Two post-close lists → packaging-collision

SPI context (not a target to copy): HPO discount 6.0% vs rest 9.6%. Realization = pricing integrity.

NOT THIS PAGE
Offer architecture → pricing-one-pager    One discount → discount-exception    Two lists post-close → packaging-collision
Program mix → staffing-mix    Unbilled hours → unbilled-leakage    Pre-quote package → deal-desk

ASK: [D] freezes this list until [review date]; exceptions only via [name].
Holes: [ ]
```

## QA (must pass)

1. Freeze-until is a date, not "until we review."
2. Who may exception is a name (or HOLE).
3. No incident-week reprice; message is not "pricing review."
4. ASK + named D + date.
5. Not a GBB offer, not a one-deal discount, not a two-list collision map.
6. No invented list prices.
7. One page.

If 1, 3, 4, or 6 fail: do not ship.

## Escalate / stop

- Reprice live work this week because the program is in trouble → refuse; same clock as packaging-collision.
- "We're doing a pricing review" with no date → refuse.
- They want you to invent rates → issues list.
- One off-list quote → [Discount Exception](../../strategy/discount-exception/SKILL.md).

## Related

- [Discount Exception](../../strategy/discount-exception/SKILL.md) — one named discount vs this freeze
- [Packaging Collision](../../ma/packaging-collision/SKILL.md) — two post-close lists; same freeze clock
- [Pricing One-Pager](../../strategy/pricing-one-pager/SKILL.md) — offer architecture, not the quote list
- [Deal Desk](../../commercial/deal-desk/SKILL.md) — pre-quote package yes/no; this is the list the desk inspects
- [Staffing Mix](../../delivery/staffing-mix/SKILL.md) — blend on top of this card
- [Unbilled Leakage](../../delivery/unbilled-leakage/SKILL.md) — hours without the invoice line
- [Utilization Bench](../../delivery/utilization-bench/SKILL.md) — do not cut the list to fill the bench
