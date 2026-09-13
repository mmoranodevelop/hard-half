---
name: voice-blueprint
description: >-
  Map a person's real writing voice into versioned blueprints other agents can
  load when writing email, messages, or documents. Use when creating or updating
  a voice blueprint, writing in someone's voice, adding a register, or
  diagnosing why generated copy does not sound like them. NOT for a brand-new
  company voice with no person behind it, NOT for legal filings, and NOT for
  executive or board memo structure (use executive-board-memo).
license: MIT
---

# Voice Blueprint

Map a person's real writing voice into versioned blueprints that other agents can load when writing email, messages, or documents.

One identity. Many situation overlays. Never one personality per recipient, and never a list of adjectives.

## When to use

Use this skill when the user wants to:

- create, update, or inspect a **voice blueprint**
- write or rewrite something **in their voice** (or another named person's)
- add a new register (professional email, friends chat, board paper, public post)
- diagnose why generated copy "doesn't sound like me"

## When not to use

- Brand-new company voice with no person behind it (still usable, but treat as a new `identity_key`, not an overlay on a human)
- Legal filings written by counsel, or any register they asked you not to imitate
- Translating meaning; this skill is about *how*, not *what*
- Executive/board memo structure — use that skill for the artifact; load a board-memo overlay here only for voice

## Modes

| Mode | When | Output |
|---|---|---|
| **calibrate** | New blueprint, or reverse-test failed | Interactive session → instance files |
| **apply** | User asked to write/rewrite as them | Loaded core + one overlay → draft |
| **list** | "what voices do we have?" | Inventory of identities and overlays |
| **inspect** | "show my professional email voice" | Human-readable card, no private extras |
| **recalibrate** | Drift, new job, new language, 3 rejected drafts | Version bump of the same identity |

If mode is unclear: **calibrate** when no instance exists for this person; otherwise **apply**.

## Architecture (load-bearing)

**Voice** is constant personality. **Tone** is this piece's 4-D setting (humor, formality, respect, energy). **Register** is why the setting moved (channel + relationship + topic). **Style** is the mechanics that make it visible (punctuation, emoji, contractions, rhythm).

Public guides that work (Mailchimp, Monzo, Slack, GOV.UK, Google, Microsoft) all do the same split: one invariant + a situation matrix. They capture **constraints**, not vibes.

```
GENERIC (this skill)
  SKILL.md                 protocol, schema, battery, lookup, lint
  assets/               empty YAML
  NEVER: names, samples, "Manuel sounds like…"

INSTANCE (person-specific, private)
  instances/<identity_key>/
    core.yaml
    overlays/<overlay_id>.yaml
    pairs/                 contrastive pairs (short)
    eval/                  reverse-test diffs
```

User-memory may store a **pointer** (`identity_key`, default overlay, path). Never embed samples in memory or in this skill.

**Core** = mechanics that survive channel (rhythm, hedge policy, default emoji, bilingual tells, global do/do-not).

**Overlay** = delta on core (greetings, tu/Lei, emoji for *this* channel, structure, extra bans, channel pairs).

**Tone-shift** at write-time (`warmth +1`, `directness +1`) — do not create a file per recipient.

**Fork a new identity** only for a different human, a brand, or a fictional persona. Cap: 1 core + ≤6 overlays. A 7th is usually a tone-shift in disguise.

### Lookup at write-time

1. Resolve `identity_key` (ask if more than one).
2. Load `core.yaml`.
3. Score overlays: +3 channel, +3 lang, +2 doc_type, +1 audience; `default_for` breaks ties.
4. Load **one** overlay. Never blend two.
5. Optional ±1 tone-shift from the brief (angry client, close friend).
6. Assemble prompt: identity first, constraints last, 3–4 contrastive pairs, keep it short.
7. Draft → slop-lint **this instance's** bans → show.
8. No match → core + say the register is unconfirmed. Never silently reuse professional-email for chat.

## Calibrate (interactive)

People cannot describe their voice. They can **discriminate** two drafts. The session produces annotated contrastive pairs (generic / LLM-default → their rewrite), then a mechanical card.

Do **not** ask "how would you describe your style?" If they volunteer adjectives, keep them only as this/not-that.

### Step 0 — Scope and consent

Ask, one at a time when needed:

1. Whose voice? (default: the user)
2. Languages for this identity (`it`, `en`, both). Overlays are language-tagged; do not assume EN is a translation of IT.
3. First target overlay: professional email / friends chat / work chat / long document / board paper / public post. Name it. Also name what it is **not** for.
4. Optional: 3–5 real messages they actually sent (gold). Hold out 2 if they give more than 5.

Tell them: samples live in instance files, not in the shared skill. They can skip gold samples; the rewrite battery still works.

### Step 1 — Target card (before any sentence)

Write, and confirm:

```
overlay_id: <slug>
for: <audience × channel × doc_type>
not_for: <two things people would wrongly use it for>
lang: it | en
```

### Step 2 — Rewrite battery

Present **one generic draft at a time**. Instruction (use the language of that item):

> Rewrite it as you would actually send it. Change everything. Delete everything. Add a greeting and sign-off if you would use them. Leave it blank if you would not send this message.

If the item is Italian: `Riscrivilo come lo manderesti davvero. Cambia tutto. Cancella tutto. Aggiungi saluto/chiusura se li useresti. Lascia vuoto se questo messaggio non lo manderesti.`

Optional after each: "What was off in the draft?" → annotation.

Default: **12 items**. Use 8 if they fatigue. Use all 16 if they write both languages in many registers. Run EN, IT, or both to match `languages[]`. Skip a language they would not use in that register (do not force a translation).

The drafts are intentionally slightly LLM-flavored, not cartoonishly bad.

Hold out 2 items from the card for the reverse test.

### Step 3 — Capture the LLM default as a negative

On ~3 items (ask, apology, sign-off), keep the generic draft as the `less_preferred` example. Their rewrite is `preferred`. That delta is the training data.

### Step 4 — Extract mechanics, not adjectives

From the rewrites, fill the schema. Look at:

- Greeting / sign-off inventory (actual strings)
- Tu / Lei / you, and whether formal Lei is capitalized
- Sentence length band, fragments, paragraphing, bullets vs prose
- Contractions; Italian elisions (`c'è`, `com'è`)
- Punctuation: em dash, ellipsis, `!`, `?` stacked, semicolon, Oxford comma, space-before-punct
- Emoji: which, where (end vs inline), never in which register
- Hedges and boosters; stacked-sorry vs fix
- Discourse markers (`anyway`, `allora`, `cmq`, `btw`)
- BLUF vs cushion on bad news
- Please / conditional politeness
- Idiosyncratic tells (do **not** "correct" them)
- This/not-that, 3–5 pairs, where Y is the **attractive failure** (confident→cocky, warm→saccharine, witty→puns on bad news)

`voice_one_liner` pattern: "I [verb] like [concrete comparison], and I never [attractive failure]."

Banned list: GOV.UK shape — term + substitution + exception. Copy an LLM-slop phrase into `forbidden_phrases` **only if the battery shows they don't use it**. If they love em dashes, those are identity, not slop.

### Step 5 — Write instance files

- `instances/<identity_key>/core.yaml`
- `instances/<identity_key>/overlays/<overlay_id>.yaml` (delta)
- `instances/<identity_key>/pairs/<overlay_id>.md` (the contrastive pairs)

Status starts as `draft`.

Also write a user-memory **pointer** (identity, path, default overlay). No samples in memory.

### Step 6 — Reverse test (required gate)

Write **3 fresh samples** not in the battery, in the right language and overlay (e.g. work email, friend chat, short recap). User edits in place.

Diff edits into rules. Bump version. Repeat until edits are cosmetic.

Then a side-by-side once: (1) LLM default (2) blueprint output (3) their rewrite if any. If they pick (1), the card is wrong.

Mark `confirmed` when:

- ≥2/3 reverse-test samples are "send as-is" or edits are spelling/facts
- Blueprint beats default in the side-by-side
- Zero hits on **this person's** banned list
- Lookup picks the right overlay on 3 hypothetical (audience × channel × doc_type) triples

### Step 7 — Handoff

Tell the user: path, overlay name, how to invoke apply, when to re-test (drift, new role, 3 rejected live drafts).

## Calibration battery

Each item: purpose, EN draft, IT draft.

### 01 Open / greet
Greeting, name, emoji, tu/Lei.
- EN: `Hi {Name}, I hope this message finds you well! I wanted to reach out regarding the project we discussed.`
- IT: `Gentile {Nome}, spero che questo messaggio La trovi bene! Le scrivo in merito al progetto di cui abbiamo parlato.`

### 02 Ask
Directness, please, hedges, question marks.
- EN: `I was wondering if you might possibly have a chance to review the attached document at your earliest convenience?`
- IT: `Mi chiedevo se per caso potesse avere un attimo per esaminare il documento in allegato alla Sua prima convenienza.`

### 03 Thanks
Warmth, brevity, emoji, inflated gratitude.
- EN: `Thank you so much for your help — I really appreciate it and it means a lot!`
- IT: `La ringrazio tantissimo per l'aiuto, lo apprezzo davvero e per me significa moltissimo!`

### 04 Apology
Stacked-sorry vs fix. LLM closer.
- EN: `I'm so sorry for the delay — I feel terrible about this. I'd be happy to jump on a call whenever works for you to make it right.`
- IT: `Mi scuso tantissimo per il ritardo, mi sento terribilmente in colpa. Sarei felice di sentirmi in chiamata quando Le fa più comodo per rimediare.`

### 05 Decline
Plain no, alternative, over-explaining.
- EN: `I'd love to help, but unfortunately I don't think I'll be able to take this on right now. That said, I'd be happy to revisit next quarter if that's useful!`
- IT: `Mi piacerebbe aiutare, ma purtroppo non credo di riuscire a prendermi questo impegno in questo momento. Detto questo, sarei felice di rivalutarlo il prossimo trimestre se può essere utile!`

### 06 Bad news
BLUF vs cushion, em dash / ellipsis.
- EN: `I wanted to share an update. Unfortunately, we won't be able to hit the original deadline. There were a number of moving pieces, and I wanted to be transparent with you as soon as possible.`
- IT: `Volevo condividere un aggiornamento. Purtroppo non riusciremo a rispettare la scadenza originale. Ci sono stati diversi elementi in movimento e tenevo a esserLe trasparente il prima possibile.`

### 07 Chase
`!` / `…` / hedges before the ask.
- EN: `Just bumping this to the top of your inbox! I know you're incredibly busy — whenever you get a chance, no rush at all, but wanted to make sure this didn't get lost.`
- IT: `Ti ripropongo questo per sicurezza! So che sei pienissimo — quando hai un attimo, senza nessuna fretta, volevo solo assicurarmi che non si fosse perso.`

### 08 Celebrate
`!`, emoji, "huge / incredible."
- EN: `This is huge — congratulations!!! I'm so incredibly proud of what the team pulled off. You should all be so proud! 🎉🎉🎉`
- IT: `È enorme — congratulazioni!!! Sono incredibilmente orgoglioso di quello che ha fatto il team. Dovreste essere tutti orgogliosissimi! 🎉🎉🎉`

### 09 Explain technical
Jargon, rule-of-three, lecture.
- EN: `At a high level, the system is designed to seamlessly leverage a robust pipeline that ingests data, transforms it, and delivers insights — in other words, it's a holistic, end-to-end solution.`
- IT: `Ad alto livello, il sistema è progettato per sfruttare in modo seamless una pipeline robusta che ingerisce i dati, li trasforma e restituisce insight — in altre parole, è una soluzione olistica end-to-end.`

### 10 Boundary
Firmness, apology for having a limit.
- EN: `I might be wrong, but I think I may not be the best person to own this. Happy to help think it through, though, if that's useful!`
- IT: `Magari sbaglio, ma forse non sono la persona più adatta a portarlo avanti. Detto questo, se può essere utile, sono più che felice di ragionarci insieme!`

### 11 Disagree
Discourse markers, face-saving.
- EN: `That's a great point! I think there might be another way to look at this, though. It's important to note that the numbers could also be read as roughly flat, rather than up.`
- IT: `Ottimo spunto! Credo però che ci sia un altro modo di vederla. È importante notare che i numeri si potrebbero leggere anche come sostanzialmente piatti, piuttosto che in crescita.`

### 12 Recap
Bullets vs prose, BLUF.
- EN: `To summarize, here are the three key takeaways: (1) we align on scope, (2) we lock the date, and (3) I'll follow up with next steps. Let me know if I missed anything!`
- IT: `Per riassumere, i tre punti chiave sono: (1) allineamento sullo scope, (2) blocco della data, e (3) farò un follow-up con i prossimi passi. Fammi sapere se ho dimenticato qualcosa!`

### 13 Introduce
Social warmth, oversell.
- EN: `I would love to introduce you two — I think there could be a really exciting opportunity to collaborate, and you'd both get a lot of value from the conversation!`
- IT: `Mi piacerebbe moltissimo presentarvi — penso possa esserci un'opportunità davvero stimolante di collaborazione, e entrambi trarreste grande valore dalla conversazione!`

### 14 Sign-off
Closer inventory. Bans "I'd be happy to" if unused.
- EN: `Please don't hesitate to reach out if you need anything else. I'd be happy to help. Best regards,`
- IT: `Non esiti a riscrivermi se ha bisogno di altro. Sarei felice di aiutarLa. Cordiali saluti,`

### 15 Urgent ask
Shortness under pressure.
- EN: `Hi — sorry to bother you. When you have a moment, could you please take a look at this today if at all possible? Totally understand if not. Thank you so much!`
- IT: `Ciao — scusa il disturbo. Quando hai un attimo, potresti per favore dargli un'occhiata oggi se in qualche modo ti è possibile? Capisco perfettamente se non ce la fai. Grazie mille!`

### 16 Mixed register (colleague-friend)
Tu/Lei leakage, humor, emoji at work.
- EN: `Hey! Flagging this for Monday's meeting — nothing urgent, just want to make sure we're aligned before we walk in. Coffee after?`
- IT: `Ehi! Ti segnalo questo per la riunione di lunedì — nulla di urgente, voglio solo essere sicuro che siamo allineati prima di entrare. Caffè dopo?`

## Apply

1. Classify the piece: audience, channel, doc_type, lang, severity (bad news / celebrate / routine).
2. Lookup overlay. State which blueprint you loaded.
3. If no overlay matches, say so and write from core with the register marked unconfirmed — or offer to calibrate that overlay first.
4. Draft in their mechanics. Headings as they would. Greetings from the inventory. No presenter-voice.
5. Lint against `forbidden_phrases` and overlay extra bans.
6. Return the piece plus a one-line voice check: overlay used, any rule you bent, anything you invented.

Do not announce the style ("I've written this in a warm professional tone"). Just write.

## Schema (instance YAML)

See `assets/core.yaml` and `assets/overlay.yaml`. Required on every instance:

- `kind`: core | overlay
- `identity_key`, `overlay_id` (null on core), `extends`, `version`, `status`, `lang`
- `match.audiences`, `channels`, `doc_types`
- `relationship_register`: formality, warmth, directness, humor, address_form (1–5 where numeric)
- `mechanics`: punctuation, emoji, contractions, paragraphing, capitalization
- `this_not_that` (3–5; Y = attractive failure)
- `do` / `do_not` (rules phrased as the desired behavior; negative *examples* allowed)
- `forbidden_phrases[]` with substitution
- `greetings[]` / `signoffs[]` (actual strings)
- `example_pairs[]`: less_preferred, preferred, annotation
- `humor_policy`, `emoji` object (default, by_channel, max, placement, never_in)

Emoji object: `{default: none|rare|ok, by_channel: {}, max_per_message, placement: end|inline, never_as_words: true, never_in: [legal, bad-news, errors]}`.

## LLM-default tells (copy into an instance only if unused)

Punctuation: em-dash pileups, tricolon padding, uniform medium-long sentences, decorative emoji clusters.

Openers/closers: `I'd be happy to`, `Please don't hesitate`, `I hope this message finds you well`, `Let me know if you need anything else`, `Great question!`, `Certainly!`, `Of course`.

IT: `Sarei felice di`, `Non esiti a riscrivermi`, `È importante notare che`, `Ad alto livello`, `soluzione olistica`, mix of tu and Lei.

Hedges: `It's important to note that`, `I might be wrong, but I think I may`, `That said,`.

Essay glue: `Furthermore`, `Moreover`, `At a high level`, `In today's fast-paced world`, `delve`, `leverage`, `robust`, `seamless`, `holistic`, `unlock`.

Structure: heading + three bullets + upbeat recap.

Phrase bans as the **positive alternative** plus a short negative example.

## Anti-patterns

1. Adjective-only voice ("friendly, professional, authentic") — that is the LLM prior.
2. This/not-that that isn't a real overshoot ("warm not cold").
3. One tone for all situations.
4. A different personality per channel (kindness, or whatever the invariant is, never turns off).
5. A blueprint per recipient.
6. Self-description as source of truth. The rewrites are the truth.
7. Mechanics as optional. Oxford comma, `!`, emoji, contractions, "please" *are* the formal/casual dial.
8. Global-banning em dashes or emoji in the skill. Personal.
9. Samples inside `SKILL.md`.
10. Blending two overlays at apply-time.
11. Silently using professional-email for chat.
12. Forced humor. If unsure, straight face.
13. "Write like you talk" without tightening — speech is more verbose than writing should be.
14. Friendliness as a universal good (precision dies; trust can too).
15. Workshop adjectives as the finished guide.

## After a session

Return:

1. What was created or updated (identity, overlay, version, path).
2. The this/not-that set and the mechanics that actually discriminate.
3. What is still unconfirmed (missing overlay, language not calibrated).
4. How to apply it next time.

If they asked to write something in the same turn, switch to **apply** after the reverse test, not before.
