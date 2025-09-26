#!/usr/bin/env python3
"""
Builds prompts/INDEX.md with a table of all prompt files.
Run from repo root:  python scripts/build_index.py
"""

import pathlib, re, textwrap, json
from urllib.parse import quote

PROMPTS_DIR = pathlib.Path("prompts")
INDEX_FILE  = PROMPTS_DIR / "INDEX.md"

def extract_title_and_description(path: pathlib.Path) -> tuple[str, str]:
    """Extract title and description.

    Title priority:
      1. JSON metadata block <!--json {"title": "..."} --> if present
      2. First markdown H1 (# Heading)
      3. Filename stem

    Description extraction:
      - Search for an XML-like <descriptions>...</descriptions> tag in the leading comment block
      - Collapse whitespace to a single space
      - Return empty string if not found.
    """
    text = path.read_text(encoding="utf-8")

    # Title via JSON metadata if present
    title = None
    m = re.match(r"\s*<!--json\s*(\{.*?\})\s*-->", text, re.DOTALL)
    if m:
        try:
            data = json.loads(m.group(1))
            if isinstance(data, dict) and data.get("title"):
                title = str(data.get("title")).strip()
        except Exception:
            pass  # ignore JSON errors

    if not title:
        for line in text.splitlines():
            if h := re.match(r"#\s*(.+)", line):
                title = h.group(1).strip()
                break
    if not title:
        title = path.stem.replace("_", " ")

    # Description via <description> tag (preferred) with fallback to legacy <descriptions>
    desc_match = re.search(r"<description>(.*?)</description>", text, re.DOTALL | re.IGNORECASE)
    if not desc_match:
        desc_match = re.search(r"<descriptions>(.*?)</descriptions>", text, re.DOTALL | re.IGNORECASE)
    description = ""
    if desc_match:
        raw = desc_match.group(1)
        # Strip leading/trailing whitespace and collapse internal whitespace
        description = re.sub(r"\s+", " ", raw).strip()

    return title, description

def main() -> None:
    files = sorted(PROMPTS_DIR.rglob("*.md"))
    rows  = []
    for f in files:
        if f.name == "INDEX.md":
            continue
        rel_path = f.relative_to(PROMPTS_DIR).as_posix()
        url      = quote(rel_path, safe="/")     # “ ” → %20, “/” untouched
        title, description = extract_title_and_description(f)
        # Escape pipe characters in title/description to not break table
        esc_title = title.replace("|", "\\|")
        esc_desc  = description.replace("|", "\\|")
        rows.append(f"| [{rel_path}]({url}) | {esc_title} | {esc_desc} |")

    header = textwrap.dedent("""\
        <!--- AUTO-GENERATED: do not edit manually.  Run scripts/build_index.py -->
        # Prompt Index

        | Path | Title | Description |
        |------|-------|-------------|
    """)
    INDEX_FILE.write_text(header + "\n".join(rows) + "\n", encoding="utf-8")
    print(f"Generated {INDEX_FILE} with {len(rows)} entries")

if __name__ == "__main__":
    main()