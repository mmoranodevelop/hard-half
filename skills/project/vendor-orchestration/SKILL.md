---
name: vendor-orchestration
description: >-
  Use when one program has multiple vendors (SI / agencies / specialists) and
  needs who-leads-whom: cross-vendor RACI, named integration owner, interface
  risks, one ASK. NOT for vendor-milestone (one gate), not vendor-sow, not
  vendor-scorecard, not raci-delivery alone, not partner-exit.
license: MIT
---

# Vendor Orchestration

**Multi-vendor who-leads-whom for ONE program** — SI / agencies / specialists on one page: lead vs specialist, cross-vendor RACI on interfaces, named integration owner (Master Conductor), interface risks, one ASK. Default: client program with ≥2 delivery vendors; same spine when an internal platform team is a "vendor."

Method origin: multi-vendor / SI orchestration practice (Master Conductor + joint RACI) + DACI-style Driver for integration — orchestra, not one gate.

If they want a RACI / multi-SI lecture: one paragraph then produce or stop.

## When to use

- ≥2 vendors on one program and "who owns the seam?" is fuzzy
- Blame game at an interface; each SOW is "green" and the program is not
- Naming or changing the integration owner / lead SI mandate
- Before SteerCo when vendor landscape is the exception

## When not to use

- One vendor milestone accept/reject — [Vendor Milestone](../../project/vendor-milestone/SKILL.md)
- Writing / buying the SOW — [Vendor SOW](../../management/vendor-sow/SKILL.md)
- Monthly score on one named vendor — [Vendor Scorecard](../../management/vendor-scorecard/SKILL.md)
- Internal deliverable RACI only (no vendor orchestra) — [RACI Delivery](../../project/raci-delivery/SKILL.md)
- Exiting a partnership / channel — [Partner Exit](../../commercial/partner-exit/SKILL.md)
- Single-project health — [Project Health](../../project/project-health/SKILL.md)

## Modes

| Mode | When | Output |
|---|---|---|
| **produce** | Default. Named program, ≥2 vendors | Orchestra one-pager + ASK |
| **redline** | They pasted a vendor list or SOW stack | Force integration owner + interface RACI; kill "all Accountable" |
| **refuse** | One vendor only, or no program name, or legal contract rewrite | Issues list. Stop |

## Hard rules

1. **ONE named program. ≥2 vendors.** A single SOW is not an orchestra.
2. **Name the integration owner** (Master Conductor / Driver) — person or firm with mandate to chase seams. Client still owns judgment.
3. **Lead vs specialist** marked per workstream; lead SI is not silently every specialist.
4. **Cross-vendor RACI on interfaces only** (not every task). One A per interface row.
5. **Interface risks:** what breaks if Vendor A is late for Vendor B — owner, trigger.
6. **One ASK:** name conductor / rewrite interface RACI / escalate partner / freeze scope at seam. Owner, date.
7. **Do not invent SLAs, fees, or % complete.** Hole them.
8. **Not a milestone gate, not a SOW, not a monthly scorecard, not partner-exit.**
9. **One page.**

## Intake

If **two** of 1–3 are missing after one round: issues list, not a fake RACI.

1. Named program + vendor list (role: lead SI / specialist / agency) — load-bearing
2. Who is supposed to integrate today (named or "nobody") — load-bearing
3. Top interfaces / seams that have failed or will fail — load-bearing
4. Contractual lead language (if any) vs practiced reality
5. Client integration owner (PMO / TMO) name
6. The ASK this period

## Output shape

```
VENDOR ORCHESTRATION  |  [PROGRAM]  |  as-of: [date]
ASK: [owner] to [name conductor / fix interface RACI / escalate / freeze seam] by [date]
Integration owner: [name / firm / nobody]    Client judgment: [name]

VENDORS
| Vendor | Role (lead SI / specialist / agency) | Scope slice | Mandate gap |

INTERFACE RACI (seams only)
| Interface / seam | R | A (one) | C | I | Need-by |

INTERFACE RISKS
| Seam | If A slips | Hits vendor | Trigger | Owner |

NOT THIS PAGE
One gate → vendor-milestone    Buy SOW → vendor-sow    Monthly score → vendor-scorecard    Exit partner → partner-exit

Holes: [ ]
```

## QA (must pass)

1. Named program; ≥2 vendors with roles.
2. Integration owner named or explicitly "nobody" (yellow/red).
3. Interface RACI has one A per seam row.
4. Interface risks with owner + trigger.
5. One ASK, owner, date.
6. No invented SLAs / fees / %.
7. Not milestone / SOW / scorecard / partner-exit.
8. One page.

If 1, 2, 5, or 6 fail: do not ship.

## Escalate / stop

- One vendor after one ask → refuse; point at [Vendor Milestone](../../project/vendor-milestone/SKILL.md) or [Vendor Scorecard](../../management/vendor-scorecard/SKILL.md).
- Contractual SOW rewrite is the job → [Vendor SOW](../../management/vendor-sow/SKILL.md); this page only names the seam gap.
- They want counsel to redline liability → stop; flag counsel.
- Integration owner is a delivery vendor with no client reporting line → flag conflict; recommend structural split.

## Related

- [Vendor Milestone](../../project/vendor-milestone/SKILL.md) — one gate accept/reject
- [Vendor SOW](../../management/vendor-sow/SKILL.md) — buy the work
- [Vendor Scorecard](../../management/vendor-scorecard/SKILL.md) — monthly pass/fail one vendor
- [RACI Delivery](../../project/raci-delivery/SKILL.md) — who does the work on deliverables
- [Partner Exit](../../commercial/partner-exit/SKILL.md) — leave a partnership
- [Steering Pack](../../project/steering-pack/SKILL.md) — board sitting
- [Interdependency Map](../../project/interdependency-map/SKILL.md) — cross-project deps
