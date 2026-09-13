---
name: eac-pulse
description: >-
  Use when Estimate at Complete / Estimate to Complete must be compared to
  budget and actuals with one ASK. NOT for budget-variance (past period P&L),
  not cash-runway, not reforecast (FY rewrite), not unbilled-leakage.
license: MIT
---

# EAC Pulse

**EAC / ETC pulse — one page** — Budget at Completion vs Actual Cost vs Estimate at Complete / Estimate to Complete; variance at complete; drivers; one ASK. Default: client / program cost pulse mid-flight; same spine for internal builds.

Method origin: Earned Value Management public (PV / EV / AC → EAC / ETC / VAC) — operator pulse, not a full EVMS / ANSI-748 lecture. Use the inputs you have; do not invent a CPI story without EV.

If they want an EVMS lecture: one paragraph then produce or stop.

## When to use

- "Will we finish inside the envelope?" with actuals in hand
- Sponsor / SteerCo needs EAC vs BAC this period, not a P&L tour
- Remaining work cost (ETC) must drive a change or contingency call
- CPI/SPI available — or honest HOLE with bottom-up ETC instead

## When not to use

- This period vs plan (price/volume/mix) — [Budget Variance](../../management/budget-variance/SKILL.md)
- Bank 13-week liquidity — [Cash Runway](../../management/cash-runway/SKILL.md)
- Remaining fiscal-year rewrite — [Reforecast](../../finance/reforecast/SKILL.md)
- Hours eaten without a CR / missing invoice line — [Unbilled Leakage](../../delivery/unbilled-leakage/SKILL.md)
- Pre-commit confidence band — [Estimate Confidence](../../project/estimate-confidence/SKILL.md)
- Client status RAG — [Sponsor Status](../../project/sponsor-status/SKILL.md)

## Modes

| Mode | When | Output |
|---|---|---|
| **produce** | Default. BAC + AC (and EV or bottom-up ETC) | Pulse page + ASK |
| **redline** | They pasted "we're over" with no EAC | Force BAC/AC/EAC/ETC; kill vibes |
| **refuse** | No BAC and no AC, or invent CPI | Issues list. Stop |

## Hard rules

1. **BAC, AC, EAC, ETC on the page.** Missing → HOLE. Do not imply green without them.
2. **Method for EAC named:** CPI-based (BAC/CPI or AC+(BAC−EV)/CPI), atypical (AC+(BAC−EV)), CPI×SPI, or **bottom-up ETC**. Pick one; say why.
3. **EV optional but honest.** No EV → use bottom-up ETC; do not fake CPI.
4. **VAC = BAC − EAC** (or labelled equivalent). Over/under in money, not adjectives.
5. **Drivers ≤3** of the EAC move vs last pulse / vs BAC. Owner + verb.
6. **One ASK** — D to accept EAC, release contingency, CR scope, or stop work by date.
7. **Never invent** AC, EV%, CPI, or remaining hours. Holes stay holes.
8. **One page.** Not a full EVMS compliance pack.

## Intake

If **two** of 1–4 are missing after one round: issues list, not a fake pulse.

1. Project + BAC (approved envelope) — load-bearing
2. AC to date (source: finance / timesheet) — load-bearing
3. EV or % complete basis, or "no EV — bottom-up ETC" — load-bearing
4. As-of date / period — load-bearing
5. Last period's EAC if any
6. Contingency remaining / drawn
7. Who has D on envelope change

## Output shape

```
EAC PULSE  |  [project]  |  as-of: [date]  |  D: [name]
Currency: [ ]     BAC source: [charter/CR v]

ASK: [D] to [accept EAC / draw contingency / raise CR / stop] by [date]

NUMBERS
|  | Amount | Source / method |
| BAC |  |  |
| AC to date |  |  |
| EV (or HOLE) |  | % complete basis: [ ] |
| CPI / SPI (or HOLE) |  |  |
| ETC |  | bottom-up / CPI-based / other: [ ] |
| EAC |  | formula: [ ] |
| VAC (BAC−EAC) |  | over / under / unknown |

TREND
Last EAC: [ ] → This EAC: [ ]     Delta: [ ]

DRIVERS (≤3)
| # | Driver | $ impact on EAC | Owner | Action by |
| 1 |  |  |  |  |

CONTINGENCY
Held: [ ]  Drawn: [ ]  Remaining vs VAC: [ ]

NOT THIS PAGE
Period P&L → budget-variance    Cash → cash-runway
FY rewrite → reforecast    Missing invoice lines → unbilled-leakage
Pre-commit band → estimate-confidence

Holes: [ ]
```

Annex: `assets/eac-strip.md`.

## QA (must pass)

1. BAC + AC present or explicitly HOLE — no silent skip.
2. EAC method named; ETC shown.
3. VAC stated or unknown labelled.
4. One ASK with owner, verb, date.
5. ≤3 drivers with owners.
6. Not variance P&L, cash, FY reforecast, or leakage register.
7. No invented CPI/EV. One page.

If 1, 2, 4, or 7 fail: do not ship.

## Escalate / stop

- AC and BAC both missing after one ask → stop.
- They want ANSI-748 / full EVMS certification pack → refuse lecture; keep pulse.
- EAC blows envelope with no D → escalate; page still shows VAC.
- Leakage explaining burn without CR → note; [Unbilled Leakage](../../delivery/unbilled-leakage/SKILL.md) owns the lines.

## Related

- [Budget Variance](../../management/budget-variance/SKILL.md) — past period P&L drivers
- [Cash Runway](../../management/cash-runway/SKILL.md) — bank cash, not project EAC
- [Reforecast](../../finance/reforecast/SKILL.md) — remaining FY company plan
- [Unbilled Leakage](../../delivery/unbilled-leakage/SKILL.md) — uneaten invoice lines
- [Estimate Confidence](../../project/estimate-confidence/SKILL.md) — pre-commit band
- [Change Control](../../project/change-control/SKILL.md) — baseline delta when EAC forces a CR
- [Sponsor Status](../../project/sponsor-status/SKILL.md) — client RAG; may cite this pulse
