# DOCUMENT KIT  |  instance: [consulting-neutral / MM / client]  |  canvas: [16:9 13.333×7.5 in / A4 210×297 mm / Letter]
Owner: [name]     In force: [YYYY-MM-DD]     Consumed by: [consulting-deck / finance-workbook / prd-spec / research-paper]
Mark: [file names] or [no mark — type lockup]     Co-brand rule: [none / defined]

## Roles (Carbon grammar: token = role; theme = hex)

Measure contrast vs the paired surface before shipping. Do not assume AA.

| Role | Light hex | Contrast vs light surface | Dark hex | Contrast vs dark surface | Notes |
|---|---|---|---|---|---|
| surface | [neutral `#F7F7F5` / MM `#F5F3EE` / client] | — | [neutral `#1B1B1B` / MM `#111318` / client] | — | |
| text | [neutral `#1B1B1B` / MM `#111318`] | [  ]:1 | [neutral `#F7F7F5` / MM `#F5F3EE`] | [  ]:1 | Body. Must ≥ 4.5:1 |
| text-muted | [`#525252` / client] | [  ]:1 | [`#C6C6C6` / client] | [  ]:1 | ≥ 4.5:1 if used as body-size |
| accent | [neutral `#0D5C63` / MM `#FF4F32` / client] | [  ]:1 | [neutral `#5CB8BC` / MM `#FF4F32` / client] | [  ]:1 | MM on light **2.95:1 — keyword/mark only, not body** |
| border | [ ] | [  ]:1 non-text | [ ] | [  ]:1 | ≥ 3:1 vs surface |
| source | [ ] | [  ]:1 | [ ] | [  ]:1 | Footer source line |
| error | [ ] | [  ]:1 | [ ] | [  ]:1 | Not colour-only (WCAG 1.4.1) |
| success | [ ] | [  ]:1 | [ ] | [  ]:1 | Not colour-only |

MM measured (do not re-assert without measuring a changed pair): text↔surface **16.76:1**; `#FF4F32` on `#111318` **5.68:1** (pass AA); `#FF4F32` on `#F5F3EE` **2.95:1** (fail AA / large / non-text).

Neutral default teal is an **operator default, not a firm identity**. Swap to client brand.

## Type (two families max)

| Role | Family | Weight | Size lock (16:9) | Notes |
|---|---|---|---|---|
| Action title / H1 | [Arial / Calibri / IBM Plex Sans / Instrument Sans] | [600–700] | [same size every exhibit] | Never shrink to fit — split the slide |
| Body / UI | [same sans] | 400 | [ ] | Embed licensed files |
| Keyword / display | [none / Instrument Serif italic] | 400 italic | [ ] | MM: keyword only, never body |
| Source / page | [same sans] | 400 | [9–11 pt] | Footer band ~0.35 in |

License: [OFL Instrument / system Arial / embedded Plex]. Office does not ship Instrument — embed or do not use.

## Grid

- Canvas: [13.333 × 7.5 in | A4 | Letter] — **one size per file**
- Columns: 12. Gutters: [16–24 px / 0.2–0.3 in]. Margins ≥ 0.5 in.
- Title block: fixed Y, 1–2 lines. Footer: source + `n / n` + optional classification. Logo in **one** corner only.
- Layouts that emerge (not a stolen master): full-width exhibit; ~60/40 chart+so-what; 2-up; 3-up MECE.

## Lockup (GOV.UK *pattern*, not GOV.UK assets)

| Version | File | Clear space | Min size screen | Min size print | Allowed grounds |
|---|---|---|---|---|---|
| Horizontal | [ ] | = [unit of the mark] | [ ] | [ ] | light / dark |
| Stacked | [ ] | [ ] | [ ] | [ ] | |
| Mark-only | [ ] | [ ] | [ ] | [ ] | |
| Mono on light | [ ] | [ ] | [ ] | [ ] | |
| Mono on dark | [ ] | [ ] | [ ] | [ ] | |

Do-not: stretch, skew, drop shadow, recolour except approved mono, rotate, low-contrast ground, MM grain + competing client mark without a co-brand rule.

## Chart series

| Token | Light | Dark |
|---|---|---|
| series-1 (highlight) | [accent] | [accent that passes] |
| series-2…6 | [ ] | [ ] |
| remainder-grey | [ ] | [ ] |
| gridline | hairline | hairline |
| axis / label | text | text |
| source | source | source |

No 3D. No data gradients (think-cell vendor: cannot apply gradient fills to think-cell elements). Direct labels > legends.

## ASK

[ship this instance / swap accent to client hex / add dark mapping / produce lockup files]
Owner: [ ]  Date: [ ]
Holes: [ ]
