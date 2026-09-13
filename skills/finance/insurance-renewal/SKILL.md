---
name: insurance-renewal
description: >-
  Use when renewing D&O / cyber / E&O: coverage vs risk appetite, gaps, premium
  vs limit ASK. NOT for vendor-sow, not vendor-scorecard.
license: MIT
---

# Insurance Renewal

**Insurance renewal one-pager** — lines in scope (D&O / cyber / E&O ± others), limits vs risk appetite, key exclusions/gaps, premium vs prior, one ASK. Default: CFO/GC/broker sitting before bind; same spine for board risk committee pre-read.

Method origin: Marsh/Aon public risk-transfer primers (D&O vs cyber complementarity, Side A erosion, first- vs third-party cyber) + NACD D&O essentials (what D&O does and does not cover after cyber).

If they want an insurance-market lecture: one paragraph then produce or stop.

## When to use

- D&O, cyber, and/or E&O renewal is inside the decision window
- "Are we covered for X?" vs appetite before bind
- Premium up / limits down / exclusions new — need approve/deny/change
- Board asks whether Side A / cyber standalone / shared tower is adequate

## When not to use

- Buying an agency/SI SOW — [Vendor SOW](../../management/vendor-sow/SKILL.md)
- Scoring a broker or carrier as a vendor — [Vendor Scorecard](../../management/vendor-scorecard/SKILL.md)
- Live cyber incident response — [Cyber Incident Brief](../../management/cyber-incident-brief/SKILL.md)
- Accruing a claim — [Litigation Reserve](../../management/litigation-reserve/SKILL.md)
- Liquidity to pay premium — [Cash Runway](../../management/cash-runway/SKILL.md)
- Policy wordings as legal advice — stop; broker + coverage counsel

This page is **risk-transfer decision pack**, not a binder rewrite.

## Modes

| Mode | When | Output |
|---|---|---|
| **produce** | Default. Lines + quotes/expiring terms | One-pager + one ASK |
| **redline** | They pasted a "we're covered" slide | Rebuild gaps vs appetite; kill vague "full cyber" |
| **refuse** | No lines named, no expiring limits, or "just pick cheapest" with no appetite | Issues list. Stop |

## Hard rules

1. **Lines named.** D&O / cyber / E&O (add others only if in this renew). No "insurance" blob.
2. **Appetite first.** What loss scenarios must transfer off the balance sheet? Limits follow appetite, not last year's habit.
3. **D&O ≠ cyber.** D&O: fiduciary / securities / oversight claims. Cyber: first-party forensics/BI/notification + third-party privacy. State both; map overlaps and gaps.
4. **Gaps explicit:** exclusions, sublimits, retentions, co-insurance, prior-acts, BI waiting periods, ransomware coinsurance, Side A vs ABC erosion.
5. **Premium vs limit table.** Prior vs quoted; do not invent market % moves. Unknown = hole.
6. **One ASK** — bind as quoted / change limit / accept named gap / instruct broker / buy Side A DIC.
7. **Never invent premiums, limits, or loss ratios.** Use quote/expiring docs only.
8. **Claims-made clocks.** Retro date / ERP options called out when material.
9. **Broker is not the decision.** Broker facts feed the page; CFO/GC/board owns bind.
10. **One page** (+ optional coverage matrix annex).

## Intake

If **two** of 1–4 are missing after one round: issues list, not a fake renew.

1. Lines renewing and effective date — load-bearing
2. Expiring limits / retentions / premium — load-bearing
3. Quoted options (or "quote pending") — load-bearing
4. Risk appetite / scenarios that must be transferred — load-bearing
5. Material claims / notice history last 3–5 years (or "none known")
6. Related policies that interact (crime, property, tech E&O)
7. The decision deadline (bind-by)

## Output shape

```
INSURANCE RENEWAL  |  [lines]  |  bind-by: [date]  |  CLASS: risk-transfer
ASK: [owner] to [bind / change limit / accept gap / instruct broker] by [date].

BLUF
[Claim.] Appetite scenarios covered: [list]. Material gaps: [list or none].
Premium vs prior: [prior → quoted | unknown]. Recommended: [option].

APPETITE
Scenarios that must transfer: [e.g. Side A personal, privacy notification, BI, E&O client claim]
Risk retained by design: [ ]

PROGRAM (prior → quoted)
| Line | Limit | Retention | Premium | Key change |
| D&O |  |  |  |  |
| Cyber |  |  |  |  |
| E&O |  |  |  |  |

GAPS / EXCLUSIONS (material)
[exclusion / sublimit / waiting period / ransomware terms / prior-acts / shared tower erosion]

D&O vs CYBER vs E&O MAP
Overlap: [ ]  Gap between policies: [ ]  Side A protected from entity erosion: [Y/N/unknown]

CLAIMS / NOTICE HISTORY
[summary or none] — drives underwriting narrative; do not invent

OPTIONS
A: [ ]  B: [ ]  Reject: [cheapest with named hole]

NOT THIS PAGE
SOW buy → vendor-sow    Broker score → vendor-scorecard    Live incident → cyber-incident-brief

Holes: [ ]
```

Optional annex: `assets/coverage-matrix.md`.

## QA (must pass)

1. Lines named; appetite scenarios stated.
2. Prior vs quoted table with holes labelled — no invented market stats.
3. D&O vs cyber complementarity addressed if both in scope.
4. Material gaps/exclusions listed or "none material."
5. One ASK with owner, verb, date.
6. One page; not a policy novel.

If 1, 2, or 5 fail: do not ship.

## Escalate / stop

- No quote and no expiring terms after one ask → refuse.
- Demand to invent "market is up X%" → refuse.
- Coverage opinion on a live claim → coverage counsel; not this page.
- Personal Side A inadequacy for directors → board + GC immediately.
- Non-renew / exclusion that kills a material scenario → do not bind silent; escalate.

## Related

- [Vendor SOW](../../management/vendor-sow/SKILL.md) — buying services; this is risk transfer
- [Vendor Scorecard](../../management/vendor-scorecard/SKILL.md) — scoring suppliers
- [Cyber Incident Brief](../../management/cyber-incident-brief/SKILL.md) — live incident uses the program
- [Litigation Reserve](../../management/litigation-reserve/SKILL.md) — claim economics after notice
- [Cash Runway](../../management/cash-runway/SKILL.md) — premium cash timing if material
