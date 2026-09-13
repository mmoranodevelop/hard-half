---
name: deprecation-notice
description: >-
  Use when a BAU feature or SKU needs last-sell, last-support, and grandfather
  on one customer notice. NOT for portfolio-keep-kill, not kill-criteria, not
  change-adoption.
license: MIT
---

# Deprecation Notice

**Deprecation notice** — last-sell, last-support, grandfather pocket, migration path, customer sentence, owner. BAU, not deal-week. Default: venture product; same spine for F500.

Method origin: Public BAU sunset **artifact shape** (Twilio Notify three-date notice; Microsoft Modern Lifecycle). Same spine as [Portfolio Keep-Kill](../../ma/portfolio-keep-kill/SKILL.md), BAU not deal.

If they want a sunsetting lecture: one paragraph then produce or stop. Shape, not a case to copy: Twilio Notify **end of sale 24 Oct 2022**, **end of life 23 Oct 2023**, existing customers supported until EOL, no new features. Microsoft: minimum **12 months'** notice before ending support if **no successor**; minimum **30 days** when customers must act to avoid significant degradation. Azure: **deprecation** = still available and supported (typical ≥12 months); **retirement** = off. Stripe: you may deprecate without a kill date. Do not collapse the two.

## When to use

- A live BAU feature / API / SKU will stop being sold or supported and customers need dates
- Engineering wants it off this Friday; no last-sell / last-support exists
- Replacement is launching and the old path has no grandfather rule

## When not to use

- Post-M&A SKU keep / kill / combine / harvest — [Portfolio Keep-Kill](../../ma/portfolio-keep-kill/SKILL.md)
- One venture, dated tests, kill / continue — [Kill Criteria](../../strategy/kill-criteria/SKILL.md)
- Behaviours at go-live — [Change Adoption](../../management/change-adoption/SKILL.md)
- Customer-facing launch of the replacement — [Launch Brief](../../delivery/launch-brief/SKILL.md)
- Two price lists, grandfather commercial terms — [Packaging Collision](../../ma/packaging-collision/SKILL.md)

## Modes

| Mode | When | Output |
|---|---|---|
| **produce** | Default. Named thing + intent to sunset | Notice + dates + ASK |
| **redline** | They pasted "we will also sunset the old thing" with no dates | Force last-sell / last-support / grandfather |
| **refuse** | Deal-week keep/kill; off-this-Friday; two load-bearing missing | Issues list. Stop |

## Hard rules

1. **Three clocks, not one.** Last-sell (no new logos / no expansion if that is the rule) ≠ last-support ≠ retirement (off). Atlassian-style: last-sell, last-change, last-support are different dates.
2. **Grandfather is a named pocket** with an end date — or "unsupported but available" (Stripe Charges). Undated grandfather becomes the product.
3. **Customer sentence is load-bearing.** What we will say. Not "nothing will change."
4. **Migration path** for anyone still buying or running it — or do not ship a Kill/EOL row.
5. **Microsoft floor if no successor: 12 months** before ending support (excluding free/preview). 30 days when the customer must act to avoid significant degradation. If you are tighter, say so as a hole, not a silent surprise.
6. **Deprecation ≠ retirement.** Still supported + no new enhancements is not "off."
7. **Do not use a post-M&A keep/kill card** for a BAU feature. Do not turn it off this Friday because engineering is tired.
8. **Do not invent customer counts or dates.** Hole stays hole.

## Intake

If **the named thing** and **what happens to customers (sell / support / off)** are both missing after one round: issues list, not a fake notice.

1. Named feature / API / SKU (load-bearing)
2. Intent: deprecate-only / last-sell + last-support / retire (load-bearing)
3. Successor (named) or "no successor"
4. Who is in-contract or in-production today (named segment, not a census)
5. Grandfather pocket: who is held, until when — or "none"
6. Owner of the notice + send-by date
7. Replacement launch date if any (then [Launch Brief](../../delivery/launch-brief/SKILL.md) is a sibling, not this page)

## Output shape

```
DEPRECATION NOTICE  |  [feature / API / SKU]  |  as-of: [date]  |  owner: [name]
Clock: BAU sunset. Not portfolio-keep-kill. Not kill-criteria.

Customer sentence: [what we will say — not "nothing will change"]

Last-sell (no new): [date or n/a — Twilio Notify shape: EOS 24 Oct 2022]
Last-support / EOL: [date or n/a — Twilio Notify shape: EOL 23 Oct 2023]
Retirement (off; SLAs end): [date or "not planned" — deprecation ≠ retirement]
Successor: [name / "none"]     If none: 12-month floor applies unless free/preview — [Y/N / HOLE]
Customer must act by: [date] (Microsoft min 30 days if degradation)

Grandfather: [who] until [date] or "unsupported but available" or NONE
Migration path: [guide / product]     New features after last-sell: N
Other products impacted: [none / list]

NOT THIS PAGE
Post-M&A SKU labels → portfolio-keep-kill    Venture test → kill-criteria
Go-live behaviours → change-adoption    Replacement go/no-go → launch-brief    Two price lists → packaging-collision

ASK: [owner] sends this notice by [date]. Last-sell and last-support locked.
Holes: [ ]
```

## QA (must pass)

1. Last-sell and last-support are dates or explicit n/a — not "soon."
2. Grandfather has who + until, or NONE.
3. Customer sentence exists; no "nothing will change."
4. No successor + support ending inside 12 months is a flagged hole (or free/preview).
5. ASK + named owner + date.
6. Not a keep/kill card, not kill-criteria, not change-adoption.
7. No invented volumes.
8. One page.

If 1, 3, 5, or 6 fail: do not ship.

## Escalate / stop

- Off this Friday with no notice → refuse.
- Post-close SKU labels → [Portfolio Keep-Kill](../../ma/portfolio-keep-kill/SKILL.md).
- Kill with no migration path → refuse.
- Launch brief that "also sunsets the old thing" with no dates → redline here or stop.

## Related

- [Portfolio Keep-Kill](../../ma/portfolio-keep-kill/SKILL.md) — deal-week SKU labels; this is BAU
- [Kill Criteria](../../strategy/kill-criteria/SKILL.md) — one venture's stop tests
- [Launch Brief](../../delivery/launch-brief/SKILL.md) — replacement go/no-go
- [Packaging Collision](../../ma/packaging-collision/SKILL.md) — grandfather of **price**, not of the SKU
- [Change Adoption](../../management/change-adoption/SKILL.md) — behaviours, not dates
- [Severity Customer](../../delivery/severity-customer/SKILL.md) — do not deprecate via an incident note
