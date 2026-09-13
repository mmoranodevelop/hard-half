---
name: data-reconciliation
description: >-
  Use when matching and reconciling records across 2+ systems / CSV / Excel —
  billing hours vs tickets, CRM vs ERP, timesheet vs PSA, payroll vs HRIS, AP
  3-way, intercompany. One Control pack + exception queue + one ASK. NOT for
  budget-variance, not cash-runway, not close-calendar.
license: MIT
---

# Data Reconciliation

**Reconciliation Control — one page** — purpose, sources, as-of, grain, match rules, totals, variance bridge, Top-N exceptions with disposition, one ASK. Default: professional-services billing / ops truth; same spine for FP&A, AP, CRM↔ERP, payroll↔HRIS, migration cutover.

Method origin: enterprise recon funnel (Wire Reconciliation deterministic→fuzzy; Claro exact→probabilistic bands; Corpay 3-way + tolerances; Deloitte IC central repository + ownership; SAP/BlackLine transaction matching + exception certify). Exact keys first; confidence labelled; holes stay holes.

If they want a matching / entity-resolution lecture: one paragraph then produce or stop.

## When to use

- Two or more exports disagree and someone must decide which rows are truth
- Client requests / tickets vs hours worked for billing or a client report
- CRM vs ERP, timesheet vs ticket/PSA, payroll vs HRIS, bank vs GL, PO/GRN/invoice
- Migration cutover: source vs target row counts / keys / amounts before go-live
- Exception queue is stale or "mostly matched" with no materiality

## When not to use

- This vs last vs plan on the P&L — [Budget Variance](../../management/budget-variance/SKILL.md)
- Bank cash / 13-week runway — [Cash Runway](../../management/cash-runway/SKILL.md)
- Who locks on which BD — [Close Calendar](../../finance/close-calendar/SKILL.md)
- Hour-by-hour go-live runbook — [Cutover Plan](../../project/cutover-plan/SKILL.md)
- CCC / DSO this month — [Working Capital](../../finance/working-capital/SKILL.md)
- One-source data cleanse with no second system to match against — stop; not this skill

A single CSV with duplicates is dedupe, not recon. Recon needs **left and right** (or 3+).

## Modes

| Mode | When | Output |
|---|---|---|
| **produce** | Default. ≥2 sources, purpose, grain | Control one-pager + Top-N queue + one ASK |
| **redline** | They pasted a "reconciled" sheet or vague match % | Rebuild classes; kill invented joins; list holes |
| **refuse** | <2 sources, grain unknown, or "just invent the matches" | Issues list. Stop |
| **diagnose** | Match rate <80% or queue exploding | Name master-data / key / grain fault; still ship page or issues list |

## Hard rules

1. **Purpose first.** Billing / audit / ops truth / migration cutover — changes keys and materiality.
2. **≥2 sources.** Name left and right (and N). Same as-of date (or labelled skew).
3. **Grain stated.** What one row means (ticket, time entry, invoice line, employee, SKU). Refuse if grain mixes without a map.
4. **Match order fixed:** primary exact key → secondary composite → fuzzy (name/email/text) with **confidence bands**. Never fuzzy-first.
5. **Classify every row:** Matched | Partial | Unmatched left | Unmatched right | Conflict (same key, different values). No silent drops.
6. **Quantify:** counts, $, hours, % matched. State **materiality** (absolute and/or %). Below-threshold noise is not Top-N.
7. **Exception queue ranked** by $ / hours / risk. Each row: suggested disposition — accept / investigate / correct source / write-off.
8. **One ASK** — owner, verb, date — to clear top exceptions or fix the upstream process.
9. **Never invent matches.** Holes stay holes. Low-confidence stays labelled. Do not round a Conflict into Matched.
10. **One page** (+ optional queue annex). Not a matching textbook.

## Intake

If **two** of 1–4 are missing after one round: issues list, not a fake recon.

1. Purpose (billing / audit / ops / cutover) — load-bearing
2. Sources (≥2 files/systems) with as-of dates — load-bearing
3. Grain (row meaning) on each side — load-bearing
4. Primary match key(s) or "unknown — propose" — load-bearing
5. Amount / hours / qty fields and materiality threshold
6. Tolerance (absolute / %) and who owns exceptions
7. Fuzzy allowed? (name/email) and auto vs review bands
8. The decision this pack must unlock (invoice, attest, cutover Go, write-off)

## Output shape

```
RECONCILIATION CONTROL  |  [purpose]  |  as-of: [date]  |  CLASS: [billing|audit|ops|cutover]
ASK: [owner] to [clear Top-N / correct source X / attest / write-off] by [date].

BLUF
[Claim.] Matched [n / %] of [grain]. Exceptions [n] = $[ ] / [ ]h above materiality [ ].
Biggest hole: [Unmatched L|R / Conflict] on [key field].

SOURCES AND GRAIN
Left:  [system/file]  rows:[ ]  grain:[ ]  as-of:[ ]
Right: [system/file]  rows:[ ]  grain:[ ]  as-of:[ ]
(+N):  [ ]  Skew: [none | left earlier/later by nd]

MATCH RULES
1 Exact: [key fields]     → Matched @ conf 1.0
2 Composite: [fields]     → Matched @ conf [ ]
3 Fuzzy (if allowed): [name/email] bands: auto≥[ ] / review[ ]–[ ] / refuse<[ ]
Tolerance: $[ ] or [ ]%   Materiality for Top-N: $[ ] / [ ]h

TOTALS
| Side | Rows | $ or hours | Matched | Partial | Unmatched | Conflict |
| Left |  |  |  |  |  |  |
| Right|  |  |  |  |  |  |
Match rate (by count / by $ or h): [ ] / [ ]

VARIANCE BRIDGE (if amounts/hours)
Left total [ ] → matched [ ] → partial Δ [ ] → unmatched L [ ] → unmatched R [ ] → conflicts Δ [ ] → Right total [ ]
Unexplained residual: [ ]  (must be 0 or labelled hole)

TOP EXCEPTIONS (rank by $ / h / risk)
| # | Class | Key/ref | Left | Right | Δ | Conf | Disposition |
| 1 |  |  |  |  |  |  | accept/investigate/correct source/write-off |
| 2 |  |  |  |  |  |  |  |
| 3 |  |  |  |  |  |  |  |

NOT THIS PAGE
P&L vs plan → budget-variance    Bank runway → cash-runway    Lock calendar → close-calendar    Go-live hours → cutover-plan

Holes: [ ]
```

Queue annex: `assets/exception-queue.md`.

## QA (must pass)

1. Purpose and ≥2 sources named; as-of and grain stated (or hole).
2. Match order exact → composite → fuzzy; bands labelled if fuzzy used.
3. Every row class used or explicitly empty; no silent drops.
4. Totals and match % present; materiality stated.
5. Top exceptions ranked with disposition; no invented joins.
6. One ASK with owner, verb, date.
7. Conflicts not relabelled Matched.
8. One page (+ optional queue); not a lecture.

If 1, 5, 6, or 7 fail: do not ship.

## Escalate / stop

- Only one source after one ask → refuse.
- They demand invented matches to hit a % → refuse.
- Fuzzy auto-merge without bands or owner → refuse.
- Suspected fraud / SOX attest / statutory write-off → pack is exhibit; principal + finance + counsel.
- Grain conflict unresolvable (ticket vs time entry with no key map) → diagnose; do not fake a join.
- Cutover Go depends on this recon and residual above materiality → stop Go; hand to [Cutover Plan](../../project/cutover-plan/SKILL.md) owners with this pack as blocker.

## Related

- [Budget Variance](../../management/budget-variance/SKILL.md) — accrual vs plan; this is record match across systems
- [Cash Runway](../../management/cash-runway/SKILL.md) — bank liquidity; bank↔GL recon can use this spine
- [Close Calendar](../../finance/close-calendar/SKILL.md) — when recon tasks lock; this is the recon itself
- [Working Capital](../../finance/working-capital/SKILL.md) — DSO/DIO/DPO; AR/AP subledger↔GL recon feeds it
- [Cutover Plan](../../project/cutover-plan/SKILL.md) — go-live hours; this certifies data before/after cut
