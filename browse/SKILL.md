---
name: emmi-browse
description: >-
  Emmi browse router: delegates to gstack browse for headless browser QA, screenshots, and dogfooding.
  Falls back to Playwright MCP if gstack is not installed.
---

# Browse

This skill is a router. The browse capability lives in gstack.

## Setup check

```bash
B="$HOME/.claude/skills/gstack/browse/dist/browse"
[[ -x "$B" ]] && echo "READY: $B" || echo "NEEDS_SETUP"
```

**If READY:** read and follow `~/.claude/skills/gstack/browse/SKILL.md` for the full command reference.

**If NEEDS_SETUP:** tell the user to run:
```bash
cd ~/.claude/skills/gstack/browse && ./setup
```

## Fallback

If gstack is not installed, use the Playwright MCP if configured. Otherwise suggest installing gstack:
```bash
git clone https://github.com/garrytan/gstack ~/.claude/skills/gstack
cd ~/.claude/skills/gstack && ./setup
```

## When to use browse

- Manually QA a feature after implementation.
- Screenshot a page for design review.
- Dogfood a user flow before shipping.
- Verify responsive layout at multiple viewports.
- Check for console errors or failed network requests in a running app.

Always run browse QA before marking a feature done. Pair with ferdig-ferdig for full production-readiness checks.
