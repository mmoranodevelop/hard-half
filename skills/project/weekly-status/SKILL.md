---
name: weekly-status
description: >-
  Use when writing the INTERNAL delivery-team weekly narrative: what happened /
  what matters / risks that moved / next week / one ASK. NOT for project-health
  (RYG), not sponsor-status (client), not operating-review (shop metrics), not
  steering-pack, not weekly-cadence (MD personal week).
license: MIT
---

# Weekly Status

**Internal weekly narrative — one page** — what happened, what matters, risks that moved, next week, one ASK. Default: delivery-team week for a named project / workstream; same spine for multi-stream program roll-up when one owner owns the week.

Method origin: PRINCE2 Highlight Report (PM → board, manage-by-exception twin) — short period narrative on progress vs tolerance, products done / next, risks & issues that moved — adapted as **internal delivery-team** status, not the client letter.

If they want a PRINCE2 / RAG lecture: one paragraph then produce or stop.

## When to use

- Friday / Monday delivery sync needs a written week, not a colour war
- PM owes the delivery lead / PMO a narrative of *this* week
- Risks or issues moved and the team must see them in prose, not only RAID
- Before SteerCo prep — the internal week that feeds the pack

## When not to use

- RYG health of one project this period — [Project Health](../../project/project-health/SKILL.md)
- Client-facing sponsor letter — [Sponsor Status](../../project/sponsor-status/SKILL.md)
- Internal exceptions of *our* shop (utilization, bench, pipeline) — [Operating Review](../../management/operating-review/SKILL.md)
- Steering sitting with up to 3 decisions — [Steering Pack](../../project/steering-pack/SKILL.md)
- MD's personal week (calendar / energy / priorities) — [Weekly Cadence](../../productivity/weekly-cadence/SKILL.md)
- Living RAID list — [RAID Register](../../management/raid-register/SKILL.md)

## Modes

| Mode | When | Output |
|---|---|---|
| **produce** | Default. Named project / workstream, this week | Narrative page + ASK |
| **redline** | They pasted a RAG deck or "95% done" wall | Force evidence + moved risks + ASK; kill % theatre |
| **refuse** | No project name, or they want the client letter / MD calendar | Issues list. Stop |

## Hard rules

1. **Internal delivery audience.** Not the client. Not the MD personal week.
2. **Named project / workstream + period (this week).** One owner of the narrative.
3. **Five blocks only:** Happened / Matters / Risks that moved / Next week / ASK.
4. **Exception-based.** Quiet green stays quiet; name what changed or threatens tolerance.
5. **Products / outcomes, not task %.** No "95% complete" without a done-looks-like.
6. **Risks that moved** — new, escalated, closed, or unchanged-but-due. Link RAID ids if known; do not dump the register.
7. **One ASK** — decide / unblock / resource / escalate / freeze. Owner, date.
8. **Never invent** burn, % complete, dates, or risk scores. Holes stay holes.
9. **One page.**

## Intake

If **two** of 1–3 are missing after one round: issues list, not a fake week.

1. Named project / workstream + our PM/owner — load-bearing
2. Period (week ending date) — load-bearing
3. What actually shipped / slipped this week (evidence) — load-bearing
4. Risks / issues that moved (or "none moved")
5. Next week's must-hit outcomes
6. The ASK this week
7. Audience (delivery lead / PMO / SteerCo prep)

## Output shape

```
WEEKLY STATUS  |  [PROJECT / WORKSTREAM]  |  week ending: [date]
Owner: [PM]    Audience: internal delivery / PMO
ASK: [owner] to [decide / unblock / resource / escalate / freeze] by [date]

HAPPENED (≤5 bullets — outcomes, not task %)
- [ ]

WHAT MATTERS THIS WEEK
- [1–3 lines: the exception / decision / dependency that sets the tone]

RISKS / ISSUES THAT MOVED
| ID / name | Was → Now | Why it moved | Owner | Need-by |
|  |  |  |  |  |

NEXT WEEK (must-hit)
| Outcome | Owner | Done looks like | Need-by |
|  |  |  |  |

NOT THIS PAGE
RYG score → project-health    Client letter → sponsor-status
Shop metrics → operating-review    SteerCo decisions → steering-pack
MD personal week → weekly-cadence    Full RAID → raid-register

Holes: [ ]
```

## QA (must pass)

1. Named project / workstream, week ending, internal audience.
2. Happened + matters + next week present (or holes labelled).
3. Risks that moved table — or explicit "none moved".
4. One ASK with owner, verb, date.
5. No invented % / burn / dates.
6. Not project-health, sponsor-status, operating-review, steering-pack, or weekly-cadence.
7. One page.

If 1, 4, or 5 fail: do not ship.

## Escalate / stop

- Colour is red *and* a baseline must move → [Change Control](../../project/change-control/SKILL.md) or [Steering Pack](../../project/steering-pack/SKILL.md).
- Client-facing note is the job → [Sponsor Status](../../project/sponsor-status/SKILL.md).
- They want RYG scoring as the page → [Project Health](../../project/project-health/SKILL.md).
- No project name after one ask → refuse.
- They want the MD calendar week → [Weekly Cadence](../../productivity/weekly-cadence/SKILL.md).

## Related

- [Project Health](../../project/project-health/SKILL.md) — RYG flags this period
- [Sponsor Status](../../project/sponsor-status/SKILL.md) — client-facing letter
- [Operating Review](../../management/operating-review/SKILL.md) — shop exceptions
- [Steering Pack](../../project/steering-pack/SKILL.md) — sitting with decisions
- [Weekly Cadence](../../productivity/weekly-cadence/SKILL.md) — MD personal week
- [RAID Register](../../management/raid-register/SKILL.md) — living R/A/I/D list
- [PMO Cadence](../../project/pmo-cadence/SKILL.md) — who meets when across the program
