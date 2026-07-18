---
name: lead-with-the-point
description: "State the conclusion or instruction first, then the supporting detail. Use when structuring a document, section, comment, commit message, or reply. Do not use where sequence is the content, such as step-by-step tutorials."
---

# Lead With the Point

Readers decide in the first sentence whether to keep reading. Put the conclusion there: what changed, what to do, or what is true. Background, reasoning, and caveats come after, ordered so the reader can stop at any paragraph and lose only detail, never the message.

## When to use

- A commit message, PR description, or reply opens with background instead of the change
- A doc section makes the reader scroll to learn what it concludes
- A comment explains history before stating what the code does
- You catch yourself writing "First, some context"

## Protocol

1. **Write the point in one sentence.** What changed, what to do, or what is true. Put it first.
2. **Order the rest by decreasing importance.** Reasons, then evidence, then caveats, then history. Each paragraph should matter less than the one before it.
3. **Apply the rule per section.** In multi-section documents, the first sentence of each section states that section's conclusion.
4. **Test by first sentences.** Read only the first sentence of each paragraph. If the message does not come through, restructure and test again.

## Example

```
Before: While investigating the login timeouts we noticed the pool was
        misconfigured, and after discussion we decided to raise the size.
After:  Raise the connection pool size from 10 to 50. Login requests
        were timing out because the pool was exhausted under load.
```

## Red flags (rationalizations to reject)

- "The reader needs context first." — The point *is* the context for everything else. Lead with it.
- "The conclusion needs its caveats." — State the conclusion, then the caveats. Never bury the verdict inside them.
- "It feels blunt." — Blunt is a feature in technical prose. The reader came for the point.

## Composes with

- [[one-idea-per-sentence]] — a clear lead sentence carries exactly one idea.
- [[omit-needless-words]] — throat-clearing openings are needless words in front of the point.
