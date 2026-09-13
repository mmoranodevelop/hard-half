---
name: client-escalation
description: >-
  Use when an angry or at-risk client needs a page this week: facts, owner, 48h
  plan, what we will not promise. NOT for crisis-holding (company incident), not
  raid-register, not churn-save.
license: MIT
---

# Client Escalation

**Client Escalation — This Week, 48 Hours** — one page: confirmed facts vs unknown vs story, single owner, ≤3 dated moves, what we will not promise, need-to-know. Default: venture / professional-services book; same spine for F500 / SaaS CS.

Method origin: HBR-public service recovery (identify the problem, act fast, give the front line authority *with a fence*) + CDC CERC public (facts vs unknown) as craft, not as a company-incident pack. Not ITIL.

If they want an escalation lecture: one paragraph then produce or stop.

## When to use

- Named client is angry, threatening to leave, or has escalated to an exec **this week**
- Need facts, one owner, and a 48h plan before anyone calls
- A thread of blame is writing itself in Slack and no one owns the next 48 hours
- We are about to over-promise to "calm them down"

## When not to use

- Company-wide incident holding statement — [Crisis Holding](../../writing/crisis-holding/SKILL.md)
- Living program risk register — [RAID Register](../../management/raid-register/SKILL.md)
- They already said they are out — [Churn Save](../../accounts/churn-save/SKILL.md)
- The talk prep only — [Difficult Conversation](../../writing/difficult-conversation/SKILL.md)
- Internal weekly exceptions — [Operating Review](../../management/operating-review/SKILL.md)
- After the 48h, the month — [Account Health](../../accounts/account-health/SKILL.md)
- The write-back note — [Pyramid Principle](../../writing/pyramid-principle/SKILL.md)

## Modes

| Mode | When | Output |
|---|---|---|
| **produce** | Default. Named client | 48h page + ASK |
| **redline** | They pasted a blame thread or "update" | Strip story; add owner + will-not |
| **refuse** | Two load-bearing facts missing, or an ITIL lecture | Issues list. Stop |
| **diagnose** | Thread with no confirmed facts | Unknown list + verifying + clock; still no essay |

## Hard rules

1. **Named client. This week.** Not a quarterly risk.
2. **Confirmed facts only**, with who confirmed. Unknowns listed. Story labelled story. Do not prosecute from Slack tone.
3. **One owner** of the next 48 hours. A committee is a fail.
4. **48-hour plan is three dated moves max.** Call, fix, write-back. Clock with timezone.
5. **What we will not promise** on the page before anyone calls. No fake dates, no free forever, no unnamed exec.
6. **Customer contact is named.** Who we call, by when. Economic buyer vs day-to-day — do not skip the angry person *or* the buyer.
7. **Internal need-to-know:** who is told, who is not. Do not CC the company.
8. **Not a holding statement for a company incident.** If the issue is a platform outage / press / regulator, [Crisis Holding](../../writing/crisis-holding/SKILL.md) first.
9. **Not RAID.** One issue, 48 hours. If it becomes a program risk, add a RAID row *after*.
10. **Do not invent facts or promises.** One page.

## Intake

If **two** of 1–3 are missing after one round: issues list. Zero facts is still producible: unknown list + verifying + clock.

1. Named client, our owner of the next 48h — load-bearing
2. What is confirmed (who confirmed) and what is not — load-bearing
3. Clock (first write-back time + timezone) — load-bearing
4. What they asked for vs what we might promise
5. Who we will call (angry person + buyer)
6. What we will not promise
7. Need-to-know (told / not told)

## Output shape

```
CLIENT ESCALATION  |  [CLIENT]  |  as-of: [date]  |  clock: [TIME TZ]
ASK: [owner] runs the next 48h; others stop promising by [time TZ]
Angry person: [ ]    Economic buyer: [ ]    Our owner (one): [ ]
Severity: angry / at-risk / exec-escalated

CONFIRMED / UNKNOWN / STORY
| Type | Item | Who / date |
| Confirmed | [ ] | [ ]
| Unknown | [ ] | verifying by [ ]
| Story (not fact) | [ ] | [ ]

48H PLAN (≤3 moves)
| When (TZ) | Move | Owner | Done looks like |
| [ ] | call / fix / write-back | [ ] | [ ]

WHAT WE WILL NOT PROMISE
- [fake date / free forever / unnamed exec / liability wording]

NEED-TO-KNOW
Told: [names]    Not told: [ ]

AFTER 48H
Still live → churn-save / account-health / RAID row. Closed → one-line close.

NOT THIS PAGE
Company incident → crisis-holding    Living register → raid-register    Leaving now → churn-save

Holes: [ ]
```

## QA (must pass)

1. Named client, today's date, clock with timezone.
2. Confirmed vs unknown vs story, labelled.
3. One owner of the 48h.
4. ≤3 dated moves.
5. What we will not promise, non-empty.
6. Named customer contact for the call.
7. Need-to-know listed.
8. ASK + owner + clock.
9. Not a company-incident holding statement, not a RAID dump.
10. No invented facts. One page.

If 1, 2, 3, or 5 fail: do not ship.

## Escalate / stop

- No client name after one ask → refuse.
- Platform / press / regulator / safety → [Crisis Holding](../../writing/crisis-holding/SKILL.md) + counsel; this page only for the named client commercial line.
- They said they are leaving → [Churn Save](../../accounts/churn-save/SKILL.md).
- Legal hold / threat of suit → counsel owns words; we still own the clock and will-not.
- Recurring 1:1 vent with no this-week event → not this skill. Refuse.

## Related

- [Crisis Holding](../../writing/crisis-holding/SKILL.md) — company incident
- [RAID Register](../../management/raid-register/SKILL.md) — living program register
- [Churn Save](../../accounts/churn-save/SKILL.md) — leaving now
- [Difficult Conversation](../../writing/difficult-conversation/SKILL.md) — the call opening
- [Account Health](../../accounts/account-health/SKILL.md) — after the 48h, the month
- [Pyramid Principle](../../writing/pyramid-principle/SKILL.md) — the write-back note
- [Sponsor Status](../../project/sponsor-status/SKILL.md) — if the sponsor sitting needs a line
