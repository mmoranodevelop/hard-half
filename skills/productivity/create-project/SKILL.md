---
name: create-project
description: >-
  Scaffold a brand-new development project: the folder, an architecture that fits
  what is actually being built, and the agent-facing files that let a fresh
  session pick the work up cold. Opens with a short interview — what you are
  building, who runs it, which language, what constraints, and whether you
  already have a plan or spec to attach — then proposes a structure and writes it
  only once you confirm. Produces the source layout, README, LICENSE,
  CONTRIBUTING, .gitignore, and the agentic layer: AGENTS.md, CLAUDE.md, a
  CONTEXT glossary, ADRs, and a living STATUS file recording what is done, what
  is next, and what is deliberately out of scope. Use when the user is starting a
  new project, repo, service, library, CLI, or prototype; asks for a project
  skeleton, boilerplate, starter structure, or to "set this up properly" before
  coding; or wants an existing idea, plan, or spec turned into a real repository.
  NOT for adding a feature, module, or package to a repository that already
  exists — this creates a root, it does not extend one. NOT for writing
  application code or choosing a framework: it produces the structure and the
  documents, then hands over.
license: MIT
---

# Create Project

## What you are actually building

Not a folder. **A project that survives a cold start.**

The test for every file this skill produces: *someone — a person or an agent — opens this repository knowing nothing, and gets productive without asking anyone a question.* That is a checkable standard. "Well organised" is not.

Cold start is the reason the agent-facing layer matters more than the source layout. Directories are easy to fix later; a project whose reasoning was never written down loses it permanently, because the person who held it moves on and the next session starts from zero every time.

Two failures this guards against, and they pull in opposite directions:

- **The bare start** — a folder, a README with the project name in it, and nothing else. Every decision gets re-litigated because none was recorded.
- **The cargo-cult scaffold** — forty files copied from a template, most irrelevant, a CONTRIBUTING.md for a solo prototype nobody will contribute to. Noise costs attention, and a file nobody maintains is worse than a file that does not exist, because it lies with authority.

**Shape follows purpose.** A CLI, a long-lived service, a library, and a weekend prototype want genuinely different trees and different amounts of ceremony. Scale the output to the project.

## The gate

**Write nothing to disk until the user has confirmed the plan.** Interview, propose, wait, then create.

This is not politeness. A scaffold is dozens of files whose structure is expensive to unpick once code sits inside it, and the interview costs a minute against a restructure that costs a day.

Two hard checks before any write:

- **The target path is confirmed as an absolute path**, stated back to the user.
- **The directory does not exist, or exists and is empty.** A non-empty directory means stop and ask — scaffolding over someone's work is unrecoverable in a way nothing else here is.

## The path

### 1. Interview — or read the plan they already have

Ask first: **do you already have a plan, spec, brief, or PRD?**

If yes, read it and **derive the answers from it.** Then confirm only what it left genuinely ambiguous. Re-asking someone questions their own document already answers reads as not having read it, and it is the fastest way to lose their patience.

If no, run the question set. Keep it short — you need enough to choose a shape, not a full specification:

1. **What are you building?** One sentence, in their words.
2. **What kind of thing is it?** CLI · service/API · web app · library · data or ML pipeline · desktop/mobile app · prototype
3. **Who runs it, and where?** Their laptop · a server · a user's machine · CI · a customer's infrastructure
4. **Language and runtime**, plus anything already decided
5. **Solo or a team?** Decides how much collaboration ceremony earns its place
6. **Public or private?** Decides LICENSE and how the README addresses the reader
7. **Anything deliberately out of scope?** The most valuable answer in the set — see step 6

Question rationale and how to handle vague answers: `references/interview.md`.

> **Done when:** you can name the project's shape, its language, its audience, and at least one thing it is explicitly not doing.

### 2. Choose the shape

Match the answers to a project shape, then adapt. `references/project-shapes.md` holds a tree per shape with the reasoning behind each directory.

Adapt rather than paste. A shape is a starting point that encodes what usually works for that kind of program — where the entry point goes, what gets tested, what belongs at the root. When an answer from step 1 conflicts with the shape, the answer wins, and the conflict is worth an ADR in step 6.

Resist directories with nothing to put in them. An empty `utils/` invites the dumping ground it names; create it when there is a second utility.

> **Done when:** every directory in the proposed tree has a stated purpose and something that will plausibly go in it this week.

### 3. Propose, and wait

Show the user: the absolute target path, the tree, the list of files, and — in one line each — the decisions you made on their behalf.

Then stop and let them answer. The corrections that arrive here are cheap; the same corrections after code exists are not.

> **Done when:** the user has approved the plan, or the revised version of it.

### 4. Create the tree and the machinery

Directories, then the files that make it a working repository: `.gitignore` generated for the actual language and toolchain, `LICENSE` matching the public/private answer, and `git init` with a first commit.

Two things worth doing properly rather than by reflex: the `.gitignore` covers this project's real toolchain rather than a generic list, and the first commit message says what the project is, because it is the first thing a `git log` shows forever.

> **Done when:** the tree exists at the confirmed path, `git status` is clean, and nothing that should be ignored is tracked.

### 5. Write the human-facing files

`README.md` and, when a team or public repo earns it, `CONTRIBUTING.md`.

The README's job is the cold start for a person: what this is, why it exists, how to run it in under a minute, and where the interesting parts live. Lead with what the project *does* — a reader who cannot tell in ten seconds leaves.

Write the run instructions as commands that work today. A README describing a build that does not exist yet is a document that trains people to distrust the repo.

Templates: `assets/README.template.md`, `assets/CONTRIBUTING.template.md`.

> **Done when:** the README states what it is, how to run it, and where to look — and every command in it would actually run.

### 6. Write the agentic layer

The part that makes the project resumable, and the part a generic scaffolder omits. Full spec for each file — what belongs in it, and what emphatically does not — is in `references/agent-files.md`.

| File | Holds | Cold-start question it answers |
|---|---|---|
| `AGENTS.md` | Operating rules: structure, conventions, commands, what breaks things | "How do I work here without breaking something?" |
| `CLAUDE.md` | A short pointer to `AGENTS.md` plus any Claude-specific standing rules | "What must I never forget?" |
| `CONTEXT.md` | The domain glossary — the project's own vocabulary | "What do these words mean here?" |
| `.agents/adr/` | Architecture Decision Records: why the shape is the shape | "Why is it like this — can I change it?" |
| `STATUS.md` | Living memory: done, in progress, next, known problems, ideas | "Where are we, and what do I do next?" |
| `.out-of-scope/` | Deliberate rejections, when there are any | "Was this considered, or forgotten?" |

Two rules that determine whether this layer is worth anything:

**Keep the always-loaded files short.** `AGENTS.md` and `CLAUDE.md` enter context every session, so depth belongs in `.agents/` behind pointers. A 400-line AGENTS.md is a tax on every future session and gets skimmed rather than read.

**Write the first ADR now**, recording the shape chosen in step 2 and why. It costs five minutes at the only moment the reasoning is fresh, and it is the single artifact that stops the structure being "fixed" back later by someone who never learned why. Step 1's out-of-scope answer seeds `.out-of-scope/`.

`STATUS.md` gets the most attention: it is the file that decides whether session two starts where session one stopped. Its structure and the discipline for keeping it honest are in `references/project-memory.md`.

> **Done when:** each file above either exists with real content, or was deliberately skipped for a stated reason — and `AGENTS.md` names the commands to build, test, and run.

### 7. Verify the cold start

Read what you produced as though you had never seen the project.

- Could you run it from the README alone?
- Could you make a change without asking anyone a question?
- Does `STATUS.md` tell you what to do next, concretely enough to start?
- Is anything in there aspirational — describing what the project will be rather than what it is?

That last one is the common failure. Scaffolds inherit vocabulary from templates and end up describing an imaginary mature project: a testing strategy for a repo with no tests, contribution guidelines for a repo with no contributors. **Delete anything not true today.** A file that lies with authority is worse than an absent one.

> **Done when:** every statement in the generated files is true right now, and the next action is written somewhere a stranger would find it.

### 8. Hand over

Tell the user what exists, what you decided for them, and what to do next. Then stop.

This skill produces structure and documents. It does not write application code, choose a framework, or start implementing — those are the next conversation, and running past the handover is how a scaffold quietly becomes an unrequested implementation.

> **Done when:** the user knows the path, the shape, and the first action — and no application code was written.

## Scale the ceremony to the project

The strongest signal of a thoughtless scaffold is uniform output regardless of input.

| | Prototype | Solo, long-lived | Team or public |
|---|---|---|---|
| README, `.gitignore`, `STATUS.md` | ✅ | ✅ | ✅ |
| `AGENTS.md` / `CLAUDE.md` | short | ✅ | ✅ |
| `LICENSE` | if public | ✅ | ✅ |
| `CONTEXT.md` | only with real jargon | ✅ | ✅ |
| ADRs | the first one only | ✅ | ✅ |
| `CONTRIBUTING.md` | ❌ | ❌ | ✅ |
| CI workflow | ❌ | when there are tests | ✅ |

When in doubt, produce less. A missing file gets added the moment it is wanted; an unmaintained one misleads for months.

## Bundled resources

| File | Read it when |
|---|---|
| `references/interview.md` | Step 1 — the question set, what each answer decides, handling vague or attached plans |
| `references/project-shapes.md` | Step 2 — the tree per project kind, with the reasoning behind each directory |
| `references/agent-files.md` | Step 6 — what belongs in each agent-facing file, and what does not |
| `references/project-memory.md` | Step 6 — `STATUS.md` structure and the discipline that keeps it honest |
| `assets/README.template.md` · `assets/CONTRIBUTING.template.md` | Step 5 |
| `assets/agent-files/` | Step 6 — templates for AGENTS, CLAUDE, CONTEXT, STATUS, and the first ADR |
