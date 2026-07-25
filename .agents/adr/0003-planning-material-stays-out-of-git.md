# Planning material and the compliance term list stay out of git

This repo converts delivery experience into public material. The characteristic failure is not a bug — it is publishing something that identifies a client, an employer, or an engagement. Git history preserves it after deletion, so the only reliable control is at the boundary.

## Decision

Three classes of file are gitignored and must stay that way.

**Planning documents** — `plan.md`, `project-status.md`, `01-github-profile-e-growth.md`, `notes/`.

They discuss employer context, IP boundaries, and launch strategy. They are the source material, not the product. `plan.md` in particular contains an explicit assessment of what may and may not be extracted from an employer — exactly the reasoning that must not be public.

**`compliance-terms.txt`** — the list of names that must never appear in the repo: client brands, project codenames, interface ID prefixes, internal domains, colleague names.

A committed list of forbidden words **is itself the disclosure.** It hands a reader the client list in one file, sorted. Only `scripts/compliance-terms.example.txt` — a template with no real entries — is tracked.

**Anything matching `*.local`.**

## Consequences

- CI can only run the pattern layer of `compliance_check.py` (credentials, internal hostnames, private IPs, local paths). **The term layer is the contributor's responsibility**, run locally before pushing. This is a real gap and it is accepted: the alternative is worse.
- `scripts/compliance_check.py` scopes its scan to what git would actually publish (`git ls-files --cached --others --exclude-standard`) rather than everything on disk. Scanning ignored planning notes produces false positives, and false positives train people to ignore the output — which is how the real hit gets waved through.
- Architectural reasoning cannot live in `project-status.md`, because nothing there is published. That is why these ADRs exist: the *why* has to survive in the repo, where the next person to touch this will actually look.

## Do not

Add `plan.md` to git "just so it doesn't get lost." Back it up outside the repo.
