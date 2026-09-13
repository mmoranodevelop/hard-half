---
name: benefits-realization
description: >-
  Use when post-go-live (or mid) benefits must be scored vs business-case
  assumptions with owners and one ASK. NOT for business-case build, not value-
  realization (customer account), not synergy-tracker (M&A), not QBR, not
  operating-review.
license: MIT
---

# Benefits Realization

**Benefits vs case — one page** — assumed benefits from the business case vs measured to date; owners; gap; sustain/kill actions; one ASK. Default: post-go-live (or mid-program benefit check) on a named initiative; same spine for F500.

Method origin: Benefits Realization Management public (APM / PMI BRM concepts: identify → deliver → sustain; benefits map linking outputs → outcomes → strategic benefits) — operator scorecard, not a BRM textbook.

If they want a BRM / benefits-map lecture: one paragraph then produce or stop.

## When to use

- Go-live happened (or mid-flight) and nobody is checking benefits vs the case
- Board / sponsor asks "did we get what we bought?" with evidence, not anecdotes
- Benefits have no owners after project close
- Assumptions in the case (adoption, run-rate, cost-takeout) need a scored refresh

## When not to use

- Writing / funding the case — [Business Case](../../strategy/business-case/SKILL.md)
- Named **customer account** promised-vs-delivered — [Value Realization](../../accounts/value-realization/SKILL.md)
- M&A cost/revenue synergy run-rate — [Synergy Tracker](../../ma/synergy-tracker/SKILL.md)
- Quarterly sitting with one customer — [QBR](../../management/qbr/SKILL.md)
- Weekly internal exceptions — [Operating Review](../../management/operating-review/SKILL.md)
- Project close checklist only — [Project Close](../../project/project-close/SKILL.md) (may hand off to this)

## Modes

| Mode | When | Output |
|---|---|---|
| **produce** | Default. Case benefits + some measures | Scorecard + owners + ASK |
| **redline** | They pasted ROI claims without owners | Force baseline/actual/gap; kill orphan benefits |
| **refuse** | No case assumptions and no measures, or invent ROI | Issues list. Stop |

## Hard rules

1. **Trace to the case.** Each benefit line cites the business-case assumption (or HOLE — "no case benefit listed").
2. **Measure vs claim.** Baseline, target, actual to date, as-of date. No measure → unknown, not green.
3. **Owner is BAU / benefit owner**, not the project manager by default. Unowned benefit = fail.
4. **Map one line (optional but sharp):** output → outcome → benefit. Skip essay maps.
5. **Gap actions:** sustain, accelerate, re-baseline target, or kill benefit claim — with owner + date.
6. **One ASK** — D (sponsor / benefit owner / CFO) to accept gap, fund sustainment, or retire a claim by date.
7. **Never invent** $ benefits, % adoption, or ROI. Holes stay holes.
8. **One page** (+ optional mini benefits map annex).

## Intake

If **two** of 1–4 are missing after one round: issues list, not a fake scorecard.

1. Named initiative + go-live (or review) date — load-bearing
2. Business-case benefit list (or pointer) — load-bearing
3. Measures available to date — or "none" — load-bearing
4. Benefit owners named or "unowned" — load-bearing if scoring
5. As-of date / review period
6. Who has D on benefit claims / sustain funding
7. Dis-benefits / costs of change observed or "none looked"

## Output shape

```
BENEFITS REALIZATION  |  [initiative]  |  as-of: [date]
Go-live / review: [date]     Case ref: [v/link]     D: [name]

ASK: [D] to [accept gap / fund sustainment / retire claim X / re-baseline target] by [date]

SCORE
| # | Benefit (from case) | Baseline | Target | Actual | Gap | Owner | Status |
| 1 |  |  |  |  |  |  | on/late/unknown/kill? |

MAP (one line each, optional)
Output → Outcome → Benefit: [ ]

ASSUMPTIONS STILL LOAD-BEARING
| Assumption | Still true? | Evidence | If false |
|  | yes/no/unknown |  |  |

ACTIONS
Sustain: [ ]     Accelerate: [ ]     Re-baseline: [ ]     Retire claim: [ ]

NOT THIS PAGE
Build the case → business-case    Customer account value → value-realization
M&A synergies → synergy-tracker    Customer QBR → qbr    Weekly ops → operating-review

Holes: [ ]
```

Annex: `assets/benefits-map-mini.md`.

## QA (must pass)

1. Case-linked benefit lines (or explicit HOLE).
2. Baseline / target / actual or unknown — no fake green.
3. Each scored benefit has an owner or "unowned" flagged.
4. One ASK with owner, verb, date.
5. Not customer value-realization, not M&A synergy tracker, not QBR.
6. No invented ROI/$. One page.

If 1, 2, 4, or 6 fail: do not ship.

## Escalate / stop

- No benefit owners after close → escalate to sponsor; page lists unowned.
- Claims exceed evidence → refuse green; score unknown.
- They want customer-account proof story → [Value Realization](../../accounts/value-realization/SKILL.md).
- They want deal synergy ledger → [Synergy Tracker](../../ma/synergy-tracker/SKILL.md).
- Material dis-benefit (harm) found → escalate; do not bury under "on track".

## Related

- [Business Case](../../strategy/business-case/SKILL.md) — assumptions this page scores
- [Value Realization](../../accounts/value-realization/SKILL.md) — one customer account promised-vs-delivered
- [Synergy Tracker](../../ma/synergy-tracker/SKILL.md) — M&A run-rate synergies
- [QBR](../../management/qbr/SKILL.md) — quarterly customer sitting
- [Operating Review](../../management/operating-review/SKILL.md) — weekly internal exceptions
- [Project Close](../../project/project-close/SKILL.md) — hands benefits to BAU owners
- [Change Adoption](../../management/change-adoption/SKILL.md) — behaviours that unlock benefits
