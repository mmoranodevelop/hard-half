---
name: vendor-sow
description: >-
  Use when a program manager is buying an agency, integrator, or software
  implementation and needs a statement of work: outcome, acceptance tests,
  price-to-scope, IP choice, exit, one ASK. NOT for legal advice, not the
  business case, not the adoption plan.
license: MIT
---

# Vendor SOW

**SOW pack** a procurement lead can see "done" on — outcome, deliverables + acceptance, commercial, RACI with the vendor, IP choice, exit. Default: venture buying an agency or SI; same spine for F500.

Method origin: FAR 37.6 PWS shape + IACCM/WorldCC (scope, responsibilities, change beat liability theatre). Do not paste Crown/FAR clause text.

If they want a PWS lecture: one paragraph then produce or stop.

## When to use

- Draft or redline an SOW / PWS / order-form attachment
- The email is still "3 FTEs, T&M"
- Acceptance, IP, or exit is missing; price does not map to scope

## When not to use

- Whether to buy, NPV, make-vs-buy — [Business Case](../../strategy/business-case/SKILL.md)
- Whether users will use what you bought — [Change Adoption](../../management/change-adoption/SKILL.md)
- The disbursement / runway impact — [Cash Runway](../../management/cash-runway/SKILL.md)
- Weekly vendor status — [Operating Review](../../management/operating-review/SKILL.md)
- Monthly pass/fail on the tests — [Vendor Scorecard](../../management/vendor-scorecard/SKILL.md)
- Internal who-has-the-D — [Decision Rights](../../management/decision-rights/SKILL.md)
- Seller-as-bridge after a deal — [TSA Schedule](../../ma/tsa-schedule/SKILL.md)
- Liability caps, indemnity, DPA — counsel owns; this skill states the *business* need

## Modes

| Mode | When | Output |
|---|---|---|
| **produce** | Default. New buy | Filled SOW pack + ASK |
| **redline** | They pasted a vendor paper or MSA with no SOW | Issues list by load-bearing element, then rewritten spine |
| **refuse** | No outcome, no acceptor, or T&M with no ceiling and no tests | Issues list. Stop |

Pasted MSA, no SOW → say the SOW is the missing artifact. Score two papers with the same grid; no beauty contest.

## Hard rules

1. Outcome in one sentence (result, date, metric). Hours are a ceiling, not the deliverable.
2. Deliverables table: criterion, who accepts, by when, if-fail (rework / credit / stop). "Client will review" is not acceptance.
3. Price maps to a baseline. Out-of-scope list. Change control prices deltas. Milestone pay **after** acceptance.
4. Commercial matches uncertainty: crisp → fixed/milestone; discovery → T&M with ceiling *and* tests; ongoing → SLAs with credits that hurt.
5. RACI includes buyer *and* vendor. One Accountable per row. Buyer-furnished items dated. Key personnel named; substitution is a change.
6. IP is a picked option. Test: "we can run this if they leave." Counsel drafts the clause.
7. Exit is a schedule: data export, overlap, surviving licences, fees, step-in if critical. Do not invent rates or ceilings.

## Intake

If **two** of 1, 3, 6 are missing after one round: issues list, not a fake SOW.

1. What is being bought and **outcome** (result + date) — load-bearing
2. In / out of scope
3. Who accepts (name/role) and what evidence they need — load-bearing
4. Commercial model / ceiling already decided?
5. IP reality — whose code, content, data
6. What happens on day 181 if we fire them — load-bearing
7. Buyer dependencies we will actually staff

## Output shape

```
STATEMENT OF WORK  |  [program]  |  [vendor or "to be selected"]  |  [date]
Related MSA / order form: [ ]   Term: [ ]   Value / ceiling: [ ]

ASK: [buyer D] to [award / redline / reject] this SOW at [ceiling] by [date], subject to counsel on liability/DPA.

1. OUTCOME
[One sentence: result, date, metric.]
Period / place: [ ]    Constraints: [security, brand, systems]

2. SCOPE
In: [ ]
Out: [ ] — explicit
Assumptions price depends on: [data, licences, SME days, environment]

3. DELIVERABLES AND ACCEPTANCE
| ID | Deliverable | Format | Due | Acceptance test (pass/fail) | Acceptor | If fail |
| D1 | | | | | [role] | rework / credit / stop |

4. COMMERCIAL (PRICE-TO-SCOPE)
Model: [fixed-milestone / T&M+ceiling / hybrid / SLA]
Price / rates / ceiling: [ ]
Milestones: [deliverable ID → amount → payable on acceptance]
Change control: [written, priced against this baseline, named approver]
Credits / holdback: [ ]

5. RACI (buyer and vendor)
| Activity | Buyer | Vendor |
| Specify | A | C |
| Build | I | A/R |
| UAT / accept | A | R (fix) |
Rule: one A per row. Key personnel: [names]. Substitution: change-controlled.
Buyer dependencies (dated): [ ]

6. IP (BUSINESS CHOICE — counsel drafts)
Background: [stays with owner; licence to …]
Project-specific: [buyer owns / vendor owns + licence]
Must-run-if-they-leave: [pass / fail — what's missing]

7. EXIT
Triggers: [convenience / cause / term end]    Exit period: [ ]
Data return / export: [format, date]    Overlap / surviving licences: [ ]
Exit assistance fees: [ ]    Step-in if critical: [yes/no]

8. GOVERNANCE
Named managers (buyer / vendor): [ ]    Cadence: [ ]    Escalation: [ ]
Open legal (not drafted here): liability / indemnity / DPA / employment / local law

NOT THIS PAGE
Whether to buy → business-case    Monthly score → vendor-scorecard    Seller-as-bridge → tsa-schedule
```

## QA (must pass)

1. Outcome is a result + date, not headcount.
2. A deliverable has a pass/fail test and a named acceptor.
3. ASK (buyer D, verb, ceiling, date).
4. Price traces to baseline; pay is on acceptance, not invoice date.
5. RACI is not internal-only; one A per row.
6. IP is not "to be agreed"; exit is not "reasonable assistance".
7. No liability/indemnity prose pretending to be legal advice.
8. The page is not a vendor brochure. No invented ceilings.

If 1, 2, 3, or 8 fail: do not ship.

## Escalate / stop

- Outcome unnamed after one question → stop.
- T&M with no ceiling and no tests → refuse; offer discovery SOW with cap + exit to a fixed phase.
- Accept the vendor's paper with blank IP/exit → fail those rows; do not "light redline".
- Employment (IR35, TUPE), data protection, sanctions → counsel.
- This *is* the investment decision → [Business Case](../../strategy/business-case/SKILL.md) first.

## Related

- [Business Case](../../strategy/business-case/SKILL.md) — whether to buy
- [Vendor Scorecard](../../management/vendor-scorecard/SKILL.md) — monthly test of this SOW
- [Change Adoption](../../management/change-adoption/SKILL.md) — whether users use what you bought
- [Cash Runway](../../management/cash-runway/SKILL.md) — the SOW is a disbursement
- [Operating Review](../../management/operating-review/SKILL.md) — vendor performance as a line
- [Decision Rights](../../management/decision-rights/SKILL.md) — who has the D to award
- [TSA Schedule](../../ma/tsa-schedule/SKILL.md) — seller-as-bridge, not a chosen supplier
- [Executive Board Memo](../../management/executive-board-memo/SKILL.md) — material contract for the board
