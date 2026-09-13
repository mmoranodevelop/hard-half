# Default kit — style guide (carousels, posts, infographics)

Reusable visual system. Load `assets/visual-kit.yaml`. Fill the lockup from the user. Do not invent a new look per post. Do not fall back to ASK Rail, dotted paper, or a rounded-card clone of another creator.

## Tokens (locked)

| Token | Hex | Role |
|---|---|---|
| ink | `#111318` | Default canvas, glass fill |
| cream | `#F5F3EE` | Primary type on dark; light-canvas alt |
| gray | `#747B86` | Secondary type, folio, hairlines |
| accent | `#FF4F32` | Monogram, one keyword, icons, glows, X/check, arrows |
| peach | `#FFB59F` | Atmosphere only (bokeh, gradients). Not a second headline colour. |
| cyan | `#A8E9E6` | Atmosphere only (bokeh). Not a headline colour. |

## Type

- **Instrument Sans** — lockup, headlines (roman/bold), body, cards, folio.
- **Instrument Serif Italic** — exactly **one** keyword per slide, in accent. The word a sceptic would fight (`news`, `busy`, `skill`, `noise`, `86`, `Monday`, `Save`). Never two serif words. Never colour a Sans word instead of using Serif.
- Headlines 56–84px at 1080w. Body 24–28px cream. Card body 22–24px cream. Folio 14px gray.
- Tracking headlines −0.02em. Do not use Inter, or any other family.

## Lockup (every slide)

Top-left, 48px from top and from left:
monogram (user initials) in Instrument Sans Bold, accent, ~22px
then a 12px cream hairline
then `YOUR NAME` (from intake) in Instrument Sans, cream, 11–12px, tracking +0.12em, stacked on one or two lines if needed.
Same place every slide. No page-fold. No left rail.

## Default carousel canvas

- 1080×1350 (LinkedIn document). Ink `#111318` full bleed.
- **Grain** ~8% over the whole frame.
- **Bokeh**: 3–6 soft pills/orbs behind the cards (accent, peach, cyan), Gaussian-blurred, some motion-smeared. They sit *behind* glass, never on type.
- **Glass cards**: corner radius 28px. Fill ink at ~55% over a blurred backdrop (or a dark translucent rect + 1px accent highlight top/left + 1px cream 20% bottom/right). Soft outer glow, not a hard print offset.
- One or two cards max. Icons in accent (X, check, arrow). No iOS dialog chrome. No full-bleed dot grid.
- Bottom-left optional: `Key insight:` in accent + one cream sentence. Palette dots (accent, cream, gray) under it on cover and CTA only.
- Folio `01 / 08` bottom-right, gray.

Light cream canvas is allowed for a single contrast slide in a sequence, not as the master. If used: ink type, accent keyword in Serif italic, monogram lockup in accent, no grain.

## Headline recipe

Sans (cream) + **one** Serif italic (accent). Example: `MYTH` Sans + `vs` Serif italic accent + `REALITY` Sans or Serif cream. The fight-word is the Serif italic.

## Object language (operator content, default chrome)

Do not paste another creator's objects. Recast the argument in *this* chrome:

| Job | Object |
|---|---|
| Hook | One glass card: empty ASK field as type; a muted stack of news lines in gray inside the card is enough |
| Stakes | Two stacked glass cards (FEED / ASK) like Myth/Reality |
| Reframe | One glass card with four labelled rows; ASK row in accent |
| Payload | One glass card; model name struck in gray; work lines in cream |
| Proof | Giant `86` in Serif or Sans accent, glass index of three skill names |
| Use | Four numbered rows on one glass card; `20'` in accent Serif |
| Synthesis | Filled glass form + small accent arrow |
| CTA | Glass card + accent `→` ; insight line |

No generated portraits. No wireframe heads unless the user supplies the asset. No mountain/cone stock unless supplied.

## Rendering

- Code (Pillow / compositor) so type is exact. Download **Instrument Sans** and **Instrument Serif** (italic). Do not substitute Inter.
- LinkedIn: 1080×1350 PNG + PDF.
- Image models only for bokeh/atmosphere if code cannot blur; never for faces; never for the whole slide; never to rewrite type.

## Sludge (fail)

Inter or any non-Instrument family; ASK Rail / left red bar; full-bleed notebook dot grid; iOS delete-app sheet; two Serif keywords; peach or cyan used as a second headline colour; generated likeness; "Swipe"; comment-YES; cloned third-party logo.

## Instance

`kits/mm.yaml` and `visual-kit.yaml` fill `lockup_name` and `monogram` from intake. Defaults are placeholders (`YOUR NAME`, `XX`). Never ship a carousel with the placeholders still on the lockup.
