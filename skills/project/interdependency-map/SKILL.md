---
name: interdependency-map
description: >-
  Use when a program has cross-project dependencies that need owners and an
  unblock ASK — critical cross-links only. Not a single dependency unblock, not
  a RAID dump, not a charter, not a RACI.
license: MIT
---

# Interdependency Map

**Critical cross-project links + one ASK** — from→to, type, owner, need-by, status, unblock. Program view of couplings, not a 100-row register. Default: venture / transformation program; same spine for F500.

Method origin: PMI Standard for Program Management (perform comprehensive dependencies management across components) + Design Structure Matrix (DSM) high-level (map couplings; surface iteration / critical path across teams — MIT OCW / dsmweb public) + operator RAID "D" craft without becoming the full register. Reconstruct the operator board. Do not invent owners or dates.

If they want a DSM / N² lecture: one paragraph then produce or stop.

## When to use

- Two or more projects on one program block each other
- SteerCo asks "what are the critical cross-links?"
- A RAID Dependencies column has grown theatre; need ≤12 critical links
- Sequencing decisions need the coupling map, not task Gantt

## When not to use

- One stuck dependency to unblock today — [Dependency Unblock](../../project/dependency-unblock/SKILL.md)
- Full Risks / Assumptions / Issues / Dependencies page — [RAID Register](../../management/raid-register/SKILL.md)
- Authorise the program — [Program Charter](../../management/program-charter/SKILL.md)
- Who does the work on deliverables — [RACI Delivery](../../project/raci-delivery/SKILL.md)
- This-quarter waves / capacity — [Program Roadmap](../../project/program-roadmap/SKILL.md)
- Single-project critical path only — stop; not this skill unless cross-project
- Locally-green workstreams that cannot be true in the same world — that is `empty-and`, not schedule couplings

## Modes

| Mode | When | Output |
|---|---|---|
| **produce** | Default. ≥2 projects; known or claimed couplings | One-pager map + critical links + ASK |
| **redline** | They pasted a 50-row dependency list or a pretty graph | Cut to ≤12 critical; force owners and need-by |
| **refuse** | Single project, or no projects named | Issues list. Stop |

## Hard rules

1. **Cross-project only.** Same-team task links stay on the project plan.
2. **≤12 critical links on page 1.** More go to annex or die.
3. **Every row:** from project → to project, dependency type (finish-to-start / data / decision / shared resource), named owner (person), need-by date, status (open / at risk / blocked / done), unblock verb.
4. **Critical = program outcome slips if this link slips.** Not "nice to have alignment."
5. **One ASK** — named D to force unblock / resequence / accept residual on the linchpin link by date.
6. **Never invent** owners, need-by dates, or "green." Holes stay holes.
7. **DSM is optional annex** (N×N check marks). Page 1 is the critical list + ASK.
8. **One page** (+ optional matrix annex).

## Intake

If **two** of 1–3 are missing after one round: issues list, not a fake map.

1. Program name and component projects in scope — load-bearing
2. Claimed or known cross-links (even messy) — load-bearing
3. Named D / program manager — load-bearing
4. Need-by dates that matter this quarter (or HOLE)
5. Shared resources or decision forums that couple teams
6. As-of date

## Output shape

```
INTERDEPENDENCY MAP  |  [program]  |  as-of: [date]  |  D: [name]
ASK: [D] to [unblock / resequence / accept residual on LINK-#] by [date]

BLUF
[n] critical cross-links. Linchpin: [from → to]. If it slips, [program outcome / tranche] breaks.

CRITICAL LINKS (≤12)
| # | From | To | Type | Owner | Need-by | Status | Unblock |
| 1 |  |  | FS/data/decision/resource |  |  |  |  |

CLUSTERS / COUPLINGS
[Projects that iterate together — name the loop; who breaks it]

NOT ON PAGE 1
Intra-project tasks    Nice-to-have alignment    Full RAID (→ raid-register)

NOT THIS PAGE
Single unblock → dependency-unblock    RAID page → raid-register
Charter → program-charter    Who does work → raci-delivery    Waves → program-roadmap

Holes: [ ]
```

Annex: `assets/dsm-grid.md` (optional).

## QA (must pass)

1. Only cross-project links; ≤12 on page 1.
2. Every row has from, to, type, owner or HOLE, need-by or HOLE, status, unblock verb.
3. Linchpin named in BLUF.
4. One ASK with owner, verb, date.
5. Not RAID theatre, not RACI, not charter, not single unblock.
6. No invented owners/dates/RAG.
7. One page (+ optional DSM annex).

If 1, 4, or 6 fail: do not ship.

## Escalate / stop

- One link is the whole problem today → [Dependency Unblock](../../project/dependency-unblock/SKILL.md).
- Risks/issues dominate → [RAID Register](../../management/raid-register/SKILL.md); keep Dependencies thin here.
- No program D → refuse until named.
- Shared-resource fight is a capacity call → note; [Program Roadmap](../../project/program-roadmap/SKILL.md) / [Capacity Demand](../../delivery/capacity-demand/SKILL.md).

## Related

- [Dependency Unblock](../../project/dependency-unblock/SKILL.md) — one link, today
- [RAID Register](../../management/raid-register/SKILL.md) — full R/A/I/D page
- [Program Charter](../../management/program-charter/SKILL.md) — authorises the program
- [RACI Delivery](../../project/raci-delivery/SKILL.md) — who does deliverable work
- [Program Roadmap](../../project/program-roadmap/SKILL.md) — waves this map must serve
