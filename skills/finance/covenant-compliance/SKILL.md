---
name: covenant-compliance
description: >-
  Use when flashing lender covenant status: headroom, breach path, cure options,
  one ASK. NOT for cash-runway (13-week bank), not reforecast, not working-
  capital (CCC).
license: MIT
---

# Covenant Compliance

**Lender covenant flash — one page** — named covenants, test date, actual vs threshold, headroom, breach path, cure (equity / waiver / amend), one ASK. Default: PE / sponsor-backed credit agreement; same spine for bilateral bank facilities.

Method origin: public credit-agreement practice — maintenance vs incurrence tests, headroom as buffer to threshold, equity-cure mechanics (Sidley / BHFS / borrower primers); PE portfolio monitoring treats proximity to covenant as an early-warning object.

If they want a leveraged-finance lecture: one paragraph then produce or stop.

## When to use

- "Are we inside covenants, and by how much?"
- Compliance certificate due; board / lender call this week
- Headroom narrowing after a soft month
- Cure / waiver / amend decision before test date
- New facility: first flash of the package

## When not to use

- 13-week bank strip / net burn — [Cash Runway](../../management/cash-runway/SKILL.md)
- Remaining-year P&L replace — [Reforecast](../../finance/reforecast/SKILL.md)
- DSO / DIO / DPO this month — [Working Capital](../../finance/working-capital/SKILL.md)
- Where next € goes (build/buy/return) — [Capital Allocation](../../strategy/capital-allocation/SKILL.md)
- Sponsor monthly KPI + cash narrative — [PE Monthly Flash](../../finance/pe-monthly-flash/SKILL.md)
- Going-concern board paper — [Executive Board Memo](../../management/executive-board-memo/SKILL.md)

Liquidity without a named covenant is runway. This page is **agreement math + path**.

## Modes

| Mode | When | Output |
|---|---|---|
| **produce** | Default. Facility + test period known | Covenant flash + headroom + one ASK |
| **redline** | They pasted a "compliant" slide with no math | Rebuild actual vs threshold; kill invented EBITDA add-backs |
| **refuse** | No agreement excerpt / definitions, or "just say green" | Issues list. Stop |

## Hard rules

1. **Name the facility and the test.** Maintenance (periodic) vs incurrence (event). Period and delivery date.
2. **Each material covenant:** definition pointer, threshold, actual (or hole), headroom (turns / € / %), trend.
3. **Headroom = buffer to breach**, not a vanity ratio. Shrinking headroom with "still compliant" is a yellow.
4. **Breach path explicit:** test fail → notice / EoD risk → standstill / acceleration (per agreement — do not invent).
5. **Cure options only if in the agreement:** equity cure (amount, timing, frequency caps), waiver, amend, prepay. No fantasy cures.
6. **One ASK** — certify / notify lender / inject cure / seek waiver / cut spend that protects the ratio. Owner, date.
7. **Do not invent EBITDA add-backs, netting, or cure caps.** Hole: `[counsel / facility schedule by DATE]`.
8. **Not legal advice.** Numbers and path; GC / counsel on notice and rights.
9. **Not the 13-week strip** (cash-runway owns bank timing).
10. **One page.**

## Intake

If **two** of 1–3 are missing after one round: issues list, not a fake green.

1. Facility name / agent / test period — load-bearing
2. Covenant list in scope (leverage, ICR/FCCR, liquidity, capex…) — load-bearing
3. Actual inputs (EBITDA, debt, cash, interest) as-of — load-bearing
4. Thresholds and any step-downs
5. Cure / waiver language available? (yes / no / unknown)
6. Certificate due date and who signs
7. The ASK this cycle

## Output shape

```
COVENANT FLASH  |  [entity / facility]  |  test period: [ ]  |  as-of: [date]
ASK: [owner] to [certify / notify / cure inject / seek waiver / protect ratio] by [date].

BLUF
Status: [inside / watch / breach path]. Tightest: [covenant] headroom [ ].
Certificate due: [date]  Signer: [ ]

COVENANTS
| Covenant | Type M/I | Threshold | Actual | Headroom | Trend | Status |
| Leverage | M |  |  |  | ↑↓→ | G/Y/R |
| ICR / FCCR |  |  |  |  |  |  |
| Liquidity / other |  |  |  |  |  |  |

DEFINITIONS / HOLES
EBITDA basis: [agreement def / hole]  Net debt / cash netting: [ ]  Add-backs used: [named or none]

BREACH PATH (if tight or red)
Trigger: [ ]  Notice / grace: [per agreement or hole]  Lender remedies risk: [do not invent]

CURE / RELIEF
| Option | Available? | Amount / timing | Caps / limits | Owner |
| Equity cure | y/n/unk |  |  |  |
| Waiver / amend |  |  |  |  |
| Prepay / cut |  |  |  |  |

NOT THIS PAGE
Bank 13w → cash-runway    Year replace → reforecast    CCC → working-capital    Sponsor KPI letter → pe-monthly-flash

Holes: [ ]
```

## QA (must pass)

1. Facility, test period, as-of date.
2. Each material covenant: threshold, actual or hole, headroom.
3. Status not "green" if headroom unknown.
4. Breach path only from agreement language or labelled hole.
5. Cure options not invented.
6. One ASK with owner, verb, date.
7. No invented add-backs.
8. Not runway, not reforecast, not CCC page.
9. One page.

If 1, 2, 5, or 6 fail: do not ship.

## Escalate / stop

- Actuals or definitions missing after one ask → refuse.
- They demand a green with no math → refuse.
- Breach or near-breach → this page is exhibit; CFO + GC + counsel + sponsor; do not draft notice without counsel.
- FX / tax / GAAP vs agreement EBITDA fight → specialist; flag hole.
- Liquidity cliff without named covenant → [Cash Runway](../../management/cash-runway/SKILL.md).

## Related

- [Cash Runway](../../management/cash-runway/SKILL.md) — bank timing; covenants may appear as floor there
- [Reforecast](../../finance/reforecast/SKILL.md) — remaining-year numbers that feed next test
- [Working Capital](../../finance/working-capital/SKILL.md) — CCC; may move leverage inputs
- [PE Monthly Flash](../../finance/pe-monthly-flash/SKILL.md) — sponsor pulse; this is lender math
- [Capital Allocation](../../strategy/capital-allocation/SKILL.md) — paydown vs invest trade
- [Executive Board Memo](../../management/executive-board-memo/SKILL.md) — board paper if going-concern / waiver
