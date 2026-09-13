# Project memory — `STATUS.md`

The file that decides whether session two starts where session one stopped.

Everything else in the agentic layer describes the project as it *is*. `STATUS.md` describes where the work *has got to*, which is the thing nobody writes down and the thing that is most expensive to reconstruct — it exists only in the head of whoever did the last piece, and it evaporates.

---

## What it must answer

A stranger opens the repository with no other information:

1. What works right now?
2. What is half-built, and how far did it get?
3. What is the next thing to do?
4. What is known-broken or known-ugly, so I don't rediscover it?
5. What has been decided that isn't visible in the code yet?

Answer those five and the file has done its job. Everything beyond them is decoration that will go stale.

---

## The structure

```markdown
# Status

_Last updated: YYYY-MM-DD_

## Where this is

One paragraph. What state the project is in, in plain language. Written for
someone who has never seen it.

## Working

- [thing] — what it does, how to see it working

## In progress

- [thing] — how far it got, what is left, anything half-finished that
  would confuse someone reading the code

## Next

1. [the single most useful next action, concrete enough to start on]
2. ...

## Known problems

- [problem] — the impact, and whether it is a deliberate trade or a real bug

## Ideas and improvements

- [idea] — not committed to, recorded so it isn't lost or re-derived

## Decisions not yet in the code

- [decision] — agreed, not implemented. Prevents someone "fixing" it back.
```

---

## The rules that keep it honest

**Concrete "Next" items.** *"Improve error handling"* is not something anyone can start on. *"Wrap the three `adapters/http.py` calls in the retry decorator already used in `adapters/queue.py`"* is. If the top item is not something a stranger could begin within five minutes, it needs sharpening — a vague next-action is the most common reason the file stops being used.

**Update it as part of the work, not afterwards.** A status file updated at the end of a session is a status file that gets skipped when the session runs long — which is exactly when it mattered most. Make it a standing rule in `CLAUDE.md`, so it is part of the change rather than a chore after it.

**Delete freely.** This file describes the present. A "Working" entry that has been true for six months and is now uncontroversial can go — the file is not a changelog, and length is what makes it stop being read. Git has the history.

**Record the half-finished state, honestly.** The single highest-value entry in the whole file is *"the parser handles the first two formats; the third is stubbed and returns an empty list, which looks like a bug but isn't yet."* That is the sentence that saves the next session an hour of confused debugging, and it is the one people are embarrassed to write.

**Separate "known problem" from "idea".** A problem is something that will bite someone. An idea is something that might be nice. Merging them produces a list where the urgent is hidden among the optional, and nobody triages it.

**Keep "Decisions not yet in the code" short and live.** An entry there is a promise. When it is implemented, delete it — the code is now the record. When it is abandoned, delete it and, if the reasoning is worth keeping, move it to `.out-of-scope/`.

---

## At scaffold time

The file is created almost empty, and that is correct — it should describe reality, and at scaffold time reality is "the structure exists and nothing is built."

```markdown
# Status

_Last updated: 2026-07-25_

## Where this is

Freshly scaffolded. The structure and documentation exist; no application code
has been written yet.

## Working

- Nothing yet — the repository builds and the test command runs against an
  empty suite.

## Next

1. [the first real implementation task, taken from the interview]
2. [the second]

## Decisions not yet in the code

- [anything decided during the interview that the code has yet to reflect]
```

Resist inventing progress. A scaffold that claims "core module implemented" because a directory exists is the aspirational-file failure, and it poisons trust in the whole layer on day one.

---

## Why not just use issues?

Issue trackers hold *tasks*. This file holds *state* — the difference between "here are twelve open tickets" and "here is where the work actually stands and what the half-finished bits look like."

The distinction is sharpest with a coding agent: an agent starting a session reads the repository, not your tracker. `STATUS.md` is in the repository, it is short enough to read entirely, and it is written for someone with no context. A tracker is none of those things.

They coexist fine. When a project has both, `STATUS.md` points at the tracker for the backlog and keeps for itself the two things a tracker holds badly: **what is half-done right now**, and **what to do next**.
