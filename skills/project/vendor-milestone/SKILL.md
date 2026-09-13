---
name: vendor-milestone
description: >-
  Use at mid-delivery vendor milestone accept/reject: evidence vs SOW, defects,
  payment gate, one ASK. NOT for writing the SOW, not client UAT signoff, not
  go-live, not the monthly scorecard.
license: MIT
---

# Vendor Milestone

**Vendor milestone accept/reject — one page** — this milestone's deliverables vs SOW tests, evidence, defects, Accept / Conditional / Reject, payment gate on/off, one ASK. Default: venture buying an agency / SI / implementation vendor; same spine for F500.

Method origin: contract milestone + acceptance practice (objective criteria, review window, payment after acceptance / deemed-acceptance rules as *facts of the paper*, cure path). Reconstruct the operator gate. Do not invent pass counts or $ due.

If they want a SOW / payment-clause lecture: one paragraph then produce or stop.

## When to use

- A contracted mid-delivery milestone is due and someone must accept or reject
- Vendor says "done"; buyer has not matched evidence to SOW tests
- Payment / holdback hinges on this gate
- Conditional accept needs defect owners and cure dates, not "we'll fix it"

## When not to use

- Writing / awarding the SOW and its tests — [Vendor SOW](../../management/vendor-sow/SKILL.md)
- **Client** UAT / acceptance of *your* deliverables to the customer — [Acceptance Signoff](../../project/acceptance-signoff/SKILL.md)
- Go / no-go of the live event — [Go-Live Readiness](../../project/go-live-readiness/SKILL.md)
- Moving the signed baseline after conditional accept — [Change Control](../../project/change-control/SKILL.md)
- Monthly vendor pass/fail trend — [Vendor Scorecard](../../management/vendor-scorecard/SKILL.md)

If there is no SOW milestone ID or no acceptor, stop.

## Modes

| Mode | When | Output |
|---|---|---|
| **produce** | Default. Milestone due | One-page gate + ASK |
| **redline** | They pasted "LGTM" or a vendor status deck | Force SOW tests, evidence, defects, payment gate |
| **refuse** | No milestone ID, no tests, or invent pass/fail | Issues list. Stop |

## Hard rules

1. **Clock is this milestone gate.** SOW bought the tests; this page runs them for *this* vendor milestone; scorecard is trend; client acceptance is a different counterparty.
2. **Tests come from the SOW / order form.** "Looks good" is not a test. Missing criteria = hole — do not invent tests to greenlight payment.
3. **Evidence or it did not happen.** What was submitted, by whom, when, build/env/version.
4. **One named buyer acceptor.** "The business" fails. Counsel does not accept quality; the named A does.
5. **Decision: Accept / Accept with conditions / Reject.** Conditions = each open defect has severity, owner, cure-by, workaround. Open P1 + Accept = fail unless acceptor writes the residual.
6. **Payment gate is explicit:** amount (from paper or HOLE), payable only on Accept (or per written deemed-acceptance rule if the paper has one). Do not invent Net terms or $.
7. **Reject path on the page:** rework window, withhold, stop, escalate, terminate-for-cause pointer (business need — counsel owns clause).
8. **Never invent** defect counts, severities, or amounts due. Holes stay holes.
9. **One ASK** — named buyer D to Accept / Conditional / Reject and release or withhold payment by date.
10. **One page.**

## Intake

If **two** of 1–4 are missing after one round: issues list, not a fake gate.

1. Vendor, SOW / order ref, milestone ID — load-bearing
2. SOW acceptance tests for this milestone — load-bearing
3. What was submitted (artifacts / links) — load-bearing
4. Who accepts (name) and payment amount tied to this gate — load-bearing if payment is in play
5. Open defects already known
6. Review window / deemed-acceptance language if in the paper
7. Downstream: does reject slip go-live or client acceptance?

## Output shape

```
VENDOR MILESTONE  |  [vendor]  |  [SOW / PO]  |  Milestone [ID / name]  |  as-of [date]
ASK: [buyer D] to [Accept / Accept with conditions / Reject] and [release / withhold] [amount or HOLE] by [date]

SOW TESTS FOR THIS MILESTONE
| Test ID | Criterion (from SOW) | Evidence | Result | Notes |
| T1 | [ ] | [link / none→HOLE] | pass / fail / HOLE | |

DEFECTS
| ID | Severity | Description | Owner | Cure-by | Workaround |
| D1 | P1/P2/P3 or HOLE | [ ] | [vendor/buyer] | [date] | [ ] |

DECISION
[ ] Accept    [ ] Accept with conditions (all defects dated)    [ ] Reject
Residual written by acceptor (if any): [ ]

PAYMENT GATE
Amount tied to this milestone: [from paper / HOLE]
Release: only on Accept / per paper rule: [ ]
Withhold / holdback: [ ]

IF REJECT
Rework window: [ ]    Escalate to: [ ]    Stop / terminate pointer: [ ]    Client/go-live impact: [ ]

NOT THIS PAGE
Write the SOW → vendor-sow    Client UAT → acceptance-signoff
Live event → go-live-readiness    Baseline move → change-control    Monthly trend → vendor-scorecard

Holes: [ ]
```

## QA (must pass)

1. Milestone ID and SOW tests cited (or HOLE — no fake green).
2. Evidence listed or HOLE per test.
3. Decision is Accept / Conditional / Reject; conditions have owners and dates.
4. Payment gate explicit; no invented $.
5. One ASK with owner, verb, date.
6. Not SOW authoring, client signoff, go-live, scorecard, or silent baseline change.
7. One page.

If 1, 3, 5, or 4 (when payment in play) fail: do not ship.

## Escalate / stop

- Security / data / licence fail on evidence → Reject or hold; do not Conditional without residual.
- Vendor pressure to pay before tests → refuse; payment follows acceptance per paper.
- Conditional accept changes scope/date/cost baseline → [Change Control](../../project/change-control/SKILL.md) in parallel.
- No SOW tests exist → stop; send to [Vendor SOW](../../management/vendor-sow/SKILL.md) redline.

## Related

- [Vendor SOW](../../management/vendor-sow/SKILL.md) — buys the tests and milestone map
- [Acceptance Signoff](../../project/acceptance-signoff/SKILL.md) — client accepts *your* deliverables
- [Go-Live Readiness](../../project/go-live-readiness/SKILL.md) — live event go/no-go
- [Change Control](../../project/change-control/SKILL.md) — baseline moves after conditional
- [Vendor Scorecard](../../management/vendor-scorecard/SKILL.md) — monthly trend, not this gate
