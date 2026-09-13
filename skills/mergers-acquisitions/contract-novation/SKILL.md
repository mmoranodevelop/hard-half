---
name: contract-novation
description: >-
  Use when a deal needs a consent / novation log: stock vs asset, notice vs
  consent vs public-sector novation, close-critical vs post-close. Third-party
  consent to keep existing contracts alive. NOT for vendor-sow, not tsa-
  schedule.
license: MIT
---

# Contract Novation

**Consent / Novation Log** — one page: counts (auto-transfer / notice-only / consent required / novation required); top material contracts with clause type, status, owner, need-by, workaround if refused; ASK which consents are close-critical vs post-close. Default: venture deal; same spine for F500.

Method origin: public-sector novation rules (stock vs asset; successor recognition is discretionary, usually not a closing condition) plus commercial doctrine (assignment is not novation; all parties must consent). Not legal advice; counsel owns the clauses.

If they want a novation / assignment lecture: one paragraph then produce the log or stop.

## When to use

- Signing or close and nobody has a consent log
- "Legal is handling contracts"
- Stock deal assumed to move every contract, or public-sector novation treated as a signing condition with no timeline
- Payroll vendor, cloud, or payment processor may refuse

## When not to use

- New work you are buying — [Vendor SOW](../../management/vendor-sow/SKILL.md)
- Seller-as-bridge services — [TSA Schedule](../../ma/tsa-schedule/SKILL.md)
- Close continuity tests — [Day-1 Continuity](../../ma/day1-continuity/SKILL.md)
- Named-logo owner/script — [Named Account Day 1](../../ma/named-account-day1/SKILL.md)
- IP / domain / repo control — [Control Handover](../../ma/control-handover/SKILL.md)
- Workstream from signing — [IMO Charter](../../ma/imo-charter/SKILL.md)

## Modes

| Mode | When | Output |
|---|---|---|
| **produce** | Default. Deal type known | Counts + top-15 log + ASK |
| **redline** | They pasted "legal is handling" or a contract dump | Force clause type, close-critical vs post-close |
| **refuse** | Two load-bearing facts missing, or a lecture | Issues list. Stop |

## Hard rules

1. **Stock deal is not an asset deal.** On a stock purchase, if the contracting party is unchanged and still performing, novation is often unnecessary. On an asset transfer the contracting party changes — assignment or novation.
2. **Public-sector successor paper is discretionary**, measured in weeks to months, typically **not** a closing condition; parties covenant to pursue it post-close, sometimes with an interim subcontract.
3. **Assignment moves rights** (seller may remain liable); **novation substitutes the party** and needs **all** counterparties' consent. Anti-assignment and change-of-control are the diligence flags. Novation can reopen price/terms.
4. **Counts on page 1:** auto-transfer (stock) / notice-only / consent required / novation required.
5. **Top 15 revenue or ops-critical:** counterparty, clause type, status, owner, need-by, workaround if refused.
6. **ASK: close-critical vs post-close.** Do not make public-sector novation a signing condition without a timeline counsel will defend.
7. **Do not invent clause types.** Holes stay holes. Do not assume vendor SOWs move because you closed.

## Intake

If **two** of 1, 2, 4 are missing after one round: issues list, not a fake log.

1. Stock vs asset (or hybrid) — load-bearing
2. Material contracts — list, count, or "unknown / legal handling" — load-bearing
3. Public-sector / regulated contracts? yes / no / unknown
4. Close-critical vs post-close already split? or "all of them" — load-bearing
5. Anti-assignment / change-of-control already flagged in diligence?
6. Need-by dates (close, customer live, payroll run)
7. Workaround if refused (interim subcontract, TSA, dual entity)

## Output shape

```
CONSENT / NOVATION LOG  |  [deal]  |  as-of: [date]  |  CLASS: CONTINUITY
Deal type: [stock / asset / hybrid]     GC / workstream owner: [name]     D: [name]
Public-sector contracts: [yes/no/unknown]

ASK: [D] to treat [named contracts] as [close-critical / post-close] by [date]; workaround if refused: [ ].
Owner of ASK: [ ]    Decide-by: [ ]

COUNTS
Auto-transfer (stock, party unchanged): [n]
Notice-only: [n]
Consent required: [n]
Novation required: [n]     Timeline: [weeks to many months typical]

TOP MATERIAL
| Counterparty | Why critical (revenue/ops) | Clause (notice/consent/novation) | Status | Owner | Need-by | Workaround if refused |
| [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [interim subcontract / TSA / dual entity / HOLE] |

NOT THIS PAGE
New buy → vendor-sow    Seller bridge → tsa-schedule    Close tests → day1-continuity
Stock does not automatically move every contract.
Public-sector novation is usually post-close, not a signing condition.

Holes: [ ]
```

## QA (must pass)

1. ASK (close-critical vs post-close, named contracts, date) + owner.
2. Deal type (stock/asset) named.
3. Counts by clause type (or labelled unknown).
4. Public-sector novation not treated as a signing condition with no timeline.
5. Top rows have workaround-if-refused.
6. Not a vendor-sow or "legal is handling".
7. No invented clause types.
8. One page.

If 1, 2, 6, or 7 fail: do not ship.

## Escalate / stop

- Two of deal type / material contracts / close-critical split missing after one ask → issues list.
- "Legal is handling contracts" → refuse the sentence; produce a hole-labelled log or stop.
- Public-sector novation as a signing condition with no timeline → refuse.
- They want a new-buy SOW → [Vendor SOW](../../management/vendor-sow/SKILL.md).
- They want legal advice on a clause → counsel; this page is the IMO log.

## Related

- [Vendor SOW](../../management/vendor-sow/SKILL.md) — new buy; this keeps existing paper alive
- [TSA Schedule](../../ma/tsa-schedule/SKILL.md) — seller bridge, not third-party consent
- [Day-1 Continuity](../../ma/day1-continuity/SKILL.md) — close tests; this log feeds holes
- [Control Handover](../../ma/control-handover/SKILL.md) — IP/domain control, not vendor consent
- [Named Account Day 1](../../ma/named-account-day1/SKILL.md) — customer comms; customer contracts sit here if consent is required
- [IMO Charter](../../ma/imo-charter/SKILL.md) — workstream from signing
