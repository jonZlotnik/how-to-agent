# how-to-agent

An **agent-agnostic knowledge library** for coding agents. One canonical source of
software-engineering lessons, projected into the native format of each agent —
Claude Code, Cursor, and OpenAI Codex (plus anything else that reads `AGENTS.md`).

"I just want my child to make good decisions" — every parent ever

## How it works

The canonical content lives in `knowledge/` and uses no agent-specific vocabulary.
Each entry is a directory with two files:

```
knowledge/<name>/
├── meta.yaml     # generic metadata: title, summary, when_to_use, related
└── content.md    # the lesson itself, pure markdown
```

A generator projects every entry into each agent's native format. **Generated files
are committed** so the repo works on clone, and they carry a `DO NOT EDIT` banner —
edit `knowledge/` instead and regenerate.

| Agent | Generated output | Trigger model |
|---|---|---|
| Claude Code | `skills/<name>/SKILL.md` | skill description ← `when_to_use` |
| Cursor | `.cursor/rules/<name>.mdc` | "Apply Intelligently" rule ← `when_to_use` |
| Codex & AGENTS.md-aware tools | `AGENTS.md` | compact index; agent opens the linked entry on match |

## Install

### Claude Code

```
/plugin marketplace add jonZlotnik/how-to-agent
/plugin install how-to-agent
```

### Cursor

Copy `.cursor/rules/` into your project (or open this repo as the project). The
rules are "Apply Intelligently" — Cursor attaches each one when its description
matches the task.

### Codex (and other AGENTS.md-aware tools)

Place this repo's `AGENTS.md` at your project root (or reference this repo). It is
a compact index: when a task matches an entry's *Use when* description, the agent
opens the linked `knowledge/<name>/content.md` and follows it.

## Adding or editing knowledge

1. Create or edit `knowledge/<name>/meta.yaml` and `knowledge/<name>/content.md`
   (`<name>` is kebab-case; it is the entry's identity).
2. Run `python3 scripts/sync_knowledge.py` (Python 3, no dependencies).
3. Commit both the canonical entry and the regenerated outputs. CI runs
   `sync_knowledge.py --check` and fails on drift.

`meta.yaml` schema:

```yaml
title: Broken Windows          # human display name
summary: >-                    # one/two sentences: what this knowledge IS
  Never silently walk past a small defect...
when_to_use: >-                # the trigger: WHEN an agent should pull this in
  Use when entering a codebase and noticing decay...
related:                       # optional: names of related entries
  - dry-audit
tags: [hygiene]                # optional
```

Only a **strict YAML subset** is supported (keeps the generator dependency-free):
plain `key: value`, quoted strings, `>-`/`|` block scalars, flow lists `[a, b]`,
and `- item` block lists. The generator hard-errors on anything else.

## Content

Current library (37 entries):

- Lessons distilled from Hunt & Thomas's *The Pragmatic Programmer*
- Lessons distilled from Eric S. Raymond's *The Art of Unix Programming*
- `pqc-*` entries distilled from Nadim Kobeissi's *Post-Quantum Migration Playbook*

## Attribution

The knowledge content is adapted from
[AdaJane/pragmatic-programmer-skills](https://github.com/AdaJane/pragmatic-programmer-skills)
by Ada Jane Anderson (MIT), which distills the books listed above. This repository
restructures that content into an agent-agnostic canonical form and adds the
multi-agent projection tooling.

## License

[MIT](LICENSE) © Ada Jane Anderson, Jon Zlotnik
