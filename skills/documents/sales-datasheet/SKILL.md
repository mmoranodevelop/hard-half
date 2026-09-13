---
name: sales-datasheet
description: >-
  Use when shipping a 1–2 page product/offer sheet: outcome H1, who, Three
  Reasons, use cases, sourced proof, how-it-works caption, features grid, one
  CTA. NOT for pricing-one-pager, not social-carousel, not unit-economics.
license: MIT
---

# Sales Datasheet

**1–2 page offer sheet** a buyer keeps: outcome H1 (not the product name), who, Three Reasons, 3–6 jobs, one footnoted proof, architecture caption a specialist can reject, capability grid, one CTA. Default: venture SaaS / program offer. Chrome from [Document Kit](../../documents/document-kit/SKILL.md) (MM optional or consulting-neutral).

Method origin: Salesforce public datasheet spine (Privacy Center Apr 2026; Security Center; Shield Data Detect; Financial Services Cloud; Automotive FY25) + Trailhead CCC BLUF + Force Management Command of the Message (training vendor) Required Capabilities. Steal structure, not Cloud blue / Salesforce Sans / Lightning.

If they want a datasheet lecture: one paragraph, then produce or stop.

## When to use

- Leave-behind after a first meeting, or a downloadable offer sheet
- A named offer needs a buyer-centric page, not a feature dump
- AppExchange-style quality: benefit-first, scoped dependencies, countable capabilities

## When not to use

- Price card / SKU grid as the point — [Pricing One-Pager](../../strategy/pricing-one-pager/SKILL.md)
- LinkedIn/IG 4:5 panels — [Social Carousel](../../branding/social-carousel/SKILL.md)
- Contribution of one more unit — [Unit Economics](../../strategy/unit-economics/SKILL.md)
- 4–8 pp industry/persona story — [Solution Brief](../../documents/solution-brief/SKILL.md)
- Named-customer FILE with commercial — [Sales Proposal](../../documents/sales-proposal/SKILL.md)
- CISO keep-sheet for the platform — [Trust Pack](../../documents/trust-pack/SKILL.md)
- Permissioned customer *story* as the artifact — [Proof Story](../../comms/proof-story/SKILL.md)
- McKinsey leave-behind — [Consulting Deck](../../documents/consulting-deck/SKILL.md)

## Modes

| Mode | When | Output |
|---|---|---|
| **produce** | Default. Who + offer exist | 1–2 page datasheet |
| **redline** | Brochure / product-name H1 / unsourced % | Force outcome H1; HOLE or delete numbers; one CTA |
| **refuse** | No who, or they want a price list / carousel / 5+ pp | Issues list + route |

## Hard rules

1. **H1 is the outcome for a named who.** Product name is the eyebrow or the last clause. "Acme Cloud" as H1 is a brochure — refuse that shape.
2. **Three Reasons** = Required Capabilities (Force Management, training vendor), not the SKU list. Each maps to a buyer job.
3. **One proof, sourced.** Named customer + metric + source, or named study. Unsourced "50% productivity" / "Customers Reported 20%" with no study → HOLE or delete. Nucleus Research (vendor) ROI is an analogue with the customer named, not a promise.
4. **How it works** is caption-level architecture a CISO/architect can reject. Boxes + data flow, not a slogan.
5. **Features grid:** name + one sentence of *behavior*. Asterisk add-ons. Not-GA gets the unreleased disclaimer — do not sell vaporware as GA.
6. **One CTA.** Webpage / demo / talk-to-expert. Not pricing. Not five next steps.
7. **Gartner / Forrester: reprint or silence.** No fake Magic Quadrant / Wave. No "No. 1 / winner / best-in-class."
8. **Clock is 1–2 pages letter.** 5 pp persona chapters → solution-brief. 12–27 pp guide → not this slug.
9. **Kit, not clone.** [Document Kit](../../documents/document-kit/SKILL.md). Never Cloud blue, Salesforce Sans, Lightning illustrations, Trailhead characters.

## Intake

If **who** and **offer** are both missing after one round: issues list, not a fake sheet.

1. Who (role or industry) + job they hire this for (load-bearing)
2. Offer name + what is in vs add-on vs not-GA (load-bearing)
3. Three Required Capabilities they actually need — or hole
4. One proof with source, or "none — HOLE the metric"
5. Architecture caption facts (where data lives, what the buyer configures)
6. CTA (one URL or meeting type) + owner / date to ship
7. Kit: MM / consulting-neutral / client (default consulting-neutral)

## Output shape

Fill `assets/artifact.md`. Spine:

```
[eyebrow: offer]
H1: [outcome for who] [with Offer — optional last clause]
Who + problem (one short block; numbers footnoted)
THREE REASONS  |  USE CASES (3–6 jobs)
PROOF: [metric] — [source]   or [HOLE]
HOW IT WORKS: [caption a specialist can reject]
FEATURES (name + behavior; *add-on; †not GA)
CTA: [one]     Owner/date: [ ]     Kit: [ ]
Holes: [ ]
```

## QA (must pass)

1. H1 is an outcome for a named who; product is not the H1.
2. Three Reasons exist; use cases are jobs.
3. Every number has a source or is `[HOLE]`. No unsourced %.
4. Architecture caption is rejectable. Add-ons / not-GA asterisked.
5. One CTA. ASK-equivalent: CTA + owner + date to ship.
6. 1–2 pages. Not a price card, carousel, unit-econ, brief, or proposal.
7. No fake MQ/Wave. No Cloud-blue clone.

If 1, 3, 5, or 6 fail: do not ship.

## Escalate / stop

- Product name as H1 and they will not change it → refuse the brochure.
- Unsourced productivity % they insist on keeping → delete the number or stop.
- They want the price table to *be* the page → [Pricing One-Pager](../../strategy/pricing-one-pager/SKILL.md).
- Industry persona chapters stretching past 2 pp → [Solution Brief](../../documents/solution-brief/SKILL.md).

## Visuals

Apply [Document Kit](../../documents/document-kit/SKILL.md) — MM optional or consulting-neutral. Letter, 1–2 pages. Never Cloud blue, Salesforce Sans, Lightning illustrations, or Trailhead characters. After produce: ship the **file**; this is not a talk spine.

## Related

- [Document Kit](../../documents/document-kit/SKILL.md) — chrome (MM optional or consulting-neutral)
- [Solution Brief](../../documents/solution-brief/SKILL.md) — 4–8 pp industry/persona
- [Sales Proposal](../../documents/sales-proposal/SKILL.md) — named-customer FILE
- [Trust Pack](../../documents/trust-pack/SKILL.md) — CISO keep-sheet
- [Proof Story](../../comms/proof-story/SKILL.md) — the story is the artifact; here proof is one callout
- [Pricing One-Pager](../../strategy/pricing-one-pager/SKILL.md) / [Social Carousel](../../branding/social-carousel/SKILL.md) / [Unit Economics](../../strategy/unit-economics/SKILL.md)
