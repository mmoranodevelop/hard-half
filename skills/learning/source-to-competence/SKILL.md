---
name: source-to-competence
description: >-
  Turn a book, paper, document, or video into concept objects a person can
  actually remember, then (if asked) into a practice playbook that builds
  competence. Use when the user wants to extract key ideas they can train on, or
  says they read something and still cannot use it. NOT for compiling an AI
  skill other agents will run (use competence-to-skill), NOT for chapter-by-
  chapter summaries, and NOT for a briefing someone will not practice.
license: MIT
---

# Source to Competence

Turn a book, paper, document, or video into concept objects a person can actually remember, then (if asked) into a practice playbook that builds competence.

Two stages, one skill. Stop after encode if the user only wants concepts. Never ship a chapter-by-chapter summary as the product.

## When to use

- "Extract the key ideas from this book / paper / doc / video so I can learn them"
- "Turn these notes into something I can train on"
- "I read it and I still can't use it"

## When not to use

- A briefing for someone who will not practice (that's a memo skill)
- Compiling an AI skill other agents will run (use Competence to Skill)
- Reproducing a book, course, or lecture as a substitute for the source
- Highlighting / progressive summarization as the goal

## Modes

| Mode | Output | Default |
|---|---|---|
| **encode** | `source.md` + literature note + 8–25 concept objects + graph | if they say "concepts / notes / remember" |
| **train** | `playbook.md` from existing concept objects | if concepts already exist |
| **both** | encode then train | if they say "learn this" / "make me competent" |

Ask once if unclear. Do not run train on a chapter summary.

## Hard rules

1. Memory is the residue of thought, not exposure.
2. Retrieval is the learning event. A summary the user rereads is the condition that loses at a delay.
3. Fluency ≠ competence. Familiarity ≠ recollection.
4. A concept is a **discrimination object**: claim, model, is-not, example, counterexample, cue, when-to-use, common error. A definition is not a concept.
5. Adler (inspectional / analytical / syntopical) is intake, not the deliverable. Throw the outline away after objects exist.
6. Own words, atomic, linked with *why*. Quotes are spare and cited.
7. A playbook is not a summary with checkboxes. It has a goal, stretch, named-error feedback, delayed pass criteria, and a stop rule.
8. Teach-back is a diagnostic, not the method.
9. Video requires a real watch pass. Title + transcript skim is inspectional residue.
10. Extract ideas. Never reproduce the work.

## Intake

Bound **competence** first, one sentence: what should a person be able to **do** after this source? If you cannot say it, you are encoding a book report. Ask the user.

Then:

| Medium | Do this | Do not |
|---|---|---|
| Book / long doc | Inspectional (title, TOC, preface, pivotal chapters) then analytical mining of propositions | Chapter summaries as output |
| Paper | Abstract, figures, methods, limits, falsifiers | Abstract-only encoding |
| Video | Watch it (watchVideo / equivalent). Interpolated free-recall every segment | Encode from title, thumbnail, or auto-transcript alone |
| User notes | Treat as literature notes; promote only what becomes a full concept | Pretty-up the notes and call it done |

Copyright: new language; short quote only when wording is the claim; cite locator; no key-passage dumps; no copied figures (redraw the causal sketch, attribute the idea).

## Stage A — encode

```
A0  Competence in one sentence (with the user).
A1  Inspectional: kind, unity, parts, go/no-go. Video: 2 min then full watch.
A2  Analytical: terms, propositions, arguments. Paper: methods + falsifiers.
    Video: watch; pause; generate; continue.
A3  Rival view: what this is NOT. Seeds is_not and counterexample.
A4  Literature note: citation + 5–10 lines of YOUR understanding. No quote dump.
A5  Promote to concept objects (only propositions that serve A0).
A6  Link each concept to ≥1 other with relation + why. Graph around USE, not chapters.
A7  Retrieval gate: close the source. Produce claim + when_to_use from cues.
    Fail = not encoded. Do not fix by rereading your own notes.
A8  Teach-back one hard concept to a novice. Gaps → common_error.
```

Volume: a worth-encoding nonfiction source yields **8–25 concept objects**. 80 = literature notes in disguise. 3 = slogans.

Refuse a chapter tour as the product. If they insist, give a short source map as appendix metadata, not as the artifact.

### Concept object (required fields)

```yaml
schema: archetype.concept.v1
id: concept.<slug>
source: source.<id>
source_span: "<locator, not a dump>"
claim: "<one proposition, encoder's words>"
model:
  verbal: "<how it works>"
  visual: "<diagram / timeline / arrows the learner must later redraw>"
is_not: ["<near-miss, not a joke>"]
example:
  - {surface: "...", structure: "..."}
counterexample: ["<where the claim fails or looks like it but isn't>"]
cue: "<world situation that should fire this, without the book in hand>"
when_to_use: "<select X over Y when Z>"
common_error: "<the fluent mistake>"
how_why_questions: ["Why is this true?", "How would I see it in the wild?"]
evidence_grade: high | moderate | method | unverified | folklore
links:
  - {to: concept.<id>, relation: "...", why: "..."}
```

If a field cannot be filled, the concept is not done. "The author talks about habits" is not a concept.

Examples must vary surface. One cute example gets remembered *as the example*.

## Stage B — train

Requires Stage A objects. Do not invent drills from a summary.

```
B0  Observable competence (not "understand X").
B1  Map concepts → subskills. Each subskill owns a common_error.
B2  Warm-up retrieval every session: cues only, then feedback.
B3  Drills: discrimination, generation, selection. Blocked only until first success, then interleave confusable neighbors. Feedback names the error.
B4  Scenarios: messy, from target_use. ≥1 transfer item (new surface, same structure).
B5  Spacing heuristic: 0d, +1d, +3d, +7d, +21d. Retrieval first; restudy only misses. Keep retrieving successes.
B6  Teach-back checkpoint (one concept, notes closed) — not a whole session.
B7  Pass criteria: delayed ≥48h, closed-book, transfer scenario. Open-note success does not count.
B8  Stop or recycle: pass twice 48h apart → stop. Fail → new drill on the actual error, not "reread chapter 4".
```

Call this **purposeful practice**. Do not claim Ericsson deliberate practice unless a human expert designed the drill path.

### Playbook header

```yaml
schema: archetype.playbook.v1
id: playbook.<slug>
competence: "<observable>"
concepts: [concept.<id>, ...]
warmup: [{type: free-recall, cues: [...], pass: "..."}]
drills:
  - id: drill.<slug>
    goal: "..."
    stretch: "..."
    format: interleaved-items | generation | discrimination
    feedback: "name the error: ..."
    reps: 8
scenarios:
  - {id: scen.<slug>, prompt: "...", transfer: true}
spacing: {heuristic: ["0d","1d","3d","7d","21d"], note: "heuristic, not fitted"}
pass_criteria:
  delayed_gap: 48h
  closed_book: true
  score: "≥4/5 scenarios including 1 novel surface"
  teachback: "..."
stop_rule: "Pass twice, 48h apart. Do not replace sessions with rereading concept files."
```

## File layout

```
skills/learning/source-to-competence/instances/<source-id>/
  source.md
  literature-note.md
  concepts/<concept-id>.md
  graph.md
  playbook.md          # only if train/both
```

Shared library skill stays generic. Instances hold the source-specific objects.

## Quality bar — reject and redo

Stage A fail (any two): ordered by chapters; slogan claims; missing or joke `is_not`; examples share one surface; no world cue; `when_to_use` is "always"; quote-heavy substitute for the source; encoder cannot produce the claim from the cue; visual model is a restated paragraph.

Stage B fail: drills are "reread the card"; scenarios copy the example; feedback is a score without an error name; pass = "finished the PDF" or "feels confident"; no delayed test; random topic soup as interleaving; successes dropped from retrieval; teach-back is the only activity; no stop rule.

## Anti-patterns

- Highlighting, rereading, 20-page notes, chapter AI summaries
- Definition-only flashcards (front must be a cue or scenario)
- Progressive summarization as studying (archive trick, not encoding)
- Open-book concept maps (map from memory or skip)
- Encoding video from title
- Interleaving unrelated domains
- Copying the book into Markdown

## After running

Return:

1. Competence sentence.
2. Concept list (id + claim only).
3. What you refused to encode (chapters, slogans, unreproducible figures).
4. If train: how to run session 0, pass criteria, stop rule.
5. Pointer to instance folder.

Do not congratulate the user on "having notes." Point them at the first retrieval.
