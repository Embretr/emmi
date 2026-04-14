---
name: emmi-browse
description: >-
  Emmi browse: headless browser QA via gstack browse when installed. Navigate, snapshot, screenshots, forms, responsive checks.
  Use when "test in browser", "open the site", "dogfood", or automated UI verification. Falls back to project MCP browser if gstack missing.
---

# Browse (gstack)

## Preferred path: gstack

If this file lives in the Emmi kit at `~/.claude/skills/emmi/browse/SKILL.md`, the **full** browse workflow (daemon, commands, `$B` setup) lives in the **gstack** install:

**Read and follow:** `~/.claude/skills/gstack/browse/SKILL.md`

Check binary:

```bash
B="$HOME/.claude/skills/gstack/browse/dist/browse"
[[ -x "$B" ]] && echo "READY: $B" || echo "NEEDS_GSTACK_BUILD"
```

If `NEEDS_GSTACK_BUILD`, tell the user to run gstack browse setup per that skill (typically `cd ~/.claude/skills/gstack/browse && ./setup` after Bun install).

## When gstack is not installed

- Use **Cursor IDE browser MCP** or **Playwright MCP** if configured in the project.  
- Otherwise suggest installing **gstack** browse (global `~/.claude/skills/gstack`) or adding Playwright tests under **ferdig-ferdig** / **test**.

## Note

This Emmi skill is a **router** so the public Emmi repo does not vendor gstack. Capability equals gstack browse plus local MCP fallbacks.
