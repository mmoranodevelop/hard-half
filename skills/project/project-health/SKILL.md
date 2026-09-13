---
name: project-health
description: >-
  Use when scoring RYG health of ONE named project this period: delivery, risk,
  stakeholder, commercial (or capacity) flags + because + one ASK. Not
  operating-review, not sponsor-status, not raid-register, not steering-pack,
  not account-health.
license: MIT
---

# Project Health

**Project Health — This Period, One Named Project** — one page: delivery, risk, stakeholder, commercial (or capacity) — each RYG with a because — overall = worst material flag, one ASK. Default: venture / professional-services delivery; same spine for F500 program workstreams.

Method origin: Traffic-light (RAG) project status reporting + account-health spine applied to one project — dimensions roll to RYG; colour without a because is theatre. Do not invent a house health index.

If they want a RAG / status-reporting lecture: one paragraph then produce or stop.

## When to use

- Named project this period: is it green, and what do we do
- Status colour is stale, unexplained, or hiding a red under an average
- Before a steering sitting, so the room is not a colour argument
- A yellow just flipped, or a key dependency / champion went quiet

## When not to use

- Internal weekly exceptions of *our* shop — [Operating Review](../../management/operating-review/SKILL.md)
- Client-facing one-pager to the sponsor — [Sponsor Status](../../project/sponsor-status/SKILL.md)
- Living RAID list — [RAID Register](../../management/raid-register/SKILL.md)
- Steering sitting (up to 3 decisions) — [Steering Pack](../../project/steering-pack/SKILL.md)
- ONE named account (CS / AM book), not a project — [Account Health](../../accounts/account-health/SKILL.md)
- This week's critical path only — [Critical Path](../../project/critical-path/SKILL.md)
- ONE named dependency to unblock — [Dependency Unblock](../../project/dependency-unblock/SKILL.md)

## Modes

| Mode | When | Output |
|---|---|---|
| **produce** | Default. Named project | This-period health page + ASK |
| **redline** | They pasted a dashboard or RAG deck | Force because + ASK; kill the mystery index |
| **refuse** | Two load-bearing facts missing, or "explain our CHI" | Issues list. Stop |

## Hard rules

1. **One named project. This period.** Not a portfolio tour.
2. **Four flags, always:** delivery (milestones / burn / quality), risk (residual that can still bite), stakeholder (sponsor + key buyer last contact / alignment), commercial **or** capacity (AR / change / margin **or** named staffing / vendor capacity — pick the load-bearing one).
3. **Each flag is G/Y/R + because (≤12 words) + evidence date.** Colour without because is a fail.
4. **Overall is the worst material flag**, not an average that hides a red.
5. **Stale >30 days is not green.** Hole it.
6. **One ASK this period.** Decide / resource / escalate / freeze / unblock. Owner, date.
7. **Do not invent burn, margin, NPS, or % complete.** Hole: `[not measured — proxy by DATE]`.
8. **Single-threaded sponsor is at best yellow** on stakeholder.
9. **Not a sponsor letter, not a RAID dump, not a steering pack.**
10. **One page.**

## Intake

If **two** of 1–3 are missing after one round: issues list, not a fake colour.

1. Named project, our PM/owner, period (this week / this month) — load-bearing
2. Delivery evidence we actually have (milestone state, dates) — load-bearing
3. Residual risks / open issues that matter this period — load-bearing
4. Sponsor / key stakeholder last contact
5. Commercial (AR, change fight, margin) **or** capacity (named people / vendor)
6. The ASK this period
7. As-of date of the evidence (or "stale")

## Output shape

```
PROJECT HEALTH  |  [PROJECT]  |  [period]  |  as-of: [date]
ASK: [owner] to [decide / resource / escalate / freeze / unblock] by [date]
Our PM: [ ]    Sponsor last contact: [date or never]
Single-threaded sponsor: yes/no
Overall: G / Y / R  because [worst material flag]

FLAGS
| Flag | RYG | Because (≤12 words) | Evidence date | If we do nothing |
| Delivery | [ ] | [ ] | [ ] | [ ]
| Risk | [ ] | [ ] | [ ] | [ ]
| Stakeholder | [ ] | [ ] | [ ] | [ ]
| Commercial / capacity | [ ] | [ ] | [ ] | [ ]

THIS PERIOD
| Move | Owner | Date | Done looks like |
| ASK | [ ] | [ ] | [ ]

NOT THIS PAGE
Client letter → sponsor-status    RAID list → raid-register    Steering sitting → steering-pack    Account CS → account-health

Holes: [ ]
```

## QA (must pass)

1. Named project, period, our PM/owner.
2. Four flags, each with because and evidence date (or hole).
3. Overall = worst material flag, not a smoothing average.
4. Stale >30 days not scored green.
5. One ASK, owner, date.
6. Single-thread sponsor flagged when true.
7. No invented burn / margin / NPS / % complete.
8. Not a sponsor letter, not a RAID dump, not a steering pack, not account-health.
9. One page.

If 1, 2, 5, or 7 fail: do not ship.

## Escalate / stop

- Colour is red *and* a baseline must move → [Change Control](../../project/change-control/SKILL.md) or [Steering Pack](../../project/steering-pack/SKILL.md).
- Client-facing note is the job → [Sponsor Status](../../project/sponsor-status/SKILL.md).
- They want the whole portfolio coloured → refuse; point at portfolio tools, not this page.
- No project name after one ask → refuse.
- They insist on a house health formula with no because → refuse the theatre.

## Related

- [Sponsor Status](../../project/sponsor-status/SKILL.md) — client-facing letter this period
- [Operating Review](../../management/operating-review/SKILL.md) — internal exceptions of our shop
- [RAID Register](../../management/raid-register/SKILL.md) — living R/A/I/D list
- [Steering Pack](../../project/steering-pack/SKILL.md) — sitting with decisions
- [Account Health](../../accounts/account-health/SKILL.md) — named account, not project
- [Critical Path](../../project/critical-path/SKILL.md) — this week's path only
- [Dependency Unblock](../../project/dependency-unblock/SKILL.md) — one named dependency
