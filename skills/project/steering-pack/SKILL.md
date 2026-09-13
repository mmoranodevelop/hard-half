---
name: steering-pack
description: >-
  Use for a steering-committee sitting: up to 3 decisions needed, exceptions,
  capacity. NOT for the weekly sponsor one-pager, not the internal operating
  review.
license: MIT
---

# Steering Pack

**Steering-committee sitting pack** — up to 3 decisions, exceptions vs baseline, capacity. The room decides. It does not receive a tour. Default: venture SteerCo; same spine for F500.

Method origin: PRINCE2 project board + management by exception (public) + operator SteerCo (decisions first). Not a highlight report.

If they want a project-board lecture: one paragraph then produce or stop.

## When to use

- Named steering / project board is sitting (monthly default, or an exception sitting)
- Need up to 3 decisions the PM cannot take alone
- A 20-slide "SteerCo update" must become decisions + exceptions + capacity

## When not to use

- Weekly client-facing status — [Sponsor Status](../../project/sponsor-status/SKILL.md)
- Internal weekly exceptions of *our* shop — [Operating Review](../../management/operating-review/SKILL.md)
- One named CR to a single D, no sitting — [Change Control](../../project/change-control/SKILL.md)
- Go/Kill an internal portfolio bet — [Portfolio Stage-Gate](../../management/portfolio-stage-gate/SKILL.md)
- Go / no-go for a named go-live — [Go-Live Readiness](../../project/go-live-readiness/SKILL.md)
- Board / ELT fiduciary paper — [Executive Board Memo](../../management/executive-board-memo/SKILL.md)
- First authorisation — [Project Charter](../../project/project-charter/SKILL.md)
- Who has the D unnamed — [Decision Rights](../../management/decision-rights/SKILL.md)

## Modes

| Mode | When | Output |
|---|---|---|
| **produce** | Default. Sitting dated | One-pager + decision cards + ASK |
| **redline** | They pasted a SteerCo deck | Decisions first; kill the tour; list slides cut |
| **refuse** | Two load-bearing facts missing, or a status readout labelled SteerCo | Issues list. Stop |

If the sitting has zero decisions: do not fake three. Route to [Sponsor Status](../../project/sponsor-status/SKILL.md) or cancel the sitting.

## Hard rules

1. **Decisions first.** Each: options (yes / no / cut), recommendation, cost of delay, named D in the room. Max 3. A fourth is a second sitting or a parked line.
2. **Exceptions only** — forecast off tolerance, or already off. Green is one sentence. Do not paste RAID.
3. **Capacity:** who is actually free if they say yes. A decision with no named capacity is a hollow Go.
4. **Last sitting's decisions** on the page. Open items have owners and dates, or they re-open as a new decision.
5. **The sitting is 45–60 min.** Chair is a person. Pre-read ≥48h. "The committee decides" needs a written rule (majority / chair-break).
6. **Do not invent envelopes or dates.** Holes stay holes.

## Intake

If **two** of 1, 2, 4 are missing after one round: issues list, not a fake pack.

1. Sitting — date, chair, members (names) — load-bearing
2. Up to 3 decisions — each one sentence with a verb — load-bearing
3. Baseline — charter version, end, envelope, tolerances
4. Exceptions vs baseline this period — load-bearing
5. Capacity — named people / money still free vs promised
6. Last sitting's decisions — closed or not
7. Venture or F500 (venture default)

## Output shape

```
STEERING  |  [project]  |  [client]  |  [YYYY-MM-DD]
Chair: [name]     Members: [names]     Time: [45–60 min]
Baseline: charter v[n] · end [date] · envelope [ ] · tolerance [ ]
CLASS: FOR DECISION

ASK: chair to close decisions 1–[n] this sitting. Unclosed → named follow-up by [date], not "next time."

DECISIONS (max 3)
| # | Decision (verb + object) | Options | Recommend | Cost of delay | D in the room |
| 1 | | yes / no / cut | | | |

EXCEPTIONS VS BASELINE
[On track / At risk / Off] because [cause].
1. [exception] — owner [ ] — needed from this room: [decision # or "note"]

CAPACITY (if they say yes)
| Name / seat | Promised | Free this period | Blocker |
| | | | |

LAST SITTING
| Decision | Owner | Due | Closed? |
| | | | |

CUT FROM THIS PACK
- [tour / RAID dump / weekly status]

NOT THIS PAGE
Weekly client → sponsor-status    Our shop → operating-review    One CR no sitting → change-control

Holes: [ ]
```

## QA (must pass)

1. Sitting date + named chair.
2. At most 3 decisions; zero decisions must route, not fake.
3. Each decision has verb, options, D.
4. ASK: close 1–n this sitting.
5. Capacity filled on a "yes" that needs people or money.
6. Not a sponsor-status one-pager in costume.
7. Not an internal operating review.
8. No invented numbers.
9. One page.

If 1, 3, 4, or 8 fail: do not ship.

## Escalate / stop

- Status readout with no decision → [Sponsor Status](../../project/sponsor-status/SKILL.md).
- They want every workstream → refuse the tour.
- Hollow Go (approve, unfunded, unnamed capacity) → fail capacity; do not ship.
- Board resolution needed → [Executive Board Memo](../../management/executive-board-memo/SKILL.md).
- Go-live gate pretending to be SteerCo → [Go-Live Readiness](../../project/go-live-readiness/SKILL.md).

## Related

- [Sponsor Status](../../project/sponsor-status/SKILL.md) — weekly, client-facing, not this sitting
- [Operating Review](../../management/operating-review/SKILL.md) — *our* shop
- [Change Control](../../project/change-control/SKILL.md) — one CR this sitting may take
- [Project Charter](../../project/project-charter/SKILL.md) — baseline
- [Portfolio Stage-Gate](../../management/portfolio-stage-gate/SKILL.md) — Go/Kill a bet, not a project SteerCo
- [Decision Rights](../../management/decision-rights/SKILL.md) — RAPID if the D is unnamed
