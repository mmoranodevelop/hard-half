# CONTEXT.md

Shared vocabulary for this repository. When a term appears in a `SKILL.md`, it means what it means here.

## Distribution

**Skill** — a directory containing `SKILL.md` and optional bundled resources, describing a reusable discipline an agent follows when the skill is active.

**Channel A** — the `skills` CLI (`npx skills add owner/repo`). The registry is GitHub itself, not npm: `owner/repo` maps directly onto the repository. Nothing is published to a package registry. Files are **copied** into the user's project, so the user owns and may edit them.

**Channel B** — the Claude Code plugin marketplace. `.claude-plugin/marketplace.json` at the repo root catalogs plugins; `.claude-plugin/plugin.json` declares this one. Installs a **managed, read-only, always-current** bundle. Skills are namespaced: `/skills-that-matter:first-principles`.

**Immutable slug** — a public identifier users install with. Three of them: the marketplace name and the plugin name (both `skills-that-matter`), and each skill's `name`. Changing one breaks existing installations with *plugin-not-found* or a dead invocation path. `displayName` is the mutable label — change that instead.

**Category** — the folder grouping skills on disk: `skills/<category>/<name>/`. Organisational only; it carries no meaning to either channel and does not appear in invocation.

**Skill declaration** — the full path of a skill in `plugin.json`'s `skills` array. Because categories nest skills one level below where the plugin's default scan looks, the declaration is what actually loads them. An undeclared skill is valid, installs, and is invisible on channel B — silently. CI treats a missing declaration as a build failure.

**Progressive disclosure** — the three loading levels: name + description are always in context; the `SKILL.md` body loads when the skill activates; `references/` and `assets/` load only when the body directs the agent to them. This is why depth is cheap and body length is not.

**Routing rule** — the `description` field, understood correctly. It is not a title; it is the thing that decides whether the skill activates.

**Negative space** — the "when NOT to use this" clause of a description. Its absence is the leading cause of spurious activation.

**Spurious activation** — a skill firing on a task it should not handle. Costs more trust than a skill that fails to fire, because it makes the whole set feel unreliable.

**User-invoked / model-invoked** — the taxonomy axis. User-invoked skills are reachable only by typing the name and exist to *orchestrate*. Model-invoked skills can also be selected automatically by the agent and hold *reusable discipline*. A user-invoked skill may call model-invoked ones; never another user-invoked one.

## Reasoning vocabulary

Used across the reasoning skills, `first-principles` in particular.

**Invariant** — something the problem requires regardless of the mechanism chosen: physics, mathematics, and genuinely binding law. Distinguished from everything else, which is a design decision with a price.

**Solution basis** — the set of mechanisms a field has silently agreed to use. "Impossible" is almost always a claim about the solution basis, not about the problem. Separating those two claims is the core move of `first-principles`.

**Constraint ledger** — the Phase 2 artifact: every constraint on the current solution, with quantities, an asserting source, a class, and a cost to remove. Classes run Law · Math · Regulatory · Economic · State-of-the-art · Organizational · Habitual. Only the first two are walls.

**Chesterton's fence** — the rule that a constraint must not be removed until its original reason is found and evaluated. An unexplained constraint is a research task, not permission.

**Floor** — the value a metric would take if only the Law and Math constraints applied. Deliberately unachievable; it is a measuring instrument, not a target.

**Gap ratio** — `current ÷ floor`. Below 2× the problem is near a wall and the objective should change; 2–10× is engineering slack; above 10× the architecture itself is the problem; above 100×, recheck the floor for an omitted cost.

**Impossibility class** — why something is called impossible: **A** proven · **B** complexity-bounded · **C** empirically unachieved · **D** economically unattractive · **E** institutionally blocked · **F** definitionally impossible. Each demands a different attack, and real problems are usually a mixture — which is itself the finding.

**Premise attack** — the correct response to a Class-A citation. Never dispute the theorem; identify which of its premises your problem does not need. The target sentence: *"That theorem forbids W under premises P. We need V, and premise Pₖ does not hold here."*

**Deletion move** — removing a component, step, or actor entirely, before considering any improvement to it. If nothing removed had to be added back, not enough was removed to have learned anything.

**Efficient-market check** — the Phase 6 obligation to explain why the world has not already done this. Valid answers: newly possible · needs a rare capability · the field is wrong for a nameable structural reason. No answer means the path is probably wrong.

**Kill experiment** — the cheapest test that would falsify a candidate: what is observed, what result kills it, what it costs, how long it takes. A path with no kill experiment is rhetoric.

**DFX** — the Phase 5 design passes: **DFC** Cost · **DFM** Manufacturing/Execution · **DFS** Simplicity · **DFPR** Production rate · **DFV** Verification · **DFR** Reversibility.

## Calibration

**Number labels** — every quantity is marked **measured**, **cited** (with source), **estimated** (with derivation), or **assumed**. Unlabelled numbers let assumptions graduate into facts, which is the main way this kind of analysis causes damage.

**Named gap** — a quantity that is needed and not available, written down with its plausible range and where it could be obtained. Always preferable to a fabricated number, which poisons everything downstream.

**Impossible as posed** — a legitimate, valuable output: a Class-A wall with no available premise attack, delivered together with the nearby objective that is not blocked.
