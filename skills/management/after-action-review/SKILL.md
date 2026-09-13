---
name: after-action-review
description: >-
  Use when a completed or mid-run event needs a short no-blame learning record:
  what was supposed to happen, what did, why, and 2–5 actions with owner, date,
  next event. Not a pre-mortem, not a RAID dump, not a performance review.
license: MIT
---

# After Action Review

**No-blame AAR record** — four questions plus 2–5 actions (owner, date, next event they change). The conversation is the work; the note is the byproduct. Default: venture program after a gate; same spine for F500.

Method origin: US Army AAR public (four questions, no rank, self-discovery). One line, not a field-manual dump.

If they want an AAR / retro lecture: one paragraph then produce or stop.

## When to use

- A sprint, launch, incident, gate, or customer event just ended (or a phase did)
- Mid-run: the work is not progressing as intended (informal, shorter)
- After a win as well as a miss — against a plan, not a vibe dump

## When not to use

- Before the work, imagined failure — [Pre-mortem](../../management/pre-mortem/SKILL.md)
- Living risks / assumptions / issues / deps — [RAID Register](../../management/raid-register/SKILL.md)
- Status cadence — [Operating Review](../../management/operating-review/SKILL.md)
- A decision still unmade — [Decision Meeting](../../management/decision-meeting/SKILL.md)
- Recovering the intent of the program — [Program Charter](../../management/program-charter/SKILL.md)
- Closing the project file — [Project Close](../../project/project-close/SKILL.md)
- Why we won or lost a deal — [Win Loss](../../strategy/win-loss/SKILL.md)

AAR ≠ RAID ≠ pre-mortem. AAR = after (or mid-run), what did happen vs plan.

## Modes

| Mode | When | Output |
|---|---|---|
| **produce** | Default. Session to run or already run | Timed agenda + filled (or blank) record |
| **redline** | They pasted a lessons-learned deck | Strip blame; restore four questions; force owner/date/next event |
| **refuse** | No event, no participants who were there, or "who failed" column | Issues list. Stop |

They already talked → produce the write-up from their notes. Mid-run short session → same four questions, thinner note.

## Hard rules

1. **Four questions, in order:** supposed to happen / actually happened / why (went well and did not) / what we will do.
2. **"Supposed to happen" is the plan,** not a mood. Facts of what happened are separate from why. Disagreements recorded, not averaged. Do not invent.
3. **People who were there.** Leader of the work is a participant, not the judge. Senior tourists last or not at all. Facilitator asks; does not brief the answers.
4. **No blame.** Rank left at the door. Object is the work, not the person.
5. **2–5 actions:** owner, date, which next event they change. A lesson is not learned until applied. No next event → you are writing history; stop.
6. **Short.** Formal longer; informal shorter. Soon (days, not next quarter). Wins have causes, not "great work."

## Intake

If **two** of 1, 3, 6 are missing after one round: issues list, not a fake AAR.

1. The event and whether it is over or mid-run — load-bearing
2. The plan / intent (charter, order, success test) — if missing, recovering it is item 2 on the agenda
3. Who was there (the people who did the work) — load-bearing
4. Formal or informal
5. Who facilitates
6. The next event the actions must change — load-bearing

If they want to document lessons with nobody who was there: refuse. The AAR is a conversation among participants.

## Output shape

```
AAR — [event / project]
Date of event: [ ]    Date of AAR: [ ]
Facilitator: [ ]    Participants (who were there): [ ]
Formal | informal
Next event these actions must change: [ ]

ASK: [named owner of the note] to close actions 1–[n] into [next event] by [date].

Intent (what was supposed to happen):
[the actual plan — one paragraph or 3 bullets]

What happened (facts; disagreements noted):
[ ]

Why (went well / did not — cause and evidence):
- [cause — evidence]

What we will do:
| Action | Owner | Date | Next event it changes |
| [ ] | [ ] | [ ] | [ ]

Not learned until applied (how we will know): [ ]
Holes: [ ]
```

Agenda for the room: `assets/agenda.md`.

## QA (must pass)

1. Four questions in order; "supposed to happen" is the plan.
2. Participants were the people who did the work.
3. No blame / "who failed" / HR verdict.
4. 2–5 actions; each has owner + date + next event.
5. ASK: note owner, actions into next event, date.
6. Not a lessons-learned binder.
7. Wins have causes.
8. Facts not averaged when the room disagreed.
9. One page.

If 3, 4, or 5 fail: do not ship.

## Escalate / stop

- Names in a "who failed" column → refuse; offer causes and actions.
- Live safety / clinical / legal incident still unfolding → stop; stabilize.
- Lessons-learned binder → refuse as AAR; one-pager only.
- Leader will lecture / will not leave rank at the door → stop calling it an AAR.
- Employment consequences hanging on the session → HR/legal, not this skill.
- No next event → refuse; you are writing history.

## Related

- [Pre-mortem](../../management/pre-mortem/SKILL.md) — same team, before; imagined failure
- [RAID Register](../../management/raid-register/SKILL.md) — AAR actions may become RAID items
- [Operating Review](../../management/operating-review/SKILL.md) — status cadence, not learning against a plan
- [Program Charter](../../management/program-charter/SKILL.md) — the intent you recover in question 1
- [Decision Meeting](../../management/decision-meeting/SKILL.md) — if the AAR surfaces a decision still unmade
- [Project Close](../../project/project-close/SKILL.md) — file close; this is learning
- [Win Loss](../../strategy/win-loss/SKILL.md) — deal autopsy, not an event AAR
