---
name: okr-cascade
description: >-
  Use when turning an already-chosen strategy into 3–5 objectives with
  measurable key results, cascaded from company to a program (not a second
  strategy). Not KPI soup, not a project plan, not a performance review.
license: MIT
---

# OKR Cascade

**Program OKR 1-pager:** few objectives, a few KRs each, committed vs aspirational labelled, owners, dates, link to parent. The program inherits company intent; it does not rewrite strategy. Default: venture / program, quarterly.

Method origin: Grove's two questions as quoted by Google re:Work + re:Work / What Matters Google playbook.

If they want to be taught OKRs: one paragraph then produce or stop. Do not dump Doerr or Grove.

## When to use

- Company (or division) strategy exists; a program must now set OKRs that serve it
- Quarterly or annual set / reset / grade
- "We have too many OKRs and no one can name the few that matter"
- Cross-team work that needs the same KR on each team's list

## When not to use

- Writing the strategy (where to play / how to win) — [Competitive Teardown](../../strategy/competitive-teardown/SKILL.md) or a strategy choice, then return
- Diagnosing a miss — [Issue Tree](../../strategy/issue-tree/SKILL.md)
- Funding the program — [Business Case](../../strategy/business-case/SKILL.md) first
- Inventing the product — [PR/FAQ](../../strategy/pr-faq/SKILL.md)
- Board paper — [Executive Board Memo](../../management/executive-board-memo/SKILL.md)
- This period's exception pack — [Operating Review](../../management/operating-review/SKILL.md)
- Performance reviews, bonus scorecards, PIP metrics — refuse (re:Work: OKRs are not employee evaluations)
- Jira dump / RACI / PMO plan / KPIs renamed "KR" — refuse or redline

If they cannot point at the parent strategy or company OKRs, they are asking you to invent strategy. Refuse.

## Modes

| Mode | When | Output |
|---|---|---|
| **produce** | Default. Company → program (grade is still produce) | 1-pager: few Os, KRs, parent links |
| **redline** | They pasted a pile of OKRs or a KPI pack | Cut to a few; relabel activities as tasks; list the pile you refused |
| **refuse** | No parent, or they want OKRs as the annual review | Issues list. Stop |

## Hard rules

1. **Every program O/KR traces to at least one parent O/KR.** They need not mirror every company OKR.
2. **Few objectives. A few KRs each.** A fifth O is usually two that should merge or a project list.
3. **Objectives are endpoints (states), one line.** Banned as the whole O: keep / maintain / continue.
4. **KRs are outcomes:** metric, baseline → target, real date, evidence. Banned verbs: consult, help, analyze, participate. "Launch X" without impact is a task.
5. **1.0 on all KRs must yield 1.0 on the Objective.** If not, the KRs are insufficient.
6. **Label committed** (expect 1.0) vs **aspirational** (expect ~0.7). Do not swap the labels.
7. **Cascade, do not photocopy.** A parent KR becomes this program's outcomes. Cross-team: each group carries the KR.
8. **If every KR lands on the last day of the quarter, you do not have a plan.** Sandbagging (all hittable with spare capacity) is a cue to cut.
9. **Do not invent baselines or targets.**

## Intake

If **two** of 1–3 are blank after one pass: issues list, not a fake cascade.

1. Parent: company or division strategy + current company OKRs (paste or point) — load-bearing
2. Program name, owner, timebox (quarter / year) — load-bearing
3. What this program exists to move (one sentence) — load-bearing
4. Already committed BAU that will not appear unless it is *the* priority
5. Cross-teams who must co-own a KR
6. Which are committed vs moonshot
7. How they grade (0.0–1.0 default). If they tie OKRs to bonus: warn; do not design the bonus.

## Output shape

```
OKR CASCADE  |  [program]  |  [Q? / year]  |  [date]
ASK: [owner] commits this stack by [date] / grades by [date]
Parent strategy / company O this serves: [ ]
Program owner: [ ]     Cycle: [ ]
Covering thought: [one sentence — what this program exists to move]

PROGRAM OKRs (few)

O1: [one-line endpoint]
Type: committed (expect 1.0) | aspirational (expect ~0.7)
Serves parent: [company O / KR]
- KR1: [metric] from [baseline] to [target] by [real date]. Evidence: [ ]
- KR2: [ ]
- KR3: [ ]
Owner: [ ]     Cross-team KR also on: [ ] / none

O2: …
O3: …

CASCADE MAP
| Program KR | Parent KR | Owner | Sister KR required? |
| [ ] | [ ] | [ ] | [ ] |

NOT OKRs (refused)
- [KPI / project / activity that stays on BAU]

GRADE (if in-cycle)
| KR | Score 0.0–1.0 | Note | Roll / close |
| [ ] | [ ] | [ ] | [ ] |
```

## QA (must pass)

1. ASK + program owner + cycle dates. Few Os, a few KRs each. Not a to-do list.
2. Every program O/KR traces to a parent (or you are explicitly writing *company* OKRs).
3. Objectives are endpoints. KRs have baseline, target, real date, unambiguous metric, evidence.
4. No consult/help/analyze/participate; no "launch X" without impact.
5. Sufficiency: 1.0 on KRs would achieve the O.
6. Committed vs aspirational labelled.
7. Covering thought is a complete sentence. Refused soup listed.
8. Not a bonus scheme. One page. No invented baselines.

If 1, 2, 3, or 5 fail: do not ship.

## Escalate / stop

- No parent strategy → refuse; do not invent strategy.
- They want OKRs as the annual review / bonus → refuse.
- They do not know what would move the parent KR → [Issue Tree](../../strategy/issue-tree/SKILL.md).
- They want a board paper of the stack → [Executive Board Memo](../../management/executive-board-memo/SKILL.md).

## Related

- [Issue Tree](../../strategy/issue-tree/SKILL.md) — if they do not know *what* would move the parent KR
- [Business Case](../../strategy/business-case/SKILL.md) — capital; OKRs measure the funded program
- [PR/FAQ](../../strategy/pr-faq/SKILL.md) — invention; OKRs come after go
- [Competitive Teardown](../../strategy/competitive-teardown/SKILL.md) — strategy choice upstream
- [Operating Review](../../management/operating-review/SKILL.md) — this period's exceptions against the plan
- [Pyramid Principle](../../writing/pyramid-principle/SKILL.md) — covering note
