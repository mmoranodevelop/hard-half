---
name: research-paper
description: >-
  Use when producing an IMRAD (or venue) manuscript: claim, evidence,
  limitation, methods that replicate, labelled confirmatory vs exploratory. Not
  source-to-competence, not a blog, not pr-faq.
license: MIT
---

# Research Paper

**IMRAD manuscript** (or the venue’s published permutation) + figures-as-claims + refs. Claim → evidence → limitation. Abstract is a structured miniature, not an ad. Methods = protocol-time information (ICMJE Jan 2026). Confirmatory vs exploratory **labelled** (Nature Registered Reports). Humans own every citation.

Method origin: ICMJE Recommendations (Jan 2026); Nature formatting + AI + Registered Reports; NeurIPS Paper Checklist; ICML 2026 CFP; ACL ARR. Science / Cell STAR = search-confirmed official pages (fetch blocked) — use those URLs, do not invent extra rules.

If they want a “how to publish” lecture: one paragraph then produce or stop.

## When to use

- Original research / Registered Report / ML conference paper
- Figures that must carry claims with *n*
- Venue kit: Nature reporting summary, Cell STAR, NeurIPS checklist, ICML impact, ARR Limitations

## When not to use

- Read sources until you can decide — [Source to Competence](../../learning/source-to-competence/SKILL.md)
- Blog / op-ed / thought-leadership — [Thought Leadership Thesis](../../branding/thought-leadership-thesis/SKILL.md) / [Principal Brief](../../writing/principal-brief/SKILL.md)
- Future press release — [PR/FAQ](../../strategy/pr-faq/SKILL.md)
- One test to run, not a manuscript — [Experiment Brief](../../strategy/experiment-brief/SKILL.md)
- Builder spec — [PRD Spec](../../documents/prd-spec/SKILL.md)
- Literature review with no methods unless the venue’s survey/position track is named (ICML position = separate CFP)

## Modes

| Mode | When | Output |
|---|---|---|
| **produce** | Default. Claim + methods path exist | IMRAD (or venue perm) + figures + refs |
| **redline** | Draft with marketing abstract / missing *n* / results in Methods | Force labels, CIs, limitations |
| **refuse** | Fake refs; dual submission; LLM as author; unlabelled HARKing | Issues list. Stop |

## Hard rules

1. **Claim → evidence → limitation.** One primary claim (or a tight set). If it will not fit a Nature four-part summary or an ICMJE structured abstract, you do not have a paper yet.
2. **IMRAD is process, not decoration** (ICMJE). Introduction: no data or conclusions of *this* work. Methods: only what was known when the protocol was written; enough to replicate; software + version; eligibility; primary/secondary outcomes; **prespecified vs exploratory labelled**. Results: sequence **without interpretation**; exact *n*; define error bars; effect size + CI, not starred *p* alone. Discussion: meaning + limitations; do not repeat Results.
3. **Abstract matches the body.** ICMJE structured: context, purpose, procedures, main findings **with effect sizes**, conclusions, **important limitations**. Nature summary ≤ ~200 words, four parts, “Here we show,” aimed outside the discipline. No “novel / for the first time / unprecedented” (Nature Communications formatting).
4. **Figures are claims.** Legend: what is *depicted*, not the result, and **not methods** if a Methods section exists (Nature: < 300 words; initial-submission < 250). Exact *n*; error bars named (SD vs SEM). Science (search-confirmed): no “data not shown” for significant conclusions.
5. **NeurIPS Limitations:** **NA** = the paper has **no** limitation (almost never); **No** = limitations exist but are **undiscussed**. ACL ARR: Limitations section required (desk reject if missing). Do not omit.
6. **Refs:** Vancouver / ICMJE numbered in order of appearance. **Every non-result number is cited.** Open the DOI. No predatory journals. No invented AI refs. Chatbots **cannot be authors** (ICMJE; Nature Red; ICML). Disclose LLM use per venue. Prompt injection = desk reject (ICML/ARR).
7. **No dual submission / duplicate publication** (ICMJE III.D; COPE). Preprint ≠ dual pub if disclosed. Related overlapping manuscripts must be declared (Nature).
8. **Venue permutation — do not mix blindly.** Nature: summary → narrative → refs → legends → Methods online. Science/Cell: explicit IMRAD (Cell: STAR + Key Resources Table). NeurIPS/ICML: compressed 8–9 pp + checklist/impact after refs; appendices unlimited but claims stay in the main paper. Registered Report: Stage 1 locks intro/methods; Stage 2 adds results; exploratory in its own subsection and **must not carry conclusions alone**.
9. Trials: prospective registration (WHO ICTRP or ClinicalTrials.gov) at or before first consent (ICMJE). CONSORT **2025** (not 2010).
10. No fabricated data/citations. Humans accountable. Do not list ChatGPT as co-author.

## Intake

If **primary claim** and **methods path (how a stranger replicates)** are both missing after one round: issues list.

1. Primary claim in one sentence (load-bearing)
2. Confirmatory / registered / exploratory — label it (load-bearing)
3. *n* plan, outcomes, analysis, software; ethics/IRB if human
4. Venue (Nature / Science / Cell / NeurIPS / ICML / ARR / other)
5. Overlapping submissions / preprints — or “none”
6. Corresponding author; date; LLM use Y/N
7. Data/code path — or labelled restriction + another verification avenue

## Output shape

Copy `assets/imrad-skeleton.md`. Write Methods and figures before the abstract. Abstract last.

```
RESEARCH PAPER  |  [venue]  |  confirmatory / exploratory / mixed (labelled)
Title: [ ]     Corresponding: [ ]     Date: [ ]

ABSTRACT (miniature of the paper — numbers appear in the body)
INTRO     context + hypothesis. No results of this study.
METHODS   protocol-time only. Replicable. Prespecified vs exploratory.
RESULTS   evidence, no interpretation. Each figure = one claim + n.
DISCUSSION  meaning + limitations (NeurIPS: not NA unless truly none).
REFS      numbered; every non-result number cited; DOIs opened.
END-MATTER  contributions, COI, funding, data/code, ethics, venue checklist

ASK: [submit / register first / split exploratory]  Owner: [ ]  Date: [ ]
Holes: [ ]
```

## QA (must pass) — one-screen fail list

1. Not a marketing abstract. Not a blog. Not a PR/FAQ.
2. Exact *n* where statistics exist. Effect size + CI (or a labelled reason).
3. No uncited numbers. No AI-invented refs (DOI opened). LLM not an author.
4. Methods ≠ results. Legends ≠ methods (if Methods exist).
5. Confirmatory vs exploratory labelled. Exploratory does not carry the conclusions alone.
6. Limitations present. NeurIPS NA almost never. ARR Limitations not missing.
7. No dual submission. Related work declared. Venue checklist filled if required.
8. ASK + corresponding author + date.

If 1, 2, 3, 5, or 6 fail: do not ship.

## Escalate / stop

- Fake refs / LLM as author / dual submission → refuse.
- Missing *n* / starred *p* with no CI / unlabelled HARKing → issues list.
- “Summarise this field” → [Source to Competence](../../learning/source-to-competence/SKILL.md).

## Related

- [Source to Competence](../../learning/source-to-competence/SKILL.md) — consume, not produce
- [PRD Spec](../../documents/prd-spec/SKILL.md) — builders, not a manuscript
- [Experiment Brief](../../strategy/experiment-brief/SKILL.md) — one test, not IMRAD
- [PR/FAQ](../../strategy/pr-faq/SKILL.md) — future press release, not results
- [Document Kit](../../documents/document-kit/SKILL.md) — figure chrome only
