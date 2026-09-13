---
name: milestone-burn
description: >-
  Use when milestones need a traffic light plus burn/slip rate and one ASK. NOT
  for critical-path network deep-dive, not sponsor-status one-pager alone, not
  steering-pack decisions pack, not go-live-readiness gate.
license: MIT
---

# Milestone Burn

**Milestone traffic light + burn/slip — one page** — named milestones RAG; planned vs forecast date; slip rate (days/period); burn (work remaining vs time); one ASK. Default: client program mid-flight; same spine for internal delivery.

Method origin: Milestone Trend Analysis (MTA) public — forecast dates plotted across reporting periods; flat = stable, rising = slip — plus burndown/burnup concepts public (remaining work vs time; scope in vs done). Operator board, not a scheduling textbook.

If they want an MTA / burndown lecture: one paragraph then produce or stop.

## When to use

- SteerCo / sponsor needs milestone RAG **and** whether dates are slipping each period
- "We're fine" but forecasts creep two periods in a row
- Need burn signal (remaining vs window) without a full network rewrite
- Hybrid agile/waterfall: common language on milestone dates + work left

## When not to use

- Full network / float / crashing math — [Critical Path](../../project/critical-path/SKILL.md)
- Client one-pager RAG without milestone trend table — [Sponsor Status](../../project/sponsor-status/SKILL.md)
- Committee sitting with ≤3 decisions + capacity — [Steering Pack](../../project/steering-pack/SKILL.md)
- Named go-live exit criteria gate — [Go-Live Readiness](../../project/go-live-readiness/SKILL.md)
- Cost EAC pulse — [EAC Pulse](../../project/eac-pulse/SKILL.md)

## Modes

| Mode | When | Output |
|---|---|---|
| **produce** | Default. Milestone list + forecasts | Traffic light + slip/burn + ASK |
| **redline** | They pasted a Gantt tour | Force ≤8 milestones; kill task soup |
| **refuse** | No milestones and no dates, or invent slip | Issues list. Stop |

## Hard rules

1. **≤8 milestones** on the page. More → annex or cut. Tasks are not milestones.
2. **Each row:** baseline date, prior forecast, current forecast, RAG, slip (days this period / cumulative).
3. **RAG meaning fixed.** Green = forecast holds baseline (or approved re-baseline). Amber = path to green with named action. Red = cannot hold without a decision. Do not hide Red as Amber.
4. **Slip rate.** Days slipped since last report (and cumulative vs baseline). Three consecutive upward MTA moves → must escalate options, not "monitor".
5. **Burn line (one).** Remaining work unit (points / tasks / % scope) vs remaining calendar — or HOLE. Burnup if scope is still moving in.
6. **One ASK** — D to accept slip / crash / cut scope / re-baseline by date.
7. **Never invent** dates or remaining %. Holes stay holes.
8. **One page** (+ optional MTA spark annex).

## Intake

If **two** of 1–3 are missing after one round: issues list, not a fake light.

1. Project + reporting period ending — load-bearing
2. Milestone list with baseline dates — load-bearing
3. Current forecast dates (or "unchanged") — load-bearing
4. Prior-period forecasts if trend matters
5. Remaining work measure (or "none — dates only")
6. Who has D on re-baseline / slip accept
7. Critical-path dependency known or "unknown"

## Output shape

```
MILESTONE BURN  |  [project]  |  period ending: [date]  |  D: [name]
Baseline: [charter/plan v]     Cadence: [weekly/biweekly]

ASK: [D] to [accept slip / re-baseline MS-x / add capacity / cut scope] by [date]

TRAFFIC LIGHT (≤8)
| ID | Milestone | Baseline | Prior fcst | Now fcst | Slip this / cum (d) | RAG | Owner |
| 1 |  |  |  |  |  |  |  |

OVERALL
[Green / Amber / Red] because [one cause]. Path: [action + owner + date / needs decision].

BURN (one line)
Unit: [pts/tasks/%]  Remaining: [ ]  Window left: [ ]  Pace OK? yes / no / unknown
Scope in this period (burnup): [none / +n]

MTA SIGNAL
Consecutive upward slips: [0/1/2/3+] on [milestone IDs]. Options if 3+: [crash / cut / re-baseline].

NOT THIS PAGE
Network/float → critical-path    Client RAG one-pager → sponsor-status
SteerCo decisions → steering-pack    Go-live gate → go-live-readiness

Holes: [ ]
```

Annex: `assets/mta-spark.md`.

## QA (must pass)

1. ≤8 milestones with baseline + current forecast.
2. Slip this period and/or cumulative shown or HOLE.
3. Overall RAG with cause; Red not hidden.
4. One ASK with owner, verb, date.
5. Burn line present or explicitly date-only.
6. Not a Gantt dump, not SteerCo pack, not go-live criteria.
7. No invented dates. One page.

If 1, 3, 4, or 7 fail: do not ship.

## Escalate / stop

- Three consecutive slips on a load-bearing milestone with no options → escalate; page lists crash/cut/re-baseline.
- They want every task RAG → refuse; [Critical Path](../../project/critical-path/SKILL.md) or cut to milestones.
- Go-live window decision → [Go-Live Readiness](../../project/go-live-readiness/SKILL.md).
- Safety / regulatory date miss → escalate now.

## Related

- [Critical Path](../../project/critical-path/SKILL.md) — network, float, crash math
- [Sponsor Status](../../project/sponsor-status/SKILL.md) — client one-pager; may cite this board
- [Steering Pack](../../project/steering-pack/SKILL.md) — decision sitting
- [Go-Live Readiness](../../project/go-live-readiness/SKILL.md) — live-event gate
- [EAC Pulse](../../project/eac-pulse/SKILL.md) — cost twin of schedule pulse
- [RAID Register](../../management/raid-register/SKILL.md) — feeds blockers behind Red
