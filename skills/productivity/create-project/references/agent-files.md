# The agentic layer

Step 6. What belongs in each agent-facing file — and, just as load-bearing, what does not.

These files are what separate a scaffold from a project that can be resumed. Directories are cheap to fix later; reasoning that was never written down is lost permanently, because the person holding it moves on and every future session restarts from zero.

**Contents**
- [The division of labour](#the-division-of-labour)
- [AGENTS.md](#agentsmd) · [CLAUDE.md](#claudemd) · [CONTEXT.md](#contextmd)
- [.agents/ and ADRs](#agents-and-adrs) · [.out-of-scope/](#out-of-scope)
- [What never goes in these files](#what-never-goes-in-these-files)

`STATUS.md` has its own file: `project-memory.md`.

---

## The division of labour

Each file answers one cold-start question. Overlap is the failure mode — the same rule in two files means one of them will go stale, and there is no way to tell which.

| File | Question | Loaded |
|---|---|---|
| `AGENTS.md` | How do I work here without breaking something? | Every session |
| `CLAUDE.md` | What must I never forget? | Every session (Claude Code) |
| `CONTEXT.md` | What do these words mean here? | On demand |
| `.agents/adr/` | Why is it like this — may I change it? | On demand |
| `STATUS.md` | Where are we, what do I do next? | Every session |
| `.out-of-scope/` | Was this considered, or forgotten? | On demand |

**Always-loaded files stay short.** `AGENTS.md` and `CLAUDE.md` enter context every single session, so their length is a permanent tax. Depth goes into `.agents/` behind pointers. A 400-line AGENTS.md is not thorough; it is skimmed, which means its important lines get skimmed too.

---

## AGENTS.md

The cross-agent standard — read by Claude Code, Codex, Cursor, and others. This is the primary operating document, and everything else points at it.

**What belongs:**

- **The commands.** Build, test, run, lint. Exactly as typed, and correct today. This is the single highest-value section, because it is what an agent needs in the first thirty seconds and what it will otherwise guess wrong.
- **The structure**, with one line per directory saying what goes in it.
- **Conventions that are not self-evident from the code** — naming, error handling, where new modules go. Skip anything a formatter or linter already enforces; that is a no-op.
- **What breaks things.** Migrations that must run in order, a config that must stay in sync, a generated file nobody should hand-edit. The costly-mistake list.
- **Pointers** into `.agents/` for depth.

**What does not:**

- Facts a reader gets from the code in ten seconds
- Anything the linter enforces
- Aspirational process ("we practise TDD") that the repo does not actually do — an aspiration stated as a rule teaches the reader that the file is unreliable
- Long explanations that belong in `.agents/`

Template: `assets/agent-files/AGENTS.template.md`.

---

## CLAUDE.md

Claude Code reads this specifically. Since `AGENTS.md` already holds the rules, **CLAUDE.md is a pointer plus anything genuinely Claude-specific.**

```markdown
The operating rules for this project live in [AGENTS.md](./AGENTS.md). Read it
before changing anything.

Depth, loaded when relevant:
- [.agents/adr/](./.agents/adr/) — why the project is shaped this way
- [CONTEXT.md](./CONTEXT.md) — domain vocabulary
- [STATUS.md](./STATUS.md) — what is done and what is next

Before committing:
    <the test command>
```

**Duplicating AGENTS.md here is the mistake to avoid.** Two copies of the same rules drift, and the reader cannot tell which is authoritative. One source of truth, pointed at from the other.

Add a standing rule here when there is a recurring instruction that must survive across sessions — *"update STATUS.md as part of any change"* is the usual one, and it is what makes the memory file actually stay current.

Template: `assets/agent-files/CLAUDE.template.md`.

---

## CONTEXT.md

The domain glossary: the project's own vocabulary, defined once.

**Worth writing when** the project has words that a competent outsider would read wrongly. "Account", "job", "session", "tenant", "run" mean something specific in most codebases and something else in the next one. That ambiguity produces real bugs, and the fix costs one paragraph.

**Skip it when** the domain is genuinely generic. A glossary that defines "database" is padding, and padding trains people to stop reading glossaries.

Define terms as the *project* uses them, not as the dictionary does. If two teams use one word differently, that is exactly the entry worth having — record both and which one wins here.

Template: `assets/agent-files/CONTEXT.template.md`.

---

## .agents/ and ADRs

`.agents/` holds depth: material too long for an always-loaded file, reached by pointer.

**`.agents/adr/` — Architecture Decision Records.** One file per decision: what was decided, what was rejected, and why.

Write the first one during scaffolding, recording the shape chosen in step 2. It costs five minutes at the only moment the reasoning is fresh, and it is the one artifact that stops the structure being "fixed" back later by someone who never learned why it was that way.

Write a new one when a decision would be **expensive to reverse** and its reasoning is **not obvious from the code**. Both conditions — a reversible decision needs no record, and an obvious one documents itself.

```
.agents/
├── adr/
│   └── 0001-<decision-in-a-few-words>.md
└── <topic>.md          # deep guidance: testing strategy, deploy process
```

The format that works: a title stating the decision as a sentence, the context, the decision, the alternatives rejected *with their reasons*, and the consequences you accepted. The rejected alternatives are the most valuable part — they are what stops the same option being re-proposed every six months.

Template: `assets/agent-files/adr.template.md`.

---

## .out-of-scope/

One file per thing deliberately **not** being built, with the reasoning.

Create it when the interview's out-of-scope answer produced something real. Skip the folder entirely if it did not — an empty convention is noise.

It earns its place because rejected ideas come back. Someone proposes it again, or an agent notices the obvious gap and helpfully implements it. Both cost the same argument twice, and the second time nobody remembers the reasoning — only that it feels like an omission.

---

## What never goes in these files

- **Secrets, tokens, connection strings.** Even in examples. `.env.example` carries variable names and never values.
- **Anything not true today.** A testing section in a repo with no tests, a deploy process that does not exist. Aspiration written as fact is the fastest way to make the whole layer untrusted — and once a reader catches one lie, they stop reading all of it.
- **Content duplicated from another of these files.** Point instead.
- **Personal machine paths.** An absolute `/Users/<name>/projects/...` in a committed file breaks for everyone else.
- **Rules with no reason.** "Always use X" without why survives exactly until someone has a good reason not to, and then it gets ignored along with everything near it.

---

## The completion test

Read the layer as a stranger and answer these five. If any answer is "ask someone", that file is not finished.

1. How do I run this?
2. How do I test a change?
3. What am I likely to break, and how do I avoid it?
4. What does this project's odd vocabulary mean?
5. What should I do next?
