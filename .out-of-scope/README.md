# Out of scope

One file per feature or change that has been **deliberately rejected**, with the reasoning and any prior requests.

## Why this folder exists

A rejected idea comes back. Someone opens the same issue a year later, or an agent reads the repo, notices the obvious gap, and helpfully implements the thing that was considered and turned down. Both cost the same argument twice, and the second time nobody remembers the reasoning — only that it feels like an omission.

Writing the rejection down converts "we didn't do that" into "we decided not to, here's why", which is a different conversation and a much shorter one.

## Format

`<short-slug>.md`:

```markdown
# <The thing being asked for>

One paragraph: what is requested, and the flat statement that it is out of scope.

## Why this is out of scope

The actual reasoning. What breaks, what it trades away, or which existing
mechanism already covers it. Be specific — a vague rejection gets re-litigated.

## What to do instead

The escape hatch that already exists, if there is one.

## Prior requests

- #NN — "quoted, in the requester's words"
```

## What belongs here

Requests turned down **on their merits** — the change is understood and not wanted.

Not this folder:

- **Not yet built** → the roadmap table in `README.md`
- **A decision about how something is built** → `.agents/adr/`
- **A bug** → an issue

## Current entries

*None.* The folder is a convention waiting for its first entry — populated when a request actually arrives, not filled speculatively.
