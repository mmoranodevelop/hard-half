---
name: unbilled-leakage
description: >-
  Use when hours or scope were eaten without a change request and the invoice
  line is missing. NOT for change-control, not budget-variance, not value-
  realization.
license: MIT
---

# Unbilled Leakage

**Leakage register** — hours or scope eaten **without a CR**, and the invoice line that should exist. Per line: bill it, late-CR it, or write it off with a **reason code** and a name. Default: venture program; same spine for F500.

Method origin: Accelo ("the hours are real; the invoice isn't") + SPI 2026 leakage KPI + Birdview — leakage begins during delivery, not at close.

If they want a leakage lecture: one paragraph then produce or stop. SPI 2026: industry revenue leakage **4.5%** (five-year low); HPOs **3.6%** vs rest **4.8%**; target **below 5%**, leading firms **below 3%**. Realization is the conversion metric. This page is the named missing lines that explain a bad realization number.

## When to use

- Time is in, work happened, no invoice line, no signed CR
- Extra scope started without a priced CR
- WIP older than the billing cycle, unapproved hours, or "we'll write it off for the relationship"

## When not to use

- One signed CR, scope baseline, approval — [Change Control](../../project/change-control/SKILL.md)
- Period actual vs plan (cost / revenue / margin) — [Budget Variance](../../management/budget-variance/SKILL.md)
- Promised vs delivered value for an account — [Value Realization](../../accounts/value-realization/SKILL.md)
- Acceptance of a deliverable — [Acceptance Signoff](../../project/acceptance-signoff/SKILL.md)
- Named people idle — [Utilization Bench](../../delivery/utilization-bench/SKILL.md)
- Quote list vs what was billed — [Rate Card](../../delivery/rate-card/SKILL.md)
- Weekly commercial commit of *invoicable* deals — [Forecast Call](../../commercial/forecast-call/SKILL.md)

## Modes

| Mode | When | Output |
|---|---|---|
| **produce** | Default. Unbilled hours or extra scope exist | Register + decision per line + ASK |
| **redline** | They pasted a P&L, a write-off dump, or "relationship" | Force lines + reason codes; kill silent donate |
| **refuse** | Signed CR as the object; two load-bearing answers missing | Issues list. Stop |

## Hard rules

1. **Leakage = hours or scope without a CR.** A signed CR going forward is [Change Control](../../project/change-control/SKILL.md), not this page.
2. **On-plan can still leak** if the plan already assumed donated hours. Period-vs-plan is [Budget Variance](../../management/budget-variance/SKILL.md).
3. **Write-off is after the invoice** (recorded). Leakage is often before. Accelo: absorbed scope without a change order.
4. **Each line has an owner and one decision:** bill it / late CR / coded write-off. "Relationship" is not a reason code.
5. **Price the CR before extra work starts** (Birdview). If the work already happened, it is leakage first, then a late CR or a coded write-off.
6. **Month-end is too late** to recover a forgotten hour. WIP older than the billing cycle needs an owner this week.
7. **Wrong rate on logged hours is value leakage** — same register, then freeze the list on [Rate Card](../../delivery/rate-card/SKILL.md).
8. **Do not invent hours or dollars.** Hole stays hole.

## Intake

If **named program** and **any unbilled hours / extra scope / aged WIP** are both missing after one round: issues list, not a fake register.

1. Named program / SOW; billing cycle (load-bearing)
2. Unbilled hours, extra scope with no CR, or WIP older than the cycle (load-bearing)
3. What would the invoice line be (role × hours × rate-card rate) — or HOLE
4. Who ate it (named person) and who can approve bill / CR / write-off
5. Already-signed CRs this period (so we do not double-count)
6. Reason anyone is saying "write it off"
7. This-month leakage % if known — or "not pulled" (SPI context: 4.5%)

## Output shape

```
LEAKAGE REGISTER  |  [program / client]  |  as-of: [date]  |  D (billing): [name]
Billing cycle: [ ]     SPI 2026 industry leakage 4.5% (HPO 3.6% / rest 4.8%; target <5%, leading <3%)

| Date | Who | Hours or scope (one line) | Invoice line that should exist | CR? | Decision (bill / late-CR / write-off) | Reason code | Owner | By when |
| [ ] | [ ] | [ ] | [role × n × rate] | N / late | [ ] | [code or HOLE] | [name] | [this week] |

WIP older than billing cycle: [lines]     Unapproved hours: [ ]
Silent donate / "relationship" with no code: FORBIDDEN
Scoreboard this month: leaked [ ]% of [revenue / hours] vs 4.5%

NOT THIS PAGE
Signed CR → change-control    Period vs plan → budget-variance    Promised vs delivered → value-realization
Idle names → utilization-bench    Wrong list → rate-card

ASK: [D] bills, late-CRs, or codes every line by [date this week].
Holes: [ ]
```

## QA (must pass)

1. Every row is hours/scope **without** a signed CR (late-CR is a decision, not a pretence that control already happened).
2. Every row has bill / late-CR / write-off + owner + date.
3. No "relationship" write-off without a reason code and a name.
4. ASK + named D + date this week.
5. Not a variance pack, not a signed-CR log, not a value-realization review.
6. No invented hours.
7. One page.

If 1, 2, 4, or 6 fail: do not ship.

## Escalate / stop

- They want you to treat a signed CR as leakage → route to change-control.
- "Write it off, relationship" with no code → refuse; that is how 4.5% hides.
- Month-end P&L as the only review → produce the weekly register or stop.

## Related

- [Change Control](../../project/change-control/SKILL.md) — signed CR going forward
- [Budget Variance](../../management/budget-variance/SKILL.md) — period vs plan
- [Value Realization](../../accounts/value-realization/SKILL.md) — promised vs delivered
- [Utilization Bench](../../delivery/utilization-bench/SKILL.md) — idle names, not unbilled hours
- [Rate Card](../../delivery/rate-card/SKILL.md) — frozen list; wrong rate is a line on this register
- [Staffing Mix](../../delivery/staffing-mix/SKILL.md) — mix vs margin; this is unpaid remainder
- [Forecast Call](../../commercial/forecast-call/SKILL.md) — do not put uninvoiced WIP in Commit
