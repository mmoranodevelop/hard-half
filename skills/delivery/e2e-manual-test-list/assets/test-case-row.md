# Test inventory row template

Use one row per test. Keep steps high-level and actionable (not UI micro-scripts unless the AC demands it). Expected results must quote or paraphrase **documented** behaviour — else mark unclear.

## Columns

| Column | Required | Notes |
|---|---|---|
| **ID** | Yes | Stable id, e.g. `E2E-014` or `SMOKE-003` |
| **Title** | Yes | Verb + object + outcome, ≤12 words |
| **Priority** | Yes | P0 / P1 / P2 / P3 (from risk: impact × likelihood / change freq) |
| **Type** | Yes | `happy` \| `alt` \| `exception` \| `neg` \| `regression` \| `smoke` \| `uat` |
| **Persona / role** | Yes | Who executes / whose journey |
| **Preconditions** | Yes | Env, data fixtures, prior state; shared login as pointer |
| **Steps** | Yes | Numbered, high-level, executable by a human |
| **Expected result** | Yes | Observable; from AC / PRD / mockup — or `[UNCLEAR — need AC]` |
| **Risk** | Yes | Impact H/M/L × Likelihood H/M/L → score note |
| **Trace** | Yes | Story/AC id, Figma frame, API contract section — or hole |
| **Pack** | Yes | `smoke-p0` \| `full-e2e` \| `uat-candidate` (can be multi) |
| **Automation later?** | No | `Y/N/maybe` — flag only; no scripts here |
| **Notes / gaps** | No | Data holes, env unknowns |

## Example row (shape only — do not copy as real product behaviour)

| ID | Title | Pri | Type | Persona | Preconditions | Steps | Expected | Risk | Trace | Pack |
|---|---|---|---|---|---|---|---|---|---|---|
| E2E-001 | Buyer completes checkout with saved card | P0 | happy | Buyer | Staging; user with saved card; stocked SKU | 1. Open cart 2. Checkout 3. Pay with saved card 4. Confirm order | Order confirmation page; order id; email receipt per AC-12 | H×H | AC-12; Fig checkout-03 | smoke-p0, full-e2e, uat-candidate |
| E2E-018 | Checkout rejects expired card | P1 | neg | Buyer | Staging; expired test card fixture | 1–3 as above with expired card | Declined message per AC-19; no order created | H×M | AC-19 | full-e2e |
| E2E-042 | Refund path after partial ship | P2 | alt | Support | [UNCLEAR — need AC for partial-ship refund] | — | `[UNCLEAR — need AC]` | M×M | — | full-e2e |

## Pack filters

- **Smoke / P0:** all `Pack` contains `smoke-p0` OR Priority = P0 happy/critical alt.
- **Full E2E:** entire inventory minus explicitly deferred.
- **UAT candidate:** business-observable journeys tagged `uat-candidate` (happy + key alt); strip deep neg/tech unless acceptor requires them.
