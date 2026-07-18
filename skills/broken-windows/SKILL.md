---
name: broken-windows
description: "Use when entering a codebase or file you'll be working in, when noticing decay (commented-out code, stale TODOs, skipped/disabled tests, dead branches, drifted docs), or when tempted to leave a small mess 'for later'."
---

# Broken Windows

One unfixed defect signals that defects are tolerated here, and the rate of new defects rises to match. The fix isn't a heroic cleanup sprint — it's a posture: when you see a broken window, you do one of three things, but never zero.

## When to use

- Opening a file you're about to edit and spotting rot
- Code review surfaces a small smell adjacent to the change
- A test is skipped/xfail'd and you can't tell why
- You're about to add a TODO without an owner or date

## Protocol

For each broken window, pick exactly one — never skip:

1. **Fix now** — if the cost is minutes and the scope is local. Comment-out dead code? Delete it. Confused name? Rename. Stale import? Remove.
2. **File and link** — if the fix is non-trivial, open a ticket *and* leave a one-line code comment pointing to it. Future readers know it's seen, not abandoned.
3. **Accept with reason** — if it's deliberate, say so in a comment: `// kept for backwards compatibility with v1.x clients, remove after 2026-12`. Acceptance with a date is fine; silent acceptance is not.

The forbidden fourth option is "walk past and say nothing".

## Common windows worth fixing-now

- Commented-out code older than a week → delete (git remembers)
- `TODO` / `FIXME` without owner or condition → add one or remove the marker
- Skipped test → unskip, delete, or document the skip with a follow-up
- A function that returns success on every failure path
- A doc block that disagrees with the code

## Red flags (rationalizations to reject)

- "Not my code, not my problem." — You're editing here; right now it is.
- "Cleanup is out of scope." — Three lines of cleanup expand scope by minutes. Pretending you didn't see expands it by months.
- "There are too many to fix all of them." — There are. Fix one. Then the next file you open has one fewer.

## Composes with

- [[dry-audit]] — duplicated knowledge is a recurring window.
- [[orthogonality-check]] — quiet coupling growth is the most expensive window.
- [[listen-to-nagging-doubts]] — a vague "this file feels bad" reaction is often a window cluster.
