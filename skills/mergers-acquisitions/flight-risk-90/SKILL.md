---
name: flight-risk-90
description: >-
  Use for a 90-day post-close flight-risk watchlist with this-week conversation
  owners. Not a skip-level, not a one-on-one (those are the meeting forms).
license: MIT
---

# Flight Risk 90

**90-day flight-risk watchlist** — one page the integration leader runs with synergies: name, signal, owner of **this week's** conversation, date, stay-slate status, next check. Default: venture deal, day 0–90 post-close; same spine for F500.

Method origin: Mercer public — **1 in 5 employees leave in the first three months**; that rate doubles by months 18–24. PwC public — people decide on and before Day 1.

If they want an attrition-theory lecture: one paragraph then produce or stop.

## When to use

- Close is inside 90 days (or T-minus) and nobody is watching who walks
- Stay slate exists but the watch column has no this-week owner
- Customer poaching / recruiter noise / skipped 1:1s have started
- Day 40 and "we'll see after the org chart"

## When not to use

- The meeting form with a direct — [One-on-One](../../management/one-on-one/SKILL.md)
- The meeting form two layers down — [Skip-Level](../../management/skip-level/SKILL.md)
- Three lists + stay-bonus yes/no — [Key Talent Slate](../../ma/key-talent-slate/SKILL.md) (this page consumes Watch)
- Closing an inbound offer — [Offer Conversation](../../writing/offer-conversation/SKILL.md)
- One hire’s 90 days — [Ninety-Day Onboarding](../../learning/ninety-day-onboarding/SKILL.md)
- Cohort landing of the bought org — [Acquired Org Onboard](../../ma/acquired-org-onboard/SKILL.md)

## Modes

| Mode | When | Output |
|---|---|---|
| **produce** | Default. Inside the 90-day window | Watchlist + this-week owners + ASK |
| **redline** | They pasted an org chart or a "key people" slide | Force a signal per name; kill cheque-only rows; add talk dates |
| **refuse** | No names (or nominators) and no 90-day window, or they want the org chart as the watchlist | Issues list. Stop |

## Hard rules

1. **A watchlist, not a meeting.** The 1:1 is [One-on-One](../../management/one-on-one/SKILL.md); the skip is [Skip-Level](../../management/skip-level/SKILL.md). This page names who, why (signal), who talks this week, and the next check.
2. **Signal is required.** Rumour of interviewing, skipped 1:1s, customer asking "are you staying," manager silence, competing offer. Org-chart membership is not a signal.
3. **Owner of this week's conversation is a name.** A committee, "HR," or "their manager eventually" is a fail.
4. **Stay-bonus is not designed here.** If the person needs a cheque, route to [Key Talent Slate](../../ma/key-talent-slate/SKILL.md). Do not stay-bonus a walk-away. Do not invent amounts on this page.
5. **Same cadence as synergies.** Weekly through day 90. If you waited for the org chart, Mercer’s 1-in-5 already left.
6. **Acquired names first, then buyer-side integration-critical.** Acquired people leave faster; below-exec names belong here.
7. **Next check is a date.** Closed (staying / left / moved to retain / moved to walk-away) or still watch.
8. **Do not invent names or offers.** Holes stay holes. Do not write a firing list.

## Intake

If **the 90-day window (close date or day-count)** and **any names or a named nominator + date** are both missing after one round: issues list, not a fake page.

1. Close date; today is Day [n] of 90 (load-bearing)
2. Names already flagged, or who nominates this week (load-bearing)
3. Signals they will actually observe (not "engagement score")
4. Who owns each conversation this week
5. Stay slate already signed? Y/N — pointer
6. Cadence (weekly default) and who chairs it (IMO / CHRO)
7. Customer / competitor poaching already in play — facts

## Output shape

```
90-DAY FLIGHT-RISK WATCHLIST  |  [deal / unit]  |  close: [date]  |  today: Day [n]/90
Chair: [IMO / CHRO]     Cadence: weekly with synergies     Next sitting: [date]
Stay slate pointer: [key-talent-slate / none — hole]

WATCHLIST
| Name | Role / side | Signal (observable) | Why it matters (thesis / customer / system) | Talk owner | Talk date (this week) | Stay-slate status | Next check | Closed? |
| [ ] | [ ] / A or T | [ ] | [ ] | [name] | [date] | retain / watch / none | [date] | stay / left / escalate |

THIS WEEK (must be non-empty if the list is non-empty)
- [owner] talks to [name] by [date] using [one-on-one | skip-level | difficult-conversation]
Do not design the stay cheque here.

MOVED OFF THIS PAGE
| Name | To | Date |
| [ ] | retain (key-talent-slate) / walk-away (counsel + difficult-conversation) / left | [ ] |

NOT THIS PAGE
The 1:1 card → one-on-one
The skip card → skip-level
Stay / walk-away / bonus → key-talent-slate
Cohort landing → acquired-org-onboard
One hire → ninety-day-onboarding

ASK: [chair] runs this list weekly through Day 90. This week's talks complete by [date].
Holes: [ ]
```

## QA (must pass)

1. Close date and day-count named; window is 90 days (or T-minus labelled).
2. Every row has an observable signal — not "important person."
3. Every live row has a this-week talk owner and date.
4. No stay amounts invented here.
5. Cadence is weekly (or a named exception).
6. ASK + chair + date.
7. Not a skip-level agenda, not a 1:1 card, not a stay-bonus table.
8. No invented names.
9. One page.

If 2, 3, 4, or 6 fail: do not ship.

## Escalate / stop

- Org chart pasted as the watchlist with no signals → refuse.
- They want you to write the 1:1 script as this page → route to one-on-one; keep the name here.
- They want stay money on this page → route to key-talent-slate.
- Safety / harassment / legal hold in a row → HR/counsel; drop from this operating list.

## Related

- [Key Talent Slate](../../ma/key-talent-slate/SKILL.md) — retain / walk-away / stay-bonus; this is the 90-day watch
- [One-on-One](../../management/one-on-one/SKILL.md) — the meeting form for this week's talk
- [Skip-Level](../../management/skip-level/SKILL.md) — the meeting form two layers down
- [Difficult Conversation](../../writing/difficult-conversation/SKILL.md) — if the talk is a no, not a check-in
- [Acquired Org Onboard](../../ma/acquired-org-onboard/SKILL.md) — cohort landing for the rest
- [Day-1 Employee Pack](../../ma/day1-employee-pack/SKILL.md) — going dark is a flight-risk cause
- [Day-1 Leadership Slate](../../ma/leadership-day1/SKILL.md) — unnamed bosses drive exits
- [Integration 100](../../management/integration-100/SKILL.md) — run this list in the same weekly cadence
- [IMO Charter](../../ma/imo-charter/SKILL.md) — who chairs the sitting
