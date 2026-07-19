---
name: omit-needless-words
description: "Deletes words that add no information. Use when revising any prose before publishing or committing it — docs, comments, commit messages, error messages, UI text. Do not use where cutting would remove precision or a necessary qualification."
---

# Omit Needless Words

Every word in technical prose should carry information. Filler phrases, redundant modifiers, and throat-clearing make the reader work harder for the same content. Concise text is not terse text: keep every word the meaning needs, and delete the rest.

## When to use

- A draft is finished and ready for a revision pass
- A sentence contains "in order to", "the fact that", "it should be noted", or similar filler
- A modifier restates what the word already says ("completely eliminate", "end result")
- A comment or doc paragraph is longer than the code it explains

## Protocol

1. **Delete filler phrases.** "In order to" → "to". "It should be noted that X" → "X". "There is a config option that controls" → "A config option controls".
2. **Delete redundant modifiers.** "Completely eliminate" → "eliminate". "Basically", "very", "quite", "actually" — delete them; keep one only if its removal changes the sentence's meaning.
3. **Replace phrases with words.** "Is able to" → "can". "In the event that" → "if". "At this point in time" → "now". "Has the ability to" → "can".
4. **Repeat until stable.** Re-read the text. If deleting a word does not change the meaning, delete it and read again. Stop when every remaining word is doing work.

## Example

```
Before: It should be noted that in order to run the tests, you will first
        need to make sure that the database is actually running.
After:  To run the tests, first start the database.
```

## Red flags (rationalizations to reject)

- "The longer version sounds more professional." — It sounds padded. Authority comes from precision.
- "The extra words soften the message." — Softening an instruction makes it ambiguous. Say what to do.
- "Readers can skim past filler." — Readers cannot tell filler from content until they have read both.

## Composes with

- [[one-idea-per-sentence]] — cutting words often reveals that one sentence was two.
- [[lead-with-the-point]] — deleted throat-clearing usually hid the point in the second paragraph.
- [[concrete-over-figurative]] — decorative wording is a form of needless words.
