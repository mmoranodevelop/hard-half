---
name: find-skill
description: >-
  Find, browse, or recommend the one Hard Half skill that owns a job — by
  purpose, category, audience, or artifact — and if none fits, write a brief
  for a skill that should exist, then offer create-skill. Use when the user
  asks which skill to use, how to navigate the catalog, is there a skill for
  X, what do you have for board / tickets / stuck problems, they don't know
  where to start, or they want a skill that is missing. NOT for doing the job
  itself. NOT for writing the new SKILL.md (that is create-skill, after the
  brief). NOT daily task triage (signal-vs-noise). NOT scaffolding a repo
  (create-project / repo-setup).
license: MIT
---

# Find Skill

## The catalog is the product; this is the door

Two hundred skills are useless if the user cannot find the one that owns *this* artifact. The default agent either grabs a neighbour by keyword or offers a tour. The leading word is **index**. You walk the index — category READMEs plus `references/catalog-map.md` — and you stop when one skill is named, or when you can honestly say the catalog has a hole.

You name the skill. You do not do the job. A spurious activation that produces a recommendation is cheap. One that writes a weekly status in this skill's name is a miss.

If they already named a skill, invoke that one — do not re-route.

## When to stop

- They named the skill → invoke it (if model-invoked) or tell them to type it
- Today's 3–5 tasks, not a catalog search → `signal-vs-noise`
- They want the new `SKILL.md` written now, and the job is already scoped → `create-skill`
- New software project folder → `create-project`
- One-time paths for this repo → `repo-setup`
- Two load-bearing intake facts blank after one ask, and they are not browsing a bucket → issues list, stop

## Mode

| Mode | When | Output |
|---|---|---|
| **Find** | Default. A situation, a goal, an artifact | One skill, two refused neighbours, how to invoke |
| **Browse** | "What do you have for board / M&A / tickets / writing?" | The bucket (or a short cluster), not 200 rows |
| **Gap** | Nothing in the index owns this job | A skill brief + offer to run `create-skill` — do not write the file unless they say yes |

Infer. Browse vs Find: if they named a category or a *kind* of work without a specific artifact, Browse. If they described a situation, Find. If Find comes up empty after the index, Gap.

## Protocol

### 0. Intake

One round. For **Find** and **Gap**, two of these are load-bearing:

1. The **artifact** they think they need (page, memo, ticket, conversation, tree) — or "I don't know, here's the situation"
2. **Who it is for** (themselves, delivery team, sponsor, board, buyer, acquired company)
3. The **decision or moment** (this week, Day-1, a sitting, a save, a close)
4. What they already tried

For **Browse**, the load-bearing fact is the bucket or purpose ("board", "skills themselves", "client tickets"). Do not interview a browser for a full situation.

> **Done when:** mode is named and its load-bearing facts exist, or you have asked once and stopped.

### 1. Walk the index — do not open two hundred files

Read, in this order, only what the mode needs:

1. `references/catalog-map.md` — one line per skill
2. The matching category `skills/<category>/README.md` files (one screen each)

Match on **audience + artifact + moment**, not on shared keywords. `weekly-status` and `sponsor-status` share "status". They are different artifacts.

Read `references/catalog-map.md` **now**. It is the index.

> **Done when:** you have a shortlist of at most five skills, or an empty shortlist.

### 2. Lattice test (Find)

Pick one. Then name the two nearest you almost picked and why they are wrong for *this* artifact. If you cannot name the neighbours, you have not picked yet.

If the shortlist is empty, go to Gap. Do not force a neighbour onto a job it refuses.

> **Done when:** one skill and two refused neighbours, or you have switched to Gap.

### 3. Gap — propose, do not build

When the index has no owner:

Write a **skill brief**, not a `SKILL.md`:

```
GAP BRIEF
Job (one sentence, the process, in order):
Leading word (or none):
Why the default agent fails without it:
Nearest existing skills and why they are the wrong artifact:
Anti-triggers:
Verdict: deserves a skill / belongs in CLAUDE.md / just ask once
```

Most gaps should not become skills. Run the no-op test: would the agent behave differently? If no, say so. If yes, ASK: `write it with create-skill` / `stop`. Do not start `create-skill` until they say write it.

Read `references/gap-brief.md` **now** if you are in Gap.

> **Done when:** a brief and a verdict exist, and no SKILL.md was written unless they asked.

### 4. Output

**Find:**

```
FIND SKILL
Situation: [one sentence]
Skill: /<name>     Bucket: <category>
Why this one: [audience + artifact + moment]
Not these:
- /<neighbour> — [why the artifact is different]
- /<neighbour> — [why]
Invoke: type the name, or say "run it"
```

**Browse:** the bucket heading, 5–12 skills with one line each, and "say which job if you want a single pick."

**Gap:** the brief + the ASK.

Stop. Do not produce the memo, the ticket, or the deck. If they say "run it", invoke the named **model-invoked** skill. Never invoke `repo-setup` (user-invoked) from here.

> **Done when:** Find names one skill and two neighbours; Browse lists a bucket; Gap has a brief; no job artifact was produced.

## Anti-patterns

- **Keyword grab.** "Status" → the first status skill, not the audience's artifact.
- **Tour.** Twenty skills when they asked for one.
- **Do the job.** This skill wrote the weekly status.
- **Ghost skill.** Inventing a catalog entry that does not exist.
- **Build on a no-op.** Gap that should have been "just ask" becomes a SKILL.md.

## Bundled references

| File | Read it when |
|---|---|
| `references/catalog-map.md` | Every run — the index |
| `references/gap-brief.md` | Mode Gap, or Find came up empty |
