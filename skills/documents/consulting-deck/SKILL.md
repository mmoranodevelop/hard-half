---
name: consulting-deck
description: >-
  Use when producing a strategy-consultant leave-behind .pptx: Minto
  pyramid/SCQ, action titles as takeaway sentences, one exhibit per slide, exec
  summary first, appendix out of the room. Not TED / Presentation Zen, not
  social-carousel, not a board memo or SteerCo one-pager.
license: MIT
---

# Consulting Deck

**Real .pptx** (or title-only storyboard + python-pptx render) at strategy-consultant **structure**: governing thought first, action titles, one exhibit, source + page, ASK. Visuals from [Document Kit](../../documents/document-kit/SKILL.md). 16:9 default. The slide *is* the leave-behind — a reader not in the room recovers the argument from titles + exhibits.

Method origin: Minto pyramid + SCQ (barbaraminto.com); MECE (McKinsey Alumni 2018 interview of Minto); action titles = takeaway sentences (alumni/vendor, matches Minto headings-are-claims). Charts: Tufte data-ink; Datawrapper dual-axis warning; think-cell = vendor.

If they want a pyramid lecture: one paragraph then produce or stop.

## When to use

- Strategy / SteerCo *slide sitting* they will leave behind
- Board *presentation* of an already-written paper (the legal artifact stays the memo)
- Ghost deck: action titles only, then render

## When not to use

- Argument as email/Slack/verbal — [Pyramid Principle](../../writing/pyramid-principle/SKILL.md)
- Fiduciary board paper — [Executive Board Memo](../../management/executive-board-memo/SKILL.md)
- SteerCo **one-pager** (≤3 decisions) — [Steering Pack](../../project/steering-pack/SKILL.md)
- Staff-to-principal page — [Principal Brief](../../writing/principal-brief/SKILL.md)
- Raise **process** page — [Fundraising One-Pager](../../strategy/fundraising-one-pager/SKILL.md); a decision-style pitch may use this skill, not TED
- Working-backwards prose — [PR/FAQ](../../strategy/pr-faq/SKILL.md)
- LinkedIn 4:5 — [Social Carousel](../../branding/social-carousel/SKILL.md)
- Narrative pre-read pack (comms) — not this leave-behind
- Presentation Zen / TED glance-media — refuse (Reynolds: best slides are useless without the speaker; consultants ship a document)

## Modes

| Mode | When | Output |
|---|---|---|
| **produce** | Default. Question + answer exist | Ghost titles → .pptx + ASK |
| **redline** | Pasted pack / “McKinsey template” | Force action titles; kill TED/clone; move appendix |
| **refuse** | No answer; stolen master; TED pack as the deliverable | Issues list. Stop |

## Hard rules

1. **Answer exists** before pyramid-dressing. Fishing trip → refuse.
2. **SCQA on the exec summary** (Minto public is SCQ; Resolution = Answer + ASK). Apex is a **claim someone could disagree with**, not a topic.
3. **Action title = takeaway sentence** (alumni/vendor + Minto heading rule — not a confidential Firm guide). ≤ ~15 words, **never more than two lines**. If it does not fit, **split the slide**, do not shrink type. Title-read test: titles only recover the case. Nothing in the title unproven in the body.
4. **One exhibit, one so-what.** Market + growth + competition = three slides. Backup tables → **appendix**, labelled, ordered to the pack — not dumped into the room.
5. Anatomy: action title → subhead (units/scope/years) → one exhibit → footer **source + page n/n**. Title slide is the document name, not an action title. Dividers are key-line **claims**, no charts.
6. **Visuals from document-kit.** 16:9 13.333×7.5 in. Neutral kit default; MM optional; client kit if they supplied hexes. **No stolen McKinsey/BCG/Bain master, navy+white clone, or “official McKinsey template.”**
7. Charts: data-ink, **no pies**, no 3D, no chartjunk, no rainbow-only encoding. Dual-axis **not default** — only with an explicit warning and a reason (Datawrapper); prefer two charts or small multiples. Direct labels > legends. think-cell = vendor (style file inherits kit; no gradient fills; labels are data-bound, not PowerPoint text boxes).
8. Length (vendor order-of-magnitude, not Firm law): exec update 5–10; board 10–20; strategy 20–35 + appendix. Room pack > ~30 exhibits ⇒ pyramid was not built.
9. **One ASK:** decide / do, owner, date. No ASK = a tour — do not ship.
10. No clipart, generated faces, unsourced numbers, topic titles (“Revenue”), speaker-dependent slides as the pack.

## Intake

If **question** and **answer/recommendation** are both missing after one round: issues list.

1. Decision the room must take; by when; whose logo (load-bearing)
2. Governing thought in one sentence (load-bearing)
3. Evidence you have (exhibits + sources) — or hole
4. Kit: [Document Kit](../../documents/document-kit/SKILL.md) instance, or ASK to produce one
5. Room pack vs appendix split
6. Owner of the ASK; date
7. Classification / confidential Y/N

## Output shape

Copy `assets/deck-outline.md`. Render with **python-pptx** (no stolen template). Sequence: kit + canvas → SCQA → ghost titles → exhibits → appendix → page numbers.

```
CONSULTING DECK  |  [engagement]  |  [date]  |  16:9  |  kit: [neutral / MM / client]
Classification: [ ]     Logo: [client / owner]     D on ASK: [name]

0 TITLE     [document name] — not an action title
1 EXEC      SCQA + recommendation + ASK (the screenshot page)
  S: [uncontested]  C: [why now]  Q: [question]  A: [claim]
2…          DIVIDER = key-line claim     EXHIBIT = action title + one proof + source + page
N           RECS      numbered verbs, owners, dates
            APPENDIX divider then backup (methods, extra cuts) — skip in the room

Title-read test: [pass / fail — missing slide or extra slide]
ASK: [decision]  Owner: [ ]  Date: [ ]
Holes: [ ]
```

## QA (must pass) — one-screen fail list

1. Governing thought on slide 1; SCQA; apex is a claim.
2. Every exhibit: action title (sentence, ≤2 lines) + one proof + source + page.
3. Title-read recovers the argument. No topic titles. No two messages on one slide.
4. Appendix is labelled and out of the room pack.
5. ASK + owner + date. No unsourced numbers.
6. Kit is not a McKinsey clone. Not TED/Zen. Not 4:5. No pies / 3D / dual-axis-as-default.
7. No generated faces. Canvas 16:9 unless print appendix is a **separate** file.

If 1, 2, 5, or 6 fail: do not ship.

## Escalate / stop

- “Write the McKinsey template” / stolen navy master → refuse.
- No answer yet → issues list; do not fake a pyramid.
- They want a one-page SteerCo → [Steering Pack](../../project/steering-pack/SKILL.md).
- Dual-axis as the house default → refuse; two charts.

## Related

- [Document Kit](../../documents/document-kit/SKILL.md) — tokens before render
- [Pyramid Principle](../../writing/pyramid-principle/SKILL.md) — thinking tool; this skill **makes the .pptx**
- [Executive Board Memo](../../management/executive-board-memo/SKILL.md) / [Steering Pack](../../project/steering-pack/SKILL.md) / [Principal Brief](../../writing/principal-brief/SKILL.md)
- [Social Carousel](../../branding/social-carousel/SKILL.md) / [PR/FAQ](../../strategy/pr-faq/SKILL.md) — not this leave-behind
