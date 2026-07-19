---
name: consistent-terminology
description: "Use exactly one name for each concept throughout a document or codebase. Use when writing or reviewing docs, API references, UI text, or comments that name a concept more than once. Do not use across projects with separate established vocabularies."
---

# Consistent Terminology

In technical prose, different words claim different meanings. If a doc says "workspace" in one paragraph and "project" in the next, readers assume two concepts exist — and search, grep, and routing agents agree with them. Pick one term per concept and repeat it without apology.

## When to use

- A document names the same concept with two or more words
- The docs use a different word than the code or API ("directory" in prose, `folder` in the API)
- A reviewer asks whether two terms mean the same thing
- Search for the concept's name misses half the places it appears

## Protocol

1. **List the recurring concepts and confirm the candidate synonyms share one referent.** Check the code or the definitions. If two terms name different things, this skill does not apply — keep both terms and define each. For each true synonym set, pick one term; prefer the name the code or API already uses.
2. **Replace the synonyms.** If the API says `workspace`, the docs say "workspace" — never "project" or "environment" for the same thing.
3. **Never vary for style.** Swapping in synonyms to avoid repetition tells the reader a distinction exists where none does. Repetition of a term is precision, not bad writing.
4. **Verify by search.** Grep the document for the rejected synonyms. Replace each occurrence or record why it stays. Repeat after edits.

## Example

```
Before: Create a workspace, then add files to your project. The
        environment syncs automatically.
After:  Create a workspace, then add files to the workspace. The
        workspace syncs automatically.
```

## Red flags (rationalizations to reject)

- "Repeating the word reads badly." — In literature. In reference prose, repetition is what makes grep work.
- "Readers will infer they're the same." — Some will. Newcomers, translators, and agents will not.
- "The old term is entrenched." — Then migrate the docs to one term and note the alias once, in one place.

## Composes with

- [[concrete-over-figurative]] — a literal term is easier to keep consistent than an image.
- [[prefer-active-voice]] — naming actors consistently requires one canonical name per actor.
- [[dry-audit]] — synonym sprawl is duplicated knowledge in vocabulary form.
