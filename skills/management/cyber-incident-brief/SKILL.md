---
name: cyber-incident-brief
description: >-
  Use for a CEO/board one-pager in the first 24–72h of a cyber incident: facts
  known/unknown, customer/regulator, containment, one ASK. NOT for crisis-
  holding generic media; not severity-customer alone.
license: MIT
---

# Cyber Incident Brief

**CEO/board cyber incident one-pager** — what we know / do not know, systems/data impact, containment status, customer and regulator clocks, insurance notice, one ASK. Default: first 24–72h after declaration; same spine for private boards (still name disclosure clocks even if SEC 8-K does not apply).

Method origin: NIST CSF 2.0 Respond (incident manage / analyze / report-communicate) + NIST SP 800-61r3 IR profile + CISA CEO escalation / reporting thresholds + NACD board material-incident briefing shape.

If they want a NIST/CSF lecture: one paragraph then produce or stop.

## When to use

- Cyber incident declared (or likely material) and CEO/board needs a facts brief
- First 24–72h: containment underway, facts incomplete
- Decision needed on customer notice, regulator report, board call, or spend authority
- Status page exists but executives still lack a single truth page

## When not to use

- First 60–90 minutes holding words — [Crisis Holding](../../writing/crisis-holding/SKILL.md)
- Customer-channel cadence after holding — [Severity Customer](../../delivery/severity-customer/SKILL.md)
- Generic RAID of program risks — [RAID Register](../../management/raid-register/SKILL.md)
- Policy renew / limits — [Insurance Renewal](../../finance/insurance-renewal/SKILL.md)
- Full IR runbook / forensics novel — stop; CISO/IR owns ops detail
- After-action once closed — [After Action Review](../../management/after-action-review/SKILL.md)

This page is **executive decision brief**, not the IR ticket stream.

## Modes

| Mode | When | Output |
|---|---|---|
| **produce** | Default. Incident open, commander named | One-pager + one ASK |
| **redline** | They pasted a vague "we were breached" deck | Rebuild known/unknown; kill speculation as fact |
| **refuse** | No incident ID/commander, or demand to invent impact | Issues list. Stop |

## Hard rules

1. **Known vs unknown split.** Facts on the left; open questions labelled. Speculation never becomes "we know."
2. **Commander and as-of clock on page 1.** Who owns IR; next update time with timezone.
3. **Impact stated as systems / data / customers — not drama.** What is down, what data classes may be involved, confidence (confirmed / suspected / unknown).
4. **Containment status:** contained / partially / not. Eradication ≠ recovery. Do not claim "secure" without evidence.
5. **Customer + regulator clocks named.** Who must be notified by when (contractual, GDPR/state, SEC materiality determination if public, CISA if in scope). Unknown clock = hole.
6. **One ASK** — authorize notice / board call / emergency spend / disclose / engage breach counsel / notify carrier.
7. **Never invent counts.** Record counts, revenue impact, ransom demand — only if sourced; else "unknown."
8. **Insurance notice flag.** Carrier notice date or "not yet."
9. **Privilege / law-enforcement.** If counsel or LE constrains facts, say "constrained" — do not invent a public narrative here.
10. **One page.** Deep forensic annex is out of scope.

## Intake

If **two** of 1–4 are missing after one round: issues list, not a fake brief.

1. Incident ID / declaration time / commander — load-bearing
2. What is known vs unknown (systems, data classes) — load-bearing
3. Containment status — load-bearing
4. Customer impact hypothesis (none / suspected / confirmed) — load-bearing
5. Regulator / contractual notice clocks known so far
6. Insurance / breach counsel engaged? (Y/N)
7. The decision this brief unlocks in next 24h

## Output shape

```
CYBER INCIDENT BRIEF  |  [incident ID]  |  as-of: [datetime TZ]  |  CLASS: IR-exec
ASK: [owner] to [authorize notice / board call / spend / carrier notice / disclose] by [datetime TZ].

BLUF
[Claim.] Containment: [contained|partial|not]. Customer impact: [none|suspected|confirmed].
Biggest unknown: [ ]. Next update: [datetime TZ] by [commander].

KNOWN / UNKNOWN
Known: [systems, TTPs at high level, timeline anchors]
Unknown: [scope of data, dwell time, exfil confirmation, third parties]
Confidence labels: confirmed / suspected / unknown — no mixing

IMPACT
Systems: [ ]  Data classes: [ ]  Customers/employees affected: [n or unknown]
Business ops: [up|degraded|down]  Critical functions: [ ]

CONTAINMENT / RESPONSE
Status: [ ]  Actions taken: [high level]  External IR/forensics: [firm or none]
Ransom / extortion: [Y/N/unknown — no negotiation advice on this page]

CUSTOMER / REGULATOR
Customer notice plan: [owner, channel, draft clock]
Regulator / contractual clocks: [list or "unknown — GC"]
Public-company materiality path: [N/A | determination owner + 8-K clock if applicable]

INSURANCE / COUNSEL
Carrier notice: [Y/N date]  Breach counsel: [ ]  Privilege posture: [ ]

NOT THIS PAGE
Holding → crisis-holding    Customer cadence → severity-customer    Renew policy → insurance-renewal

Holes: [ ]
```

Optional annex: `assets/clock-strip.md`.

## QA (must pass)

1. Known/unknown split; no speculation as fact.
2. Commander + as-of + next-update TZ present.
3. Containment status explicit.
4. Customer/regulator clocks named or labelled hole.
5. No invented counts or impact $.
6. One ASK with owner, verb, datetime.
7. One page; not a forensic novel.

If 1, 2, 5, or 6 fail: do not ship.

## Escalate / stop

- No commander after one ask → refuse.
- Demand to invent victim counts or root cause → refuse.
- Active extortion negotiation tactics → stop; breach counsel + IR only.
- Materiality / 8-K / multi-jurisdiction notice → GC + disclosure committee; this page is exhibit.
- Safety / OT / life-critical systems → principal + CISO + relevant ops immediately.

## Related

- [Crisis Holding](../../writing/crisis-holding/SKILL.md) — first hour words
- [Severity Customer](../../delivery/severity-customer/SKILL.md) — ongoing customer updates
- [Insurance Renewal](../../finance/insurance-renewal/SKILL.md) — program design; this is an incident against it
- [Litigation Reserve](../../management/litigation-reserve/SKILL.md) — if claims/contingencies crystallize later
- [After Action Review](../../management/after-action-review/SKILL.md) — after close
