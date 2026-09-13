---
name: sla-credit
description: >-
  Use after an SLA breach: credit owed, root cause class, customer letter spine,
  prevent-repeat ASK. NOT for severity-customer (sev taxonomy), not client-
  escalation (angry week), not deprecation-notice.
license: MIT
---

# SLA Credit

**SLA breach → credit + letter + prevent** — contract metric missed, measured availability / performance, credit tier owed, exclusions checked, root-cause class, customer letter spine, one ASK to prevent repeat. Default: enterprise SaaS / managed service; same spine for ITIL-style service credit.

Method origin: ITIL/public service-credit practice — credit as contractual remedy, not goodwill theatre. Enterprise SaaS public SLA examples (Atlassian, Smartsheet, hyperscaler tiers) — tiered % of monthly fees, claim windows, monitoring as source of truth, sole-remedy limits, chronic-failure exit triggers.

If they want an SLA-law lecture: one paragraph then produce or stop.

## When to use

- Availability / response / restore SLA missed in a named period
- Customer (or finance) asks "what credit do we owe?"
- Need a customer letter spine: facts, credit, next steps — not a war story
- Breach must produce a prevent-repeat action, not only a credit memo
- Claim window is open and evidence must be frozen

## When not to use

- First 60–90 min customer incident update — [Severity Customer](../../delivery/severity-customer/SKILL.md)
- Angry multi-thread week with exec heat — [Client Escalation](../../accounts/client-escalation/SKILL.md)
- Tech API / feature retirement notice — [Deprecation Notice](../../delivery/deprecation-notice/SKILL.md)
- Holding statement while facts incomplete — [Crisis Holding](../../writing/crisis-holding/SKILL.md)
- After-action learning write-up — [After Action Review](../../management/after-action-review/SKILL.md)
- Renegotiating the whole MSA (offer this page as input to counsel)

## Modes

| Mode | When | Output |
|---|---|---|
| **produce** | Default. Contract SLA + period + measured result | Credit calc + letter spine + ASK |
| **redline** | They pasted "we'll give 10% goodwill" with no contract math | Force contract tiers, exclusions, claim window |
| **refuse** | No contract metric, no period, and they want a gesture % | Issues list. Stop |

## Hard rules

1. **Contract first.** Name the SLA metric, commitment (e.g. monthly uptime %), measurement source, and credit schedule. No schedule = HOLE — do not invent tiers from "industry norms."
2. **Period and measured result on the page.** Calendar month / window; measured % or minutes; commitment; delta.
3. **Exclusions checked.** Maintenance, customer-caused, third-party, force majeure — list applied or "none applied." Silent exclusion is a fail.
4. **Credit math is arithmetic.** Tier → % of fees in scope → $ or invoice credit. Cap / sole-remedy note if in contract. Do not invent %.
5. **Claim window.** Customer or vendor must file by [date]; monitoring source of truth if contract says so.
6. **Root-cause class, not a novel.** Capacity / change / dependency / process / unknown — enough to drive prevent-repeat. Full AAR is separate.
7. **Letter spine ≠ legal advice.** Facts, apology if appropriate, credit offered, what changes, who to contact. Counsel reviews before send when MSA risk is material.
8. **One ASK.** Approve credit + send letter + owner for prevent-repeat by date — not "make the customer happy."

## Intake

If **contract SLA reference** and **breach period** are both missing after one round: issues list.

1. Customer + contract / order form reference
2. SLA metric + commitment + credit schedule (or HOLE)
3. Period of breach + measured result + evidence source
4. Exclusions considered
5. Fees in scope for the period ($) or HOLE
6. Customer temperature (calm claim / angry / silent)
7. Approver (CS / Finance / counsel) + decide-by

## Output shape

```
SLA CREDIT  |  [customer]  |  period: [ ]  |  contract ref: [ ]
ASK: approve credit [$/%] + send letter | prevent-repeat owner [ ] by [date]

BREACH
Metric: [ ]    Commitment: [ ]    Measured: [ ]    Source of truth: [ ]
Exclusions applied: [none / list]    Claim window closes: [ ]

CREDIT
| Tier trigger | Credit % | Fees in scope | Credit $ | Cap / sole remedy |
| [from contract or HOLE] | [ ] | [ ] | [ ] | [ ] |

ROOT-CAUSE CLASS: [capacity/change/dependency/process/unknown] — one line: [ ]
PREVENT-REPEAT: [action] — owner [ ] — due [ ]

LETTER SPINE
1. What happened (facts, period, measured vs commitment)
2. Credit: [amount / %] applied how [next invoice / other]
3. What we are changing (prevent-repeat)
4. Contact: [name, channel]
5. Optional: chronic-failure / exit rights status [if contract has them]

NOT THIS PAGE
Live sev update → severity-customer | Angry week → client-escalation | API EOL → deprecation-notice
HOLES: [ ]
```

## QA (must pass)

1. Contract metric + commitment cited or HOLE labelled.
2. Period + measured result present.
3. Exclusions explicitly checked.
4. Credit arithmetic from contract tiers — no invented %.
5. Letter spine has facts + credit + prevent-repeat.
6. One ASK + owner + date.
7. Not sev taxonomy, not escalation war-room, not deprecation notice.
8. One page.

If 1, 4, 6, or 7 fail: do not ship.

## Escalate / stop

- They want goodwill % with no contract → refuse; route to commercial concession with eyes open.
- Chronic breach near termination trigger → counsel + [Client Escalation](../../accounts/client-escalation/SKILL.md).
- Facts still unstable inside first hour → [Severity Customer](../../delivery/severity-customer/SKILL.md) / [Crisis Holding](../../writing/crisis-holding/SKILL.md).
- Security / privacy / regulated outage → legal + security before letter.

## Related

- [Severity Customer](../../delivery/severity-customer/SKILL.md) — live customer update clock
- [Client Escalation](../../accounts/client-escalation/SKILL.md) — angry multi-thread week
- [Deprecation Notice](../../delivery/deprecation-notice/SKILL.md) — planned tech retirement
- [Crisis Holding](../../writing/crisis-holding/SKILL.md) — sparse holding statement
- [After Action Review](../../management/after-action-review/SKILL.md) — learning write-up after credit ships
- [Customer CEO Letter](../../comms/customer-ceo-letter/SKILL.md) — higher-stakes executive letter if needed
