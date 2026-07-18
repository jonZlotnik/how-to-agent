#!/usr/bin/env python3
"""Project canonical knowledge/ entries into agent-specific formats.

  knowledge/<name>/{meta.yaml,content.md}   (canonical, hand-written)
      -> skills/<name>/SKILL.md             (Claude Code)
      -> .cursor/rules/<name>.mdc           (Cursor "Apply Intelligently" rule)
      -> AGENTS.md                          (index for Codex & AGENTS.md-aware tools)

Usage:
  python3 scripts/sync_knowledge.py           # regenerate all outputs
  python3 scripts/sync_knowledge.py --check   # exit non-zero if outputs drift

Stdlib only. meta.yaml must use the strict YAML subset documented in README.md:
plain `key: value`, quoted strings, `>-`/`|` block scalars, flow lists [a, b],
and `- item` block lists. Anything else is a hard error.
"""

import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
KNOWLEDGE = REPO / "knowledge"
SKILLS = REPO / "skills"
CURSOR_RULES = REPO / ".cursor" / "rules"
AGENTS_MD = REPO / "AGENTS.md"

BANNER = "<!-- DO NOT EDIT — generated from knowledge/ by scripts/sync_knowledge.py -->"
REQUIRED_FIELDS = ("title", "summary", "when_to_use")
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
KEY_RE = re.compile(r"^([A-Za-z_][A-Za-z0-9_]*):(.*)$")


def die(msg: str) -> None:
    sys.exit(f"sync_knowledge: error: {msg}")


def unquote(value: str, where: str) -> str:
    if value.startswith('"') or value.startswith("'"):
        q = value[0]
        if len(value) < 2 or not value.endswith(q):
            die(f"{where}: unterminated quoted string")
        return value[1:-1]
    return value


def parse_meta(text: str, path: Path) -> dict:
    """Parse the strict YAML subset. Hard-error on anything unsupported."""
    data: dict = {}
    lines = text.split("\n")
    i = 0
    while i < len(lines):
        line = lines[i]
        where = f"{path}:{i + 1}"
        if not line.strip() or line.lstrip().startswith("#"):
            i += 1
            continue
        if line[0] in (" ", "\t"):
            die(f"{where}: unexpected indentation (dangling block line?)")
        m = KEY_RE.match(line)
        if m is None:
            die(f"{where}: expected `key: value`, got {line!r}")
        key, rest = m.group(1), m.group(2).strip()
        if key in data:
            die(f"{where}: duplicate key {key!r}")

        if rest in (">", ">-", "|", "|-"):
            # Block scalar: collect lines indented by two spaces.
            block: list[str] = []
            i += 1
            while i < len(lines) and (lines[i].startswith("  ") or not lines[i].strip()):
                block.append(lines[i][2:] if lines[i].startswith("  ") else "")
                i += 1
            while block and not block[-1].strip():
                block.pop()
            if not block:
                die(f"{where}: empty block scalar for {key!r}")
            if rest.startswith(">"):
                data[key] = " ".join(l.strip() for l in block if l.strip())
            else:
                data[key] = "\n".join(block)
            continue

        if rest == "":
            # Block list: `- item` lines indented by two spaces.
            items: list[str] = []
            i += 1
            while i < len(lines) and (lines[i].startswith("  - ") or not lines[i].strip()):
                if lines[i].strip():
                    items.append(unquote(lines[i].strip()[2:].strip(), where))
                i += 1
            if not items:
                die(f"{where}: key {key!r} has no value and no list items")
            data[key] = items
            continue

        if rest.startswith("["):
            if not rest.endswith("]"):
                die(f"{where}: flow list must open and close on one line")
            inner = rest[1:-1].strip()
            data[key] = (
                [unquote(s.strip(), where) for s in inner.split(",")] if inner else []
            )
            i += 1
            continue

        data[key] = unquote(rest, where)
        i += 1
    return data


def load_entries() -> list[dict]:
    if not KNOWLEDGE.is_dir():
        die(f"missing canonical directory {KNOWLEDGE}")
    entries = []
    for entry_dir in sorted(p for p in KNOWLEDGE.iterdir() if p.is_dir()):
        name = entry_dir.name
        if not NAME_RE.match(name):
            die(f"{entry_dir}: entry name must be kebab-case")
        meta_path = entry_dir / "meta.yaml"
        content_path = entry_dir / "content.md"
        if not meta_path.is_file():
            die(f"{entry_dir}: missing meta.yaml")
        if not content_path.is_file():
            die(f"{entry_dir}: missing content.md")
        meta = parse_meta(meta_path.read_text(encoding="utf-8"), meta_path)
        for field in REQUIRED_FIELDS:
            if not meta.get(field):
                die(f"{meta_path}: missing or empty required field {field!r}")
        entries.append(
            {
                "name": name,
                "meta": meta,
                "content": content_path.read_text(encoding="utf-8"),
            }
        )
    if not entries:
        die(f"{KNOWLEDGE} contains no entries")
    return entries


def quote_yaml(value: str) -> str:
    return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'


def render_skill(entry: dict) -> str:
    return (
        "---\n"
        f"name: {entry['name']}\n"
        f"description: {quote_yaml(entry['meta']['when_to_use'])}\n"
        "---\n\n"
        f"{BANNER}\n\n"
        f"{entry['content']}"
    )


def render_cursor_rule(entry: dict) -> str:
    return (
        "---\n"
        f"description: {quote_yaml(entry['meta']['when_to_use'])}\n"
        "globs:\n"
        "alwaysApply: false\n"
        "---\n\n"
        f"{BANNER}\n\n"
        f"{entry['content']}"
    )


def table_cell(value: str) -> str:
    return value.replace("|", "\\|")


def render_agents_md(entries: list[dict]) -> str:
    lines = [
        BANNER,
        "",
        "# how-to-agent — knowledge library",
        "",
        "This repository is a library of software-engineering knowledge for coding",
        "agents. Each entry below has a one-line summary and a *Use when* trigger.",
        "When the task at hand matches an entry's *Use when* description, open the",
        "linked file and follow it. Do not load entries that are not relevant.",
        "",
        "| Knowledge | Summary | Use when | File |",
        "|---|---|---|---|",
    ]
    for entry in entries:
        meta = entry["meta"]
        path = f"knowledge/{entry['name']}/content.md"
        lines.append(
            f"| {table_cell(meta['title'])} "
            f"| {table_cell(meta['summary'])} "
            f"| {table_cell(meta['when_to_use'])} "
            f"| [{path}]({path}) |"
        )
    return "\n".join(lines) + "\n"


def expected_outputs(entries: list[dict]) -> dict[Path, str]:
    outputs: dict[Path, str] = {AGENTS_MD: render_agents_md(entries)}
    for entry in entries:
        outputs[SKILLS / entry["name"] / "SKILL.md"] = render_skill(entry)
        outputs[CURSOR_RULES / f"{entry['name']}.mdc"] = render_cursor_rule(entry)
    return outputs


def find_orphans(entries: list[dict]) -> list[Path]:
    names = {entry["name"] for entry in entries}
    orphans: list[Path] = []
    if SKILLS.is_dir():
        orphans += [p for p in SKILLS.iterdir() if p.is_dir() and p.name not in names]
    if CURSOR_RULES.is_dir():
        orphans += [
            p
            for p in CURSOR_RULES.glob("*.mdc")
            if p.stem not in names
        ]
    return sorted(orphans)


def check(entries: list[dict]) -> None:
    drifted: list[str] = []
    for path, content in expected_outputs(entries).items():
        if not path.is_file():
            drifted.append(f"missing: {path.relative_to(REPO)}")
        elif path.read_text(encoding="utf-8") != content:
            drifted.append(f"stale:   {path.relative_to(REPO)}")
    for orphan in find_orphans(entries):
        drifted.append(f"orphan:  {orphan.relative_to(REPO)}")
    if drifted:
        print("generated files drift from knowledge/ — run scripts/sync_knowledge.py:")
        print("\n".join(f"  {line}" for line in drifted))
        sys.exit(1)
    print(f"clean: {len(entries)} entries, all generated files up to date")


def generate(entries: list[dict]) -> None:
    written = 0
    for path, content in expected_outputs(entries).items():
        path.parent.mkdir(parents=True, exist_ok=True)
        if not path.is_file() or path.read_text(encoding="utf-8") != content:
            path.write_text(content, encoding="utf-8")
            written += 1
    removed = 0
    for orphan in find_orphans(entries):
        if orphan.is_dir():
            skill_md = orphan / "SKILL.md"
            if skill_md.is_file():
                skill_md.unlink()
            try:
                orphan.rmdir()
            except OSError:
                die(f"orphan {orphan} has unexpected extra files; remove it manually")
        else:
            orphan.unlink()
        removed += 1
    print(f"{len(entries)} entries -> {written} files written, {removed} orphans removed")


def main() -> None:
    entries = load_entries()
    if "--check" in sys.argv[1:]:
        check(entries)
    else:
        generate(entries)


if __name__ == "__main__":
    main()
