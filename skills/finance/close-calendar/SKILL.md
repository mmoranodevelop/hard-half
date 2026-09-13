---
name: close-calendar
description: >-
  Use when month-end needs named owners, business-day slots, and a lock date —
  not “finance will close.” NOT for synergy-tracker (first combined close), not
  operating-review (exec exception pack), not day1-continuity (M&A morning).
license: MIT
---

# Close Calendar

**Month-end operator close calendar** — one page: target BD-lock, critical path, named close manager, today’s blockers, one ASK (cut a task / pull into pre-close / slip the lock with a named cost). Task × owner × BD × dependency × status on the same page or a reverse annex. Default: venture, single entity, 5 BD target (inventory often N/A). Same spine for F500 (multi-entity stagger; still **one named owner per task**).

Method origin: FEI public — close **calendar** + individual task ownership; APQC measure 100162 median **6.0 calendar days** (n = 10,198); Ledge 2025 via CFO.com — **50%** take **6+ business days**.

If they want a close-process lecture: one paragraph then produce or stop.

## When to use

- Period-end is dated and nobody has named who does what on which BD
- Lock keeps slipping; “AP” is the owner
- Pre-close work during the month needs a cutoff the rest of the company acknowledges

## When not to use

- First **combined** close after a deal — annex on [Synergy Tracker](../../ma/synergy-tracker/SKILL.md)
- M&A close **morning** (payroll, bank, entity, access) — [Day-1 Continuity](../../ma/day1-continuity/SKILL.md)
- This period’s exec exception pack — [Operating Review](../../management/operating-review/SKILL.md)
- Bank / 13-week — [Cash Runway](../../management/cash-runway/SKILL.md)
- This vs last vs plan on the P&L — [Budget Variance](../../management/budget-variance/SKILL.md)
- Remaining FY vs original plan — [Reforecast](../../finance/reforecast/SKILL.md)
- This month’s CCC — [Working Capital](../../finance/working-capital/SKILL.md)
- Project RACI rebuild — [RACI Delivery](../../project/raci-delivery/SKILL.md)

## Modes

| Mode | When | Output |
|---|---|---|
| **produce** | Default. Period-end and a close manager (or nominator) exist | Calendar + critical path + ASK |
| **redline** | They pasted a 40-line ERP cutover or “finance will close” | Force one human per task + BD; kill the 3-day slogan |
| **refuse** | No names and no BD; or they want first-combined / Day-1 morning | Issues list. Stop |

## Hard rules

1. Clock is **business days after period-end**, plus pre-close **during** the month. Holidays: working days, not calendar dates.
2. Every task has **one human**, a BD slot (BD0 cutoff → BDn lock), and what it waits on. “AP” never finished a task.
3. Build **backward from the reporting deadline** (Stampli vendor education — label). Critical path sets length. Status R/Y/G daily.
4. Three-day close is industry buzz, not the median (APQC 6.0 calendar days; Ledge: 50% at 6+ BD). Do not invent a 3-day close the team has never hit.
5. Quarter-end: extend a day rather than steal review.
6. This calendar **produces** numbers that [Working Capital](../../finance/working-capital/SKILL.md), [Budget Variance](../../management/budget-variance/SKILL.md), and [Reforecast](../../finance/reforecast/SKILL.md) read. Without a lock date those pages are drafts.
7. Do not invent owners or dates. Holes stay holes.

Typical BD skeleton (operator reconstruction from public 5-day calendars — not a firm SOP): BD0 cutoffs → BD1 cash/bank → BD2 AR/AP/accruals → BD3 recs + JEs → BD4 flux + draft pack → BD5 lock.

## Intake

If **period-end** and **named close manager (or a nominator + date)** are both missing after one round: issues list, not a fake page.

1. Entity (or entity list); period-end date (load-bearing)
2. Named close manager — one human (load-bearing)
3. Target lock BD and the reporting deadline it serves
4. Last close: actual BD-to-lock, late tasks, post-close adjustments
5. Critical-path tasks and who they wait on — or “build the skeleton”
6. Who signs the pack (CFO / MD)
7. Constraints: inventory N/A, multi-entity stagger, statutory filings — or “single entity”

## Output shape

```
MONTH-END CLOSE CALENDAR  |  [entity]  |  period: [month]  |  as-of: [date]
Target lock: BD[n] ([date])     Close manager: [name]     Signs: [CFO/MD]
Critical path: [task → task → lock]
Today’s blockers: [ ]

| BD | Gate | Owner (one human) | Depends on | Status R/Y/G | Slip cost |
| D−n / BD0 | Cutoffs published (AP, billing, payroll, inventory) | [ ] | [ ] | [ ] | [ ] |
| BD1 | Cash / bank; subledger freeze start | [ ] | [ ] | [ ] | [ ] |
| BD2 | AR/AP aging final; payroll / accruals | [ ] | [ ] | [ ] | [ ] |
| BD3 | Recs done; material JEs posted | [ ] | [ ] | [ ] | [ ] |
| BD4 | Flux vs last / plan; draft pack | [ ] | [ ] | [ ] | [ ] |
| BD5 | Lock; pack to MD/CFO | [ ] | [ ] | [ ] | [ ] |

TASK STRIP (critical path on page 1; annex = full list)
| Task | Owner | BD | Dependency | Status |

NOT THIS PAGE: first combined close → synergy-tracker annex; M&A morning → day1-continuity; exec reds → operating-review

ASK: [cut a task / pull into pre-close / slip the lock with named cost]
Owner: [ ]  Date: [ ]
Holes: [ ]
```

## QA (must pass)

1. Target lock is a BD + date, not “finance will close.”
2. Every page-1 task has one human owner.
3. Critical path is named; today’s blockers are named or “none.”
4. ASK + owner + date.
5. Not a first-combined-close plan, not Day-1 continuity, not an exec review.
6. No invented 3-day close.
7. One page (+ optional task annex).

If 1, 2, 4, or 5 fail: do not ship.

## Escalate / stop

- “Finance will close” with no names and no BD → refuse.
- First combined close after a deal → [Synergy Tracker](../../ma/synergy-tracker/SKILL.md).
- Close morning of an M&A → [Day-1 Continuity](../../ma/day1-continuity/SKILL.md).
- A 40-line ERP cutover labelled “close calendar” → redline or refuse.

## Related

- [Working Capital](../../finance/working-capital/SKILL.md) — reads DSO / DIO / DPO after lock
- [Budget Variance](../../management/budget-variance/SKILL.md) / [Reforecast](../../finance/reforecast/SKILL.md) — past period / remaining year; need closed (or flash) numbers
- [Operating Review](../../management/operating-review/SKILL.md) — exception pack this calendar feeds
- [Cash Runway](../../management/cash-runway/SKILL.md) — direct cash weekly; close is accrual lock
- [Decision Debt](../../finance/decision-debt/SKILL.md) — aged Ds blocking cutoff / recs
- [Synergy Tracker](../../ma/synergy-tracker/SKILL.md) / [Day-1 Continuity](../../ma/day1-continuity/SKILL.md) — not this clock
