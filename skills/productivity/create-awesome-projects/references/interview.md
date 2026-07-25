# The interview

Step 1. Seven questions, each of which decides something concrete downstream. If an answer decides nothing, it should not be asked — an interview that feels like a form gets abandoned.

**Ask in one batch, not one at a time.** A seven-turn interrogation to create a folder is exhausting and people bail halfway. One message, numbered, with your best guess offered where you have one.

---

## When they already have a plan

Ask this first, before anything else:

> Do you already have a plan, spec, brief, or PRD for this? Point me at it and I'll work from that.

If they do, **read it and derive the answers.** A plan usually settles the shape, the language, the audience, and the constraints. Then confirm only what it genuinely left open:

> I've read the plan. I'm taking it as: a Python CLI, running on developers' laptops, solo project, private for now. It doesn't say anything about how config is loaded — is there a preference, or should I leave that open?

Re-asking questions the document already answers reads as not having read it, and it is the fastest way to lose someone's patience at the very start.

A plan that is genuinely thin is a different situation: say so plainly and ask the missing questions, rather than inventing answers to keep the flow smooth.

---

## The question set

### 1. What are you building? One sentence.

**Decides:** the README's opening line, the first commit message, the project's name.

Take their sentence nearly verbatim. Their phrasing carries the framing they actually hold, and a polished rewrite loses it. If the sentence contains a solution rather than a purpose ("a Redis-backed queue"), ask what it is *for* — the purpose belongs in the README, the mechanism belongs in an ADR.

### 2. What kind of thing is it?

CLI · service/API · web app · library · data or ML pipeline · desktop or mobile app · prototype

**Decides:** the entire tree. This is the highest-leverage answer, and the shape it selects is in `project-shapes.md`.

Offer the list rather than asking open-ended — people describe what their software *does*, not what category it belongs to, and the category is what you need.

**When two apply**, that is information: a library that also ships a CLI is a real and common shape, not an indecision to resolve. Take both.

### 3. Who runs it, and where?

Their laptop · a server they own · an end user's machine · CI · a customer's infrastructure

**Decides:** configuration strategy, secret handling, logging, packaging, and how paranoid the `.gitignore` needs to be.

The answer that changes the most is *a customer's infrastructure* — it pulls in versioning, backwards compatibility, and support concerns that a laptop tool never faces.

### 4. Language and runtime, plus anything already decided.

**Decides:** `.gitignore` contents, the build and test commands recorded in `AGENTS.md`, the tooling files at the root.

Ask what is **already decided** too — a framework chosen, a database mandated, a dependency required. Decisions already made are ADR material, and capturing them now costs nothing while reconstructing them later is guesswork.

If they have no preference and the shape has an obvious default, propose one with a reason rather than making them choose from a list.

### 5. Solo, or a team?

**Decides:** whether `CONTRIBUTING.md` earns its place, how much of `AGENTS.md` covers collaboration, whether CI is worth it now.

A solo project does not need contribution guidelines. Writing them anyway produces a document nobody reads and nobody updates, which is the definition of the cargo-cult scaffold.

### 6. Public, or private?

**Decides:** `LICENSE`, README tone, and whether a compliance pass matters.

If public: which licence, with MIT proposed as the default and one line on what it means. If they are unsure, MIT is the safe answer and a licence change before the first release is trivial.

If private but possibly public later: still add a `LICENSE`, because retro-fitting one across contributors is far harder than choosing now.

### 7. What is this deliberately NOT doing?

**Decides:** the README's scope section, `.out-of-scope/`, and — more than anything else — whether the project stays finishable.

The most valuable answer in the set, and the one nobody volunteers. Ask it directly, because scope creep is a default and an explicit non-goal is the only thing that resists it.

If the answer is "I don't know yet", that itself is worth recording: a project with no stated boundary will grow one by accident.

---

## Handling vague answers

**"I'm not sure yet."** Fine — propose a default with its reasoning and mark it in the first ADR as provisional. A recorded provisional decision beats an unrecorded real one.

**"Just make it good."** They want to skip the interview. Compress to the two questions that cannot be guessed — *what kind of thing* and *what language* — infer the rest, and state your inferences explicitly in step 3 so the corrections come cheap.

**A description that is really three projects.** Say so, and ask which one is being started today. Scaffolding all three produces three half-projects and is the most expensive mistake available at this stage.

**Answers that contradict each other** — a public library that handles customer secrets, say. Name the tension and ask which side wins. It is almost always a real design question surfacing early, which is exactly where you want it.

---

## Done when

You can state, in one breath: the shape, the language, who runs it, whether anyone else will touch it, whether it is public, and one thing it will not do.

If any of those is still missing, the tree you propose next is a guess.
