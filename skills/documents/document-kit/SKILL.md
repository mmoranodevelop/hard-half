---
name: document-kit
description: >-
  Use when setting colours, type, grid, lockup, and light/dark tokens for
  business files (deck, Excel, PRD, paper). Not social-carousel (4:5 LinkedIn),
  not a storyline, not a McKinsey template clone.
license: MIT
---

# Document Kit

**Token file + type + grid + lockup + light/dark** — one kit later file skills consume. Two instances, one grammar: consulting-neutral (default, client/board) or optional MM. Not a deck. Not a moodboard. Not LinkedIn 4:5.

Method origin: IBM Carbon (token = role, theme = hex); GOV.UK lockup/contrast; WCAG 2.2 AA; Microsoft 16:9 default 13.333×7.5 in; ISO 216 A4.

If they want a brand lecture: one paragraph then produce or stop.

## When to use

- First file of an engagement: colours, type, grid, mark, dark/light
- Owner-branded vs client-branded business files (same roles, different hex)
- Excel / PRD / paper that must inherit the same tokens as the deck

## When not to use

- LinkedIn 4:5 / IG / TikTok 9:16 — [Social Carousel](../../branding/social-carousel/SKILL.md)
- SCQA / argument — [Pyramid Principle](../../writing/pyramid-principle/SKILL.md) then [Consulting Deck](../../documents/consulting-deck/SKILL.md)
- Board paper — [Executive Board Memo](../../management/executive-board-memo/SKILL.md)
- SteerCo one-pager — [Steering Pack](../../project/steering-pack/SKILL.md)
- One-page raise process — [Fundraising One-Pager](../../strategy/fundraising-one-pager/SKILL.md)
- Staff one-pager — [Principal Brief](../../writing/principal-brief/SKILL.md); working-backwards prose — [PR/FAQ](../../strategy/pr-faq/SKILL.md)
- Presentation Zen / TED as the kit — refuse (consultants ship a leave-behind)

## Modes

| Mode | When | Output |
|---|---|---|
| **produce** | Default. Canvas + instance known | Token file (both themes) + lockup + grid |
| **redline** | Pasted hexes / a stolen “McKinsey template” | Force roles; kill clone; measure contrast |
| **refuse** | Moodboard with no roles; 16:9 mixed with 4:5; TED kit | Issues list. Stop |

## Hard rules

1. **Roles, not a moodboard.** Name `text`, `text-muted`, `surface`, `surface-dark`, `accent`, `border`, `source`, `error`, `success`. Never “use the red because it looks McKinsey.”
2. **Light + dark = the same roles remapped** (Carbon). Recalculate contrast. Dark is not invert-the-logo.
3. **Measure WCAG 2.2** before shipping: body 4.5:1 / large 3:1; non-text 3:1; meaning not by colour alone (1.4.1). Logotypes exempt from text contrast.
4. **Two type families max.** Body/UI = sans. Display = serif *or* the same sans at display size. Embed licensed files; do not assume Office has Instrument.
5. **One canvas per kit.** Screen default: **16:9, 13.333 × 7.5 in** (Microsoft). Print: **A4 210 × 297 mm** (ISO 216) or Letter. Never mix 16:9 and 4:5. Never mix sizes in one .pptx.
6. **Grid.** 8px mini unit (Carbon). 16:9: 12 columns, gutters 16–24 px (0.2–0.3 in), margins ≥ 0.5 in, footer band ~0.35 in. Titles and footers **do not move**.
7. **Lockup is a fixed layout** (GOV.UK pattern, not GOV.UK assets): horizontal, stacked, mark-only, mono-light, mono-dark. Clear space = a unit of the mark. No stretch, skew, shadow, recolour, rotation, or a second competing mark without a co-brand rule.
8. **Consulting-neutral must not impersonate McKinsey navy+white.** Alumni Arial/Georgia claims are hearsay, not a brand book. Body: Arial or Calibri, or embedded IBM Plex. Accent is a **swap token** — default teal `#0D5C63` light / `#5CB8BC` dark (measured 7.18:1 / 7.41:1). User may replace with client brand.
9. **Optional MM** (business files only): `#111318` `#F5F3EE` `#FF4F32`; Instrument Sans (body/UI/action title) + Instrument Serif italic (keyword, never body). **Measured:** text↔surface **16.76:1** (pass AA). Accent on dark **5.68:1** (pass AA). Accent on light **2.95:1** (**fail** AA normal, fail large 3:1, fail non-text 3:1). On light, `#FF4F32` is mark/keyword only; body stays `#111318`. Do not invent a fourth “official” MM hex. **Not** Social Carousel (different grid, 4:5, grain/glass).
10. Chart tokens: series 1–6, highlight, remainder-grey, hairline grid, axis, label, source. No 3D, no data gradients (think-cell vendor: no gradient fills). think-cell style file binds fills/fonts if present; native charts still use the series.
11. No clipart, generated faces, fake team photos. Face photos are user-supplied.
12. Holes stay holes. Without instance + canvas + owner + date: do not ship.

## Intake

If **instance** and **canvas** are both missing after one round: issues list, not a fake kit.

1. Instance: consulting-neutral / MM / client-brand (load-bearing)
2. Canvas: 16:9 exec vs A4/Letter print (load-bearing)
3. Mark files + the lockup unit, or `[no mark — type lockup]`
4. Client accent hex, or accept default teal (neutral) / MM trio
5. Dark theme required Y/N
6. Owner of the kit; date in force (load-bearing for ship)
7. Consumed by: deck / excel / prd / paper

## Output shape

Copy `assets/token-table.md`. Fill every role both themes. ASK = which instance ships.

```
DOCUMENT KIT  |  instance: [neutral / MM / client]  |  canvas: [16:9 13.333×7.5 in / A4]
Owner: [ ]  In force: [date]  Consumed by: [deck / xlsx / prd / paper]

ROLES (light | dark) — hex + measured contrast vs its surface
text / text-muted / surface / accent / border / source / error / success

TYPE  body: [Arial | Calibri | Plex | Instrument Sans]  display: [same | Instrument Serif italic keyword]
GRID  12-col  gutter [ ]  margin ≥ 0.5 in  footer ~0.35 in  title Y locked
LOCKUP  H / stacked / mark / mono-light / mono-dark  clear-space = [unit]  min size screen/print
CHART  series 1–6  highlight  remainder-grey  hairline  source slot
DO-NOT  McKinsey navy+white clone; 16:9+4:5 mix; TED kit; generated faces

ASK: [ship this instance / swap accent to client / add dark]
Owner: [ ]  Date: [ ]
Holes: [ ]
```

## QA (must pass) — one-screen fail list

1. Every role named; not a moodboard.
2. Light and dark are mappings of the same roles; contrast **measured**, not assumed.
3. Body pairs pass WCAG AA. MM `#FF4F32` on `#F5F3EE` is not body text.
4. One canvas. No 16:9 + 4:5. No 16:9 + 4:3 in one file.
5. Neutral kit is not McKinsey navy+white sold as official.
6. Lockup do-nots hold. No dual identity without a co-brand rule.
7. Owner + date + ASK. No generated faces.

If 1, 2, 3, 4, or 5 fail: do not ship.

## Escalate / stop

- “Make it look like McKinsey” / stolen master → refuse.
- Social 4:5 requested → [Social Carousel](../../branding/social-carousel/SKILL.md).
- Moodboard, no roles → issues list.

## Related

- [Consulting Deck](../../documents/consulting-deck/SKILL.md) — consumes this kit
- [Finance Workbook](../../documents/finance-workbook/SKILL.md) / [PRD Spec](../../documents/prd-spec/SKILL.md) / [Research Paper](../../documents/research-paper/SKILL.md) — same tokens, different files
- [Social Carousel](../../branding/social-carousel/SKILL.md) — optional shared MM hexes; **different product**
