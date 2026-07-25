# Do things that don't scale

The scale check. Raise it the moment someone proposes automating, building infrastructure for, or "properly engineering" something nobody has used yet.

---

## The argument

At the start of anything, the manual version is not a compromise you tolerate until the real one is ready. **It is the fastest route to the only thing that matters early: real feedback from real users.**

Onboard the first users by hand. Send the emails yourself. Run the process in a spreadsheet. Do the thing personally, badly, for ten people.

Premature scaling costs twice. It spends the time — and it **removes the direct contact that would have told you what to build**. The automated version puts a layer between you and the user precisely when you most need to see their face while they are confused.

The scaled version of the wrong thing is worse than no version, because now it is expensive to change and there is sunk cost arguing for keeping it.

---

## The question to ask

> What would you learn from ten users done by hand that you cannot learn from the automated version?

The answer is usually "everything that matters", and it arrives weeks earlier.

Manual contact surfaces things instrumentation never will: where they hesitate, what they call things, the question they ask before starting, the workaround they already have, the reason they would not pay. None of that appears in a funnel chart, and all of it changes what should be built.

---

## The counter-argument, taken seriously

"This doesn't scale" is sometimes a real objection rather than premature optimisation. It is worth separating the cases honestly, because a skill that dismisses every scaling concern will be ignored by anyone who has been burned.

**Automate when:**

- The manual version is **provably working** — people want the outcome and come back for it
- The volume genuinely hurts, now, not in a projection
- The manual step is the **bottleneck on learning** rather than the source of it
- It is a **regulatory or safety** requirement, where the manual version is not acceptable at any volume

**Keep it manual when:**

- You have not yet talked to ten users
- You are not sure what the product is
- The automation would take longer than the manual version for the next month
- The manual step is where you learn what to build

**The tell that it is premature:** the person can describe the system they want to build in more detail than they can describe the user they are building it for.

---

## Experiment rate

The world changes fast enough that the rate of experimentation has to match it. A plan executed perfectly over twelve months, against assumptions that were true when it was written, loses to twelve experiments run in the same period.

Practically:

- **Prefer many small tests to one large bet**, when the information gained is comparable. Not always — some things cannot be tested small — but the default should be many.
- **Size an experiment by the cost of being wrong**, not the cost of running it. A cheap experiment whose failure is unrecoverable is not cheap.
- **Run experiments that can actually fail.** A test whose outcome cannot surprise you is a demonstration, and it produces no knowledge.

---

## Turning failure into knowledge

Failure produces feedback, feedback becomes knowledge, knowledge compounds. But only one thing makes that chain hold:

> **Write down what you expected, before you run it.**

Without a recorded expectation, a failure is just a loss. You cannot tell whether the idea was wrong, the execution was wrong, or it needed longer — and those have completely different lessons. Afterwards, memory reconstructs an expectation that conveniently matches the outcome, which feels like learning and is not.

The minimum viable record, two lines before starting:

```
Expect: [what happens if the idea is right — with a number where possible]
Kills it: [the result that would tell me the idea is wrong]
```

Then afterwards, one line on which it was and what changes because of it.

That is the entire discipline, it costs a minute, and it is the difference between ten experiments that compound and ten that produce ten separate opinions.

**The failure that teaches nothing** is the one where the expectation was never stated, so every outcome gets absorbed as "we learned a lot" and nothing specific changes. If you cannot name what is different in the next cycle, the failure was just cost.
