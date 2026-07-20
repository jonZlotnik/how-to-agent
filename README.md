# how-to-agent

[![validate-skills](https://github.com/jonZlotnik/how-to-agent/actions/workflows/validate-skills.yml/badge.svg)](https://github.com/jonZlotnik/how-to-agent/actions/workflows/validate-skills.yml)
[![skill-quality](https://github.com/jonZlotnik/how-to-agent/actions/workflows/skill-quality.yml/badge.svg)](https://github.com/jonZlotnik/how-to-agent/actions/workflows/skill-quality.yml)

A library of **Agent Skills** — small, sharp software-engineering lessons on
decision-making, debugging, hygiene, defensive design, and Unix-style composition.

Each skill is a plain [`SKILL.md`](https://agentskills.io) file: the **open standard**
(originally from Anthropic) that ~40 tools read natively — Claude Code, OpenAI Codex,
Cursor, GitHub Copilot, Gemini CLI, and more. Write the lesson once; every
skills-compatible agent can load it on demand.

## Layout

```
skills/<name>/
└── SKILL.md      # frontmatter (name, description) + the lesson in markdown
rules/
└── core.md       # always-on rules, loaded into every session via rulesync
```

Nothing is generated — `SKILL.md` *is* the portable format. Agents use
**progressive disclosure**: at startup they read only each skill's `name` and
`description`; when a task matches the description, the full file is loaded.

## Skills vs. always-on rules

The two directories split by trigger:

- A **skill** has a clear trigger ("entering code", "writing error handling").
  The agent loads it when the trigger fires, so its lesson costs nothing the
  rest of the time.
- An **always-on rule** has no trigger — it applies to every action. The
  writing rules are the core example: agents write prose in every session, so
  "use literal language" cannot wait for a skill to fire. These live in
  [rules/core.md](rules/core.md), which rulesync compiles into each tool's
  always-loaded file (`CLAUDE.md`, `AGENTS.md`, `.cursor/rules`, …).

Add a rule only if it must apply when no skill fires; otherwise write a skill.
Every rule line loads in every consumer session forever, so CI enforces a
60-line ceiling on rule files and checks that each `[[link]]` resolves to a
skill.

## Use it in your project

### Any agent — via [rulesync](https://github.com/dyoshikawa/rulesync)

[rulesync](https://github.com/dyoshikawa/rulesync) fetches shared skills and rules from a
repo and generates the right files for 30+ tools. This is the only path that installs
the always-on rules. From your project:

```bash
npx rulesync fetch jonZlotnik/how-to-agent --features rules,skills
npx rulesync generate --targets "*" --features rules,skills
```

### Claude Code — via the plugin (global, one command)

Loads the skills in every project from your user install, no per-project copy.
The plugin ships skills only — use rulesync to install the always-on rules:

```
/plugin marketplace add jonZlotnik/how-to-agent
/plugin install how-to-agent
```

### Any agent — manual copy

Skills are self-contained folders. Copy the ones you want into your agent's skills
directory (e.g. `.claude/skills/`, or your tool's documented location — see the
[agentskills.io client list](https://agentskills.io/clients)):

```bash
git clone --depth 1 https://github.com/jonZlotnik/how-to-agent
cp -r how-to-agent/skills/broken-windows ~/.claude/skills/
```

## Adding or editing a skill

1. Create `skills/<name>/SKILL.md` (`<name>` is kebab-case and must match the
   frontmatter `name`).
2. Frontmatter needs `name` and `description` — the description is the trigger the
   agent matches against. Write it in three parts: a third-person verb summary of
   what the skill does, then "Use when" triggers, then a "Do not use" boundary:

   ```yaml
   ---
   name: broken-windows
   description: "Fixes, files, or deliberately accepts each small defect — never
     ignores one. Use when entering code you will work in, noticing decay (stale
     TODOs, skipped tests, dead code), or leaving a mess 'for later'. Do not use
     to justify unscoped rewrites."
   ---
   ```

   The `writing-agent-skills` skill is the authoritative guide to this pattern.
3. Write the lesson below the frontmatter. Optionally bundle `scripts/`,
   `references/`, or `assets/` in the skill folder — the standard supports it.

That's the whole workflow. No build step; commit the file.

## Content

Current library (29 skills):

- Lessons distilled from Hunt & Thomas's *The Pragmatic Programmer*
- Lessons distilled from Eric S. Raymond's *The Art of Unix Programming*
- Technical-writing skills distilled from Strunk & White's *The Elements of
  Style*, William Zinsser's *On Writing Well*, and Google's developer
  documentation style guide
- A meta-skill on authoring skills (`writing-agent-skills`), informed by
  Anthropic's [skill-creator](https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md),
  [obra/superpowers' writing-skills](https://github.com/obra/superpowers/blob/main/skills/writing-skills/SKILL.md),
  and this repository's own CI findings

## Attribution

The Pragmatic Programmer and Unix skills are adapted from
[AdaJane/pragmatic-programmer-skills](https://github.com/AdaJane/pragmatic-programmer-skills)
by Ada Jane Anderson (MIT). The technical-writing skills are original to this
repository and distill the sources listed above.

## License

[MIT](LICENSE) © Ada Jane Anderson, Jon Zlotnik
