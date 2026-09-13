---
name: margin-bridge
description: >-
  Use when explaining gross or contribution margin this period versus last:
  three drivers, one action. Not unit-economics. Not a full P&L budget-variance.
license: MIT
---

# Margin Bridge

**Margin-bridge one-pager** — this vs last (gross or contribution), three drivers that add up, one action with owner and date. Default: venture; same spine for an F500 line.

Method origin: managerial accounting (OpenStax public) — contribution vs gross; price / volume / mix on the revenue side; cost on the other. A bridge reconciles last → this.

If they want a lecture on PVM: one paragraph then produce or stop.

## When to use

- "Why did margin move" this month / quarter vs last (or vs last year)
- Gross profit $ and/or rate changed and the room is guessing
- Mix looks like volume; discounting looks like cost
- You need **one** action, not a 12-line variance novel

## When not to use

- Physics of one more unit (CAC, payback, contribution per unit) — [Unit Economics](../../strategy/unit-economics/SKILL.md)
- Full P&L vs budget (this vs last vs plan, opex, reallocation) — [Budget Variance](../../management/budget-variance/SKILL.md)
- Weekly exceptions — [Operating Review](../../management/operating-review/SKILL.md)
- Price architecture — [Pricing One-Pager](../../strategy/pricing-one-pager/SKILL.md)
- One named off-list deal — [Discount Exception](../../strategy/discount-exception/SKILL.md)
- Cash / runway — [Cash Runway](../../management/cash-runway/SKILL.md)

## Modes

| Mode | When | Output |
|---|---|---|
| **produce** | Default. Two periods, some numbers | Bridge + three drivers + one action |
| **redline** | They pasted a P&L comment or a 20-bar waterfall | Force three drivers that add; kill "other" |
| **refuse** | Only one period, or no $ at all, and they want a story | Issues list. Stop |

Pick **gross** or **contribution**. Default contribution for venture; gross if they are a product/COGS business and said so.

## Hard rules

1. **Two periods, same definition.** Do not mix gross and contribution in one bridge. State which.
2. **$ and rate.** Margin dollars and margin %. Volume can lift $ and sink %. Both on the page.
3. **Three drivers, then residual.** Typical: price (realized), volume, mix, cost. Residual = this − last − the three. If residual is large, you picked wrong or the file is dirty — say so.
4. **Reconcile.** Last + drivers + residual = this. Round honestly; still add up.
5. **Mix is not volume.** Mix = shift toward/away from higher-margin SKUs/segments. Volume = more/fewer units at last period's mix.
6. **Price is pocket, not list.** Discounts, rebates, extra months live in price (or a named leak). Do not call it "COGS".
7. **One action.** Owner, date, the driver it attacks.
8. **Do not invent SKU-level numbers.** If you only have totals, the mix row is a hole.

## Intake

If **this period's margin** and **last period's margin** are both missing after one round: issues list.

1. Gross or contribution; this period and last (dates)
2. Revenue, units if any, COGS / variable cost — what they actually have
3. Mix they can see (SKU, segment, geo) or "totals only"
4. Anything known (a discount, a supplier hike, a one-off)
5. The action they already want, if any
6. Currency
7. Venture or F500 (venture default)

## Output shape

```
MARGIN BRIDGE  |  [product / company slice]  |  [this] vs [last]
Definition: gross | contribution     Currency: [ ]

ASK (one): [action that attacks the named driver]
Owner: [ ]    Date: [ ]

HEADLINE (one sentence): [Rate vs $. Named drivers.]

|  | Last | This | Δ $ | Δ pp |
| Revenue | [ ] | [ ] | [ ] | [ ] |
| COGS / variable | [ ] | [ ] | [ ] | [ ] |
| Margin $ | [ ] | [ ] | [ ] | [ ] |
| Margin % | [ ] | [ ] | [ ] | [ ] |

BRIDGE (last margin $ → this)
| Driver | Δ $ | Δ pp | One-line cause |
| Price (pocket) | [ ] | [ ] | [ ] |
| Volume | [ ] | [ ] | [ ] |
| Mix | [ ] | [ ] | [ ] |
| Cost / unit | [ ] | [ ] | [ ] |
| Residual (must be small or explained) | [ ] | [ ] | [ ] |
| SUM | = Δ $ | [ ] | CHECK: last + sum = this |

ONE ACTION (attacks [driver])
What: [ ]    Who: [ ]    When: [ ]    How we will know: [ ]

NOT THIS PAGE
Unit physics → unit-economics    Whole P&L vs budget → budget-variance
Weekly exceptions → operating-review    A single deal's off-list → discount-exception

HOLES
- [units missing so mix is a hole; pocket vs list unknown]
```

## QA (must pass)

1. Two periods, one definition (gross **or** contribution).
2. Margin $ and % both shown.
3. Three drivers named; residual shown.
4. Arithmetic: last + drivers + residual = this.
5. Mix not labelled as volume.
6. Price is pocket, or list-vs-pocket is a hole.
7. One action, owner, date.
8. Not a unit-economics model. Not a full P&L.
9. No invented SKU math.
10. One page.

If 1, 4, or 7 fail: do not ship.

## Escalate / stop

- One period only → refuse the bridge; offer a unit-economics page or wait.
- They want a long driver list — allow a residual bucket **named**, still pick three to act on.
- They want you to "explain" without numbers → issues list.
- Accounting restatement / inventory policy change — name it as a driver or a hole; do not treat it as operations.
- They actually want "does one more unit work" → [Unit Economics](../../strategy/unit-economics/SKILL.md).

## Related

- [Unit Economics](../../strategy/unit-economics/SKILL.md) — per-unit physics; this is the period-to-period walk
- [Budget Variance](../../management/budget-variance/SKILL.md) — this vs last vs plan on the P&L; this page is margin only
- [Operating Review](../../management/operating-review/SKILL.md) — weekly exceptions
- [Pricing One-Pager](../../strategy/pricing-one-pager/SKILL.md) — if price is the driver to redesign
- [Discount Exception](../../strategy/discount-exception/SKILL.md) — if one deal is the price driver
- [Cash Runway](../../management/cash-runway/SKILL.md) — cash is not margin
