---
name: ai-ops-policy
description: >-
  Use when an exec needs an allowed / banned / human-review AI use policy by
  workflow, plus data rules and one ASK to approve. NOT for prd-spec, not
  experiment-brief, not competence-to-skill.
license: MIT
---

# AI Ops Policy

**Exec AI use policy — one page** — workflow classes → Allowed / Banned / Human-review required; data rules (what may leave the tenant); logging / retention; one ASK to approve. Default: enterprise or venture operator policy for staff use of genAI tools; same spine for board-facing "how we use AI".

Method origin: NIST AI RMF 1.0 (Govern → Map → Measure → Manage; voluntary, use-case agnostic) + EU AI Act public risk tiers (prohibited / high-risk / transparency) as **category labels for internal policy**, not legal opinion + OpenAI / Google public enterprise usage patterns (no training on business data by default; disallowed high-stakes automated decisions without human review). Reconstruct the operator policy. Do not practise law.

If they want an AI ethics lecture: one paragraph then produce or stop.

## When to use

- Leadership asks "what may staff put into ChatGPT / Copilot / our LLM?"
- A draft policy is slogans ("use AI responsibly") with no workflow classes
- High-stakes workflows (hire, fire, credit, medical, legal advice to clients) need human-review gates
- Customer / employee data rules for prompts and RAG are undefined
- Board or customer asks for a one-page AI use stance

## When not to use

- Product requirements for an AI feature — [PRD Spec](../../documents/prd-spec/SKILL.md)
- A single A/B or pilot experiment card — [Experiment Brief](../../strategy/experiment-brief/SKILL.md)
- Turning a competence into a reusable skill pack — [Competence to Skill](../../learning/competence-to-skill/SKILL.md)
- Where customer data **physically** lives vs contract — [Data Residency](../../management/data-residency/SKILL.md)
- Vendor SOW for an AI vendor — [Vendor SOW](../../management/vendor-sow/SKILL.md)

If they cannot name **workflows** (or refuse to), stop. Issues list.

## Modes

| Mode | When | Output |
|---|---|---|
| **produce** | Default. Named org + tool set + workflow list | Policy one-pager + ASK |
| **redline** | They pasted "responsible AI" fluff | Force Allowed/Banned/Review table; kill slogans |
| **refuse** | No workflows, or "ban all AI" / "allow all" with no classes | Issues list. Stop |

## Hard rules

1. **Classify by workflow, not by tool.** Same model can be Allowed for draft email and Banned for automated firing.
2. **Three buckets only:** Allowed (default with data rules) / Human-review required (AI drafts; human decides) / Banned.
3. **Map high-stakes to Human-review or Banned.** Employment decisions, credit/essential services, health, client legal advice, biometric ID — label using EU AI Act *public categories* as internal risk language; counsel confirms jurisdiction.
4. **Data rules explicit.** What may leave the corporate tenant; customer PII / secrets / source code; training opt-out / enterprise tier required; logging.
5. **Human owns the decision** wherever the bucket is Human-review. "AI said so" is not a decision.
6. **One ASK** — named exec to approve the policy (or the delta) by a date. Not "circulate for awareness".
7. **Never invent** fine amounts, compliance %, or model accuracy. Holes stay holes.
8. **Not legal advice.** First line of the page says so. Point to counsel for Act / sector overlay.
9. **One page.** Playbooks and tool lists can annex; the policy is the table + data rules + ASK.

## Intake

If **two** of 1–4 are missing after one round: issues list, not a fake policy.

1. Org / BU in scope and who must approve — load-bearing
2. Tools in scope (vendor names / internal models) — load-bearing
3. Top workflows staff actually run with AI today (or planned) — load-bearing
4. Data classes that must not leave the tenant (PII, secrets, client) — load-bearing
5. Sector overlay (health, financial, public sector) or "none stated"
6. Existing DPA / enterprise tier vs consumer accounts in use
7. Logging / retention owner
8. Effective date desired

## Output shape

```
AI OPS POLICY  —  NOT LEGAL ADVICE  |  [org/BU]  |  as-of: [date]
ASK: [exec] to [approve / revise] this policy by [date]
Tools in scope: [ ]     Enterprise tier / training opt-out: [yes/no/HOLE]

WORKFLOW CLASSES
| Workflow | Bucket | Human owner of decision | Notes |
| Draft internal email / notes | Allowed | n/a | data rules apply |
| Client deliverable draft | Human-review | [role] | human ships |
| Hiring / performance / exit | Banned or Human-review | [role] | no automated decision |
| Credit / eligibility / medical advice | Banned or Human-review | [role] | sector overlay |
| [named] |  |  |  |

DATA RULES
- May leave tenant: [classes]     Must not: [PII/secrets/source/client]
- Consumer AI accounts for work: [banned / HOLE]
- Logging / retention: [owner] [period or HOLE]
- Customer data in prompts/RAG: [rule]

BANNED (non-exhaustive, align to public prohibited/high-risk categories — counsel confirms)
- [list]     Transparency-labelled uses: [disclose AI involvement]

NOT THIS PAGE
AI product PRD → prd-spec    Pilot card → experiment-brief
Skill pack from competence → competence-to-skill    Data location vs contract → data-residency

Holes: [ ]
```

## QA (must pass)

1. Workflow table with Allowed / Human-review / Banned — not slogans.
2. Data rules name what may / must not leave the tenant.
3. High-stakes workflows gated or banned.
4. One ASK with named exec + date.
5. "Not legal advice" on the page.
6. No invented fines, accuracy, or compliance %.
7. Not a PRD, not an experiment, not a skill-authoring guide.
8. One page.

If 1, 2, 4, or 6 fail: do not ship.

## Escalate / stop

- They want a binding legal opinion on EU AI Act applicability → counsel; policy uses categories only.
- Consumer ChatGPT already holding customer PII → immediate ban path + [Data Residency](../../management/data-residency/SKILL.md) gap map.
- They demand "allow everything if employees pinky-swear" → refuse.
- Productising an AI feature → [PRD Spec](../../documents/prd-spec/SKILL.md).

## Related

- [Data Residency](../../management/data-residency/SKILL.md) — where data lives vs contract; this is use policy
- [PRD Spec](../../documents/prd-spec/SKILL.md) — build an AI product; this governs staff use
- [Experiment Brief](../../strategy/experiment-brief/SKILL.md) — one pilot; this is standing policy
- [Vendor SOW](../../management/vendor-sow/SKILL.md) — buy an AI vendor; attach this policy as exhibit
- [Decision Rights](../../management/decision-rights/SKILL.md) — who has the D to approve this policy
