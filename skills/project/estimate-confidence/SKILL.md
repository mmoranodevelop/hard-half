---
name: estimate-confidence
description: >-
  Use when a delivery date and/or cost needs a confidence band (P50/P80 or
  best/likely/worst), named drivers, and one ASK. NOT for business-case NPV, not
  budget-variance, not cash-runway, not go-live-readiness, not scenario-planning
  worlds.
license: MIT
---

# Estimate Confidence

**Confidence band one-pager** — date and/or cost: P50/P80 (or best / likely / worst), drivers of the range, where we sit on the Cone, one ASK. Default: client delivery estimate before commit; same spine for internal programs.

Method origin: three-point estimating / PERT public (O–M–P → expected + spread) + Cone of Uncertainty public (range narrows only as uncertainty is removed) + PMI Practice Standard for Project Estimating (estimating as a living process, not a single-point promise). Operator band, not a Monte Carlo lecture.

If they want a PERT / Cone lecture: one paragraph then produce or stop.

## When to use

- Sponsor wants a date or cost **with a band**, not a fake precision point
- Bid / SOW / charter commit is about to lock and the range is still a vibe
- "We're 80% sure" with no drivers or P50/P80 stated
- Re-baseline after scope clarity; Cone should have narrowed — prove it

## When not to use

- Fund / kill NPV options — [Business Case](../../strategy/business-case/SKILL.md)
- This period vs plan drivers — [Budget Variance](../../management/budget-variance/SKILL.md)
- Bank 13-week liquidity — [Cash Runway](../../management/cash-runway/SKILL.md)
- Named go-live go/no-go — [Go-Live Readiness](../../project/go-live-readiness/SKILL.md)
- 3–4 external worlds for a bet — [Scenario Planning](../../strategy/scenario-planning/SKILL.md)
- In-flight EAC vs BAC — [EAC Pulse](../../project/eac-pulse/SKILL.md)

## Modes

| Mode | When | Output |
|---|---|---|
| **produce** | Default. Scope enough to estimate | Band page + drivers + ASK |
| **redline** | They pasted a single-point date/$ | Force band + drivers; kill fake precision |
| **refuse** | No WBS/scope basis, or invent P80 | Issues list. Stop |

## Hard rules

1. **Band, not a point.** State P50 and P80 (or best / likely / worst). A single date/$ without a band fails.
2. **Method visible.** Three-point (O/M/P) or named analogous/parametric basis — or HOLE. Do not invent PERT math from thin air.
3. **Drivers ≤5.** What moves the range (scope, dependency, skill, vendor, unknown). Each: owner or "unowned".
4. **Cone position.** Phase / % definition complete → expected range width. Early Cone ≠ commit-ready. Say if commit is premature.
5. **Date and cost may both appear**, but label which the ASK locks. Do not blend silently.
6. **One ASK** — named D to accept band / fund contingency / delay commit / cut scope by date.
7. **Never invent** hours, $, probabilities, or historical accuracy %. Holes stay holes.
8. **One page.**

## Intake

If **two** of 1–4 are missing after one round: issues list, not a fake band.

1. What is being estimated (deliverable / phase / whole) — load-bearing
2. Date band, cost band, or both — load-bearing
3. Basis: three-point inputs, analogous ref, or "none" — load-bearing
4. Decision this band feeds (bid, charter, re-baseline) — load-bearing
5. Known drivers / unknowns already on RAID
6. Who has D on the commit
7. Contingency already held or "none"

## Output shape

```
ESTIMATE CONFIDENCE  |  [what]  |  [client/program]  |  as-of: [date]
D: [name]     Basis: three-point / analogous / parametric / HOLE
Cone position: [phase or % definition] — commit-ready? yes / no / unknown

ASK: [D] to [accept P80 commit / hold contingency $X / delay lock / cut scope Y] by [date]

BAND
| Metric | Best (or P10) | Likely (P50) | Worst (or P80/P90) | Unit |
| Date |  |  |  |  |
| Cost |  |  |  |  |

METHOD (one line)
O/M/P or ref used: [ ]. Formula/weight: [PERT (O+4M+P)/6 or triangular or named]. Contingency in band? yes/no/HOLE

DRIVERS (≤5)
| # | Driver | Moves date / cost / both | Direction | Owner |
| 1 |  |  |  |  |

CONE / COMMIT
Why this width is honest: [ ]. What would narrow it next: [work + owner + date].
Premature commit risk: [one line or "none stated"].

NOT THIS PAGE
NPV fund/kill → business-case    Period variance → budget-variance
Cash → cash-runway    Go-live gate → go-live-readiness    Worlds → scenario-planning
In-flight EAC → eac-pulse

Holes: [ ]
```

Annex: `assets/three-point-sheet.md`.

## QA (must pass)

1. Band stated (P50/P80 or best/likely/worst) — not a lone point.
2. Basis named or HOLE — no invented probability.
3. ≤5 drivers with owners or unowned.
4. One ASK with owner, verb, date.
5. Cone/commit readiness addressed in one line.
6. Not business-case, variance, cash, go-live, or scenarios.
7. No invented numbers. One page.

If 1, 2, 4, or 7 fail: do not ship.

## Escalate / stop

- They demand a single date with no band → refuse; produce band or stop.
- Commit demanded in wide Cone with no contingency owner → escalate; page still shows premature.
- Monte Carlo / full quantitative risk → one paragraph; this page stays the operator band.
- In-flight remaining cost only → [EAC Pulse](../../project/eac-pulse/SKILL.md).

## Related

- [Business Case](../../strategy/business-case/SKILL.md) — fund/kill NPV; this is estimate honesty before/beside it
- [Budget Variance](../../management/budget-variance/SKILL.md) — past period drivers
- [Cash Runway](../../management/cash-runway/SKILL.md) — bank liquidity
- [Go-Live Readiness](../../project/go-live-readiness/SKILL.md) — live-event gate
- [Scenario Planning](../../strategy/scenario-planning/SKILL.md) — external worlds, not PERT band
- [EAC Pulse](../../project/eac-pulse/SKILL.md) — EAC/ETC after work is underway
- [Project Charter](../../project/project-charter/SKILL.md) — plan of record that absorbs the commit
