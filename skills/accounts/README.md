# accounts

Multi-client account management — plans, health, renewals, and saves.

## Model-invoked

Reachable by you *or* selected automatically by the agent when a task matches.

- [`account-handoff`](account-handoff/SKILL.md) — Use when transferring a named account (sales to AM, AM to AM, AM to CS): what must be true, risks, intro plan, ASK both owners.
- [`account-health`](account-health/SKILL.md) — Use when scoring ONE named account this month: usage/delivery, relationship, commercial flags, one ASK.
- [`account-plan`](account-plan/SKILL.md) — Use when writing a 12-month plan for ONE named account: outcomes, whitespaces, risks, next ASK.
- [`book-of-business`](book-of-business/SKILL.md) — Use when ranking ALL accounts this AM/MD owns: health, revenue, renewal date, capacity, grow/hold/exit.
- [`churn-save`](churn-save/SKILL.md) — Use when a named account is about to leave: why, save offer or dignified exit, ASK this week.
- [`client-escalation`](client-escalation/SKILL.md) — Use when an angry or at-risk client needs a page this week: facts, owner, 48h plan, what we will not promise.
- [`expansion-whitespace`](expansion-whitespace/SKILL.md) — Use when finding where else we can create value in a named account: job, offer, next conversation.
- [`mutual-action-plan`](mutual-action-plan/SKILL.md) — Use when writing a MAP with the customer: joint outcomes, their owners plus ours, dates.
- [`renewal-risk`](renewal-risk/SKILL.md) — Use for a named renewal inside 2 quarters: risk, multi-thread, commercial, ASK to save or walk.
- [`value-realization`](value-realization/SKILL.md) — Use when scoring promised vs delivered value for a named account this period: evidence, gap, next proof.

## User-invoked

*None yet in this bucket.* User-invoked skills are reachable only by typing the name. See [`.agents/invocation.md`](../../.agents/invocation.md).
