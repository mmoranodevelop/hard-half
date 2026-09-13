# PRD / TECH SPEC  |  [one named problem]  |  [YYYY-MM-DD]  |  Owner: [name]
Status: [review / decided YYYY-MM-DD / archive]     Reviewers: [names]
Discovery evidence: [PR/FAQ signed / job + go / study ref] — if missing, stop

The key words "MUST", "MUST NOT", "SHOULD", "SHOULD NOT", "MAY" are to be interpreted as described in RFC 2119, **when and only when they appear in all capitals**, as shown here (RFC 8174).

## 1. Context and scope

[Objective background facts only. Not a requirements dump. Ubl: keep it succinct.]

## 2. Goals

- [ ]

## 3. Non-goals (declined plausible goals)

Not “the system shouldn’t crash.” Each line is a reasonable goal we are **not** doing, and why.

| Declined goal | Why not this spec |
|---|---|
| [plausible alternative scope] | [ ] |
| [ ] | [ ] |

## 4. Use-cases

Agree these **before** debating solutions (Gerrit).

| ID | Actor | Interaction | Primary / secondary | In this spec? |
|---|---|---|---|---|
| UC-1 | [ ] | [ ] | primary | YES |
| UC-2 | [ ] | [ ] | secondary | [YES / MAY be out] |

## 5. Acceptance criteria (done)

- [condition that MUST be true to call the feature done]

## 6. Design / solution + trade-offs

[How it works, at the level that collects feedback — not an implementation manual.]

Trade-offs: [ ]

If there are no trade-offs, stop: write the code, or this is the wrong clock.

## 7. Alternatives considered

| Alternative | Strong | Weak | Decision |
|---|---|---|---|
| A — [chosen] | [ ] | [ ] | Chosen because [ ] on [date] |
| B — [ ] | [ ] | [ ] | Declined because [ ] |
| C — [ ] | [ ] | [ ] | Declined because [ ] |

## 8. Requirements (RFC 2119)

| ID | Text | Level | Owner | Verification (test / demo / analysis) | Pass/fail |
|---|---|---|---|---|---|
| R1 | The system MUST [interoperability or harm-prevention] | MUST | [name] | [named test] | [ ] |
| R2 | The system SHOULD [weighed default] | SHOULD | [name] | [ ] | [ ] |
| R3 | The system MAY [truly optional] | MAY | [name] | [ ] | [ ] |

No MUST without owner + test. No lowercase must/should as if they were BCP 14.

## 9. Privacy / security / telemetry

- Privacy: [data classes, retention, lawful basis / “no PII”]
- Security: [authn/z, threat notes]
- Telemetry: success metric [ ]; guardrail [ ]; **how measured** [ ]
- Tracing: do not reject unknown tracing headers (Azure public analogue); request-id on responses if API

## 10. Rollout / kill-in-prod / rollback

- Stages / canary: [ ]
- Feature flag: [name]
- Kill of **this feature in production**: [trigger + owner]
- Rollback: [steps]
- Capacity / promo spike: [ ]
- Customer-facing go/no-go is **not this document** — [Launch Brief](sand-workflow:launch-brief)
- Kill of the **bet** is [Kill Criteria](sand-workflow:kill-criteria)

## 11. Metrics clock

Launch: usage / errors / adoption. Scale: revenue / operational risk. This spec is on clock: [launch / scale].

## 12. API annex (if the system exposes HTTP)

Pointer only: [OpenAPI 3.1 / TypeSpec path]. The annex is the contract. It is **not** the PRD. Do not paste IDL into the body.

## ASK

[decide this spec / name the missing MUST owner / return to discovery]
Owner: [ ]  Date: [ ]
Holes: [ ]
