---
name: launch-brief
description: >-
  Use when a customer-facing go/no-go needs the promise, the support path, and
  the kill-old-path. Not go-live-readiness, not a cutover plan, not a PR-FAQ,
  not an experiment brief.
license: MIT
---

# Launch Brief

**Launch brief** — customer-facing go / no-go: one-sentence **promise**, who answers the phone, **kill-old-path**, error-budget go/no-go. Not a deploy. Default: venture launch; same spine for F500 programs.

Method origin: Google SRE Ch. 27 — a launch is **any new code that introduces an externally visible change**; Launch Coordination Engineering signs off that it is "safe."

If they want a launch-process lecture: one paragraph then produce or stop. AWS public splits three narratives: PR/FAQ (product-to-be), operational readiness (can you operate), Correction of Errors (after impact). This page is none of those. SRE Workbook: if the service exceeded its error budget for the preceding **four-week** window, **halt all changes other than P0 / security** until back within SLO. A green binary can still be a no-go.

## When to use

- Externally visible change is 48–72 hours out and nobody has written the customer sentence
- Support cannot explain the new path; old URL still works with no end date
- Error budget is red and engineering still wants to ship

## When not to use

- IT/system gate, environments, platform rollback — [Go-Live Readiness](../../project/go-live-readiness/SKILL.md)
- Hour-by-hour technical cutover — [Cutover Plan](../../project/cutover-plan/SKILL.md)
- Working backwards from a future customer — [PR-FAQ](../../strategy/pr-faq/SKILL.md)
- One experiment, kill criteria, sample — [Experiment Brief](../../strategy/experiment-brief/SKILL.md)
- Turn a BAU feature off over months — [Deprecation Notice](../../delivery/deprecation-notice/SKILL.md)
- Customer-facing incident after T+60–90 min — [Severity Customer](../../delivery/severity-customer/SKILL.md)

## Modes

| Mode | When | Output |
|---|---|---|
| **produce** | Default. Promise date exists; ORR green or waived | Brief + go/no-go + ASK |
| **redline** | They pasted "we deployed" or a go-live checklist | Force promise + support + kill-old-path |
| **refuse** | Deploy-as-launch; two load-bearing answers missing | Issues list. Stop |

## Hard rules

1. **Launch ≠ deploy.** Google: externally visible change. If the old path still works and support cannot explain the new one, you deployed.
2. **Promise:** one sentence the customer will hear. Not a changelog.
3. **Support:** who owns tickets, knowledge article, escalation, on-call. SRE: document so any team member can run it.
4. **Kill-old-path:** redirect, feature flag off, dual-run end date, or "old URL dies on [date]." Both paths live with no date is a hidden deprecation — [Deprecation Notice](../../delivery/deprecation-notice/SKILL.md), not a launch.
5. **Error budget is a gate.** Go / no-go / conditional-go. Conditional needs a dated waiver. Four-week overrun → halt except P0/security.
6. **Abort = switch off**, not a new all-hands. Flags independently revert.
7. **Do not invent SLOs or owners.** Hole stays hole.
8. After launch, incidents use [Severity Customer](../../delivery/severity-customer/SKILL.md), not a restarted brief.

## Intake

If **the customer promise (or "we have none")** and **the date the customer will see it** are both missing after one round: issues list, not a fake go.

1. What the customer will be told is true — one sentence (load-bearing)
2. Date/time the change becomes externally visible (load-bearing)
3. Support path: tickets, article, on-call, escalation — or HOLE
4. Kill-old-path: flag / redirect / dual-run end date — or "both stay live" (then this is not a launch)
5. Error budget last four weeks: in / out / unknown
6. ORR / go-live: green, waived (who + date), or not done
7. Who signs go/no-go (LCE analogue / GM / eng + support)

## Output shape

```
LAUNCH BRIEF  |  [product / change]  |  visible: [datetime]  |  D (go/no-go): [name]
Launch = externally visible change (Google SRE). Not a deploy.

PROMISE (one sentence the customer hears): [ ]
SUPPORT: tickets [owner]  article [url or HOLE]  on-call [rot]  escalation [name]
KILL-OLD-PATH: [redirect / flag off / dual-run ends [date] / old URL dies [date]]
Abort: [flag / switch] — independently revert: Y/N

ERROR BUDGET (preceding 4 weeks): IN / OUT / UNKNOWN
GO / NO-GO / CONDITIONAL-GO: [ ]     Waiver if conditional: [who + date + hole]
ORR / go-live: green / waived by [name, date] / NOT DONE → do not fake a go

Capacity vs promo spike: [ ]     Manual process any teammate can run: Y/N / HOLE
NOT THIS PAGE
System gate → go-live-readiness    Hour chart → cutover-plan    Product-to-be → pr-faq
Test → experiment-brief    BAU sunset → deprecation-notice    Incident after holding → severity-customer

ASK: [D] signs go/no-go by [date]. Kill-old-path date locked. Support can execute the promise.
Holes: [ ]
```

## QA (must pass)

1. Promise is one customer sentence, not "we shipped."
2. Support owner + kill-old-path date (or explicit dual-run end) exist, or HOLE flagged.
3. Error-budget go/no-go is filled; OUT without P0/security exception is a no-go.
4. ASK + named D + date.
5. Not a go-live checklist, not a cutover, not a PR/FAQ, not an experiment brief.
6. No invented SLOs.
7. One page.

If 1, 3, 4, or 5 fail: do not ship.

## Escalate / stop

- "We deployed, so we launched" → refuse.
- Both paths live with no end date → refuse as launch; route to deprecation-notice.
- Error budget OUT and they still want GA → no-go unless P0/security.
- They want Working Backwards as this artifact → [PR-FAQ](../../strategy/pr-faq/SKILL.md).

## Related

- [Go-Live Readiness](../../project/go-live-readiness/SKILL.md) / [Cutover Plan](../../project/cutover-plan/SKILL.md) — IT clock
- [PR-FAQ](../../strategy/pr-faq/SKILL.md) / [Experiment Brief](../../strategy/experiment-brief/SKILL.md) — idea / test clock
- [Deprecation Notice](../../delivery/deprecation-notice/SKILL.md) — BAU last-sell / last-support
- [Severity Customer](../../delivery/severity-customer/SKILL.md) — customer sentence after holding
- [Change Adoption](../../management/change-adoption/SKILL.md) — behaviours at go-live, not this brief
