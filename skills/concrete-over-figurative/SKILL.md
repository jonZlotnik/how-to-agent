---
name: concrete-over-figurative
description: "Replaces metaphor and decorative wording with literal, specific language. Use when writing or reviewing technical prose — docs, comments, commit messages, error text. Do not use for deliberately narrative writing such as talks or essays."
---

# Concrete Over Figurative

Technical prose exists to transfer facts, and metaphor makes the reader interpret an image before reaching the fact. "Excavate the requirement" means "identify the requirement". "A load-bearing assumption" means "an assumption the design depends on". The literal version costs nothing to decode, translates across languages and readers, and states exactly one thing.

## When to use

- A verb is an image: excavate, surface, sprout, bubble up, drill down, journey
- A qualifier is intensity without measurement: "blazing fast", "rock solid", "massive"
- A reviewer or reader asks what a phrase means
- Text will be read by non-native speakers or by agents matching on descriptions

## Protocol

1. **Find the images.** Read the text for words describing physical actions or objects that are not literally present.
2. **State what each image stands for.** "The config sprouts conditionals" → "the config accumulates conditionals". If no literal statement exists behind the image, the sentence has no content — delete it.
3. **Replace intensity with facts you have — never invent them.** If a measurement exists in the code, a benchmark, or your own observation, use it: "huge file" → "a 2 GB file". If no measurement exists, do not fabricate one: delete the intensity claim, name its source, or ask. An invented number is worse than a vague word — the vague word is visibly vague, while the invented number looks authoritative.
4. **Re-read for residue.** If any remaining term requires the reader to interpret an image, replace it and read again.

## Example

```
Before: Excavate the real need — treat every load-bearing assumption
        with care before the design calcifies.
After:  Identify the real need. Confirm every assumption the design
        depends on before the design becomes expensive to change.
```

## Red flags (rationalizations to reject)

- "It reads as boring without style." — Reference prose earns nothing from style. It earns from precision.
- "Everyone knows the metaphor." — Non-native readers, newcomers, and routing agents do not.
- "The image explains it faster." — Then keep the image *and* state the literal fact. Never the image alone.
- "A specific number reads better." — Only when it is real. A fabricated measurement is a correctness bug dressed as style.

## Composes with

- [[omit-needless-words]] — decorative wording is needless by definition.
- [[consistent-terminology]] — metaphors drift; a literal term stays fixed.
- [[prove-dont-assume]] — replacing intensity with measurement forces you to actually measure.
