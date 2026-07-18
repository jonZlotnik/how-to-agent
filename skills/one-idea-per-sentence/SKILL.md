---
name: one-idea-per-sentence
description: "Split sentences and paragraphs so each carries a single idea. Use when a sentence chains clauses with 'and', 'which', or dashes, or when a paragraph covers several topics. Do not use where joining two ideas expresses a real dependency between them."
---

# One Idea Per Sentence

A sentence that carries two ideas makes the reader hold both while parsing the join. Technical readers are already holding the system in their head; spend their attention on the content, not the syntax. Short declarative sentences are the cheapest way to be understood.

## When to use

- A sentence runs past ~25 words or stacks clauses with "and", "which", "while", or dashes
- A reader must re-read a sentence to parse it
- A paragraph discusses more than one topic
- A doc review comment says "unclear" without pointing to a specific error

## Protocol

1. **Flag the overloaded sentences.** Look for length past ~25 words, two or more conjunctions, or nested subordinate clauses.
2. **Split at the clause boundaries.** Give each new sentence its own subject and verb. "The parser reads the header, which contains the version, and rejects unknown versions" → "The parser reads the version from the header. It rejects unknown versions."
3. **Keep one topic per paragraph.** The first sentence names the topic. Move stray sentences to the paragraph where they belong.
4. **Re-read for parse cost.** If any sentence still takes two readings, split it again. Stop when each sentence parses on the first pass.

## Example

```
Before: The exporter, which runs nightly and is configured in cron.yaml,
        writes CSVs to the bucket while also pruning files older than
        30 days, unless pruning is disabled.
After:  The exporter runs nightly; see cron.yaml. It writes CSVs to the
        bucket. It also prunes files older than 30 days unless pruning
        is disabled.
```

## Red flags (rationalizations to reject)

- "Short sentences feel choppy." — Choppy beats ambiguous. Rhythm is not a goal of reference prose.
- "The ideas are related." — Related ideas belong in the same paragraph, not the same sentence.
- "Joining shows sophistication." — It shows the reader a puzzle. Sophistication is being understood once.

## Composes with

- [[omit-needless-words]] — splitting exposes connective filler you can delete.
- [[lead-with-the-point]] — single-idea sentences make the lead sentence possible.
