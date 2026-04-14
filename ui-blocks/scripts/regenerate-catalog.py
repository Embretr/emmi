#!/usr/bin/env python3
"""Regenerate ui-blocks/*/BLOCKS.md, CATALOG.md, and README.md after file changes."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parent


def list_jsx_tsx(base: Path, rel_root: Path) -> list[str]:
    files = sorted(base.rglob("*.jsx")) + sorted(base.rglob("*.tsx"))
    return [f.relative_to(rel_root).as_posix() for f in files]


def category_tree(base: Path, indent: str = "") -> list[str]:
    lines: list[str] = []
    if not base.is_dir():
        return lines
    subs = sorted([p for p in base.iterdir() if p.is_dir()])
    files = sorted(
        [p for p in base.iterdir() if p.is_file() and p.suffix in (".jsx", ".tsx")]
    )
    for f in files:
        lines.append(f"{indent}- `{f.name}`")
    for s in subs:
        n = len(list(s.rglob("*.jsx"))) + len(list(s.rglob("*.tsx")))
        lines.append(f"{indent}- **{s.name}/** ({n} components)")
        lines.extend(category_tree(s, indent + "  "))
    return lines


def main() -> None:
    libs = {
        "marketing": ROOT / "marketing" / "react",
        "ecommerce": ROOT / "ecommerce" / "react",
        "application": ROOT / "application" / "react",
        "components": ROOT / "components" / "typescript",
    }
    sections: list[str] = []

    for name, react_root in libs.items():
        if not react_root.exists():
            print(f"skip missing {react_root}")
            continue
        all_files = list_jsx_tsx(react_root, react_root)
        tree_lines = category_tree(react_root)
        body = "\n".join(tree_lines) if tree_lines else "(no nested tree)"
        flat = "\n".join(f"- `{p}`" for p in all_files)
        header = f"""# {name.title()} UI blocks

Base path: `ui-blocks/{name}/` — component files under `{react_root.relative_to(ROOT).as_posix()}/`.

## How to use (AI)

1. Pick a category below (or search filenames for keywords: hero, cart, table, etc.).
2. `Read` the `.jsx` / `.tsx` file(s) as layout and Tailwind reference; adapt markup to the target app.

**Total files:** {len(all_files)}

## Category tree

"""
        footer = "\n\n## All files (flat)\n\n"
        out = ROOT / name / "BLOCKS.md"
        out.write_text(header + body + footer + flat, encoding="utf-8")
        print(f"wrote {out} ({len(all_files)} files)")
        n = len(all_files)
        sections.append(
            f"- **{name}** — `{react_root.relative_to(ROOT).as_posix()}/` — see [BLOCKS.md]({name}/BLOCKS.md) ({n} files)"
        )

    (ROOT / "CATALOG.md").write_text(
        """# UI blocks — master catalog

Repo root: `ui-blocks/`. Each library has a generated **BLOCKS.md** with a category tree and a flat file list.

"""
        + "\n".join(sections)
        + """

## Fetch workflow for Claude / Cursor

1. Read this file or the library **BLOCKS.md** to choose paths.
2. Open only the component files needed (avoid loading entire trees into context).
3. Use filenames as inspiration: numbered variants (01, 02, …) are alternate layouts for the same block type.
""",
        encoding="utf-8",
    )
    print(f"wrote {ROOT / 'CATALOG.md'}")

    (ROOT / "README.md").write_text(
        """# UI blocks library

React/TSX snippets organized by product type: marketing sections, ecommerce flows, application UI, and UI primitives (shadcn color tokens).

| Library | Role | Index |
|---------|------|-------|
| [marketing](marketing/) | Landing/marketing sections & elements | [BLOCKS.md](marketing/BLOCKS.md) |
| [ecommerce](ecommerce/) | Store, cart, checkout, product | [BLOCKS.md](ecommerce/BLOCKS.md) |
| [application](application/) | Dashboards, forms, shells, data display | [BLOCKS.md](application/BLOCKS.md) |
| [components](components/) | Headless UI primitives (TSX), shadcn palette | [BLOCKS.md](components/BLOCKS.md) |

Start from [CATALOG.md](CATALOG.md) or [FETCH.md](FETCH.md) for navigation.

Emmi kit (install globally): [README](../../README.md) · run `./bin/setup` from repo root.
""",
        encoding="utf-8",
    )
    print(f"wrote {ROOT / 'README.md'}")


if __name__ == "__main__":
    main()
