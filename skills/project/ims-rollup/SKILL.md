---
name: ims-rollup
description: >-
  Use when rolling up >=2 component schedules into one program IMS view: program
  milestones, slip deltas, critical cross-links, one ASK. NOT for single-project
  Gantt, not program-roadmap capability tranches, not critical-path this week
  alone, not interdependency-map, not milestone-burn, not tsa-schedule.
license: MIT
---

# IMS Rollup

**Program IMS rollup across ≥2 component plans** — program milestones, slip deltas vs baseline, critical cross-links (giver→receiver), one ASK. Default: multi-workstream / multi-vendor program; same spine for aerospace-style IMS or venture delivery with ≥2 real schedules.

Method origin: DoD/aerospace IMS–IMP public practice (vertical + horizontal integration; summary master = rollup of component schedules) + GAO schedule integration concepts — not a house Gantt novel.

If they want an IMS / critical-path lecture: one paragraph then produce or stop.

## When to use

- ≥2 named component plans must answer: is the *program* still on the milestone?
- Slip in one workstream / vendor plan threatens a cross-linked milestone
- Before a SteerCo so the room sees program milestones + cross-links, not five Gantts
- Baseline vs forecast deltas on program events need one page

## When not to use

- Capability waves / board tranche decisions — [Program Roadmap](../../project/program-roadmap/SKILL.md)
- This week's single-project critical path + float — [Critical Path](../../project/critical-path/SKILL.md)
- Cross-project dependency owners map (not schedule dates) — [Interdependency Map](../../project/interdependency-map/SKILL.md)
- Milestone traffic light + burn only — [Milestone Burn](../../project/milestone-burn/SKILL.md)
- Seller-as-bridge TSA catalog — [TSA Schedule](../../ma/tsa-schedule/SKILL.md)
- Single-project health colour — [Project Health](../../project/project-health/SKILL.md)

## Modes

| Mode | When | Output |
|---|---|---|
| **produce** | Default. ≥2 component plans named | Program IMS one-pager + ASK |
| **redline** | They pasted a mega-Gantt or "master plan" deck | Force vertical rollup + cross-links + slip deltas; kill fake float |
| **refuse** | Only one plan, or no program milestones, or they want MS Project rebuilt | Issues list. Stop |

## Hard rules

1. **≥2 component plans.** One Gantt is not an IMS rollup.
2. **Program milestones first** (events / accomplishments), then component tasks that feed them — vertical rollup, not a task dump.
3. **Horizontal integrity:** every critical cross-link is giver → receiver → date → owner. Orphan predecessors fail.
4. **Slip delta = forecast − baseline** (days). No invented baseline; hole it.
5. **Overall program colour = worst material program milestone**, not an average of workstreams.
6. **One ASK** this period: re-baseline / protect path / force giver date / escalate interface. Owner, date.
7. **Do not invent durations, % complete, or float.** Hole: `[not measured — proxy by DATE]`.
8. **Not a program-roadmap tranche page, not this week's single critical path, not TSA.**
9. **One page.**

## Intake

If **two** of 1–3 are missing after one round: issues list, not a fake master schedule.

1. Named program + ≥2 component plans (owner each) — load-bearing
2. Program milestones with baseline + forecast dates — load-bearing
3. Critical cross-links (giver→receiver) that can move a program milestone — load-bearing
4. As-of date of each component schedule (or "stale")
5. Known constraints / freezes / external gates
6. The ASK this period

## Output shape

```
IMS ROLLUP  |  [PROGRAM]  |  as-of: [date]  |  components: [n]
ASK: [owner] to [re-baseline / protect path / force giver / escalate] by [date]

PROGRAM MILESTONES
| Event | Baseline | Forecast | Slip (d) | Driver component | RYG | Because |
| [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |

CRITICAL CROSS-LINKS
| Giver (plan/task) | Receiver | Need-by | Forecast | Owner | If slips |

WORST PATH
Program colour: G/Y/R because [worst material milestone]
Linchpin: if [giver] slips [n]d, [event] breaks

NOT THIS PAGE
Tranches → program-roadmap    This week CP → critical-path    Dep owners → interdependency-map    TSA → tsa-schedule

Holes: [ ]
```

## QA (must pass)

1. ≥2 component plans named with owners.
2. Program milestones show baseline, forecast, slip (or hole).
3. Critical cross-links have giver→receiver→need-by→owner.
4. Overall = worst material program milestone.
5. One ASK, owner, date.
6. No invented durations / % / float.
7. Not a roadmap tranche page, not single-project CP, not TSA.
8. One page.

If 1, 2, 5, or 6 fail: do not ship.

## Escalate / stop

- Only one schedule after one ask → refuse; point at [Critical Path](../../project/critical-path/SKILL.md).
- Baseline must move and SteerCo owns it → [Steering Pack](../../project/steering-pack/SKILL.md) or [Change Control](../../project/change-control/SKILL.md).
- They want the MS Project file rebuilt here → refuse.
- Stale >30 days on a load-bearing component → hole; do not paint green.

## Related

- [Program Roadmap](../../project/program-roadmap/SKILL.md) — capability waves / board tranches
- [Critical Path](../../project/critical-path/SKILL.md) — this week's path on one plan
- [Interdependency Map](../../project/interdependency-map/SKILL.md) — dependency owners, not dates
- [Milestone Burn](../../project/milestone-burn/SKILL.md) — milestone RYG + burn rate
- [TSA Schedule](../../ma/tsa-schedule/SKILL.md) — seller bridge services
- [Steering Pack](../../project/steering-pack/SKILL.md) — sitting with decisions
- [Change Control](../../project/change-control/SKILL.md) — baseline move
