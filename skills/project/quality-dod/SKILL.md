---
name: quality-dod
description: >-
  Use when a named deliverable or phase needs Definition of Done / quality gate
  BEFORE client acceptance: exit criteria, evidence, residual defects, Go/No-Go
  to present for accept. Not acceptance-signoff itself, not phase-gate
  portfolio, not e2e-manual-test-list, not go-live-readiness, not cutover-plan.
license: MIT
---

# Quality DoD

**Definition of Done / quality gate before client acceptance** — named deliverable or phase: exit criteria checklist, evidence links/dates, residual defects (sev + count), Go / No-Go to *present* for accept. Default: venture / PS delivery; same spine for F500 phase exit.

Method origin: Scrum Guide Definition of Done (shared quality measures for the Increment) + predictive quality-gate / exit-criteria craft — gate before the acceptance ceremony.

If they want a DoD / quality-gate lecture: one paragraph then produce or stop.

## When to use

- "Are we actually done enough to show the client?"
- Phase / deliverable exit before UAT or acceptance pack
- Residual defects disputed: ship theatre vs real Done
- Redline a vague "Done" checklist with no evidence

## When not to use

- Client UAT / acceptance ceremony itself — [Acceptance Signoff](../../project/acceptance-signoff/SKILL.md)
- Named delivery phase go/no-go pack (broader than quality) — [Phase Gate](../../project/phase-gate/SKILL.md)
- Building the manual E2E test inventory — [E2E Manual Test List](../../delivery/e2e-manual-test-list/SKILL.md)
- Go-live event go/no-go — [Go-Live Readiness](../../project/go-live-readiness/SKILL.md)
- Hour-by-hour cutover — [Cutover Plan](../../project/cutover-plan/SKILL.md)
- Living RAID — [RAID Register](../../management/raid-register/SKILL.md)

## Modes

| Mode | When | Output |
|---|---|---|
| **produce** | Default. Named deliverable/phase | Quality DoD one-pager + ASK |
| **redline** | They pasted a "Done" list or exit deck | Force evidence + residual defects + Go/No-Go; kill theatre |
| **refuse** | No named deliverable, or they want acceptance signed here | Issues list. Stop |

## Hard rules

1. **Named deliverable or phase.** Not "the project is Done."
2. **Exit criteria are binary + evidence** (link, date, owner). Checkbox without evidence fails.
3. **DoD ≠ acceptance criteria.** DoD = quality bar for *any* item/phase; AC = item-specific. Both required to present.
4. **Residual defects table:** severity, count, waived? by whom. Unknown count = hole, not green.
5. **Go / No-Go to present for accept** — this page does not *be* acceptance-signoff.
6. **One ASK:** fix criteria / gather evidence / waive named defect / delay present. Owner, date.
7. **Do not invent pass rates, coverage %, or defect counts.** Hole them.
8. **Not acceptance ceremony, not go-live, not cutover, not the E2E list build.**
9. **One page.**

## Intake

If **two** of 1–3 are missing after one round: issues list, not a fake Done.

1. Named deliverable or phase + owner — load-bearing
2. Agreed exit criteria / DoD (or "none — draft") — load-bearing
3. Evidence we actually have (tests, reviews, artifacts) — load-bearing
4. Open defects by severity (or "unknown")
5. Who may waive — name
6. Target present-for-accept date
7. The ASK

## Output shape

```
QUALITY DoD  |  [DELIVERABLE / PHASE]  |  as-of: [date]
ASK: [owner] to [fix criteria / evidence / waive / delay present] by [date]
Present-for-accept target: [date]    Waivers by: [name]

EXIT CRITERIA
| Criterion | Met? (Y/N/Hole) | Evidence (link/date) | Owner |

RESIDUAL DEFECTS
| Sev | Open | Waived | Waived by | Blocks present? |

GO / NO-GO TO PRESENT
Decision: GO / NO-GO  because [ ]
If NO-GO: must-fix before present: [ ]

NOT THIS PAGE
Client accept → acceptance-signoff    Phase pack → phase-gate    E2E inventory → e2e-manual-test-list    Live event → go-live-readiness

Holes: [ ]
```

## QA (must pass)

1. Named deliverable/phase + owner.
2. Exit criteria with evidence or hole.
3. Residual defects table (or explicit unknown hole).
4. Explicit Go/No-Go to *present*, not acceptance signed.
5. One ASK, owner, date.
6. No invented coverage / counts.
7. Not acceptance / go-live / cutover / E2E-build.
8. One page.

If 1, 4, 5, or 6 fail: do not ship.

## Escalate / stop

- They want the client signature on this page → refuse; use [Acceptance Signoff](../../project/acceptance-signoff/SKILL.md).
- Go-live is the event → [Go-Live Readiness](../../project/go-live-readiness/SKILL.md).
- No criteria after one ask → refuse; draft criteria first, do not invent Done.
- Waiver of sev-1 without named authority → refuse green.

## Related

- [Acceptance Signoff](../../project/acceptance-signoff/SKILL.md) — client accept ceremony
- [Phase Gate](../../project/phase-gate/SKILL.md) — broader phase exit pack
- [E2E Manual Test List](../../delivery/e2e-manual-test-list/SKILL.md) — build the test inventory
- [Go-Live Readiness](../../project/go-live-readiness/SKILL.md) — live event gate
- [Cutover Plan](../../project/cutover-plan/SKILL.md) — hour-by-hour
- [Project Health](../../project/project-health/SKILL.md) — period colour including quality flag
