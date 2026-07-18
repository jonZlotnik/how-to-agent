#!/usr/bin/env python3
"""One-time port: convert Ada-format skills/<name>/SKILL.md into knowledge/<name>/.

Mapping:
  frontmatter `description:` -> meta.yaml `when_to_use`
  H1 title                   -> meta.yaml `title`
  first paragraph after H1   -> meta.yaml `summary` (best-effort, refine by hand)
  [[wikilinks]] in body      -> meta.yaml `related`
  body (frontmatter stripped)-> content.md verbatim

Kept for provenance; not needed after the initial port.
"""

import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
WIKILINK = re.compile(r"\[\[([a-z0-9-]+)\]\]")


def parse_skill(path: Path) -> tuple[str, str]:
    """Return (description, body). Body starts at the H1, verbatim."""
    text = path.read_text(encoding="utf-8")
    parts = text.split("---\n", 2)
    if len(parts) != 3 or parts[0] != "":
        sys.exit(f"{path}: unexpected frontmatter layout")
    frontmatter, body = parts[1], parts[2].lstrip("\n")

    description = None
    for line in frontmatter.splitlines():
        m = re.match(r"^description:\s*(.*)$", line)
        if m:
            description = m.group(1).strip()
            if description.startswith('"') and description.endswith('"'):
                description = description[1:-1]
            elif description.startswith("'") and description.endswith("'"):
                description = description[1:-1]
    if not description:
        sys.exit(f"{path}: no description in frontmatter")
    return description, body


def extract_title_and_summary(body: str, path: Path) -> tuple[str, str]:
    lines = body.splitlines()
    if not lines or not lines[0].startswith("# "):
        sys.exit(f"{path}: body does not start with an H1")
    title = lines[0][2:].strip()

    # First paragraph after the H1: skip blanks, collect until next blank line.
    para: list[str] = []
    for line in lines[1:]:
        if not line.strip():
            if para:
                break
            continue
        if line.startswith("#"):
            break
        para.append(line.strip())
    summary = " ".join(para)
    return title, summary


def emit_meta(title: str, summary: str, when_to_use: str, related: list[str]) -> str:
    out = [f"title: {title}"]
    out.append("summary: >-")
    out.append(f"  {summary}")
    out.append("when_to_use: >-")
    out.append(f"  {when_to_use}")
    if related:
        out.append("related:")
        out.extend(f"  - {name}" for name in related)
    return "\n".join(out) + "\n"


def main() -> None:
    src_root = REPO / "skills"
    dst_root = REPO / "knowledge"
    if not src_root.is_dir():
        sys.exit(f"missing {src_root}")

    count = 0
    for skill_md in sorted(src_root.glob("*/SKILL.md")):
        name = skill_md.parent.name
        description, body = parse_skill(skill_md)
        title, summary = extract_title_and_summary(body, skill_md)
        related = list(dict.fromkeys(WIKILINK.findall(body)))

        entry = dst_root / name
        entry.mkdir(parents=True, exist_ok=True)
        (entry / "meta.yaml").write_text(
            emit_meta(title, summary, description, related), encoding="utf-8"
        )
        (entry / "content.md").write_text(body, encoding="utf-8")
        count += 1

    print(f"ported {count} entries into {dst_root}")


if __name__ == "__main__":
    main()
