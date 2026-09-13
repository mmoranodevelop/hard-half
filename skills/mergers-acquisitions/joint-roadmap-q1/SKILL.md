---
name: joint-roadmap-q1
description: >-
  Use after a close to publish a joint 2-quarter roadmap: what ships, what is
  frozen, what is not promised. Not a PR/FAQ for a new product, not jobs-to-be-
  done.
license: MIT
---

# Joint Roadmap Q1

**Joint 2Q roadmap** — what ships, what is frozen, what is explicitly not promised. One "better together" sentence a named customer can repeat. Default: venture close.

Method origin: Bain tech scope deals public (failure to integrate product portfolios is the #1 revenue-synergy miss) + BCG software PMI (set the portfolio in motion so Day 1 has a sentence).

If they want a roadmap-merge lecture: one paragraph then produce or stop.

**Clock.** Week 1 = freeze public promises and kill rumours. Quarter 1 = ships / freeze / not-promised. Do **not** rewrite the 18-month vision in week 1.

## When to use

- Two committed backlogs now sit in one company
- Sales is demoing a "platform" that engineering has not named
- Q1: need one 2-quarter page the CRO can not over-promise from

## When not to use

- Working-backwards a **new** product — [PR/FAQ](../../strategy/pr-faq/SKILL.md)
- The job the customer hires — [Jobs to Be Done](../../strategy/jobs-to-be-done/SKILL.md)
- SKU keep / kill / combine / harvest — [Portfolio Keep-Kill](../../ma/portfolio-keep-kill/SKILL.md)
- 100-day outcomes + kill-old-path — [Integration 100](../../management/integration-100/SKILL.md)
- Stop rule for one bet — [Kill Criteria](../../strategy/kill-criteria/SKILL.md)

## Modes

| Mode | When | Output |
|---|---|---|
| **produce** | Default. 2Q window named | Ships / freeze / not-promised + ASK |
| **redline** | They pasted two roadmaps or an 18-month vision | Cut to 2Q; force not-promised |
| **refuse** | Week-1 vision rewrite; two load-bearing facts missing | Issues list. Stop |

## Hard rules

1. **Window is two quarters.** Not 18 months. Not "the platform."
2. **Ships ≤7.** Each: whose code, which customer is waiting, date, already-sold vs net-new, owner. Customer-facing date only if engineering has named it. Holes stay holes.
3. **Frozen** = do not demo. Harvest/kill SKUs freeze net-new. Revisit date required.
4. **Not promised** = rumours to kill. Sales may not imply them.
5. **Better-together is one sentence that is already true**, or it is a hole. Do not invent the combined product.
6. **Substitute, do not add.** Integration work displaces backlog. Do not invent a ratio.
7. **Week 1:** freeze public promises + one true sentence. Shipping dates that engineering has not named → refuse. 18-month rewrite → refuse.
8. Combined planning ritual by Day 30/45/75. Structural reporting-line merge is later.

## Intake

If **two** of 1, 2, 3 are missing after one round: issues list, not a fake roadmap.

1. Deal + close date — load-bearing
2. Committed backlog both sides (sold items + in-flight) — load-bearing
3. What sales is already saying (including rumours) — load-bearing
4. Harvest / kill SKUs already labelled (or "none yet" → portfolio-keep-kill)
5. Named customer waiting on a combined thing (or none)
6. Owner of the ASK (CPO) and decide-by

## Output shape

```
JOINT 2Q ROADMAP  |  [deal]  |  close: [date]  |  window: Q[n]–Q[n+1]
ASK: [CPO] freeze public promises; approve ships / freezes / not-promised by [date].
Owner of ASK: [CPO]    Decide-by: [ ]
Clock: week-1 freeze only | Q1 ships

WEEK-1 (if Day 0–7): public promises frozen. Rumour killed: [ ]. Better-together (already true): [ ]. No new ship dates.

SHIPS (≤7)
| Item | Whose code | Customer who is waiting | Date | Already-sold or net-new | Owner |
| [ ] | buyer / target / both | [name or none] | [date or hole] | sold / net-new | [name] |

FROZEN (do not demo)
| Item | Why frozen | Revisit date |
| [ ] | harvest / kill / capacity | [date] |

NOT PROMISED (do not let sales imply)
| Item | Rumour to kill |
| [ ] | [ ]

BETTER-TOGETHER (one sentence customers can repeat)
[already true / HOLE]
Cadence: one combined planning ritual by Day [30/45/75]. Structural merge: later.

NOT THIS PAGE
New product → pr-faq    Customer job → jobs-to-be-done    SKU labels → portfolio-keep-kill    Stop rule → kill-criteria

Holes: [ ]
```

## QA (must pass)

1. Window is two quarters, not an 18-month vision.
2. Every ship date has an engineering name, or is a hole.
3. Frozen rows have a revisit date.
4. Not-promised is filled when rumours exist.
5. No week-1 vision rewrite, no invented ship dates.
6. ASK + owner + date.
7. Not a PR/FAQ or a JTBD.
8. One page.

If 1, 5, or 6 fail: do not ship.

## Escalate / stop

- "We'll figure the platform in week 1" → refuse the vision; freeze promises.
- Dual roadmaps left standing with a "platform" rumour → redline into not-promised.
- SKUs unlabelled and they want to kill a line here → [Portfolio Keep-Kill](../../ma/portfolio-keep-kill/SKILL.md).

## Related

- [PR/FAQ](../../strategy/pr-faq/SKILL.md) — a new product, working backwards
- [Jobs to Be Done](../../strategy/jobs-to-be-done/SKILL.md) — the job; this is two backlogs
- [Portfolio Keep-Kill](../../ma/portfolio-keep-kill/SKILL.md) — SKU labels that feed freeze/kill
- [Kill Criteria](../../strategy/kill-criteria/SKILL.md) — stop rule for one bet
- [Integration 100](../../management/integration-100/SKILL.md) — 100-day outcomes
