---
name: decision-meeting
description: >-
  Use when one named decision must be taken in a room this week: invite with a
  named D, narrative pre-read, same-day decision record. Not an operating
  review, not a 1:1, not a RAPID operating model.
license: MIT
---

# Decision Meeting

**Decision-meeting pack** — sendable invite + same-day decision record. One decision. Named D. First action with owner and date. Default: venture, Type 2, named person as D. F500: same pack; committee as D needs a written rule before discussion.

Method origin: Grove mission-oriented meeting (public) + Bezos 2017 study hall (public letters) + Bain RAPID D in the room.

If they want a RAPID / Grove lecture: one paragraph then produce or stop.

## When to use

- One named decision this week must be taken in a room
- Invite has no D, or the subject is a noun topic ("pricing")
- Last minutes were "robust discussion" with no outcome

## When not to use

- Weekly / monthly status sitting — [Operating Review](../../management/operating-review/SKILL.md)
- Recurring RAPID map across decisions — [Decision Rights](../../management/decision-rights/SKILL.md). This skill uses RAPID *today, in this room*
- A 1:1 — [One-on-One](../../management/one-on-one/SKILL.md)
- Board / ELT paper that must be a resolution — [Executive Board Memo](../../management/executive-board-memo/SKILL.md) first, then this meeting
- Recap of a meeting already over, from notes — [Meeting Notes to Decisions](../../writing/meeting-notes-to-decisions/SKILL.md)
- Brainstorm with no decision on the table — refuse the label

## Modes

| Mode | When | Output |
|---|---|---|
| **produce** | Default. Named decision + a date | Invite + timed agenda + decision record + ASK |
| **redline** | They pasted an agenda or minutes | Same pack; kill slide theatre and "robust discussion" |
| **refuse** | Two load-bearing answers missing | Issues list. Stop |

## Hard rules

1. **One decision per pack.** Two verbs = two packs.
2. **Named D in the room.** A committee needs a written rule (chair's call / majority) before discussion.
3. **Verb sentence.** "Pricing" is a topic, not a decision.
4. **Narrative pre-read.** Study hall then discuss then D decides. Slides are not the pre-read.
5. **Same-day record** with first action / owner / date. Residual dissent once, then commit.
6. **I is not a vote.** A is bounded. Type 2 does not wear Type 1 clothes.
7. **Do not invent RAPID names** the user did not give.

## Intake

If **the decision sentence** and **the D** are both missing after one round: issues list, not a fake pack.

1. The decision, one sentence with a verb — load-bearing
2. D, by when — load-bearing
3. Type 1 (one-way) or Type 2 (two-way) — default Type 2
4. R, A (or none), I, P
5. Pre-read — exists? Who writes it, by when, pages (narrative, not slides)
6. Cost of doing nothing
7. Committee rule if the D is a body — or "named person"

No D → issues list: name the D or route to [Decision Rights](../../management/decision-rights/SKILL.md). Do not run a séance.

## Output shape

```
DECISION-MEETING PACK  |  [verb + object]
Type: 1 (one-way) | 2 (two-way)     Meeting: [date, time, tz]
D: [name]    R: [name]    A: [name or none]    P: [name]
I in the room: [names]    Informed after (not in the room): [names]

INVITE
To: [D, R, A if any, essential I, P]
Subject: DECIDE: [verb + object] by [date]
We will decide: [one sentence].
Pre-read: [memo, pages, owner, due]. Study hall in the room: [N] minutes, then discuss, then D decides.
If you are not on this list you are Informed after.

ROOM (after study hall)
1. Chair restates the decision and the D
2. Study hall — silent read
3. Clarifying questions — facts, not positions
4. R on the recommendation; I on unique facts; A on the bounded veto
5. D decides out loud, one sentence — or defers: [information] / [who] / [date]
6. Residual dissent once, then commit. P repeats first action
7. Chair restates decision, conditions, owner, date. End. No leftover status.

DECISION RECORD (same day — this is what ships)
Decision (one sentence): [ ]
Outcome: approved | approved with conditions | rejected | deferred to [date] pending [information]
Conditions (testable): [ ]
First action / owner / date: [action] / [name] / [date]
Residual dissent (one line, then commit): [name]: [ ]
Link to pre-read: [ ]

ASK: D decides [verb + object] by [meeting date]. First action: [P] by [date].
Holes: [ ]
```

Also `assets/invite.md`, `assets/agenda.md`, `assets/decision-record.md`.

## QA (must pass)

1. ASK + named D + date.
2. Decision is a verb sentence, not a noun topic.
3. Minutes / record has an outcome, not "robust discussion".
4. Not an operating review in disguise.
5. D will admit they are the D (or a written committee rule).
6. Pre-read is narrative, not slide theatre.
7. No invented RAPID names.
8. First action / owner / date on the same-day record.

If 1, 2, 3, or 7 fail: do not ship.

## Escalate / stop

- No D → [Decision Rights](../../management/decision-rights/SKILL.md).
- Status sitting → [Operating Review](../../management/operating-review/SKILL.md).
- Recap of a past meeting → [Meeting Notes to Decisions](../../writing/meeting-notes-to-decisions/SKILL.md).
- Board resolution → [Executive Board Memo](../../management/executive-board-memo/SKILL.md).
- Brainstorm with no decision → refuse the label.

## Related

- [Decision Rights](../../management/decision-rights/SKILL.md) — RAPID as an operating model
- [Operating Review](../../management/operating-review/SKILL.md) — process meeting; status
- [Executive Board Memo](../../management/executive-board-memo/SKILL.md) — the paper a board D reads
- [Pyramid Principle](../../writing/pyramid-principle/SKILL.md) — the short written argument
- [One-on-One](../../management/one-on-one/SKILL.md) — Grove process meeting, not this
- [Pre-mortem](../../management/pre-mortem/SKILL.md) — optional last hour before a Type 1
