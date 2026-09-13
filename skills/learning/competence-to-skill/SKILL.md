---
name: competence-to-skill
description: >-
  Use when compiling a Source-to-Competence instance (concepts + playbook) into
  a generic AI SKILL.md other agents can run. Optimize with the user. Not for
  encoding a book or writing a practice playbook.
license: MIT
---

# Competence to Skill

**Skill-spec from a Source-to-Competence instance** — a portable `SKILL.md` (when to use, intake, output template, QA, stop). Private samples stay in the instance. Default: one agent job, one artifact.

Method origin: the instance's playbook + Archetype skill spine. Do not dump a quality-bar essay into the body.

If they want a lecture on "how to write skills": one paragraph then produce or stop.

## When to use

- They have a `source-to-competence` instance and want an agent that *does the thing*
- "Turn what I learned into a skill my other agents can run"
- Redline a draft skill compiled from their own training artifacts

## When not to use

- Authoring or repairing a SKILL.md from scratch (description, hierarchy, trigger tests) — [create-skill](../../productivity/create-skill/SKILL.md)
- Encoding a book / paper into concepts — [Source to Competence](../../learning/source-to-competence/SKILL.md)
- Writing the practice playbook (Stage B) — [Source to Competence](../../learning/source-to-competence/SKILL.md)
- Teaching a team a method they already run — [Team Method Transfer](../../learning/team-method-transfer/SKILL.md)
- A document kit, not an agent recipe — [Document Kit](../../documents/document-kit/SKILL.md)
- Dumping concept YAML into `SKILL.md` and calling it a skill — refuse

## Modes

| Mode | When | Output |
|---|---|---|
| **produce** | Default. Instance exists (concepts + playbook) | Filled skill-spec (`SKILL.md` skeleton) + keep/drop list |
| **redline** | They pasted a draft skill | Force when-not, intake refuse, fenced artifact, QA; strip book outline and private samples |
| **refuse** | No observable agent job, missing concepts/playbook, or they want a notebook | Issues list. Stop |

## Hard rules

1. **One observable job.** If they cannot state what another agent **does** in one sentence, you have a notebook, not a skill.
2. **Compile from the instance, not the book.** Load `source.md`, `concepts/*.md`, `graph.md`, `playbook.md`. Ignore chapter maps. If concepts or playbook are missing, send them back to [Source to Competence](../../learning/source-to-competence/SKILL.md).
3. **Optimize with the user.** Keep / drop is required. Do not auto-compile the whole notebook. The skill follows the user's dissent (`is_not` / `common_error`).
4. **Generic and portable.** No names, no private samples, no unpublished numbers. Contrastive pairs only if they are generic method, not the person's mail.
5. **Artifact first.** The compiled skill produces a named output with holes, an ASK, and a refuse. Workflow is not "think about the concepts."
6. **Do not paste concept YAML** into the recipe. Do not paste a quality-bar document as the body.
7. **Human-only drills do not transfer** (delayed tests, spacing calendars). Convert to "ask the user to verify later" or drop.
8. **Do not invent pass criteria.** Holes stay holes.

## Intake

If **two** of 1–3 are missing after one round: issues list, not a fake skill.

1. What another agent **does** when this skill fires (observable) — load-bearing
2. Path to the Source-to-Competence instance (concepts + playbook present) — load-bearing
3. What must stay private (samples, client names, unpublished numbers) — load-bearing
4. Who uses the skill (learner, teammate, any assistant)
5. Category folder and kebab-case id
6. When-to-use line (the only thing an agent sees when deciding to load it)

## Output shape

```
SKILL SPEC  (compiled SKILL.md uses gold H2s in this order)
YAML name: [Title Case]
YAML description: Use when [one line]. Not [sibling].

Title: [Title]
Artifact line: **[Named artifact]** — [one sentence]. Default: [venture / stated].
Method origin: [one line from the instance]
Lecture rule: one paragraph then produce or stop.

When to use: [bullets]
When not to use: [Name](../../category/name/SKILL.md)
Modes:
  produce | Default | [artifact]
  redline | Pasted draft | [force the spine]
  refuse | Two load-bearing facts missing | Issues list. Stop
Hard rules: [from playbook / concepts — behaviour + short negative]
Intake: if two of [load-bearing] missing after one round: issues list.
  1. [ ] — load-bearing
Output shape: [copy-paste template with [placeholders]]
QA (must pass): [from pass_criteria an agent can check]
Escalate / stop: [ ]
Related: [Source to Competence](../../learning/source-to-competence/SKILL.md)

KEEP / DROP
Kept concept IDs: [ ]
Dropped (and why): [ ]
Private (stays in instance): [ ]
SOURCE.md pointer: [instance path]
```

Save: `skills/<category>/<id>/SKILL.md` plus a `SOURCE.md` that **points** at the instance. Do not copy the book.

## QA (must pass)

1. Observable job in the description ("Use when…").
2. When-not routes to a named sibling (at least source-to-competence).
3. Modes include produce / redline / refuse.
4. Fenced output template with placeholders.
5. QA checklist the agent can fail.
6. No private samples, no book outline as the body.
7. Not a restatement of a quality-bar document.
8. Keep/drop list returned with the spec.

If 1, 4, 5, or 6 fail: do not ship.

## Escalate / stop

- Concepts or playbook missing → [Source to Competence](../../learning/source-to-competence/SKILL.md).
- Job undefined after one ask → refuse (notebook).
- They want the skill to "remember the book" → refuse.
- Duplicates an existing skill unless they want a specialized variant — say so; do not silently fork.
- Legal / irreversible / safety auto-resolve → must stay in Escalate of the compiled skill.

## Related

- [Source to Competence](../../learning/source-to-competence/SKILL.md) — encode/train; this compiles the instance
- [Team Method Transfer](../../learning/team-method-transfer/SKILL.md) — humans already running a method
- [Document Kit](../../documents/document-kit/SKILL.md) — files, not an agent recipe
- [Voice Blueprint](../../writing/voice-blueprint/SKILL.md) — voice overlay; do not mix into a method skill
