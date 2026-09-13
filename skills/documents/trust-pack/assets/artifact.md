# TRUST PACK — [service / offer] — as-of [date]
Kit: consulting-neutral / MM / client  |  One page (2 if architecture reverse)
CISO keep-sheet. SPARC-shaped: named audits + exclusions. Not a SOC paste. Not Trust-site chrome.

Infra unknown → HOLE, do not imply coverage. "We are ISO certified" with no scope/date → HOLE, not a claim.

## Scope

- **Service(s):** [named]
- **Infrastructure:** first-party / named public cloud / **[HOLE]**
- **Data the customer would put here:** [categories — no PHI claim unless BAA/service in scope]

## Architecture (a CISO can reject)

Caption: [multitenant vs single-tenant; logical segregation; residency pointer; in-transit / at-rest encryption; key management if claimed; SSO/MFA; logging/SIEM; subprocessors pointer].

| Control | How it works (specific enough to reject) | Vendor-operated / customer-configurable |
|---|---|---|
| Tenancy / segregation | [ ] | [ ] |
| Residency | [ ] or [HOLE] | [ ] |
| Encryption in transit | [TLS version / standard] | [ ] |
| Encryption at rest + keys | [who holds keys — or HOLE] | [ ] |
| Auth (SSO / MFA) | [ ] | customer-configurable |
| Logging / SIEM export | [ ] | [ ] |
| Subprocessors | [pointer URL] | [ ] |
| Backup / DR | [RPO/RTO if claimed, else HOLE] | [ ] |
| Return / deletion of customer data | [ ] | [ ] |
| Incident notify | [window if claimed, else HOLE] | [ ] |

Banned substitutes: "bank-grade," "zero-trust" as adjective, "encrypted" with no key story.

## Shared responsibility

Customer must configure: [MFA, SSO, encryption policies, event monitoring, retention, access reviews].
Vendor operates: [infra, physical, listed platform controls].
If customer-configurable controls are missing from this page, the CISO will assume we run their org — fail.

## Certifications (current, scoped)

| Name | Scope (services) | Date (YYYY-MM) | Exclusions | Status |
|---|---|---|---|---|
| ISO 27001 | [ ] or HOLE | [ ] or HOLE | [list or "none named"] | claim / **HOLE** |
| SOC 2 | [ ] | [ ] | [ ] | claim / **HOLE** |
| [PCI AOC / HIPAA-BAA / FedRAMP / other] | [ ] | [ ] | [ ] | claim / **HOLE** — do not claim if excluded |

Pattern: `ISO 27001 (scope: {services}, date: {YYYY-MM}, exclusions: {list or "none named"})`.
Invented certs → refuse. No scope/date → **HOLE**.

## What is NOT covered

- [Services / SKUs excluded from the named audits]
- [HIPAA / PCI / FedRAMP — only if the source excludes them, say so]
- Generative AI / third-party functionality: [in / excluded / HOLE / N/A]

## How to verify

- Compliance / SPARC / status URL: [ ]
- Document date: [YYYY-MM-DD]
- Do not paste the SOC report or SPARC wholesale (copyright + wrong clock). Point.

## ASK

CISO files or rejects this keep-sheet by [date]. Owner: [ ]. Next: questionnaire / BAA via counsel if in scope.

## Not this page

Control-handover (M&A register). PRD-spec (builder). Sales-datasheet (buy-this-SKU Shield/Privacy Center). Vendor-sow (BAA/DPA). 40-page control matrix.

## Holes

- [ ]
