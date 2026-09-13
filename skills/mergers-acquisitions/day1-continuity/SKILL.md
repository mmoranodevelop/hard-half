---
name: day1-continuity
description: >-
  Use for close go/no-go: payroll, legal entity, bank, access for critical
  roles, customer comms. Continuity and control, not a product go-live. Not go-
  live-readiness, not cutover-plan, not integration-100.
license: MIT
---

# Day-1 Continuity

**Close go / conditional / no-go card** — payroll, entity, bank, access, customer comms, TSA executable, what will **not** change on Day 1. Default: venture close; same spine for F500.

Method origin: McKinsey/KPMG public Day 1 as continuity and control, not a product launch; Workiva public bank craft (signatories / wires morning of close).

If they want a Day 1 / cutover-CAB lecture: one paragraph then produce or stop.

## When to use

- Close date (or scenarios) needs go / no-go
- Payroll, bank, entity, or customer comms are still "IT will handle"
- Someone filed a 40-line ERP cutover as the Day 1 page
- "Day 1 = new CRM"

## When not to use

- Named new-service go/no-go, defects, rollback — [Go-Live Readiness](../../project/go-live-readiness/SKILL.md)
- Hour-by-hour of a system event — [Cutover Plan](../../project/cutover-plan/SKILL.md)
- First 100-day outcomes + kill-old-path — [Integration 100](../../management/integration-100/SKILL.md)
- Bank mandates / IdP / domain / repos / IP register — [Control Handover](../../ma/control-handover/SKILL.md)
- Named-logo owner + script + SLA freeze — [Named Account Day 1](../../ma/named-account-day1/SKILL.md)
- Stay / walk-away slate — [Key Talent Slate](../../ma/key-talent-slate/SKILL.md)
- Who runs the unit Day 1 — [Day-1 Leadership Slate](../../ma/leadership-day1/SKILL.md)
- TSA economics / exit dates — [TSA Schedule](../../ma/tsa-schedule/SKILL.md)

Day 1 often must not cut over the ERP. Plug-and-play workarounds are expected.

## Modes

| Mode | When | Output |
|---|---|---|
| **produce** | Default. Close dated or this week | Go / Conditional / No-Go card + ASK |
| **redline** | They pasted an IT cutover or "Day 1 = new CRM" | Kill system theatre; force payroll/bank/entity/comms |
| **refuse** | Two load-bearing facts missing, or a go-live lecture | Issues list. Stop |

## Hard rules

1. This gate is **close**, not a system. Call Go / Conditional / No-Go.
2. Tests that must work: payroll (right entity, funded, tax routing); legal entity and invoice names; banking / cash / AP; access to systems the business already runs; customer-facing continuity; employee + key-account comms; TSA services executable.
3. Payroll cannot pause. Dry-run or labelled hole.
4. Write what will **not** change. "Day 1 = new CRM" fails.
5. Residual risks with named D. Multiple close-date scenarios if clearance is live.
6. Point control objects (mandates, IdP, domain, repos, IP) at [Control Handover](../../ma/control-handover/SKILL.md); do not duplicate the register.
7. Named accounts: this page says comms went out; the script lives on [Named Account Day 1](../../ma/named-account-day1/SKILL.md).
8. **Do not invent dry-run dates or payroll paths.** Holes stay holes.

## Intake

If **two** of 1, 2, 7 are missing after one round: issues list, not a fake gate.

1. Close date (or scenarios) — load-bearing
2. Payroll path — entity, funded account, dry-run result (or "none") — load-bearing
3. Bank / signatories / AP
4. Access for named critical roles (continuity, not directory merge)
5. Customer comms — named accounts, who sends, what brand/hours/SLA
6. What will not change on Day 1
7. D for go / no-go (name) — load-bearing

## Output shape

```
DAY 1 CONTINUITY  |  [deal]  |  Close: [date]  |  Scenarios: [ ]
D for go/no-go: [name]     Integration Leader: [name]

ASK: [D] to call [Go / Conditional / No-Go] for close on [date] with residual [list].
Owner of ASK: [D]    Decide-by: [date]

CALL: [Go / Conditional / No-Go]

| Must work Day 1 | Owner | Test (evidence) | Status |
| Payroll (entity, funded account, tax routing) | [ ] | [dry-run date / HOLE] | [ ] |
| Legal entity, signatories, invoice names | [ ] | [ ] | [ ] |
| Banking / cash / AP | [ ] | [mandates live — see control-handover] | [ ] |
| Access for named critical roles | [ ] | [names] | [ ] |
| Customer-facing continuity (hours, SLA, who to call, brand) | [ ] | [ ] | [ ] |
| Comms — employees | [ ] | [sent / draft / HOLE] | [ ] |
| Comms — key accounts | [ ] | [named list / named-account-day1] | [ ] |
| TSA services executable | [ ] | [ ] | [ ]

WILL NOT CHANGE ON DAY 1: [ERP / CRM / …]
RESIDUAL RISKS (named D): [ ]
Holes: [ ]
```

Also `assets/artifact.md`.

## QA (must pass)

1. ASK (D, Go/Conditional/No-Go, date).
2. Close date or scenarios present.
3. Payroll row filled or labelled HOLE.
4. Not "Day 1 = new CRM/ERP" as the plan.
5. "Will not change" is written.
6. Named D.
7. Not a go-live-readiness or cutover-plan in costume.
8. No invented dry-runs. One page.

If 1, 2, 3, or 6 fail: do not ship.

## Escalate / stop

- Two of close date / payroll test / D missing after one ask → issues list.
- 40-line IT cutover as this page → refuse; route [Cutover Plan](../../project/cutover-plan/SKILL.md).
- "Day 1 = new CRM" → refuse.
- They want 100-day outcomes → [Integration 100](../../management/integration-100/SKILL.md).

## Related

- [Go-Live Readiness](../../project/go-live-readiness/SKILL.md) — new service, not close
- [Cutover Plan](../../project/cutover-plan/SKILL.md) — hours of a system event
- [Integration 100](../../management/integration-100/SKILL.md) — after Day 1 holds
- [Control Handover](../../ma/control-handover/SKILL.md) — mandates, IdP, domain, repos, IP
- [Named Account Day 1](../../ma/named-account-day1/SKILL.md) — logo scripts
- [Key Talent Slate](../../ma/key-talent-slate/SKILL.md) / [Day-1 Leadership Slate](../../ma/leadership-day1/SKILL.md)
- [TSA Schedule](../../ma/tsa-schedule/SKILL.md) — economics; this page only asks "executable?"
- [IMO Charter](../../ma/imo-charter/SKILL.md)
