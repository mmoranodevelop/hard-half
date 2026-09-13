---
name: go-live-readiness
description: >-
  Use for the go / no-go on a named go-live: exit criteria, defects, owners,
  rollback. NOT for change-adoption (behaviours after), not the hour-by-hour
  cutover.
license: MIT
---

# Go-Live Readiness

**One-page go / no-go** for a named go-live. Exit criteria, open defects, named owners, rollback trigger. The gate, not the hour-by-hour. Default: venture service go-live; same spine for F500.

Method origin: ITIL 4 service-transition / CAB go-no-go public (evidence, named risk owner, rollback understood). Operator cut.

If they want a CAB / ITIL lecture: one paragraph then produce or stop.

## When to use

- A named go-live date needs go / no-go / conditional
- Exit criteria exist (or must be written) and defects need a disposition
- Rollback is a slogan and must become a trigger + owner

## When not to use

- Hour-by-hour sequence, freeze, step owners — [Cutover Plan](../../project/cutover-plan/SKILL.md)
- People doing the new behaviour after — [Change Adoption](../../management/change-adoption/SKILL.md)
- First 100 days after close / go-live — [Integration 100](../../management/integration-100/SKILL.md)
- Client UAT evidence pack — [Acceptance Signoff](../../project/acceptance-signoff/SKILL.md) (feeds this)
- Steering sitting with other decisions — [Steering Pack](../../project/steering-pack/SKILL.md)
- Imagined failure before the date — [Pre-mortem](../../management/pre-mortem/SKILL.md)

Go-live-readiness ≠ cutover ≠ adoption. This page decides. Cutover runs the hours. Adoption changes behaviour after.

## Modes

| Mode | When | Output |
|---|---|---|
| **produce** | Default. Named go-live | One-page go / no-go + ASK |
| **redline** | They pasted a 40-line "readiness checklist" | Force criteria, defects, owners, rollback; list what you killed |
| **refuse** | No go-live date, no D, or a CAB lecture | Issues list. Stop |

## Hard rules

1. Write **exit criteria as tests**, not vibes. Each: met / not / unknown. One unknown on a load-bearing criterion = not a Go.
2. Defects: P1 must be zero or explicitly accepted by the D with a workaround. P2: count, owner, date. "We'll fix in hypercare" without a name fails.
3. **Rollback:** trigger (observable), owner, time to reverse, point of no return. Untested rollback = No-Go unless the D accepts that residual in writing.
4. Owners: D (gate), service/BAU owner Day 1, cutover lead (pointer to the runbook). Committees are not owners.
5. Recommendation: **Go / Conditional Go / No-Go**. Conditional = named conditions + owner + date *before* the window. Recommendation is not the decision.
6. ASK the D to call it. Do not write the hour-by-hour here. Do not write ADKAR here.
7. **Do not invent defect counts.** Holes stay holes.

## Intake

If **two** of 1, 2, 5 are missing after one round: issues list, not a fake gate.

1. Named go-live — what goes live, date/window, client — load-bearing
2. Exit criteria already written, or "none" — load-bearing
3. Defects they have — P1/P2 counts, or "unknown"
4. Who accepts operational risk (name)
5. D for go / no-go (name) — load-bearing
6. Rollback — exists / tested / slogan
7. BAU owner Day 1

## Output shape

```
GO / NO-GO  |  [what goes live]  |  [client]
Window: [start–end, timezone]     D: [name]     BAU owner Day 1: [name]
Cutover lead: [name]     Runbook: [pointer / "none — cutover-plan"]

ASK: [D] to call GO / CONDITIONAL GO / NO-GO by [date/time].

RECOMMENDATION
[Go / Conditional Go / No-Go] because [one line]. Residual accepted by: [name or "none"].

EXIT CRITERIA
| # | Test (observable) | Met? | Evidence | Owner |
| 1 | [ ] | yes / no / unknown | [ ] | [ ]

DEFECTS
P1 open: [n]     P2 open: [n]
| ID | Severity | Workaround | Owner | Date | Accepted by D? |
| [ ] | [ ] | [ ] | [ ] | [ ] | [ ]

ROLLBACK
Trigger: [observable]. Owner: [name]. Time to reverse: [ ]. Point of no return: [time]. Tested: yes / no / unknown.

CONDITIONAL (only if Conditional Go)
| Condition | Owner | Must be true by | If missed |
| [ ] | [ ] | [ ] | No-Go / slip window |

NOT THIS PAGE
Hour-by-hour → cutover-plan    Behaviours → change-adoption    UAT evidence → acceptance-signoff
Holes: [ ]
```

Also `assets/go-nogo.md`.

## QA (must pass)

1. Named go-live / window.
2. ASK (D, GO/CONDITIONAL/NO-GO, date).
3. Exit criteria are tests, not vibes ("ready", "comfortable").
4. P1 open has D acceptance, or P1 is zero.
5. Rollback has a trigger and an owner.
6. BAU owner Day 1 named.
7. Not a cutover runbook or an ADKAR essay.
8. No invented defect counts. One page.

If 1, 2, 5, or 8 fail: do not ship.

## Escalate / stop

- No D after one ask → stop.
- They want to Go with untested rollback and no residual owner → No-Go; do not ship a fake Go.
- They want the hour-by-hour on this page → [Cutover Plan](../../project/cutover-plan/SKILL.md).
- They want behaviours / training as the gate → [Change Adoption](../../management/change-adoption/SKILL.md).
- Safety / clinical / regulated go-live → specialist + this page still names the D and residual.

## Related

- [Cutover Plan](../../project/cutover-plan/SKILL.md) — the hours after this gate
- [Change Adoption](../../management/change-adoption/SKILL.md) — behaviours after
- [Integration 100](../../management/integration-100/SKILL.md) — 100 days after
- [Acceptance Signoff](../../project/acceptance-signoff/SKILL.md) — UAT evidence that feeds criteria
- [Steering Pack](../../project/steering-pack/SKILL.md) — sitting that may take this call
- [Pre-mortem](../../management/pre-mortem/SKILL.md) — imagined failure *before* the date
