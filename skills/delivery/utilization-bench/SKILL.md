---
name: utilization-bench
description: >-
  Use when named people are off billable this week and need a date back on work
  plus an owner of the next seat. Not a headcount plan, not a WIP limit, not a
  calendar-kill (calendar-audit).
license: MIT
---

# Utilization Bench

**Bench list** — named people not on billable work this week: last billable date, what they are doing instead, **date back on billable**, owner of the next seat, blocker. A utilization % is the quarterly scoreboard, not Monday's page. Default: venture delivery shop; same spine for F500 programs.

Method origin: SPI 2026 PS Maturity Benchmark (public recaps) + NetSuite — bench = a consultant with no active project.

If they want a utilization lecture: one paragraph then produce or stop. Utilization ≠ realization ≠ margin. SPI 2026: industry billable utilization **66.4%** (survey-history low) vs **70%** floor / **75%** optimal; project margin **37.7%** while EBITDA **9.9%**. Magnetic: 80% util × 85% realization = **68%** yield. None of those numbers staff a name this week.

## When to use

- People are idle, in pre-sales, internal, leave, or waiting — nobody has a date back on billable
- QBR said ~66% and someone wants to hire or fire from the %
- Realization looks wrong and the first guess is "we are not busy enough"

## When not to use

- Roles, start dates, cost, plan vs actual HC — [Headcount Plan](../../management/headcount-plan/SKILL.md)
- Too much work in flight, finish-to-start — [WIP Limit](../../productivity/wip-limit/SKILL.md)
- Kill / delegate / protect the calendar — [Calendar Audit](../../productivity/calendar-audit/SKILL.md)
- This program's onshore / contractor / vendor split — [Staffing Mix](../../delivery/staffing-mix/SKILL.md)
- Hours delivered but not invoiced — [Unbilled Leakage](../../delivery/unbilled-leakage/SKILL.md)
- RAID / weekly status — [RAID Register](../../management/raid-register/SKILL.md) / [Sponsor Status](../../project/sponsor-status/SKILL.md)
- Weekly commercial commit — [Forecast Call](../../commercial/forecast-call/SKILL.md)

## Modes

| Mode | When | Output |
|---|---|---|
| **produce** | Default. Names or a roster source exist | Named bench list + ASK |
| **redline** | They pasted a util dashboard or "we are at 66%" | Force names + dates; kill hire/fire-from-% |
| **refuse** | A % with no names; two load-bearing answers missing | Issues list. Stop |

## Hard rules

1. **Named person, not a %.** Utilization is a quarterly scoreboard. This week's object is a name with a date back on billable.
2. **Every row:** role, last billable date, doing instead (pre-sales / internal / leave / wait / HOLE), date back on billable, next-seat owner, blocker.
3. **Do not hire or fire from 66.4%.** The % has no owner. The name does.
4. **Read utilization with realization on the same people** this month. Booked at 80% × 85% still yields 68%.
5. **Do not invent names or dates.** Hole stays hole.
6. **Bench ≠ mix.** Mix is [Staffing Mix](../../delivery/staffing-mix/SKILL.md).
7. **One page.** The 70/75 strip is a footnote, not the artifact.

## Intake

If **named people (or a named roster + date)** and **last billable / what they are doing instead** are both missing after one round: issues list, not a fake page.

1. Unit / shop; as-of date (load-bearing)
2. Named people off billable, or who pulls the roster by when (load-bearing)
3. Last billable date + what they are doing instead, per name (load-bearing)
4. Sold work that could take them this week, or "none"
5. Who owns seating (delivery lead / RM)
6. This-month utilization AND realization if known — or "not pulled"
7. Constraint: leave, visa, client-barred, notice — or "none"

## Output shape

```
BENCH LIST  |  [unit / shop]  |  as-of: [date]  |  D (seating): [name]

SCOREBOARD (quarterly; not this week's job)
Billable util: [ ]%   vs SPI 2026 66.4% industry; 70% floor / 75% optimal
Realization (same people): [ ]%    Yield (util × realization): [ ]%
Project margin: [ ]% (SPI 37.7%)    Firm EBITDA: [ ]% (SPI 9.9%)

THIS WEEK — named, not a %
| Name | Role | Last billable | Doing instead | Date back on billable | Next-seat owner | Blocker |
| [ ] | [ ] | [date] | pre-sales / internal / leave / wait / [ ] | [date] | [name] | [ ] |

Unnamed idle: HOLE — [n] or "roster incomplete"
Hire/fire from the %: FORBIDDEN on this page

NOT THIS PAGE
HC plan → headcount-plan    WIP → wip-limit    Calendar → calendar-audit
Program mix → staffing-mix    Unbilled hours → unbilled-leakage

ASK: [D] seats every named person or names the blocker by [date this week].
Holes: [ ]
```

## QA (must pass)

1. At least one named person, or an explicit roster HOLE — not a % as the body.
2. Each named row has date back on billable (or HOLE) and next-seat owner (or HOLE).
3. No hire/fire from the industry %.
4. ASK + named D + date this week.
5. Not a headcount cost table, not a WIP board, not a calendar.
6. No invented names.
7. One page.

If 1, 3, 4, or 6 fail: do not ship.

## Escalate / stop

- "We are at 66% so hire / fire" → refuse; that is not a bench list.
- Firm-wide utilization target as the weekly artifact → refuse; QBR strip only.
- Names exist but nobody will own the next seat this week → do not ship a % page.

## Related

- [Staffing Mix](../../delivery/staffing-mix/SKILL.md) — this program's blend vs margin; this page is idle names
- [Unbilled Leakage](../../delivery/unbilled-leakage/SKILL.md) — hours without an invoice, not idle hours
- [Rate Card](../../delivery/rate-card/SKILL.md) — frozen quote list; do not reprice to fill the bench
- [Headcount Plan](../../management/headcount-plan/SKILL.md) / [WIP Limit](../../productivity/wip-limit/SKILL.md) / [Calendar Audit](../../productivity/calendar-audit/SKILL.md)
- [Forecast Call](../../commercial/forecast-call/SKILL.md) — weekly commercial commit; do not park bench % in Commit
