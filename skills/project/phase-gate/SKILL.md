---
name: phase-gate
description: >-
  Use when a named delivery phase (design/build/UAT/etc.) needs exit criteria
  go/no-go, holes, and one ASK. Not go-live-readiness (live event), not
  portfolio-stage-gate (portfolio bet), not acceptance-signoff pack, not
  e2e-manual-test-list.
license: MIT
---

# Phase Gate

**Phase exit go / no-go — one page** — named phase; exit criteria as tests; met / not / unknown; holes; recommendation; one ASK. Default: client delivery phase (design → build → UAT → …); same spine for internal programs.

Method origin: Stage-Gate / phase-gate public (Cooper high-level: gates are resource decisions with deliverables + criteria + Go/Kill/Hold/Recycle) + exit-criteria practice (observable tests, not vibes). Operator cut for **one delivery phase** — not portfolio investment theatre, not the go-live event gate.

If they want a Cooper Stage-Gate lecture: one paragraph then produce or stop.

## When to use

- Design / build / UAT / migrate / hypercare-entry needs a clear exit
- Team says "we're ready for the next phase" with no written tests
- Holes in evidence must be visible before money/people move to the next phase
- Conditional go: named conditions + owners before the window

## When not to use

- Named **go-live** event go/no-go + rollback — [Go-Live Readiness](../../project/go-live-readiness/SKILL.md)
- Portfolio bet Go/Kill/Hold/Recycle + resource commit — [Portfolio Stage-Gate](../../management/portfolio-stage-gate/SKILL.md)
- Client UAT evidence / sign-off pack — [Acceptance Signoff](../../project/acceptance-signoff/SKILL.md) (feeds this)
- Building the manual E2E list — [E2E Manual Test List](../../delivery/e2e-manual-test-list/SKILL.md)
- Hour-by-hour cutover — [Cutover Plan](../../project/cutover-plan/SKILL.md)

Phase-gate ≠ go-live ≠ portfolio gate. This page exits a **named phase**. Go-live decides the live event. Portfolio stage-gate funds or kills a bet.

## Modes

| Mode | When | Output |
|---|---|---|
| **produce** | Default. Named phase + criteria | Go/no-go page + ASK |
| **redline** | They pasted a vibe checklist | Force tests + met/not/unknown; kill "ready" |
| **refuse** | No phase name, no D, or invent pass | Issues list. Stop |

## Hard rules

1. **Phase named** (design / build / UAT / …) with entry date and proposed exit date.
2. **Exit criteria are tests**, observable. Each: met / not / unknown + evidence pointer. Vibes ("comfortable", "mostly done") fail.
3. **One unknown on a load-bearing criterion = not a Go.** Label load-bearing vs nice-to-have.
4. **Recommendation:** Go / Conditional Go / No-Go / Recycle (rework in-phase). Conditional = named conditions + owner + date *before* next-phase start.
5. **Next-phase resources** named or HOLE (hollow Go = fail). Money/people/date of next review.
6. **One ASK** — D to call Go / Conditional / No-Go / Recycle by date.
7. **Never invent** pass/fail or defect counts. Holes stay holes.
8. **One page.**

## Intake

If **two** of 1, 2, 5 are missing after one round: issues list, not a fake gate.

1. Named phase + what "exit" unlocks next — load-bearing
2. Exit criteria written, or "none yet" — load-bearing
3. Evidence they have (docs, test results, sign-offs) or "unknown"
4. Open defects / holes already known
5. D for the gate (name) — load-bearing
6. Next-phase owner + rough capacity needed
7. Prior gate conditions still open or "none"

## Output shape

```
PHASE GATE  |  [phase name]  |  [project/client]
Exit target: [date]     Next phase: [name]     D: [name]
Next-phase owner: [ ]     Resources for next: [named / HOLE]

ASK: [D] to call GO / CONDITIONAL GO / NO-GO / RECYCLE by [date].

RECOMMENDATION
[Go / Conditional Go / No-Go / Recycle] because [one line].
Residual accepted by: [name or "none"].

EXIT CRITERIA
| # | Test (observable) | Load-bearing? | Met? | Evidence | Owner |
| 1 |  | Y/N | yes/no/unknown |  |  |

HOLES / OPENS
| Item | Blocks Go? | Owner | Date |
|  |  |  |  |

CONDITIONAL (only if Conditional Go)
| Condition | Owner | Must be true by | If missed |
|  |  |  | No-Go / slip exit |

NOT THIS PAGE
Live event → go-live-readiness    Portfolio bet → portfolio-stage-gate
UAT evidence pack → acceptance-signoff    E2E list build → e2e-manual-test-list

Holes: [ ]
```

Annex: `assets/exit-criteria.md`.

## QA (must pass)

1. Phase named; next phase named.
2. ASK (D, Go/Conditional/No-Go/Recycle, date).
3. Criteria are tests; met/not/unknown — no vibe-only rows.
4. Load-bearing unknowns block Go.
5. Next-phase resources named or HOLE called out.
6. Not go-live rollback page, not portfolio Kill paper, not E2E list.
7. No invented passes. One page.

If 1, 2, 4, or 7 fail: do not ship.

## Escalate / stop

- No D after one ask → stop.
- Hollow Go (approved, unfunded next phase) → No-Go or Hold resources; do not ship fake Go.
- They mean the production cutover night → [Go-Live Readiness](../../project/go-live-readiness/SKILL.md).
- They mean kill the whole internal bet → [Portfolio Stage-Gate](../../management/portfolio-stage-gate/SKILL.md).
- Safety / regulated phase exit → specialist + this page still names D and residual.

## Related

- [Go-Live Readiness](../../project/go-live-readiness/SKILL.md) — live-event gate + rollback
- [Portfolio Stage-Gate](../../management/portfolio-stage-gate/SKILL.md) — fund/kill portfolio bet
- [Acceptance Signoff](../../project/acceptance-signoff/SKILL.md) — UAT evidence feeding exit
- [E2E Manual Test List](../../delivery/e2e-manual-test-list/SKILL.md) — builds tests this gate may require
- [Cutover Plan](../../project/cutover-plan/SKILL.md) — hour-by-hour after a Go
- [Steering Pack](../../project/steering-pack/SKILL.md) — sitting that may hear this gate
