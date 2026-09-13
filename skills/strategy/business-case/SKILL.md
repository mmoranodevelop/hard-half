---
name: business-case
description: >-
  Use when an MD must allocate capital: options including do-nothing,
  incremental cash, NPV (or honest payback-only), sensitivity, kill criteria,
  named owner. Not pr-faq, not issue-tree, not a 40-page IC novel, not
  executive-board-memo as the whole job.
license: MIT
---

# Business Case

**Business Case — Fund / Stage / Kill** — one page + cash appendix: options including do-nothing, incremental after-tax cash, NPV at a named hurdle (or honest payback-only), sensitivity, kill switch, named owner, next cheque. Default: venture / program (Type 2 unless they say one-way door or F500 IC); same spine for F500.

Method origin: CFA-public capital allocation (incremental cash, NPV vs IRR) + Bezos Type 1/2 (cost of undo). Operator 1-pager, not an IC novel.

If they want an NPV lecture: one paragraph then produce or stop.

## When to use

- Fund / kill / stage a project, plant, platform, bolt-on, or program
- Compare 2–4 mutually exclusive options, including do-nothing / delay
- Set kill criteria and an owner before money moves
- Rewrite a bloated IC deck into something a CFO will read

## When not to use

- Customer-back invention — [PR/FAQ](../../strategy/pr-faq/SKILL.md) first, then this money test
- Why something is broken — [Issue Tree](../../strategy/issue-tree/SKILL.md)
- Board paper that must be minuted — wrap this 1-pager in [Executive Board Memo](../../management/executive-board-memo/SKILL.md)
- Covering email — [Pyramid Principle](../../writing/pyramid-principle/SKILL.md)
- Unit "does one more customer make money" — [Unit Economics](../../strategy/unit-economics/SKILL.md)
- 13-week cash — [Cash Runway](../../management/cash-runway/SKILL.md)
- Gate meeting — [Portfolio Stage-Gate](../../management/portfolio-stage-gate/SKILL.md) (this page is the exhibit)

## Modes

| Mode | When | Output |
|---|---|---|
| **produce** | Default. Options named | 1-pager + cash appendix + ASK |
| **redline** | They pasted a case / model summary | Fail QA; fix cash-flow sins; no extra slides |
| **refuse** | Two load-bearing facts missing, or sunk cost in FCF | Issues list. Stop |

## Hard rules

1. **Options include do-nothing** (and delay if real). One "the project" with no alternative is a brochure.
2. **Incremental after-tax cash**, not accounting profit. Ignore sunk. Charge opportunity cost. Cannibalization on or off with a reason. Interest lives in the hurdle, not the cash line.
3. **NPV at a named hurdle** is the decision metric. If NPV and IRR rank differently, NPV wins. Payback is a liquidity screen — allowed only if labelled.
4. **Base / down / up** on the 2–4 drivers that flip the sign. No fake decimals.
5. **Kill criteria:** metric, threshold, date, who calls it — before the next cheque.
6. **Type 1 = full rigor. Type 2 = stage + kill;** do not bloat to look serious.
7. **Named owner, named next cheque, named date.**
8. **One page for the meeting.** Appendix holds the cash table. "Strategic value" with no cash / option / named veto (safety, licence) is cut.
9. **Do not invent a NPV, hurdle, or margin.** Holes stay holes.

## Intake

If **two** of 1–3 are missing after one round: issues list, not a fake case.

1. Decision (fund / kill / stage), who, by when — load-bearing
2. Options including do-nothing — load-bearing
3. Owner after yes — load-bearing
4. Cash they actually have (capex, opex, timing, WC, tax, terminal) or "payback only"
5. Hurdle (WACC / project / payback-only)
6. Rest-of-firm (cannibalization, stranded, compliance) + kill criteria they will live with
7. Door: Type 1 or Type 2 (cost of undo)

## Output shape

```
BUSINESS CASE  |  FUND / STAGE / KILL  |  as-of: [date]
ASK: [fund / stage / kill] option [A] vs do-nothing by [date]
Owner (after yes): [ ]     Door: Type 1 | Type 2 (undo = [ ])
Hurdle: [WACC / project / payback-only] — source: [ ] or HOLE

RECOMMENDATION
[Complete-sentence claim. Base NPV. What has to be true. Kill criterion.]

OPTIONS
| Option | What changes vs today | Next cheque | NPV / IRR / payback | Kill / undo |
| 0 Do nothing / delay | [ ] | — | [opportunity cost] | [ ]
| A [ ] | [ ] | [ ] | [ ] or HOLE | [ ]
| B [ ] | [ ] | [ ] | [ ] | [ ]

CASH (incremental, after-tax) — summary
Horizon: [ ]    Base NPV / IRR / payback: [ ]
Down / up NPV: [ ]    Drivers that flip the sign: [ ]

KILL CRITERIA
Stop the next cheque if [metric] [threshold] by [date], called by [role].

NOT THIS PAGE
Customer-back → pr-faq    Diagnosis → issue-tree    Fiduciary wrapper → executive-board-memo

Holes: [ ]
```

## QA (must pass)

1. ASK + owner + date. Options include do-nothing; mutually exclusive.
2. Cash incremental, after-tax; sunk excluded; opportunity cost and cannibalization addressed (even "none — because…").
3. Financing not double-counted in the cash line.
4. NPV at a named hurdle, or honest payback-only label. Else `[HOLE]`.
5. If IRR conflicts with NPV on ranking, the page follows NPV.
6. Sensitivity on drivers that matter.
7. Kill criteria: metric, threshold, date, caller.
8. One page + appendix. No 40-page IC. No invented hurdle.
9. Not a PR/FAQ, not an issue tree.

If 1, 2, 4, or 7 fail: do not ship.

## Escalate / stop

- No options or no owner after one ask → refuse.
- They want sunk cost in FCF → refuse.
- SWOT / vision with no cash → refuse.
- They want a 40-page IC novel → refuse; this page is the exhibit; wrap in [Executive Board Memo](../../management/executive-board-memo/SKILL.md) if it must be minuted.
- Invented hurdle or "benchmark" margin they cannot source → hole or stop.

## Related

- [Issue Tree](../../strategy/issue-tree/SKILL.md) — diagnosis before the case
- [PR/FAQ](../../strategy/pr-faq/SKILL.md) — customer test; this is the money test
- [Unit Economics](../../strategy/unit-economics/SKILL.md) — one more unit; this is the cheque
- [Executive Board Memo](../../management/executive-board-memo/SKILL.md) — fiduciary wrapper
- [OKR Cascade](../../strategy/okr-cascade/SKILL.md) — after funding, how the program is measured
- [Cash Runway](../../management/cash-runway/SKILL.md) — liquidity, not capital allocation
- [Portfolio Stage-Gate](../../management/portfolio-stage-gate/SKILL.md) — the sitting; this is the exhibit
