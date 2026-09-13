---
name: working-capital
description: >-
  Use when this month’s operating cycle is the object: DSO, DIO, DPO, CCC, and
  one cash ASK. NOT for cash-runway (bank / 13-week), not budget-variance (P&L
  this vs last vs plan), not margin-bridge, not synergy-tracker.
license: MIT
---

# Working Capital

**Working-capital this month** — one page the MD sends: DSO / DIO / DPO / CCC vs last and vs a named plan/peer, cash trapped, one collect / cut-stock / stretch-AP ASK. Default: venture (AR-heavy; inventory often `[no inventory — SaaS]`). Same spine for F500 / industrial (all three levers).

Method origin: J.P. Morgan / CFI public — **CCC (days) = DSO + DIO − DPO**.

If they want a working-capital lecture: one paragraph then produce or stop.

## When to use

- Month just closed (or an in-month flash, labelled) and CCC is unmanaged
- Accrual P&L looks fine while AR or inventory ages
- Named invoices, slow SKUs, or stretchable trade AP are the cash question *this month*

## When not to use

- Bank, 13-week strip, payroll, net burn — [Cash Runway](../../management/cash-runway/SKILL.md)
- This period vs last vs plan on the P&L — [Budget Variance](../../management/budget-variance/SKILL.md)
- Gross / contribution drivers — [Margin Bridge](../../strategy/margin-bridge/SKILL.md)
- Deal synergy cash / first combined close — [Synergy Tracker](../../ma/synergy-tracker/SKILL.md)
- Remaining FY vs original plan — [Reforecast](../../finance/reforecast/SKILL.md)
- Named owners + business-day lock — [Close Calendar](../../finance/close-calendar/SKILL.md)
- Period exception pack — [Operating Review](../../management/operating-review/SKILL.md)
- One more unit — [Unit Economics](../../strategy/unit-economics/SKILL.md)

## Modes

| Mode | When | Output |
|---|---|---|
| **produce** | Default. AR / inventory / AP exist (or a labelled N/A) | CCC strip + one cash ASK |
| **redline** | They pasted a 13-week labelled “working capital,” or a P&L | Force days not bank; kill payroll stretch |
| **refuse** | No AR, no inventory, and no AP; or they want runway / payroll | Issues list. Stop |

## Hard rules

1. Clock is **this month’s CCC**. Not weeks of cash. Do not ship a hybrid with [Cash Runway](../../management/cash-runway/SKILL.md).
2. **CCC = DSO + DIO − DPO.** Label the basis (revenue vs credit sales; COGS). Seasonal: say so.
3. Do not invent DIO for a services book — `[no inventory — SaaS]`.
4. Cash trapped = Δ days × daily sales or COGS (**labelled which**).
5. AP: statutory (payroll, tax, debt) vs trade. Stretching DPO by missing payroll, tax, or a sole-source is refuse.
6. Public bar (PwC Working Capital Study 25/26, >17,000 listed): DPO **+11.5%** globally since 2015 is **masking** worse receivables (DSO 47.3 → **50.0** days) and bloated inventory (medium-firm DIO **+24.2%**). Excess NWC they cite: **€1.84tn**. Do not “win” by stretching vendors you need.
7. One ASK: collect named invoices / cut named SKU / stretch named non-critical AP — owner, date, $ implied by the days.
8. Do not invent days or dollars. Holes stay holes. Without a lock (or flash label) from [Close Calendar](../../finance/close-calendar/SKILL.md), this page is a draft.

## Intake

If **entity + period** and **any of AR, inventory, or AP (or a labelled N/A)** are both missing after one round: issues list, not a fake page.

1. Entity; as-of; month just closed or in-flight flash (load-bearing)
2. AR $ + aging, and credit sales / revenue for DSO
3. Inventory $ + COGS for DIO, or `[no inventory]` (2 or 3 load-bearing with 1)
4. AP $ + COGS for DPO; statutory vs stretchable
5. Last month’s DSO / DIO / DPO and a named plan / peer — or hole
6. Who has D on collections / stock / payables
7. Named overdue invoices, slow SKUs, or stretchable vendors — or “not listed”

## Output shape

```
WORKING-CAPITAL THIS MONTH  |  [entity]  |  period: [month]  |  as-of: [date]
Close: locked / flash (labelled)     D on AR / inventory / AP: [names]
CCC = DSO + DIO − DPO

| Metric | This month | Last | Plan/peer | Δ days | $ trapped (basis labelled) |
| DSO | [ ] d  AR $[ ] | [ ] | [ ] | [ ] | Δ × daily sales = $[ ] |
| DIO | [ ] d  Inv $[ ] or N/A | [ ] | [ ] | [ ] | Δ × daily COGS = $[ ] |
| DPO | [ ] d  AP $[ ] | [ ] | [ ] | [ ] | statutory vs stretch |
| CCC | [ ] d | [ ] | [ ] | [ ] | net $[ ] |

AR AGING (top overdue)
| Name | $ | Days | Dispute Y/N | Promise-to-pay | Owner |

INVENTORY (slow / obsolete / just-because) — or [no inventory — SaaS]
| SKU / class | $ | Days | Service-level risk | Cut Y/N |

AP (trade vs statutory)
| Vendor / class | $ | Terms | Statutory Y/N | Stretch Y/N | Risk if late |

NOT THIS PAGE: bank / 13-week → cash-runway; P&L this vs last vs plan → budget-variance

ASK: [collect named invoices / cut named SKU / stretch named non-critical AP]
Owner: [ ]  Date: [ ]  Cash $ implied: [ ]
Holes: [ ]
```

## QA (must pass)

1. CCC is DSO + DIO − DPO, this month, vs last (or hole).
2. Cash trapped has a labelled basis (sales or COGS).
3. No payroll / tax / sole-source stretch.
4. One ASK + named owner + date + $.
5. No invented days or dollars.
6. Not a 13-week strip, not a P&L variance, not a margin bridge.
7. One page.

If 1, 4, 5, or 6 fail: do not ship.

## Escalate / stop

- “How much runway / can we make payroll?” → refuse; [Cash Runway](../../management/cash-runway/SKILL.md).
- They want to “improve DPO” by missing payroll, tax, or a critical vendor → refuse.
- Inventing a CCC with no AR, no inventory, and no AP → issues list.

## Related

- [Close Calendar](../../finance/close-calendar/SKILL.md) — lock (or flash) before these days are controller-grade
- [Cash Runway](../../management/cash-runway/SKILL.md) — bank; this page feeds collection / payable *timing*
- [Budget Variance](../../management/budget-variance/SKILL.md) — past-period P&L, not days
- [Reforecast](../../finance/reforecast/SKILL.md) — remaining year vs original plan
- [Operating Review](../../management/operating-review/SKILL.md) — a red DSO can appear there; the move is here
- [Unit Economics](../../strategy/unit-economics/SKILL.md) / [Business Case](../../strategy/business-case/SKILL.md) — not the cycle
- [Decision Debt](../../finance/decision-debt/SKILL.md) — aged D on collections / stock / payables
