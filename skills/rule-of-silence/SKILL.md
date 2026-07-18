---
name: rule-of-silence
description: "Use when adding logging, progress messages, or 'success' notifications to a tool. Also use when reviewing CLI output that includes banners, decorations, status lines, or 'Done!' messages that downstream consumers will have to strip."
---

<!-- DO NOT EDIT — generated from knowledge/ by scripts/sync_knowledge.py -->

# Rule of Silence

When a program has nothing surprising to say, it should say nothing. Useful information should flow downstream; ceremony, banners, and self-congratulation should not. Silence is honest: the absence of output is a signal that nothing went wrong.

## When to use

- Adding logs or progress output to a tool that may be scripted
- A CLI prints an "Operation completed successfully." banner alongside its real output
- A library wraps every call site with an "Entering function X" log
- Output includes ANSI color or table formatting that other tools will have to undo

## Protocol

1. **Distinguish output from chatter.** Output is *the answer*: data the caller asked for. Chatter is everything else. Send chatter to stderr (or a log file), not stdout.
2. **On success, default to silent.** Print only what was asked for. Empty output on success is a feature.
3. **Make chatter opt-in.** `-v` / `--verbose` / `RUST_LOG=…` for progress. Quiet stays the default.
4. **On failure, be loud and specific** — stderr, non-zero exit, a real error message ([[crash-early]]). The contrast with the quiet success path is what makes failure detectable.
5. **Never decorate piped output.** No headers, no totals, no "Found N results" lines mixed into the data stream. If you want a summary, make it a separate command or a `--summary` flag.

## Red flags (rationalizations to reject)

- "Users like to see that it's working." — Add a `--progress` flag for humans. Don't impose it on every script that pipes through you.
- "Silence is scary." — Scarier still: a "success" line that fired even though the real work silently failed two layers down.
- "It's just one log line." — Multiplied by every tool in the pipeline, it's a wall of noise that hides the actual signal.

## Composes with

- [[rule-of-composition]] — pipelines depend on clean streams; chatter on stdout breaks them.
- [[crash-early]] — silence on success only works because failure is loud and specific.
- [[rule-of-least-surprise]] — silent success matches the convention every Unix tool already follows.
- [[prove-dont-assume]] — assertions can fail loudly without polluting the stdout of the happy path.
