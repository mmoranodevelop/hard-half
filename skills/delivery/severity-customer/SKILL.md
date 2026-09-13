---
name: severity-customer
description: >-
  Use after the first 60–90 minutes of a customer-visible incident for owner,
  customer sentence, and next-update clock. Not crisis-holding, not after-
  action, not client-escalation.
license: MIT
---

# Severity Customer

**Customer incident update** — after the holding window: **Communication owner** (not the person SSHing), **customer sentence** (impact, not RCA), **next-update clock**, SEV, workaround. Cadence until mitigated. Default: venture program; same spine for F500.

Method origin: Google SRE Ch. 14 (Communication = public face, periodic updates; Ops is the only group modifying the system) + Google Cloud incident lifecycle + ITIL 4 major-incident communications model.

If they want an incident-management lecture: one paragraph then produce or stop. Holding is sparse and fast — [Crisis Holding](../../writing/crisis-holding/SKILL.md). This page starts **after** 60–90 minutes. Google Cloud: subsequent updates include **timelines for communication, tailored to the incident**. Silence is the failure, not "no new information." Microsoft: top priority is continuity, not isolating the cause. Restore ≠ root cause (ITIL problem management / later AAR).

## When to use

- Holding went out; customers still need a named owner, a sentence, and a next-update time
- SEV 1/2 is open and the status page has gone quiet
- Handoff of commander is happening and the customer channel would otherwise restart from zero

## When not to use

- First 60–90 min holding statement — [Crisis Holding](../../writing/crisis-holding/SKILL.md)
- No-blame after-action, RCA, actions — [After-Action Review](../../management/after-action-review/SKILL.md)
- Angry / at-risk client this week (relationship, not the outage clock) — [Client Escalation](../../accounts/client-escalation/SKILL.md)
- RAID item, not a live outage — [RAID Register](../../management/raid-register/SKILL.md)
- Sponsor weekly status — [Sponsor Status](../../project/sponsor-status/SKILL.md)
- Launch go/no-go — [Launch Brief](../../delivery/launch-brief/SKILL.md)

## Modes

| Mode | When | Output |
|---|---|---|
| **produce** | Default. Holding done or waived; incident still live | Update + next clock + ASK |
| **redline** | They pasted RCA-in-the-customer-sentence or a restarted holding | Force owner + impact sentence + next time |
| **refuse** | Rewrite holding; AAR during the outage; two load-bearing missing | Issues list. Stop |

## Hard rules

1. **After holding, not instead of it.** Do not restart [Crisis Holding](../../writing/crisis-holding/SKILL.md) at hour three.
2. **One Communication owner** — public face. Not Ops. SRE: Ops is the only group modifying the system.
3. **Customer sentence = impact now**, not internal guess, not root cause. Workaround if any.
4. **Next update is a clock**, even if nothing changed. Tailor the cadence to the incident (Google Cloud).
5. **SEV is a shared word** (Atlassian public): SEV 1 critical / SEV 2 major / SEV 3 minor with workaround. Severity ≠ priority.
6. **Handoff is live and acknowledged** ("You're now the incident commander, okay?"). Named next commander.
7. **Do not freelance a second status page** if Service Health / the agreed channel already owns it (Microsoft).
8. **After restore:** [After-Action Review](../../management/after-action-review/SKILL.md). Not during. If the **client** is angry/at-risk this week: [Client Escalation](../../accounts/client-escalation/SKILL.md) — do not substitute a SEV note for an account save.
9. **Do not invent impact scope.** Hole stays hole.

## Intake

If **the incident (named service + SEV)** and **whether holding already went** are both missing after one round: issues list, not a fake update.

1. Named service / program; SEV 1/2/3 (load-bearing)
2. Holding sent? When? Channel? (load-bearing) — if not, go to crisis-holding first
3. Customer sentence: who is impacted, what they cannot do
4. Communication owner (name) vs Ops owner (name)
5. Next update time already promised — or "none, that is the hole"
6. Workaround / mitigation status
7. Agreed channel (status page / named email / PSH) — do not add a second one

## Output shape

```
CUSTOMER INCIDENT UPDATE  |  [service / program]  |  SEV [1/2/3]  |  as-of: [time]
Clock: AFTER 60–90 min holding. Do not restart crisis-holding.

Holding went: [time / channel]     Communication owner: [name]     Ops (only modifiers): [name]
Commander now: [name]     Next commander (acked): [name / n/a]

CUSTOMER SENTENCE (impact, not RCA): [who cannot do what]
Workaround: [or none]
Channel (one): [status page / named email / PSH]     Do not freelance a second page.

NEXT UPDATE: [datetime] — even if nothing changed. Silence = fail.
Cadence until mitigated: [e.g. every 30/60 min / tailored]

NOT THIS PAGE
0–90 min → crisis-holding    After restore → after-action-review
Angry/at-risk account this week → client-escalation    RAID → raid-register

ASK: [Communication owner] ships this sentence on [channel] and hits [next-update time].
Holes: [ ]
```

## QA (must pass)

1. Holding already went, or the page says "go to crisis-holding first."
2. Communication owner ≠ Ops owner (or flagged as HOLE if one person is doing both).
3. Customer sentence has impact, not root cause.
4. Next-update datetime exists.
5. ASK + named owner + clock.
6. Not holding, not AAR, not client-escalation.
7. No invented customer counts.
8. One page.

If 1, 3, 4, or 5 fail: do not ship.

## Escalate / stop

- They want you to rewrite the first 60–90 minutes → [Crisis Holding](../../writing/crisis-holding/SKILL.md).
- RCA in the customer sentence → redline or refuse.
- After-action during the outage → refuse.
- Client angry/at-risk this week, not the outage clock → [Client Escalation](../../accounts/client-escalation/SKILL.md).
- Freelancing a second status page → refuse.

## Related

- [Crisis Holding](../../writing/crisis-holding/SKILL.md) — first 60–90 min
- [After-Action Review](../../management/after-action-review/SKILL.md) — after restore
- [Client Escalation](../../accounts/client-escalation/SKILL.md) — relationship save this week
- [Launch Brief](../../delivery/launch-brief/SKILL.md) — go/no-go; incidents after launch use this page
- [RAID Register](../../management/raid-register/SKILL.md) / [Sponsor Status](../../project/sponsor-status/SKILL.md) — not a live outage
