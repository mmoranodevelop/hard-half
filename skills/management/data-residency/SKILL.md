---
name: data-residency
description: >-
  Use when customer data location must be checked against contracts: gap map,
  remediation, one ASK. NOT for trust-pack, not data-reconciliation.
license: MIT
---

# Data Residency

**Data residency gap map — one page** — where customer / personal data actually lives (regions, processors, subprocessors) vs what contracts / DPAs / customer promises say; gap class; remediation; one ASK. Default: SaaS / cloud product with EU or regulated customers; same spine for internal employee data when contracts bind it.

Method origin: GDPR Art. 3 territorial scope (EDPB Guidelines 3/2018: establishment + targeting) + Chapter V transfer regime (residency is operational; "transfer" is legal) + AWS / Azure public region & EU Data Boundary docs (region choice ≠ automatic legal adequacy) + enterprise DPA patterns (processor locations, subprocessor lists, SCCs / adequacy). Reconstruct the operator gap map. Do not practise law.

If they want a sovereignty lecture: one paragraph then produce or stop.

## When to use

- A customer or prospect asks "where does our data live?" and nobody has a current map
- Contract / DPA / trust page promises a region; infra may differ (backups, support, AI, logs)
- Expanding to EU / UK / sector-regulated customers and residency is undefined
- Subprocessor or region change landed without a gap check
- Board / CISO wants gaps ranked with remediation owners

## When not to use

- Sales trust collateral / security questionnaire pack — [Trust Pack](../../documents/trust-pack/SKILL.md)
- Matching rows across two systems / CSVs — [Data Reconciliation](../../finance/data-reconciliation/SKILL.md)
- Staff AI prompt policy — [AI Ops Policy](../../management/ai-ops-policy/SKILL.md)
- Vendor commercial SOW only — [Vendor SOW](../../management/vendor-sow/SKILL.md) (attach this map)
- Hour-by-hour cutover of a migration — [Cutover Plan](../../project/cutover-plan/SKILL.md)

If there is no **named data class + contract promise** (or they refuse to name either), stop.

## Modes

| Mode | When | Output |
|---|---|---|
| **produce** | Default. Systems + contract claims exist | Gap map + remediation + ASK |
| **redline** | They pasted "we are GDPR compliant / EU-only" | Force region/processor evidence; kill slogan |
| **refuse** | No systems inventory, or "just say EU" | Issues list. Stop |

## Hard rules

1. **Promise vs reality.** Every row: what the contract / DPA / public trust page claims vs where data actually sits (primary, replicas, backups, logs, support, AI/RAG).
2. **Name processors and regions.** Cloud account ≠ region. EU region on a US-parent provider is still a fact to disclose; do not invent "sovereign" (AWS/Azure public docs: residency commitments are product- and config-specific).
3. **Classify gaps:** Match | Config-gap (fixable) | Contract-gap (promise exceeds reality) | Transfer-gap (Chapter V / SCC / TIA needed) | Unknown.
4. **Subprocessors on the page.** Or HOLE. Silent subprocessors are a Contract-gap.
5. **Remediation is owner + verb + date** — move region, tighten config (e.g. EU Data Boundary), amend DPA, stop feature, disclose.
6. **One ASK** — named owner to accept residual risk or fund remediation by a date.
7. **Never invent** adequacy, fine risk $, or "100% EU". Holes stay holes.
8. **Not legal advice.** Counsel owns transfer impact assessment / SCC choice; this page owns the inventory and gaps.
9. **One page** (+ optional system annex). Not a trust brochure.

## Intake

If **two** of 1–4 are missing after one round: issues list, not a fake map.

1. Named product / environment and customer segment in scope — load-bearing
2. Contract / DPA / trust-page residency claims (quote or cite) — load-bearing
3. Systems that store or process the data (prod, backup, logs, support, AI) — load-bearing
4. Cloud providers + regions actually configured — load-bearing
5. Subprocessor list (current) or "none maintained"
6. Cross-border access patterns (support, admin, affiliates)
7. Who owns remediation budget / customer disclosure
8. Deadline (deal, audit, DPA renewal)

## Output shape

```
DATA RESIDENCY GAP MAP  —  NOT LEGAL ADVICE  |  [product]  |  as-of: [date]
ASK: [owner] to [accept residual / fund remediation / amend DPA / disclose] by [date]
Customer segment: [ ]     Governing claims: [DPA § / trust page / MSA]

PROMISE
Claimed residency / transfer basis: [EU-only / region X / SCC / adequacy / HOLE]

REALITY (inventory)
| Data class | System | Provider | Region(s) | Replica/backup | Access from | Gap class |
| Customer PII | prod DB | AWS/Azure/... | [ ] | [ ] | [support geo] | Match/Config/Contract/Transfer/Unknown |
| Logs / support |  |  |  |  |  |  |
| AI/RAG prompts |  |  |  |  |  |  |

SUBPROCESSORS: [list or HOLE]

REMEDIATION
| Gap | Action | Owner | Date | Residual if deferred |
| 1 |  |  |  |  |

NOT THIS PAGE
Sales trust collateral → trust-pack    Row matching → data-reconciliation
Staff AI use rules → ai-ops-policy    Migration hours → cutover-plan

Holes: [ ]
```

## QA (must pass)

1. Promise quoted/cited and reality inventory present.
2. Gap classes used; no silent "we're fine".
3. Subprocessors listed or HOLE.
4. Remediation with owners/dates or explicit accept-residual.
5. One ASK with owner, verb, date.
6. No invented sovereignty / adequacy / fine $.
7. "Not legal advice" on page.
8. Not a trust pack, not a recon.

If 1, 2, 5, or 6 fail: do not ship.

## Escalate / stop

- Active regulator inquiry or breach → counsel + incident path; this map is exhibit only.
- They want you to rewrite the DPA → counsel; list required amendments only.
- "Just put EU on the website" with US-only reality → refuse; Contract-gap.
- Feature that cannot meet the promise → stop feature or amend promise; do not hide.

## Related

- [Trust Pack](../../documents/trust-pack/SKILL.md) — sales collateral; this is the internal gap map that must be true first
- [Data Reconciliation](../../finance/data-reconciliation/SKILL.md) — row match across systems; this is location vs contract
- [AI Ops Policy](../../management/ai-ops-policy/SKILL.md) — what staff may paste; residency constrains tools
- [Vendor SOW](../../management/vendor-sow/SKILL.md) — processor commercial terms
- [Vendor Scorecard](../../management/vendor-scorecard/SKILL.md) — score processors; residency is one criterion
