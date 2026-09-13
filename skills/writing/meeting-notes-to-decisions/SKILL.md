---
name: meeting-notes-to-decisions
description: >-
  Use after a meeting to turn notes into a sendable decision log: decided,
  pending, parked, each with owner and date. Not meeting design, not RAID, not a
  commitment register, not an AAR.
license: MIT
---

# Meeting Notes to Decisions

**Decision log** — decided / pending / parked + actions table. Sendable within 24 hours. Every action: one named human, one calendar date. Default: venture program call. F500: same log; board minutes stay with the secretary.

Method origin: minutes-lite (public cousins: decision record, MFR).

If they want a lecture on how to take minutes: one paragraph then produce or stop.

## When to use

- The meeting just happened and notes must become a sendable log
- Actions exist without owners or dates
- Open items were labelled "decided" in the notes
- Recipients must confirm or correct by the next day

## When not to use

- Designing the meeting, pre-read, or RAPID in the room — [Decision Meeting](../../management/decision-meeting/SKILL.md)
- Lessons after an event — [After Action Review](../../management/after-action-review/SKILL.md)
- Living program risks/assumptions/issues/dependencies — [RAID Register](../../management/raid-register/SKILL.md)
- Promises as an integrity register — [Commitment Register](../../productivity/commitment-register/SKILL.md)
- Staff-to-principal yes/no *before* the meeting — [Principal Brief](../../writing/principal-brief/SKILL.md)
- Board minutes counsel or the secretary must own — [Executive Board Memo](../../management/executive-board-memo/SKILL.md)
- Weekly status pack — [Operating Review](../../management/operating-review/SKILL.md)

## Modes

| Mode | When | Output |
|---|---|---|
| **produce** | Default | Sendable log from their notes |
| **redline** | They pasted minutes | Strip narrative; force owners and dates; no fake "decided" |
| **refuse** | Two load-bearing answers missing | Issues list. Stop |

Notes with no decisions → produce pending questions, not invented "decided" lines.

## Hard rules

1. **Three buckets only.** Decided, pending, parked. Transcript is a fail.
2. **Decided is a complete sentence** a stranger could execute. Topics ("pricing") are not decisions.
3. **Do not invent decided.** Open items stay pending.
4. **Parked has a reason and a fate** (revisit date or dead because).
5. **Owners are one human.** "The team" is not an owner. "ASAP" is not a date.
6. **Disagreement stays on the page.** Name both holds and the tie-break.
7. **Risks belong here only if they change an owner or a date.** A risk list is RAID.
8. **You do not decide in the recap** what the room did not.

## Intake

If **meeting identity** and **who was in the room** are both missing: refuse.

1. Meeting — name, date, purpose — load-bearing
2. Who was in the room and who can actually decide — load-bearing
3. Notes — paste, bullets, or memory (label memory unverified)
4. Anything already known decided / parked
5. Where this log lives — email / doc / ticket, so owners are taggable

Voice overlay: load [Voice Blueprint](../../writing/voice-blueprint/SKILL.md) if one exists.

## Output shape

```
Subject: [Meeting] — decided: [one-line biggest decision, or "no decisions — pending below"]

Meeting: [name]
When: [date, time, tz]
In the room (deciders): [names]
Copied (need to know): [names]

DECIDED (complete sentence a stranger could execute)
- [We will …] Decider: [name / the room]. Effective: [date].

PENDING (not a polite decided)
- [Question still open.] Decider: [name]. By: [date]. Needs: [input].
Disagreement: [name] holds [X]; [name] holds [Y]; tie-break: [rule].

PARKED (reason + fate)
- [Item]. Why: […]. Revisit: [date] / Dead because […].

ACTIONS
| Action | Owner (one human) | Date |
| [ ] | [name] | [date] |

Not decided (on purpose)
- [ ]

ASK: Recipients confirm or correct by [date + next day]. Overdue: new date or escalate to [name].
Holes: [unknown — need owner / date / whether this was actually decided]
```

Chase overdue rows only: `assets/chase.md`. Do not rewrite history.

## QA (must pass)

1. ASK, owner on each action, calendar date.
2. Decided lines are verb sentences, not topics.
3. No fake decisions — open items labelled pending.
4. Parked has reason and fate.
5. Not a transcript / "robust discussion".
6. Disagreement not smoothed away.
7. Not a RAID dump, commitment register, or AAR in disguise.
8. You did not decide in the recap what the room did not.

If 1, 3, or 8 fail: do not ship.

## Escalate / stop

- They want the meeting designed → [Decision Meeting](../../management/decision-meeting/SKILL.md).
- Board minutes → secretary / [Executive Board Memo](../../management/executive-board-memo/SKILL.md).
- They want you to close a D that the room left open → refuse; put it in pending.

## Related

- [Decision Meeting](../../management/decision-meeting/SKILL.md) — designs the meeting; this writes what came out
- [After Action Review](../../management/after-action-review/SKILL.md) — learns after an event
- [RAID Register](../../management/raid-register/SKILL.md) — living program log
- [Commitment Register](../../productivity/commitment-register/SKILL.md) — promises as integrity, not meeting output
- [Principal Brief](../../writing/principal-brief/SKILL.md) — the pre-read
- [Executive Board Memo](../../management/executive-board-memo/SKILL.md) — minutable board resolutions
