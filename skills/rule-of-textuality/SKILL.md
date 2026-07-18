---
name: rule-of-textuality
description: "Use when choosing a serialization for configs, logs, IPC, or persisted state. Also use when reviewing a proposal to introduce a binary protocol, custom marshalling format, or 'efficient' opaque blob."
---

<!-- DO NOT EDIT — generated from knowledge/ by scripts/sync_knowledge.py -->

# Rule of Textuality

Plain text is the universal solvent. Anything textual can be grep'd, diff'd, version-controlled, fixed by hand at 3am, and inspected by tools nobody has written yet. Binary formats foreclose all of that for a transient gain — usually one nobody actually measured.

## When to use

- Picking a config or interchange format (text vs binary)
- Designing a log format, on-disk format, or IPC payload
- Tempted to introduce protobuf/MessagePack/custom struct dumps for "performance"
- Reviewing an opaque blob that can only be read by the program that wrote it

## Protocol

1. **Pick textual by default** — JSON, TOML, YAML, RFC-822 style, CSV, line-record formats. Whatever fits the structure of the data with the least ceremony.
2. **Require a measured reason to go binary.** "Throughput", "size", "speed" need a profile and a budget, not vibes. Often the text version is good enough by orders of magnitude.
3. **If you must use binary, build a text twin.** A `--dump` or `--inspect` mode that emits the equivalent text representation. Never ship a format you can't print.
4. **Make textual formats line-oriented when you can.** One record per line means standard tools (grep, awk, cut, sort, uniq, head, tail) just work — for free, forever.
5. **Be conservative about format choice.** Cute custom syntax is a forever cost; existing standards (JSON, INI, RFC-822) are free leverage.

## Red flags (rationalizations to reject)

- "Text is too slow / too big." — Measure. For most workloads the gap is invisible; for the rest, compression is one pipe stage away.
- "Nobody reads it by hand." — Until the day production breaks and you'd kill for the ability to.
- "Binary is more typed/safer." — Type safety belongs in the parser, not the byte layout. A schema'd text format gives you both.

## Composes with

- [[rule-of-composition]] — text is what pipelines speak; binary breaks the chain.
- [[rule-of-robustness]] — textual formats let you be liberal in what you accept and audit what you emit.
- [[prove-dont-assume]] — text means you can actually see the bytes when something looks wrong, instead of trusting the marshaller.
- [[dry-audit]] — a textual canonical format prevents the "code knows X, fixture knows Y, doc says Z" drift.
