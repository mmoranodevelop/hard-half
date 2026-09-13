---
name: sales-proposal
description: >-
  Use when producing a customer-named proposal FILE: cover, this-customer
  situation, recommended solution, commercial, assumptions, next step. Quote/CPQ
  is a mode (commercial appendix), not a separate skill. Not proposal-narrative,
  not vendor-sow, not bid-no-bid, not mutual-action-plan.
license: MIT
---

# Sales Proposal

**Proposal FILE named to {Customer}:** cover, situation from discovery, recommended solution mapped to capabilities they accepted, one analogue proof, commercial (or bound quote), assumptions / add-ons / not-GA, one next step. Default: venture / mid-market named deal. Chrome from [Document Kit](../../documents/document-kit/SKILL.md) (MM optional or consulting-neutral).

Method origin: Trailhead *Write a Sales Proposal* (challenges *they* solve, solutions *you* provide, pricing, timeline, next steps) + Trailhead CPQ quote templates (Prepared For / Prepared By; merge fields bind *this* quote) + Force Management Command of the Message (training vendor) Before Scenario → Required Capabilities. MEDDIC on Trailhead is **inspection**, not the genre. A search-replace-logo file is not a proposal.

If they want a proposal lecture: one paragraph, then produce or stop. Do not write `quote-pack` — CPQ lives here as **commercial-quote**.

## When to use

- This account will accept or e-sign a FILE
- Discovery notes exist: confirmed challenges, economic buyer, champion
- Commercial must sit *with* situation, not as a naked price card

## When not to use

- Comms spine / corporate narrative — [Proposal Narrative](../../comms/proposal-narrative/SKILL.md)
- SOW / acceptance / RACI as the whole file — [Vendor SOW](../../management/vendor-sow/SKILL.md)
- Internal go/no-go — [Bid No-Bid](../../commercial/bid-no-bid/SKILL.md)
- Joint close plan without commercial — [Mutual Action Plan](../../accounts/mutual-action-plan/SKILL.md)
- Discount exception / non-standard terms decision — [Deal Desk](../../commercial/deal-desk/SKILL.md)
- Industry brief with no named logo — [Solution Brief](../../documents/solution-brief/SKILL.md)
- Offer sheet — [Sales Datasheet](../../documents/sales-datasheet/SKILL.md)
- ROI model as the artifact — [Value Eng](../../documents/value-eng/SKILL.md) (annex, not the proposal)
- Price card without situation — [Pricing One-Pager](../../strategy/pricing-one-pager/SKILL.md)

## Modes

| Mode | When | Output |
|---|---|---|
| **produce** | Default. This-customer situation exists | Named proposal FILE |
| **commercial-quote** | Line items / CPQ exist | Same FILE + quote appendix (never quote-only) |
| **redline** | Logo-swap brochure or SOW-as-proposal | Force named situation; point SOW out |
| **refuse** | Situation still works for another logo; quote-only; they want SOW/MAP/bid memo | Issues list + route |

## Hard rules

1. **Named to THIS customer.** Cover: customer, offer, date, Prepared For / Prepared By. If the situation paragraph still works after a logo swap, it is a datasheet/brief — refuse.
2. **Situation from discovery.** Confirmed challenges, Before Scenario + negative consequences, who we spoke to. Match their lingo (Trailhead CCC). MEDDIC letters are facts on the page (pain, EB, champion), not a scorecard dump.
3. **Recommended solution** = Required Capabilities they agreed, then how the offer meets them. Product last, 1:1.
4. **One analogue proof**, permissioned, sourced, aligned to *this* situation. Unsourced ROI inside the proposal → attach [Value Eng](../../documents/value-eng/SKILL.md) with customer inputs or HOLE the number.
5. **Commercial** is in the FILE: what they buy, term, price, payment. **commercial-quote** binds a CPQ-style appendix (line items, terms, signature). Quote-only PDF is not this slug.
6. **Assumptions:** in vs add-on vs customer-owned vs not-GA. Unreleased disclaimer when true.
7. **One next step:** signature / e-sign / workshop — owner + date. T&Cs pointer, not SOW body.
8. **Length:** 4–8 pages + quote appendix. Trailhead floor is 2–3; commercial + assumptions expand. Past ~12 pp it is becoming an SOW or RFP binder.
9. **Gartner / Forrester: reprint or silence.** No fake MQ/Wave. No "No. 1 / winner."
10. **Kit, not clone.** Never Cloud blue, Salesforce Sans, Lightning.

## Intake

If **customer name** and **this-customer situation** (discovery notes, not a generic industry paragraph) are both missing after one round: issues list. Do not emit a brochure.

1. Customer legal name + Prepared For (load-bearing)
2. Confirmed challenges / Before Scenario / who we spoke to (load-bearing)
3. Required Capabilities they accepted + offer map
4. Commercial: SKUs / term / price — or "appendix later, still need a number or HOLE"
5. Add-ons / customer-owned / not-GA
6. One analogue proof with source — or hole
7. Next step (who signs, date) + kit (default consulting-neutral)

## Output shape

Fill `assets/artifact.md`. Spine:

```
COVER: Proposal for [Customer]  |  [offer]  |  [date]
        Prepared For / Prepared By
SITUATION (this customer — fails a logo swap)
RECOMMENDED SOLUTION (capabilities they accepted → offer 1:1)
PROOF (analogue + source) or [HOLE]
COMMERCIAL (or bound quote appendix)
ASSUMPTIONS / add-ons / not-GA / customer-owned
TIMELINE  |  NEXT STEP: [who] [date]  |  T&Cs: pointer
Kit: [ ]   Holes: [ ]
```

## QA (must pass)

1. Customer named on cover. Situation fails a logo-swap test.
2. Recommended solution maps to capabilities they accepted.
3. Commercial present (or labelled HOLE with a date to bind the quote). Next step: who + date.
4. Every number sourced or `[HOLE]`. No unsourced ROI.
5. Not a narrative spine, SOW, bid memo, MAP, or price card.
6. 4–8 pp + optional quote appendix. No fake MQ. No Cloud-blue clone.

If 1, 3, or 5 fail: do not ship.

## Escalate / stop

- No discovery, only a product brochure → refuse; send back to discovery.
- They want quote-only / `quote-pack` → refuse; use **commercial-quote** on this FILE (situation still required).
- They want the SOW body → [Vendor SOW](../../management/vendor-sow/SKILL.md).
- Talk-track cover only → [Proposal Narrative](../../comms/proposal-narrative/SKILL.md).

## Visuals

Apply [Document Kit](../../documents/document-kit/SKILL.md) — MM optional or consulting-neutral. Letter/A4. Never Cloud blue, Salesforce Sans, or Lightning. After produce: ship the named-customer **FILE**. Talk cover lives on [Proposal Narrative](../../comms/proposal-narrative/SKILL.md).

## Related

- [Proposal Narrative](../../comms/proposal-narrative/SKILL.md) — talk cover / comms spine; this is the FILE
- [Vendor SOW](../../management/vendor-sow/SKILL.md) / [Bid No-Bid](../../commercial/bid-no-bid/SKILL.md) / [Mutual Action Plan](../../accounts/mutual-action-plan/SKILL.md) / [Deal Desk](../../commercial/deal-desk/SKILL.md)
- [Solution Brief](../../documents/solution-brief/SKILL.md) / [Sales Datasheet](../../documents/sales-datasheet/SKILL.md)
- [Value Eng](../../documents/value-eng/SKILL.md) — ROI annex with customer inputs
- [Document Kit](../../documents/document-kit/SKILL.md) — chrome
