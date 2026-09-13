# Project shapes

Step 2. One tree per kind of project, with the reasoning behind each directory.

**Adapt, do not paste.** A shape encodes what usually works for that kind of program. When an answer from the interview conflicts with it, the answer wins — and the conflict is worth recording as the first ADR.

**Contents**
- [Rules that apply to every shape](#rules-that-apply-to-every-shape)
- [CLI](#cli) · [Service / API](#service--api) · [Web app](#web-app) · [Library](#library) · [Data / ML pipeline](#data--ml-pipeline) · [Prototype](#prototype)
- [Monorepo](#monorepo)
- [Language conventions](#language-conventions)

---

## Rules that apply to every shape

**Create no directory you cannot fill this week.** An empty `utils/` becomes the dumping ground its name invites. Add it when a second utility exists, and the folder earns its name from real contents.

**The root is prime real estate.** Everything at the root competes for the reader's first ten seconds. Tooling config that a tool insists on living there is unavoidable; everything else earns its place or moves down.

**Separate what you write from what you generate.** Source, build output, and dependencies never share a directory. This is what makes `.gitignore` writable as a short list rather than a running battle.

**Tests mirror source.** Whatever the language convention is — `tests/` alongside, or `_test` files next to the code — apply it consistently from the first file, because retrofitting a test layout is pure friction with no payoff.

---

## CLI

```
project/
├── src/<pkg>/
│   ├── __main__.py / main.go / index.ts   # entry point, thin
│   ├── commands/                          # one file per subcommand
│   └── core/                              # the logic, importable without the CLI
├── tests/
├── docs/                                  # only if flags outgrow --help
├── README.md
└── AGENTS.md, CLAUDE.md, STATUS.md, .agents/
```

**Why the split.** `core/` must be usable without the CLI layer — that is what makes the logic testable without spawning a process and what lets the tool later grow a library or an API surface without a rewrite. Entry points that grew argument parsing *and* business logic together are the single most common reason a CLI is hard to test.

`commands/` pays off from about the third subcommand. Below that it is ceremony.

---

## Service / API

```
project/
├── src/
│   ├── api/            # routes, handlers — HTTP-aware, thin
│   ├── domain/         # business logic, no framework imports
│   ├── adapters/       # database, queues, third-party clients
│   └── config/         # settings, environment loading
├── tests/
│   ├── unit/
│   └── integration/
├── migrations/
├── docker-compose.yml  # local dependencies
├── .env.example        # every variable, no real values
└── README.md, AGENTS.md, CLAUDE.md, CONTEXT.md, STATUS.md, .agents/
```

**Why `domain/` imports no framework.** It is the layer with the longest life. Frameworks get replaced; business rules outlive them. Keeping the dependency arrow pointing inward — `api/` and `adapters/` depend on `domain/`, never the reverse — is what makes that survivable.

**`.env.example` is not optional here.** It is the cold-start contract: it tells a newcomer exactly which variables exist without leaking a single value. Every variable the service reads appears in it, with a comment, and no real secret ever does.

A service earns `CONTEXT.md` more than most shapes, because it usually has domain vocabulary that outsiders read wrongly.

---

## Web app

```
project/
├── src/
│   ├── routes/ or pages/     # follow the framework's convention
│   ├── components/
│   ├── lib/                  # logic that isn't UI
│   └── styles/
├── public/                   # static assets served as-is
├── tests/
└── README.md, AGENTS.md, CLAUDE.md, STATUS.md, .agents/
```

**Follow the framework here rather than imposing a structure.** Web frameworks have strong conventions with real machinery behind them — file-based routing, build-time discovery — and fighting them costs more than any tidiness gained.

`lib/` is the piece people skip: logic that is not UI wants to live outside the component tree, or it becomes untestable without rendering.

---

## Library

```
project/
├── src/<pkg>/
│   └── __init__.py / index.ts / lib.rs   # the public surface, explicit
├── tests/
├── examples/                             # runnable, not snippets
├── docs/
├── CHANGELOG.md
└── README.md, AGENTS.md, CLAUDE.md, CONTEXT.md, STATUS.md, .agents/
```

**The public surface is a design artifact.** One file states what is exported; everything else is internal and free to change. Without that boundary every symbol becomes public by accident, and the first release freezes your entire internal structure into a compatibility promise.

`CHANGELOG.md` from day one, because a library's users experience it as the product. `examples/` holds programs that actually run — an example that has drifted out of date is worse than none, and a runnable one can be tested in CI.

---

## Data / ML pipeline

```
project/
├── src/
│   ├── ingest/ transform/ train/ evaluate/   # stages, in order
│   └── common/
├── notebooks/          # exploration; not the pipeline
├── configs/            # experiment configs, versioned
├── data/               # gitignored, with a README explaining what belongs here
├── models/             # gitignored, or pointers to storage
├── tests/
└── README.md, AGENTS.md, CLAUDE.md, CONTEXT.md, STATUS.md, .agents/
```

**Directories named for pipeline stages** make the data flow legible from the tree alone, which matters more here than anywhere else because the flow *is* the architecture.

**`data/` and `models/` are gitignored but present**, each with a committed README saying what belongs there and where the real artifacts live. An empty ignored directory with no explanation is a trap for the next person, who cannot tell whether the files are missing or elsewhere.

**Notebooks are for exploration, never the pipeline.** They resist review, diff badly, and hide execution order. When a notebook's logic starts to matter, it moves into `src/`. Say this in `AGENTS.md` — it is the single most-violated rule in this shape.

---

## Prototype

```
project/
├── src/
├── README.md         # what it is, how to run it, what it will NOT become
└── STATUS.md
```

**That is the whole thing.** The point of a prototype is answering one question fast, and ceremony is what stops it doing that.

Two files still earn their place. `README.md` records what question this answers and — crucially — states that it is a prototype, so nobody finds it in six months and deploys it. `STATUS.md` holds the finding, which is the actual output; a prototype whose conclusion was never written down was wasted.

Add `AGENTS.md` only if the thing lives longer than expected. If it does, that is the moment to reconsider the shape properly.

---

## Monorepo

Only when packages are genuinely released or deployed independently. Otherwise directories in one project do the same job with a fraction of the tooling.

```
repo/
├── packages/<name>/     # each with its own package manifest and tests
├── shared/              # only what two or more packages actually use
├── tooling/
└── README.md, AGENTS.md, CLAUDE.md, CONTEXT.md, STATUS.md, .agents/
```

`shared/` is where monorepos rot: things land there "in case" another package needs them. The rule that keeps it honest — code moves into `shared/` on the day a *second* consumer appears, not in anticipation of one — belongs in `AGENTS.md`.

---

## Language conventions

Follow the ecosystem rather than imposing a house style. A layout that surprises a newcomer costs more than any consistency it buys.

| Language | Source | Tests | Notes |
|---|---|---|---|
| **Python** | `src/<pkg>/` | `tests/` | `src/` layout prevents importing the uninstalled package by accident |
| **TypeScript / Node** | `src/` | `tests/` or `*.test.ts` beside source | Both conventions are normal; pick one and hold it |
| **Go** | `cmd/<binary>/`, `internal/`, `pkg/` | `*_test.go` beside source | `internal/` is enforced by the compiler — use it for anything not public |
| **Rust** | `src/` | `tests/` for integration, `#[cfg(test)]` inline for units | Cargo's layout is not negotiable |
| **Java / Kotlin** | `src/main/<lang>/` | `src/test/<lang>/` | Build tools assume it |

When the user's toolchain has an official scaffolder — `cargo new`, `npm create`, a framework CLI — **run it and add the agentic layer on top.** It will produce the ecosystem's expected layout more reliably than reconstructing it by hand, and the value this skill adds is the layer that tool does not create.
