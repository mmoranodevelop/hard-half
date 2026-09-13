---
name: customer-concentration
description: >-
  Use when top-N customers are a material revenue or credit risk and an MD needs
  the math plus what we will do this quarter. Not unit economics of a product,
  not a QBR with one account.
license: MIT
---

# Customer Concentration

A **top-N risk 1-pager**: who pays us, what % of revenue (and AR), what breaks if they leave, **what we do this quarter**. Default: venture or a line that has three logos doing most of the billings.

Public method: US GAAP ASC 280 major-customer rule (10% of consolidated revenue is the public flag); SEC Regulation S-K Item 101 when dependence is material; Deloitte / PwC public: common-control groups and a government count as **one** customer; AR concentration is credit risk, not just sales mix. Reconstruct the operator card. Not an accounting opinion.

## When to use

- "How exposed are we to [Customer A] / our top 5?"
- Before a board, lender, or fundraise that will ask the 10% question
- Top-N renewal, down-sell, or insolvency would hit payroll
- Set the quarter's de-risk actions (not a 3-year "diversify" slogan)

## When not to use

- Whether **one more unit** makes money — [Unit Economics](../../strategy/unit-economics/SKILL.md)
- Quarterly review **with** that customer — [QBR](../../management/qbr/SKILL.md)
- 13-week collections on named invoices — [Cash Runway](../../management/cash-runway/SKILL.md) (this page may **feed** it)
- Competitive position of a rival — [Competitive Teardown](../../strategy/competitive-teardown/SKILL.md)
- Pricing architecture — [Pricing One-Pager](../../strategy/pricing-one-pager/SKILL.md)

If they cannot name revenue by customer (or a honest hole), stop.

## Modes

| Mode | When | Output |
|---|---|---|
| **produce** | Default | Top-N 1-pager + this-quarter ASK |
| **redline** | They pasted a "we have logo risk" slide | Same numbers; 10% math; dated actions |
| **refuse** | No revenue split, or a lecture on ASC 280 | Issues list or one paragraph then stop |

## Hard rules

1. **Name the N.** Default top 5 plus anyone ≥10% of trailing-12 or last-quarter revenue. Groups under common control = one customer (ASC 280 public).
2. **Revenue % and AR %.** A customer at 12% of sales and 40% of AR is a credit problem, not just a mix problem.
3. **10% is a flag, not comfort.** Below 10% can still be fatal in a small book (one customer at 8% *and* 70% of contribution).
4. **Contribution, not just revenue.** If the whale is negative contribution, concentration is worse ([Unit Economics](../../strategy/unit-economics/SKILL.md) as input).
5. **What breaks.** Payroll, covenant, hire plan, valuation story — one line each if true.
6. **This quarter's actions.** New logos, expand others, contractual notice, collections, diversify *named* pipeline. "Build a diversified base" with no owner is a fail.
7. **Do not name the customer in an external memo** if disclosure rules or NDAs say not to — use Customer A internally as filings do, unless they already public.
8. **One ASK.** De-risk X / accept concentration / change terms. Owner, date.
9. **Do not invent a second customer.** Hole the book.
10. **One page.**

## Intake

Refuse a FOR-SENDING page if revenue-by-customer *and* the decision (accept vs de-risk) are both missing. Two load-bearing holes → issues list.

1. **Period** (L12M / last quarter / YTD) and total revenue
2. **Top-N names, $ , %** (and AR if material)
3. **Contract end / notice / renewal dates** for anyone ≥10%
4. **What we will do this quarter** if the finding holds
5. **Who has the D** on accept vs de-risk
6. **External vs internal** page (names allowed?)

## Workflow

1. Rank customers by revenue; flag ≥10% and top 5 cumulative %.
2. Add AR %, contribution if known, renewal dates.
3. Stress: lose #1, lose top 2 — remaining run-rate vs floor.
4. This-quarter actions only. ASK.

## Output shape

```markdown
# Customer concentration — [entity] — [period] — [date]

ASK: [accept / de-risk] — [owner] to [action] by [date]
Book: revenue [$]   Top-5: [%]   Anyone ≥10%: [names or A/B]

## Top N
| # | Customer | Rev $ | Rev % | AR % | CM$ / % | Renewal / notice | If they leave |
|---|---|---|---|---|---|---|---|
| 1 | | | | | | | |

## Stress
- Lose #1: remaining run-rate [$]  vs opex floor [$]
- Lose top 2: …

## This quarter (only)
| Action | Owner | Date | How we will know |
|---|---|---|---|
| | | | |

## What we will not do
- Discount the whale to "save" a bad unit
- Pretend pipeline logos are revenue

## Disclosure / names
Internal names: yes/no   External: Customer A style unless already public
```

## QA (must pass)

1. Period and total revenue named.
2. Top-N table with %; ≥10% flagged or "none ≥10%, top-5 = X%".
3. AR % if AR is material, or explicit "AR not concentrated".
4. Stress: lose #1.
5. This-quarter actions with owners and dates — not a 3-year slogan.
6. One ASK.
7. Common-control grouping considered or hole.
8. No invented customers.
9. Not unit-economics of the product, not a QBR script.
10. Names policy stated.

If 1, 2, 5, or 6 fail: do not ship.

## Escalate / stop

- Going-concern if #1 leaves this quarter → [Cash Runway](../../management/cash-runway/SKILL.md) + principal; this page is the exhibit.
- Accounting disclosure wording for a 10-K → controller / counsel; we provide the math.
- They want a QBR to "save the whale" — [QBR](../../management/qbr/SKILL.md) as the meeting; this page is the risk.

## Related

- [Unit Economics](../../strategy/unit-economics/SKILL.md) — whether the whale *should* exist
- [QBR](../../management/qbr/SKILL.md) — the sitting with one customer
- [Cash Runway](../../management/cash-runway/SKILL.md) — collections if AR is the hole
- [Win Loss](../../strategy/win-loss/SKILL.md) — if concentration is about to become a lost deal
- [Executive Board Memo](../../management/executive-board-memo/SKILL.md) — if the board must minute acceptance of the risk
