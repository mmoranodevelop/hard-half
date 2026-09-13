---
name: decision-debt
description: >-
  Use when aged undecided items need a single owner, age in days, and a next
  decision date. NOT for decision-journal (already taken), not commitment-
  register, not raid-register, not meeting-notes-to-decisions, not decision-
  meeting.
license: MIT
---

# Decision Debt

**Decision debt** — one page of aged **undecided** items: the decision in one sentence, one D, opened date, age in calendar days, next decide-by (or the date it dies / defaults), cost of waiting, default if silent, ASK (decide this week / kill the item / assign D). Cap ≤12 on page 1; hot 3 by age × blast radius. Default: the MD’s personal pile plus company-level Ds they own. Same spine for F500: one function or one program, not an enterprise philosophy.

Method origin: Forbes Technology Council (Nirmal Jingar, 9 Jul 2026) — postponed trade-offs; busy calendars are the **interest**; name the decision, one owner, deadline, reopen rule. Cutler “decision drift” was fetched **to exclude** (drift *after* a call is not this page).

If they want a decision-debt lecture: one paragraph then produce or stop. Do **not** rebuild RAPID / RACI — [Decision Rights](../../management/decision-rights/SKILL.md) / [RACI Delivery](../../project/raci-delivery/SKILL.md) already map the D.

## When to use

- Calls have aged with no owner and no decide-by
- Alignment without ownership is delaying work (calendars are the interest)
- A RAID issue, a promise, or a logged decision is being mislabelled as “debt”

## When not to use

- Decision **taken**, waiting to see if it worked — [Decision Journal](../../learning/decision-journal/SKILL.md)
- Promise to board / customer / team — [Commitment Register](../../productivity/commitment-register/SKILL.md)
- Risks / assumptions / issues / dependencies — [RAID Register](../../management/raid-register/SKILL.md)
- Notes from one meeting → decided / pending / parked — [Meeting Notes to Decisions](../../writing/meeting-notes-to-decisions/SKILL.md)
- One named call **in a room today** — [Decision Meeting](../../management/decision-meeting/SKILL.md)
- Who has the D on a **type** of decision — [Decision Rights](../../management/decision-rights/SKILL.md)
- Period reds — [Operating Review](../../management/operating-review/SKILL.md) (an aged D can appear as a red; the paydown list is here)

## Modes

| Mode | When | Output |
|---|---|---|
| **produce** | Default. At least one named undecided item exists | Register + hot 3 + ASK |
| **redline** | They pasted a RAID, a journal, meeting notes, or a backlog labelled “decision debt” | Strip decided / promises / risks; force owner + age + next date |
| **refuse** | No named undecided item *and* no one who will assign D; or they want RAPID rebuilt | Issues list. Stop |

## Hard rules

1. Object is **aged, still undecided**. Decided rows **leave** this page. If consequential they **enter** [Decision Journal](../../learning/decision-journal/SKILL.md). If it was a promise → [Commitment Register](../../productivity/commitment-register/SKILL.md).
2. Item is a **decision** in one sentence (“launch phased vs full”), not “discuss launch.”
3. Owner is **one name**. “Steering” is a hole. Input ≠ ownership (do not rebuild RAPID here).
4. Age = calendar days from first recognised. Next date is a **decision date**, not a review-the-risk date.
5. Cost of waiting is named (rework, blocked hire, signalling, option decay). Default if silent is named.
6. Cap the live list (≤12 on page 1). Hot 3 by age × blast radius.
7. A RAID issue with no decision date is **not** this page. A product backlog labelled “decision debt” is refuse. No Wardley map as the artifact.
8. Do not invent items, owners, or dates. Holes stay holes.

## Intake

If **any named undecided item** and **owner (or who assigns D by when)** are both missing after one round: issues list, not a fake page.

1. Entity / program; as-of (load-bearing with 2)
2. Named undecided items — the *decision*, not a topic (load-bearing)
3. Owner (D) per item, or who assigns D by when
4. Date first recognised (for age)
5. Next decide-by, or the date it dies / defaults
6. Cost of waiting if known — or “derive”
7. Scope: MD personal pile / one function / one program — not enterprise-wide philosophy

## Output shape

```
DECISION DEBT  |  [entity / program]  |  as-of: [date]
Object: aged UNDECIDED. Decided rows leave → decision-journal. Cap ≤12. D = one name.

HOT 3 (age × blast radius)
| # | Decision (one sentence) | Owner (D) | Opened | Age (d) | Next date | Cost of waiting | Default if silent |
| 1 | [launch phased vs full — not “discuss launch”] | [name] | [date] | [n] | [decide-by] | [rework / blocked hire / signal / option decay] | [what happens] |

LIVE LIST (rest, ≤9)
| Decision | D | Opened | Age | Next date | Cost of waiting | Default if silent |

NOT THIS PAGE: taken → decision-journal; promises → commitment-register; R/A/I/D → raid-register; notes → meeting-notes-to-decisions; one call in a room → decision-meeting; RAPID map → decision-rights

ASK: [decide this week / kill the item / assign D] for items [ ]
Owner: [ ]  Date: [ ]
Holes: [ ]
```

## QA (must pass)

1. Every row is still undecided. No decided / promise / RAID-issue rows.
2. Every row has one named D (or HOLE, not “steering”).
3. Age in days + next **decision** date (or default-if-silent).
4. Hot 3 present if the list is >3.
5. ASK + owner + date.
6. Not a journal, RAID, commitment register, meeting-notes dump, or RAPID rebuild.
7. No invented items. One page.

If 1, 2, 5, or 6 fail: do not ship.

## Escalate / stop

- Logging a decision before the outcome → [Decision Journal](../../learning/decision-journal/SKILL.md).
- Rebuilding RAPID / RACI → [Decision Rights](../../management/decision-rights/SKILL.md) / [RACI Delivery](../../project/raci-delivery/SKILL.md).
- Product backlog or Wardley map labelled “decision debt” → refuse.
- Cutler-style drift after a call already made → not this page; journal / sense-making.

## Related

- [Decision Journal](../../learning/decision-journal/SKILL.md) — taken + expected + review date
- [Commitment Register](../../productivity/commitment-register/SKILL.md) — promises
- [RAID Register](../../management/raid-register/SKILL.md) — R/A/I/D; letters are not Decisions
- [Meeting Notes to Decisions](../../writing/meeting-notes-to-decisions/SKILL.md) / [Decision Meeting](../../management/decision-meeting/SKILL.md)
- [Decision Rights](../../management/decision-rights/SKILL.md) — RAPID map; this page **uses** a D
- [Operating Review](../../management/operating-review/SKILL.md) — period reds
- [Close Calendar](../../finance/close-calendar/SKILL.md) / [Working Capital](../../finance/working-capital/SKILL.md) / [Reforecast](../../finance/reforecast/SKILL.md) / [Cap Table](../../finance/cap-table/SKILL.md) / [Follow-On](../../finance/follow-on/SKILL.md) — pay down Ds blocking those pages
