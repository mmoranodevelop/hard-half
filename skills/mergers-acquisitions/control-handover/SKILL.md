---
name: control-handover
description: >-
  Use when handing control at close: GC / CISO / CFO sign the register (bank
  mandates, IdP, domain, repos, IP assignments, hold-separate denies). Control,
  not integration. Not a cutover plan.
license: MIT
---

# Control Handover

**GC / CISO / CFO control register at close** — bank / IdP / registrar / DNS / cloud root / repos / secrets / signing keys / IP assignments. Owner after close, evidence, hole, TSA if still on seller. ASK: residual access the D accepts. Default: venture close; same spine for F500.

Method origin: Workiva public Day 1 signatory/wire update + BCG public hold-separate deny; 17 U.S.C. § 204 writing for copyright assignment.

If they want an IAM / cutover lecture: one paragraph then produce or stop.

## When to use

- Close is dated and old signers, registrar, or repos still sit with seller/founder
- "IT will sort access next week"
- Domain on a personal registrar
- Hold-separate may require **deny**, not grant

## When not to use

- Hour-by-hour of a system event — [Cutover Plan](../../project/cutover-plan/SKILL.md)
- Close go/no-go (payroll, customer comms) — [Day-1 Continuity](../../ma/day1-continuity/SKILL.md)
- Named new platform go-live — [Go-Live Readiness](../../project/go-live-readiness/SKILL.md)
- Third-party consent to keep contracts alive — [Contract Novation](../../ma/contract-novation/SKILL.md)
- TSA economics of leftover access — [TSA Schedule](../../ma/tsa-schedule/SKILL.md)
- Integration office charter — [IMO Charter](../../ma/imo-charter/SKILL.md)

This is a **control register** the GC / CISO / CFO sign. Not a migration.

## Modes

| Mode | When | Output |
|---|---|---|
| **produce** | Default. Close dated | Register + residual ASK |
| **redline** | They pasted "access next week" or an IT cutover | Force objects, evidence, revoke-or-TSA |
| **refuse** | Two load-bearing facts missing, or a cutover lecture | Issues list. Stop |

## Hard rules

1. **Rows, not a migration story.** Bank mandates; IdP/MFA admin; registrar/DNS; cloud root; source repos; secret stores; signing keys; IP assignments. For each: owner **after close**, evidence, hole, TSA if still on seller.
2. **Bank:** new authorised signers, dual control, old signers **revoked**. Public craft: effective morning of Day 1.
3. **Identity:** critical roles can log in; leftover seller/contractor access removed **or** TSA-retained with expiry. Do not merge directories on Day 1 unless that *is* the continuity plan.
4. **Domain:** buyer-controlled registrar or documented TSA; transfer lock; org-owned recovery email. Hosting access ≠ domain ownership. Personal registrar = fail.
5. **Repos:** admin on the org that owns them; keys/secrets rotated; personal-account repos named as holes.
6. **IP:** SPA schedules executed at close. Copyright assignment requires a signed writing (17 U.S.C. § 204) — formality, not a standup.
7. **Hold-separate: deny** commercial data across the fence. Gun-jumping / remedy breach is a regulatory event.
8. **Do not invent evidence.** Holes stay holes.

## Intake

If **two** of 1, 2, 4 are missing after one round: issues list, not a fake register.

1. Close date — load-bearing
2. Bank mandates / old signers — known / unknown — load-bearing
3. IdP — who can log in Day 1; leftover seller/contractor access
4. Domain / registrar / recovery email — who owns it today — load-bearing
5. Repos / deploy keys / secrets
6. IP assignment — SPA schedules executed? (copyright needs a signed writing)
7. Hold-separate / ring-fence? yes / no / unknown

## Output shape

```
CONTROL HANDOVER  |  [deal]  |  Close: [date]  |  CLASS: CONTROL
D (accept residual): [CFO / GC / CISO names]     Hold-separate: [yes/no/unknown]

ASK: [D] to accept residual access [list] until [date] **or** delay close.
Owner of ASK: [ ]    Decide-by: [ ]

| Object | Owner after close | Evidence | Hole | TSA / expiry | Revoke old? |
| Bank mandates / signatories / wires | [ ] | [ ] | [ ] | [ ] | [old names] |
| IdP / admin MFA | [ ] | [ ] | [ ] | [ ] | [seller leftover] |
| Registrar / DNS / recovery email | [ ] | [ ] | [ ] | [ ] | [ ] |
| Cloud root / org | [ ] | [ ] | [ ] | [ ] | [ ] |
| Source repos | [ ] | [ ] | [personal-account repos] | [ ] | [ ] |
| Secret stores / deploy keys | [ ] | [rotated?] | [ ] | [ ] | [ ] |
| Signing keys | [ ] | [ ] | [ ] | [ ] | [ ] |
| IP assignments (SPA schedules) | [ ] | [executed writing] | [ ] | n/a | n/a |

HOLD-SEPARATE DENY (if remedy): [objects / data that must NOT be granted]
HOLES: [ ]
SIGN: CFO ________  GC ________  CISO ________
```

Also `assets/artifact.md`.

## QA (must pass)

1. ASK: accept residual or delay close, with date.
2. Bank row filled or labelled a hole.
3. Domain/registrar owner named; personal registrar flagged.
4. Leftover seller access revoked or TSA-dated.
5. IP assignment has evidence or is a hole.
6. Hold-separate is not "grant everyone access".
7. Not a cutover plan.
8. No invented evidence.
9. One page.

If 1, 2, or 8 fail: do not ship.

## Escalate / stop

- Two of close date / bank / domain-or-IdP missing after one ask → refuse.
- "IT will sort access next week" → refuse.
- Domain left on a personal registrar with no TSA → refuse as a hole; do not green it.
- They want hour-by-hour → [Cutover Plan](../../project/cutover-plan/SKILL.md).

## Related

- [Day-1 Continuity](../../ma/day1-continuity/SKILL.md) — close go/no-go; this is the control register
- [Cutover Plan](../../project/cutover-plan/SKILL.md) — hours of a system event
- [Go-Live Readiness](../../project/go-live-readiness/SKILL.md) — new service gate
- [Contract Novation](../../ma/contract-novation/SKILL.md) — third-party consent; this is asset control
- [TSA Schedule](../../ma/tsa-schedule/SKILL.md) — leftover access as a dated TSA row
- [IMO Charter](../../ma/imo-charter/SKILL.md) — office; this is the register
