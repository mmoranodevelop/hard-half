---
name: trust-pack
description: >-
  Use when producing a security/compliance/architecture one-pager a CISO can
  keep: SPARC-shaped, named audits with scope/date/exclusions or HOLE. NOT for
  control-handover, not prd-spec. Architecture a CISO can reject.
license: MIT
---

# Trust Pack

**One-page CISO keep-sheet** (2 if architecture needs a reverse): named service + infrastructure, rejectable architecture, shared responsibility, certifications with scope/date/exclusions, what is NOT covered, customer-configurable controls, how to verify. Default: the platform/offer the buyer is putting data into. Chrome from [Document Kit](../../documents/document-kit/SKILL.md) (MM optional or consulting-neutral). Do not steal Trust-site chrome.

Method origin: Salesforce SPARC (Security, Privacy and Architecture; first-party PDF published 24 Jul 2026, 15 pp — the *source*, not the leave-behind) + trust.salesforce.com shared-responsibility language + Shield/Security Center/Privacy Center as *product* trust features (those sheets are [Sales Datasheet](../../documents/sales-datasheet/SKILL.md) when the job is "buy this SKU"). SPARC names audits **and** services excluded from each.

If they want a SPARC/SOC lecture: one paragraph, then produce or stop.

## When to use

- CISO / security reviewer asked for a keep-sheet they can file
- Security questionnaire is coming; they need architecture + certs *this page*, not a 40-page matrix
- Buyer is putting data into the offer even if no security SKU is sold today
- Cert claim would otherwise ship without scope, date, or exclusions

## When not to use

- M&A control register (bank, IdP, repos) — [Control Handover](../../ma/control-handover/SKILL.md)
- Builder spec / control PRD — [PRD Spec](../../documents/prd-spec/SKILL.md)
- Buy-this-SKU security product sheet — [Sales Datasheet](../../documents/sales-datasheet/SKILL.md)
- BAA / DPA / legal instrument — [Vendor SOW](../../management/vendor-sow/SKILL.md) + counsel
- McKinsey leave-behind — [Consulting Deck](../../documents/consulting-deck/SKILL.md)
- Wholesale paste of SPARC or a SOC report — point to the live document; do not rewrite it (copyright + wrong clock)

## Modes

| Mode | When | Output |
|---|---|---|
| **produce** | Default. Service + infrastructure known or HOLE | 1-page keep-sheet |
| **redline** | "We are ISO certified" with no scope/date; "bank-grade" architecture | Force named certs or HOLE; rejectable architecture |
| **refuse** | Invented certs; HIPAA/PCI claimed for an excluded service; 40-page control matrix | Issues list + route |

## Hard rules

1. **Scope first.** Named service(s) + infrastructure (first-party / named public cloud / unknown). If infrastructure is unknown, **HOLE** — do not imply coverage.
2. **Architecture a CISO can reject.** Multitenant vs single-tenant, logical segregation, residency pointer, encryption in transit/at rest, key management *if claimed*, auth (SSO/MFA), logging/SIEM, subprocessors pointer. Caption + 6–10 controls. "Bank-grade," "zero-trust" as adjective, "encrypted" with no key story → fail.
3. **Shared responsibility.** Customer-configurable controls belong on the page. Otherwise the CISO assumes you run their org.
4. **Certifications, current, scoped.** Pattern: `ISO 27001 (scope: {services}, date: {YYYY-MM}, exclusions: {list or "none named"})`. No scope/date → **HOLE**, not a claim. Do not invent certifications.
5. **What is NOT covered.** SPARC Certification Excluded Services pattern. Do not claim HIPAA / PCI / FedRAMP for a service the source excludes. PHI/BAA only if the BAA/service is in scope.
6. **How to verify.** Link to the live compliance/status page + document date. Transparency is part of the artifact.
7. **AI / subprocessors caveat** if the offer uses generative AI or third-party functionality.
8. **One page** (2 if architecture reverse). SPARC 15–17 pp is the source. A 40-page matrix is control-handover.
9. **Kit, not clone.** Never Cloud blue, Salesforce Sans, Lightning, Trust-site chrome.

## Intake

If **service** and **any current cert with scope/date (or an explicit HOLE)** are both missing after one round: issues list, not a fake ISO claim.

1. Named service(s) + infrastructure (load-bearing)
2. Architecture facts a CISO could reject (tenancy, residency, keys, auth, logs)
3. Certifications: name / scope / date / exclusions — or HOLE (load-bearing with 1)
4. Customer-configurable controls vs vendor-operated
5. Excluded services / claims we must not make
6. Verify-at URL + document as-of date
7. Generative AI / subprocessors? Kit (default consulting-neutral)

## Output shape

Fill `assets/artifact.md`. Spine:

```
TRUST PACK  |  [service]  |  infra: [ ] or [HOLE]  |  as-of [date]
ARCHITECTURE (CISO-rejectable caption + 6–10 controls)
SHARED RESPONSIBILITY  |  customer-configurable: [ ]
CERTS: name | scope | date | exclusions | or HOLE
NOT COVERED: [ ]
VERIFY: [URL]  [document date]
AI / subprocessors: [ ] or N/A
ASK: CISO files / rejects by [date]
Holes: [ ]
```

## QA (must pass)

1. Service named. Infrastructure named or `[HOLE]`.
2. Architecture is specific enough to reject. No "bank-grade" as a substitute.
3. Every cert has scope + date + exclusions, or is `[HOLE]`. No invented certs.
4. Shared-responsibility split present. Verify link + document date.
5. Not a control-handover, PRD, SOC paste, or security datasheet.
6. ASK: CISO review by date. One page (or 2).
7. No Cloud-blue / Trust-site clone.

If 1, 2, 3, or 5 fail: do not ship.

## Escalate / stop

- "We are ISO / SOC 2 certified" with no scope/date and they will not HOLE it → stop.
- Claim HIPAA/PCI/FedRAMP for an excluded service → refuse.
- They want the SOC report rewritten into this page → hand the **link**; do not paste.
- M&A access register → [Control Handover](../../ma/control-handover/SKILL.md).

## Visuals

Apply [Document Kit](../../documents/document-kit/SKILL.md) — MM optional or consulting-neutral. One page (or 2). Never Cloud blue, Salesforce Sans, Lightning, or Trust-site chrome. After produce: CISO keeps the **file**; point at SPARC/SOC — do not paste them.

## Related

- [Control Handover](../../ma/control-handover/SKILL.md) — M&A control register
- [PRD Spec](../../documents/prd-spec/SKILL.md) — builder spec
- [Sales Datasheet](../../documents/sales-datasheet/SKILL.md) — Shield/Privacy Center *product* sheets
- [Vendor SOW](../../management/vendor-sow/SKILL.md) — BAA/DPA are legal instruments
- [Document Kit](../../documents/document-kit/SKILL.md) — chrome (not Trust-site clone)
