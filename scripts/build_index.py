#!/usr/bin/env python3
"""
Builds prompts/INDEX.md with a table of all prompt files.
Run from repo root:  python scripts/build_index.py
"""

import pathlib, re, textwrap, json
from urllib.parse import quote

PROMPTS_DIR = pathlib.Path("prompts")
INDEX_FILE  = PROMPTS_DIR / "INDEX.md"

def extract_title(path: pathlib.Path) -> str:
    """Grab title from leading JSON metadata (<!--json ... -->), then first H1, then fallback to filename."""
    text = path.read_text(encoding="utf-8")

    # Detect leading <!--json ... --> block
    m = re.match(r"\s*<!--json\s*(\{.*?\})\s*-->", text, re.DOTALL)
    if m:
        try:
            data = json.loads(m.group(1))
            if isinstance(data, dict) and data.get("title"):
                return str(data.get("title")).strip()
        except Exception:
            # ignore JSON errors and fall back
            pass

    # Fallback: first H1 heading
    for line in text.splitlines():
        if h := re.match(r"#\s*(.+)", line):
            return h.group(1).strip()
    return path.stem.replace("_", " ")

def main() -> None:
    files = sorted(PROMPTS_DIR.rglob("*.md"))
    rows  = []
    for f in files:
        if f.name == "INDEX.md":
            continue
        rel_path = f.relative_to(PROMPTS_DIR).as_posix()
        url      = quote(rel_path, safe="/")     # “ ” → %20, “/” untouched
        rows.append(f"| [{rel_path}]({url}) | {extract_title(f)} |")

    header = textwrap.dedent("""\
        <!--- AUTO-GENERATED: do not edit manually.  Run scripts/build_index.py -->
        # Prompt Index

        | Path | Title |
        |------|-------|
    """)
    INDEX_FILE.write_text(header + "\n".join(rows) + "\n", encoding="utf-8")
    print(f"Generated {INDEX_FILE} with {len(rows)} entries")

if __name__ == "__main__":
    main()