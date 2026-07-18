---
name: fix-the-problem-not-the-blame
description: "Use when investigating any bug, test failure, crash, or unexpected behavior — establishes root-cause-first debugging mindset before proposing or applying any fix."
---

<!-- DO NOT EDIT — generated from knowledge/ by scripts/sync_knowledge.py -->

# Fix the Problem, Not the Blame

The goal of debugging is to understand. Blaming the compiler, the OS, the library, "flaky tests", or the user is almost always wrong and always premature. Start from the assumption that your code is the culprit, gather facts, and let the evidence — not intuition — drive the fix.

## When to use

- Any bug, test failure, or "it worked yesterday" report
- A symptom is reproducible but its cause is unclear
- You're tempted to wrap something in a try/except, retry, or `if not None` check to make it go away
- A teammate or LLM suggests "must be a flake, just rerun"

## Protocol

1. **Don't panic.** Take ten seconds. Panic-debugging spreads damage to working code.
2. **Reproduce reliably** before changing anything. If you can't trigger it on demand, you can't verify the fix. Capture the minimal repro.
3. **Read the actual error.** Not the summary, not what you expect — the literal message, the literal stack, the literal values. Half of bugs surrender here.
4. **Default suspicion to your own code.** Libraries and platforms have bugs, but they're rare compared to yours. Eliminate yours first.
5. **Form one hypothesis at a time.** Predict what you'd see if it's true. Test that prediction with a check that can fail. Update; don't accumulate.
6. **Find the root cause, not a symptom that disappears.** A fix you can't explain is a fix that will return.

## Red flags (rationalizations to reject)

- "It must be a compiler bug." — Almost never. Look again.
- "The test is flaky." — Sometimes true. More often the test exposes a real race or order dependency you don't want to face.
- "Adding a retry / try-except makes it pass." — Pass is not fix. You hid a problem that will resurface louder.
- "I don't know why this works now." — Then it doesn't work. See [[prove-dont-assume]].
- "Good enough, ship it." — A bug you don't understand will pick its own moment to reappear.

## Composes with

- [[prove-dont-assume]] — every step of the hypothesis must be verified, not believed.
- [[listen-to-nagging-doubts]] — the "this still feels off" feeling after a green test is data; chase it.
- [[crash-early]] — once the root cause is known, replace any masking handler with a hard failure so future occurrences are loud.
- [[design-by-contract]] — if a precondition was silently violated, add the contract so the next violation is impossible to ignore.
