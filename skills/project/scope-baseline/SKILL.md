---
name: scope-baseline
description: >-
  Use for in/out scope baseline + cost of saying yes to a creep ask. NOT for
  change-control (formal CR), not project-charter, not prd-spec, not kill-
  criteria.
license: MIT
---

# Scope Baseline

**In / Out Baseline + Cost of Yes** — one page: what is in, what is out, the creep ask, cost of saying yes (time / cost / risk), one ASK. Default: venture / PS delivery; same spine for F500 workstreams.

Method origin: PMI scope baseline public (approved scope statement / WBS / WBS dictionary — change only via formal control) + MoSCoW public for prioritising what stays in when time is fixed.

If they want a scope-baseline / MoSCoW lecture: one paragraph then produce or stop.

## When to use

- Need a clear in/out line for a live project before more work lands
- Someone asked for "just one more thing" and you need the cost of yes
- MoSCoW / priority fight: Must vs Won't this time
- Charter exists but the working in/out list is fuzzy

## When not to use

- Formal change request against a signed baseline — [Change Control](../../project/change-control/SKILL.md)
- First authorisation of the project — [Project Charter](../../project/project-charter/SKILL.md)
- Product requirements / PRD depth — [PRD Spec](../../documents/prd-spec/SKILL.md)
- Dated kill tests for a bet — [Kill Criteria](../../strategy/kill-criteria/SKILL.md)
- Whole-project RYG — [Project Health](../../project/project-health/SKILL.md)
- Client weekly status — [Sponsor Status](../../project/sponsor-status/SKILL.md)
- Steering sitting with several decisions — [Steering Pack](../../project/steering-pack/SKILL.md)

## Modes

| Mode | When | Output |
|---|---|---|
| **produce** | Default | In/out page + cost-of-yes + ASK |
| **redline** | They pasted a wish-list / backlog / "scope doc" | Force in/out + cost of the creep ask; kill the novel |
| **refuse** | Two load-bearing facts missing, or they want a full WBS dictionary | Issues list. Stop |

## Hard rules

1. **One named project / workstream.** Not a portfolio.
2. **In and Out are both written.** Out is not "TBD" — name what we will not do this time.
3. **Creep ask is one named ask** (or "none — baseline only"). Do not smuggle a CR pack here.
4. **Cost of saying yes** — time, cost, risk, and what drops (MoSCoW: Must protected; Could/Won't absorb). No invented €/$ — hole amounts.
5. **MoSCoW labels optional but useful** on contested rows: Must / Should / Could / Won't this time.
6. **One ASK** — hold out / accept with trade / route to change-control. Owner, date.
7. **If they already need formal approve/defer/reject against a signed baseline →** hand off to [Change Control](../../project/change-control/SKILL.md); this page can be the exhibit.
8. **Do not invent effort or budget.** Hole: `[not estimated — by DATE]`.
9. **Not a charter, not a PRD, not a kill-test card.**
10. **One page.**

## Intake

If **two** of 1–3 are missing after one round: issues list, not a fake baseline.

1. Named project + signed/agreed reference (charter / SOW / prior in-out) — load-bearing
2. Current in list (or "unknown — rebuild") — load-bearing
3. The creep ask (or explicit none) — load-bearing
4. Out list / Won't this time
5. Constraints: end date, envelope, capacity
6. Who can say yes (sponsor / CCB)
7. The ASK candidate

## Output shape

```
SCOPE BASELINE  |  [PROJECT]  |  as-of: [date]  |  ref: [charter/SOW v]
ASK: [owner] to [hold-out / accept-with-trade / open-CR] by [date]

IN (this time)
| Item | MoSCoW | Owner | Notes |
| [ ] | M/S/C | [ ] | [ ]

OUT / WON'T THIS TIME
| Item | Why out | Revisit? |
| [ ] | [ ] | [date or no]

CREEP ASK
Ask: [one sentence]    Requested by: [ ]
Cost of YES:
  Time: [days/weeks or hole]
  Cost: [amount or hole]
  Risk: [ ]
  What drops / moves to Won't: [ ]

RECOMMEND: hold-out / accept-with-trade / open change-control
because [≤12 words]

NOT THIS PAGE
Formal CR → change-control    First authorisation → project-charter    PRD depth → prd-spec    Kill tests → kill-criteria

Holes: [ ]
```

## QA (must pass)

1. Named project + reference (or hole labelled).
2. In list and Out / Won't list both present.
3. Creep ask named or explicit "none."
4. Cost of yes: time / cost / risk / what drops — holes allowed, inventions not.
5. One ASK, owner, date.
6. No invented effort / budget numbers.
7. Not a formal CR pack, not a charter, not a PRD, not kill-criteria.
8. One page.

If 1, 2, 5, or 6 fail: do not ship.

## Escalate / stop

- Ask needs formal approve/defer/reject against signed baseline → [Change Control](../../project/change-control/SKILL.md).
- No project yet authorised → [Project Charter](../../project/project-charter/SKILL.md).
- Product requirements depth is the job → [PRD Spec](../../documents/prd-spec/SKILL.md).
- Bet needs dated kill tests → [Kill Criteria](../../strategy/kill-criteria/SKILL.md).
- No in/out and no creep ask after one round → refuse.

## Related

- [Change Control](../../project/change-control/SKILL.md) — formal CR against baseline
- [Project Charter](../../project/project-charter/SKILL.md) — first authorisation
- [PRD Spec](../../documents/prd-spec/SKILL.md) — product requirements depth
- [Kill Criteria](../../strategy/kill-criteria/SKILL.md) — dated kill tests for a bet
- [Steering Pack](../../project/steering-pack/SKILL.md) — sitting that may decide the trade
- [Project Health](../../project/project-health/SKILL.md) — period RYG
- [Sponsor Status](../../project/sponsor-status/SKILL.md) — client letter
