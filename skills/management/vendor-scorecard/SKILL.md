---
name: vendor-scorecard
description: >-
  Use when scoring whether a named vendor is passing the SOW tests this month:
  quality, schedule, cost, management, credits, continue/cure/exit. NOT for the
  SOW itself. Not the program operating review.
license: MIT
---

# Vendor Scorecard

**Monthly vendor scorecard** — pass/fail on this period's SOW tests, credits due, one ASK (continue / CAP / credit / exit). Default: venture buying an agency or SI; same spine for F500.

Method origin: FAR 42.1503 / CPARS — rate against contractual requirements with facts, not vibes. IACCM/WorldCC: post-award governance is where value erodes. This page tests the [Vendor SOW](../../management/vendor-sow/SKILL.md). Do not rewrite the SOW here.

If they want a CPARS lecture: one paragraph then produce or stop.

## When to use

- "Is this vendor passing?" / month-end vendor review
- Credits, holdback, or a cure notice is on the table
- Renewal, extension, or "we should fire them" needs evidence
- Two vendors on one program — one scorecard each

## When not to use

- Drafting or redlining the **SOW** — [Vendor SOW](../../management/vendor-sow/SKILL.md)
- Weekly **program** exceptions (people, cash, RAID) — [Operating Review](../../management/operating-review/SKILL.md)
- Whether users adopted what the vendor shipped — [Change Adoption](../../management/change-adoption/SKILL.md)
- Whether to buy at all — [Business Case](../../strategy/business-case/SKILL.md)
- Quarterly sitting with a **customer or sponsor** — [QBR](../../management/qbr/SKILL.md)
- A fail that must become a RAID row — [RAID Register](../../management/raid-register/SKILL.md)
- Counsel's default/termination letter — flag; do not impersonate counsel

## Modes

| Mode | When | Output |
|---|---|---|
| **produce** | Default. Period just closed or closing | Filled scorecard + ASK |
| **redline** | They pasted a vendor "green" pack or a prior scorecard | Fail rows; rewrite the ASK |
| **refuse** | No SOW tests, no period, or they want a vibe rating | Issues list. Stop |

## Hard rules

1. **Score the SOW tests this period, not the relationship.** If the test is not in the SOW / order form, it is not a fail — it is a change, or a hole.
2. **Facts, then rating.** "They're difficult" is not a rating.
3. **Buyer-caused delay is named, not hidden.** If we missed a dependency, the vendor does not fail that row.
4. **Credits and holdback are arithmetic.** If the contract has a credit and we missed the SLA, the ASK includes collecting it. "We'll let it go this month" is a decision, written.
5. **Red/yellow have owner, date, next action.** Colour without a CAP is theatre.
6. **One ASK:** continue / collect-credit / CAP-with-date / stop-work / exit. Named owner. Not "monitor closely".
7. **Do not impersonate counsel** on termination for cause. Do not invent uptime, burn, or UAT pass-rates.

## Intake

If **period** and **SOW tests due** are both missing after one round: issues list, not a fake page.

1. Vendor, contract / SOW pointer, period (month default) — load-bearing
2. Tests due this period (acceptance, SLA, milestone) — load-bearing
3. Actuals you have (pass/fail, numbers) and holes
4. Buyer dependencies we missed
5. Credits / holdback / CAP already in the paper
6. What you want to be true by next period (continue / cure / exit)
7. F500 or venture (venture default)

## Output shape

```
VENDOR SCORECARD  |  [vendor]  |  [program]  |  [period]
SOW / order: [pointer]   Ceiling / remaining: [ ]   Acceptor: [role]

VERDICT (one sentence): PASS | CONDITIONAL | FAIL
ASK: continue | collect credit [amount] | CAP by [date] | start exit
Owner of ASK: [name]    Decide-by: [date]

| ID | SOW test this period | Standard | Actual | Rating | Evidence | If fail |
| | | | | E/VG/S/M/U or hole | | credit / CAP / n/a |

FACTOR ROLL-UP (against this SOW)
Quality:  [rating]  [one fact]
Schedule: [rating]  [one fact]
Cost:     [rating]  [one fact]   (n/a if firm-fixed and no overrun)
Management / business relations: [rating]  [one fact]

BUYER-CAUSED (does not fail the vendor)
- [dependency we missed → impact]

CREDITS / HOLDBACK
Due this period: [amount or 0]    We will collect / waive (named decision): [ ]

CAP (if CONDITIONAL or FAIL)
Gap: [ ]    Vendor action: [ ]    Buyer action: [ ]    Review date: [ ]

NEXT PERIOD TESTS
- [ ]

NOT THIS PAGE
The SOW itself → vendor-sow    Program exceptions → operating-review    User behaviour → change-adoption

Holes: [ ]
```

## QA (must pass)

1. Period and vendor named.
2. Every scored row traces to a SOW / SLA / milestone test (or is marked hole).
3. Verdict is PASS / CONDITIONAL / FAIL, not a paragraph.
4. ASK is one of: continue / credit / CAP-with-date / exit. Owner + date.
5. Buyer-caused delay is not scored as vendor fail.
6. Credits are computed or explicitly waived.
7. No invented actuals.
8. Not an operating-review of the whole program.
9. Not a rewrite of the SOW.
10. One page.

If 2, 4, or 7 fail: do not ship.

## Escalate / stop

- No tests in the contract → stop. Route to [Vendor SOW](../../management/vendor-sow/SKILL.md). Do not invent SLAs to fail them against.
- They want "unsatisfactory" with no event → refuse.
- They want to skip the credit they are owed "to keep the relationship" → write the waiver as the ASK, do not hide it.
- Termination / employment / data incident → counsel. Scorecard can still say FAIL.
- This is actually "are we adopting the tool" → [Change Adoption](../../management/change-adoption/SKILL.md).

## Related

- [Vendor SOW](../../management/vendor-sow/SKILL.md) — the tests you are scoring
- [Operating Review](../../management/operating-review/SKILL.md) — program exceptions; this is one vendor line
- [Change Adoption](../../management/change-adoption/SKILL.md) — user behaviour after they ship
- [RAID Register](../../management/raid-register/SKILL.md) — a fail may become a RAID item
- [Cash Runway](../../management/cash-runway/SKILL.md) — the SOW is a disbursement; credits are cash
- [QBR](../../management/qbr/SKILL.md) — one customer/sponsor quarter; this is the vendor this month
