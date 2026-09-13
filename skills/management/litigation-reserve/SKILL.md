---
name: litigation-reserve
description: >-
  Use when a material dispute needs exposure, reserve range, settlement band,
  counsel status, and one ASK. NOT for crisis-holding (comms), not raid-register
  (generic risks).
license: MIT
---

# Litigation Reserve

**Litigation reserve one-pager** — matter facts, probable/possible/remote, accrued vs disclosed range, insurance recovery, settlement band, counsel status, one ASK. Default: MD/CFO/GC sitting on a named dispute; same spine for audit committee pre-read.

Method origin: ASC 450 / IAS 37 contingency recognition (probable + reasonably estimable → accrue; reasonably possible → disclose range or state cannot estimate) + Big 4 litigation-contingency practice summaries.

If they want an ASC 450 / IAS 37 lecture: one paragraph then produce or stop.

## When to use

- Named lawsuit, arbitration, regulatory action, or threatened claim is material
- "What should we reserve / disclose / settle for?"
- Settlement authority or accrual change needs a decision this week
- Audit / board pack needs exposure + range, not a war-story memo

## When not to use

- First-hour holding statement — [Crisis Holding](../../writing/crisis-holding/SKILL.md)
- Generic program risks / assumptions / issues — [RAID Register](../../management/raid-register/SKILL.md)
- Customer-visible outage cadence — [Severity Customer](../../delivery/severity-customer/SKILL.md)
- Going-concern liquidity — [Cash Runway](../../management/cash-runway/SKILL.md)
- Policy renewals / limits — [Insurance Renewal](../../finance/insurance-renewal/SKILL.md)
- Legal strategy memo or privilege log — stop; counsel owns that

This page is **accounting + settlement economics for operators**, not litigation advice.

## Modes

| Mode | When | Output |
|---|---|---|
| **produce** | Default. Named matter + counsel input | One-pager + one ASK |
| **redline** | They pasted a "reserve" with no probable/possible split | Rebuild ASC/IAS classes; kill invented midpoints |
| **refuse** | No matter named, no counsel status, or "just pick a number" | Issues list. Stop |

## Hard rules

1. **Matter first.** Caption / counterparty / forum / claim theory / stage. No anonymous "legal risk."
2. **Likelihood class explicit:** remote | reasonably possible | probable (ASC 450) — or remote / possible / probable (IAS 37). Do not invent probability %.
3. **Accrue only if probable AND reasonably estimable.** Else disclose nature + range or "estimate cannot be made." Never invent a point estimate to look decisive.
4. **Range over fake precision.** Low–high from counsel / history / offers. If only low end known (e.g. settlement offer), say so — offer can be evidence of low end.
5. **Insurance is separate.** Recovery probable + estimable may offset; do not net into zero exposure without naming carrier, notice status, reservation of rights.
6. **Settlement band ≠ reserve.** Reserve follows accounting; settlement band is negotiation authority. Label both.
7. **Counsel status on page 1.** External counsel named; privilege respected — facts and ranges they cleared, not strategy dump.
8. **One ASK** — owner, verb, date — approve accrual / disclosure language / settlement authority / notice to carrier.
9. **Never invent numbers.** Holes stay holes. "Cannot estimate" is a valid ASC/IAS outcome.
10. **One page.** Not a brief, not a deposition summary.

## Intake

If **two** of 1–4 are missing after one round: issues list, not a fake reserve.

1. Matter ID (caption/counterparty/forum) — load-bearing
2. Claimed relief / theories and current stage — load-bearing
3. Counsel status (in-house + external) and what they cleared for disclosure — load-bearing
4. Prior accrual / disclosure language (or "none") — load-bearing
5. Insurance notice / coverage position if any
6. Settlement discussions / offers (dates, amounts) if any
7. The decision this pack unlocks (accrue, disclose, settle, stand)

## Output shape

```
LITIGATION RESERVE  |  [matter]  |  as-of: [date]  |  CLASS: contingency
ASK: [owner] to [approve accrual / disclosure / settlement band / carrier notice] by [date].

BLUF
[Claim.] Likelihood: [remote|reasonably possible|probable]. Accrue: [Y/N $ or range].
Disclosed range: [low–high | cannot estimate]. Settlement band: [low–high | none].

MATTER
Counterparty: [ ]  Forum: [ ]  Stage: [pleadings|discovery|MSJ|trial|appeal|settlement]
Theories / claimed relief: [ ]  Materiality: [why this is on the page]

LIKELIHOOD AND MEASUREMENT
Standard: [ASC 450 | IAS 37 | both]
Class: [ ]  Basis: [counsel opinion / offer / precedent — cite source, not invented %]
Accrual: [amount or "none — not probable and/or not estimable"]
Reasonably possible excess: [range or "cannot estimate" + why]

INSURANCE / RECOVERY
Carrier notice: [Y/N date]  Position: [cover / ROR / deny / unknown]
Recoverable if probable+estimable: [ ]  Cap / retention: [ ]

SETTLEMENT BAND
Authority sought: [low–high]  Walk-away: [ ]  Offers on table: [ ]
Band owner: [GC/CFO]  Privilege note: [ranges cleared for this pack]

COUNSEL STATUS
In-house: [ ]  External: [firm]  Next milestone: [date]

NOT THIS PAGE
Holding → crisis-holding    Generic risks → raid-register    Policy limits → insurance-renewal

Holes: [ ]
```

Optional annex: `assets/matter-strip.md`.

## QA (must pass)

1. Matter named; likelihood class stated without invented %.
2. Accrue vs disclose logic follows probable + estimable (or IAS equivalent).
3. Range or "cannot estimate" — no fake midpoint.
4. Insurance separated from gross exposure.
5. Settlement band labelled separately from reserve.
6. One ASK with owner, verb, date.
7. No invented numbers; holes labelled.
8. One page; not a legal brief.

If 1, 2, 6, or 7 fail: do not ship.

## Escalate / stop

- No counsel input on likelihood/range after one ask → refuse.
- They want a number with no facts → refuse.
- Privilege / strategy beyond cleared ranges → stop; GC owns.
- Criminal / regulatory personal exposure → principal + GC + outside counsel.
- Going-concern or disclosure clock (earnings / 8-K) → this page is exhibit; CFO + GC + board.

## Related

- [Crisis Holding](../../writing/crisis-holding/SKILL.md) — first-hour words; this is reserve/settlement economics
- [RAID Register](../../management/raid-register/SKILL.md) — generic risks; this is one named dispute
- [Insurance Renewal](../../finance/insurance-renewal/SKILL.md) — program limits; this is a claim against them
- [Cash Runway](../../management/cash-runway/SKILL.md) — if settlement cash timing binds liquidity
- [Executive Board Memo](../../management/executive-board-memo/SKILL.md) — board paper that may embed this exhibit
