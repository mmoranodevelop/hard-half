---
name: project-close
description: >-
  Use to close a named project: outcomes vs charter, leftovers, handover,
  lessons pointer to AAR. NOT for the AAR itself, not benefits tracking as a
  novel.
license: MIT
---

# Project Close

**Project Close One-Pager** — outcomes vs the signed charter, leftovers with owners, handover to BAU, AAR pointer, ASK the sponsor to authorise close and release people. Default: venture client project; same spine for F500.

Method origin: PRINCE2 closing a project public (end project report, handover, follow-on actions, board authorises close). Not a lessons binder.

If they want a PRINCE2-close lecture: one paragraph then produce or stop.

## When to use

- A named project should end (planned or early)
- Need outcomes vs charter, leftovers, handover, a close signature
- A 40-page closure report must become one page + AAR pointer

## When not to use

- The learning conversation — [After Action Review](../../management/after-action-review/SKILL.md) (this page *points* at it)
- First 100 days of ops after close — [Integration 100](../../management/integration-100/SKILL.md)
- Client UAT / accept the product — [Acceptance Signoff](../../project/acceptance-signoff/SKILL.md) first
- Status of a live project — [Sponsor Status](../../project/sponsor-status/SKILL.md)
- Program still running — [Operating Review](../../management/operating-review/SKILL.md)
- The baseline this page scores — [Project Charter](../../project/project-charter/SKILL.md)

Close ≠ AAR ≠ acceptance.

## Modes

| Mode | When | Output |
|---|---|---|
| **produce** | Default. Named project ending | Close page + ASK |
| **redline** | They pasted a closure binder | Outcomes vs charter; leftovers; handover; AAR pointer |
| **refuse** | Two load-bearing facts missing, or they want the AAR on this page | Issues list. Stop |

## Hard rules

1. **Compare to the charter.** No rewrite of history. Early close: say why against the same rows.
2. **Leftovers have names and dates.** A leftover with no owner is still the project's.
3. **Receiving owner + date.** Hypercare has an exit test or routes to integration-100. Thrown over the fence fails.
4. **Lessons = AAR pointer**, not a binder. If no AAR booked, the ASK includes booking it.
5. **ASK is authorise close, release people.** Benefits after close stay with line owners — one line each, not a novel.
6. **Acceptance first** unless this is early close.
7. **Do not invent spend or fake "met".** Holes stay holes.

## Intake

If **two** of 1, 2, 4 are missing after one round: issues list, not a fake close.

1. Project + charter (version, dates, envelope, success tests) — load-bearing
2. What actually happened — outcomes, spend, dates (or unknown) — load-bearing
3. Acceptance signed? If no, route unless early close
4. Sponsor (D) who can authorise close — load-bearing
5. Leftovers — defects, unpaid, un-handed work
6. BAU / receiving owner
7. AAR done / booked / not

## Output shape

```
PROJECT CLOSE  |  [project]  |  client: [name]  |  close date asked: [date]
Charter: v[n] signed [date]     Close type: planned / early
Sponsor / D: [name]     PM: [name]     CLASS: FOR CLOSE
ASK: [D] to authorise close of [project] on [date], release [names], accept leftovers table.

OUTCOMES VS CHARTER
| Test / constraint | Charter | Actual | Met? |
| Outcome | [ ] | [ ] | yes / no / unknown |
| End date | [ ] | [ ] | [ ]
| Envelope | [ ] | [ ] or HOLE | [ ]
| Success test 1 | [ ] | [ ] | [ ]
| Kill test (if early) | [ ] | [ ] | [ ]

LEFTOVERS
| Item | Owner (BAU / named) | Date | If missed |
| [ ] | [ ] | [ ] | [ ]

HANDOVER
Receiving owner: [name]     Date: [ ]
Hands over: [product / access / docs / residual defects]
Hypercare exit: [test + date] or none — integration-100

LESSONS
AAR: [done date / booked date / not booked]. Facilitator: [ ]. This page does not contain the AAR.

MONEY / PEOPLE
Spend vs envelope: [ / unknown]     Vendor bills open: [ ]
People released from [date]: [names]

SIGN: D ________  PM ________  Receiving owner ________
NOT THIS PAGE
Learning → after-action-review    Product accept → acceptance-signoff    Live status → sponsor-status
Holes: [ ]
```

## QA (must pass)

1. ASK (D, authorise close, date).
2. Charter rows to compare (or explicit "no charter — hole").
3. Every leftover has a named owner.
4. Receiving owner + handover date.
5. Lessons are an AAR pointer, not a novel.
6. Not an AAR, UAT sign-off, or 100-day plan.
7. No invented spend or fake "met". One page.

If 1, 3, 4, or 7 fail: do not ship.

## Escalate / stop

- Product not accepted and this is not early close → [Acceptance Signoff](../../project/acceptance-signoff/SKILL.md).
- They want the AAR as this page → [After Action Review](../../management/after-action-review/SKILL.md).
- Benefits-realisation binder → name leftover measures + line owners; stop the novel.
- Keep the team "just in case" with no leftovers table → refuse hollow close.

## Related

- [Project Charter](../../project/project-charter/SKILL.md) — the baseline this page scores
- [Acceptance Signoff](../../project/acceptance-signoff/SKILL.md) — product signed before close
- [After Action Review](../../management/after-action-review/SKILL.md) — the learning conversation
- [Integration 100](../../management/integration-100/SKILL.md) — 100 days of ops after
- [Sponsor Status](../../project/sponsor-status/SKILL.md) — live periods; not close
- [RAID Register](../../management/raid-register/SKILL.md) — leftovers may come from open issues
