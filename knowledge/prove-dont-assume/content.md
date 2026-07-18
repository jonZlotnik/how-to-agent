# Prove, Don't Assume

Most debugging dead-ends are paved with unverified assumptions. "It should be non-null here." "This function returns sorted output." "The cache is invalidated." *Should* is not evidence. Replace every load-bearing belief with a cheap check.

## When to use

- Investigation has stalled and you can't tell which step is wrong
- About to make a non-trivial change to unfamiliar code
- A library's behavior at a boundary matters to your fix
- Someone (including yourself, including an AI) said something that *sounds* right

## Protocol

1. **List the assumptions** the current plan depends on. Write each as a falsifiable sentence: "X is non-null when reaching line Y."
2. **For each, write the one-line check.** A `print`, `assert`, log line, REPL evaluation, or a one-line test. Cheapness matters — if it's hard to verify, refactor until it isn't.
3. **Run the checks.** Don't predict the outcome before running; predictions bias what you see.
4. **Act only on what survived.** Cross off the disproven assumptions. The bug usually lives in the gap between what you believed and what you measured.
5. **Leave the cheapest checks in** as assertions or tests where they'd catch future regressions.

## Red flags (rationalizations to reject)

- "I just read the code, it's obvious." — Reading proves nothing. Run it.
- "Adding a print is overkill." — Five seconds of printf > thirty minutes of theorizing.
- "I'm sure the library does X." — Sure enough to run a one-line test? Then prove it.
- "The types guarantee this." — Types catch a lot. They don't catch runtime data, third-party JSON, or stale caches.

## Composes with

- [[fix-the-problem-not-the-blame]] — proof-driven hypothesis testing is the workhorse step of root-cause analysis.
- [[design-by-contract]] — assumptions you verify often deserve to become contracts so they can't silently break later.
- [[listen-to-nagging-doubts]] — when a doubt resists naming, "what would I check?" turns it into a falsifiable assumption.
