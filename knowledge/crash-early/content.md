# Crash Early

A program that has wandered into an impossible state is no longer your program. Every line it executes afterwards is operating on a lie. The earlier and louder it stops, the smaller the blast radius, the more honest the diagnostic, and the less time you spend later wondering how data got into that shape.

## When to use

- Writing any `try`/`catch`, `except`, `Result::unwrap_or`, `?? defaultValue` branch
- Adding a "just in case" `if value is None` guard
- A library returns an unexpected error and you're tempted to log-and-continue
- Reviewing code that catches a broad exception class

## Protocol

Classify every error path into one of three buckets, then act accordingly:

1. **Bug ("impossible" state).** Assertion or hard abort. This is a contract violation ([[design-by-contract]]) — your program now lies if it keeps running. Examples: invariant broken, null where the type forbids it, "this branch is unreachable".
2. **Exceptional (rare, recoverable, real).** Raise/return an error type. The caller must explicitly handle or propagate. Examples: network timeout, disk full, lock contention.
3. **Expected (normal control flow).** Handle locally with a normal return value. Examples: user not found in a lookup, end-of-stream, optional config missing.

Confusion among the three is the source of most "silent corruption" bugs. The cure is to *name the bucket* in the comment, type, or error name. `BugError`, `ConfigMissing`, `Result<T, NetworkError>`.

## Specific anti-patterns to refuse

- `except Exception: pass` — bug-class swallowing. Crash.
- `if x is None: return None` for an x that should never be None — invents a sentinel; future code can't tell bug from expected.
- A retry loop around a deterministic error — retrying a bug just makes it slower.
- A fallback that masks the failure ("oh well, we'll use the default") when the failure means data loss.

## Red flags (rationalizations to reject)

- "We can't let it crash in production." — Crashing on a violated contract is *better* than continuing on corrupted state. Recover at the *process* boundary (supervisor, retry-the-request), not by lying to your own code.
- "I'll log and continue." — Logging is not handling. Now you have corrupted state *and* noise.
- "Defensive programming is safer." — Defending against impossible states *creates* the conditions for them to go unnoticed.

## Composes with

- [[design-by-contract]] — crash-early is how a violated contract gets enforced.
- [[fix-the-problem-not-the-blame]] — a clean crash with a real stack trace is the cheapest possible bug report.
- [[prove-dont-assume]] — assertions that crash early are the lasting form of "prove it".
- [[listen-to-nagging-doubts]] — when a fallback feels like it's hiding something, it usually is.
