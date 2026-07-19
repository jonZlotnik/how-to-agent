---
name: prefer-active-voice
description: "Rewrites passive sentences so a named actor performs the action. Use when drafting or reviewing docs, comments, commit messages, or error messages. Do not use when the actor is unknown or irrelevant and naming one would mislead."
---

# Prefer Active Voice

Passive voice hides the actor, and in technical prose the actor is usually the information the reader needs. "The file is deleted" does not say who deletes it or when. "The daemon deletes the file after upload" does. Default to active; use passive only as a deliberate choice.

## When to use

- A sentence uses a form of "be" plus a past participle: "is handled", "was created", "are validated"
- A reader could ask "by whom?" or "by what?" and the text does not answer
- An error message or doc leaves the responsible component unnamed
- A commit message says what "was changed" instead of what the change does

## Protocol

1. **Find the passives.** Search the text for "is/are/was/were/been/being" followed by a past participle.
2. **Name the actor you can verify.** "The config is read at startup" → "The server reads the config at startup" — only if the code or observed behavior confirms the server does it. If you cannot verify the actor, keep the passive rather than guess: a wrong actor is a fabricated fact, and worse than a missing one.
3. **Keep passive only on purpose.** When the actor is truly unknown or irrelevant ("the packet was corrupted in transit"), passive is correct. Make it a decision, not a default.
4. **Recheck the revision.** Scan the result for remaining passives. Fix each one or record why it stays.

## Example

```
Before: The cache is invalidated when the config is changed.
After:  Saving the config invalidates the cache.
```

## Red flags (rationalizations to reject)

- "Passive sounds more objective." — It sounds evasive. Objectivity comes from accuracy, not hidden actors.
- "We don't want to assign blame." — Name the component, not a person: "the migration dropped the index".
- "Everyone writes docs this way." — Common is not clear. The reader still has to guess the actor.

## Composes with

- [[omit-needless-words]] — active rewrites are usually shorter.
- [[consistent-terminology]] — naming the actor forces you to pick its one canonical name.
