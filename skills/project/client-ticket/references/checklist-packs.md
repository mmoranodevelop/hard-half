# Checklist packs

Prefer a **template already on the destination** (ClickUp task template, Jira checklist add-on, Asana task template). These packs are the fallback. Delete any item that cannot apply to this ask. A change with no assets must not carry "Upload assets".

Language: match the destination list. Translate this pack if the list is not English.

## Size S / Data Entry / Config — operating checklist

Include only what the ask touches:

- Configure the entity in the admin panel
- Set values on every list / environment the ask names
- Enable only the bound surfaces
- Apply inclusion / exclusion rules if the ask names them
- Upload assets only if the ask includes them
- Confirm conflict / stacking rules if the ask is a campaign or launch
- Test on staging
- UAT with the requester / PM
- Go-live confirmed

A flag-only task might keep only: configure flag, staging test, UAT, go-live.

## Size M+ — four lists

Do not attach all four to an S. M gets all four unless the user said analysis-only.

### Analysis & planning

- Outcome and context in the description
- Functional requirements written and validated
- Out of scope stated
- External dependencies identified
- Requester prerequisites collected
- Acceptance criteria shared
- Estimate filled
- Milestone dates set
- Mockups approved (drop if no UI)
- PRD written or attached (keep for L/XL; drop for M if a short description is the spec)

### Build

- Branch from the correct default branch
- Built to the requirements
- Automated tests (drop if the repo has none)
- Code review approved
- Merge to the target branch
- Deploy staging
- Developer self-test

### Dev test

- Happy path
- Edge cases cited in the analysis
- Regression on related flows
- Test on the bound environment / surface
- Multi-device (drop if not frontend)
- Performance under the stated bar (drop if not relevant)
- No unexpected errors in console / logs
- Real data
- User-facing errors and messages
- Evidence (screenshot/video)
- Acceptance criteria met
- PM sign-off before UAT

### Pre-release & deploy

- Customer UAT (or declared not needed)
- Merge to production
- Production config checked
- Feature flag (drop if none)
- DB migration (drop if none)
- Rollback plan
- Customer communication
- Docs updated
- Post-deploy smoke
- No production regression

## Bug (any size)

Use Dev test + a short operating list of: reproduce on staging, fix, regression on the failing surface, UAT if customer-facing. Skip campaign / launch bullets.
