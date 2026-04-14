---
name: emmi
version: 0.3.0
description: >-
  Emmi opinionated skill kit: iterative product planning (MVP to production), UI/UX with block library,
  hard QA (ferdig-ferdig), testing and CI/CD, Railway-first deployment, Next.js+tRPC+Prisma+Better Auth+Tailwind,
  Expo+NativeWind, Turborepo, performance work, architecture, product and team management, browse, and analytics.
  Use when the user wants Emmi workflows, sub-skill by name, or "the kit". Read sub-skills from this repo root.
---

# Emmi

## Communication style

- Never use emojis in any output, code comments, docs, or generated content unless the user explicitly requests them.

## Update check (optional)

```bash
./bin/emmi-update-check 2>/dev/null || ~/.claude/skills/emmi/bin/emmi-update-check 2>/dev/null || true
```

If output includes `UPGRADE_AVAILABLE`, tell the user to `git pull` in the Emmi repo (or reinstall via `./bin/setup`).

## Kit root

When this file lives at `~/.claude/skills/emmi/SKILL.md`, all paths below are relative to `~/.claude/skills/emmi/`. In a git clone, they are relative to the repository root.

## Governance

- **`rules/`:** Patterns to avoid. **Do not add or edit entries without asking the user.** Propose candidates when you see repeated mistakes.
- **`evaluators/`:** Signals of good solutions. **Do not add or edit without asking.** Propose metrics when they would sharpen decisions.

Read existing entries at session start when doing substantive product or UI work.

## Sub-skills (read the matching `SKILL.md`)

| Sub-skill | When |
|-----------|------|
| [iterative-process](iterative-process/SKILL.md) | New features, new projects, nothing → MVP → production plan, feedback rounds |
| [ui-ux](ui-ux/SKILL.md) | UI from blocks + ecommerce / marketing / application rules |
| [ferdig-ferdig](ferdig-ferdig/SKILL.md) | Ship-quality QA, Playwright (web) or Maestro (mobile), adversarial use |
| [test](test/SKILL.md) | Unit through smoke tests, CI/CD, regression prevention |
| [deployment](deployment/SKILL.md) | Railway-first deploy, env, rollbacks |
| [web-dev](web-dev/SKILL.md) | Next.js, Better Auth, Prisma, Tailwind, tRPC |
| [mobile-dev](mobile-dev/SKILL.md) | Expo, NativeWind |
| [monorepo-dev](monorepo-dev/SKILL.md) | Turborepo combining web and mobile |
| [efficiency-dev](efficiency-dev/SKILL.md) | Load time, efficiency, scaling |
| [architect-dev](architect-dev/SKILL.md) | System and data-flow planning |
| [product-manager](product-manager/SKILL.md) | Product scope, priorities, outcomes |
| [team-manager](team-manager/SKILL.md) | Tasks, process, GitHub |
| [browse](browse/SKILL.md) | Headless browser testing (see skill; optional tooling there) |
| [analytics](analytics/SKILL.md) | PostHog and related instrumentation |

## SEO (external skill — always prefer)

For any SEO-related task, defer to the dedicated SEO skill instead of improvising. These are not Emmi sub-skills — they live externally and are invoked directly.

**If the skill is not installed**, install it first:
```bash
curl -fsSL https://raw.githubusercontent.com/AgriciDaniel/claude-seo/main/install.sh | bash
```
Source: https://github.com/AgriciDaniel/claude-seo

| Intent | Invoke |
|--------|--------|
| Full site audit | `/seo` or `/seo-audit` |
| Single page analysis | `/seo-page` |
| Technical SEO (crawlability, Core Web Vitals, indexability) | `/seo-technical` |
| Schema / structured data | `/seo-schema` |
| Content quality, E-E-A-T | `/seo-content` |
| Sitemap | `/seo-sitemap` |
| Backlinks | `/seo-backlinks` |
| Local SEO, Google Business Profile | `/seo-local` |
| Maps intelligence, geo-grid ranking | `/seo-maps` |
| GEO / AI Overviews / ChatGPT / Perplexity visibility | `/seo-geo` |
| Google APIs (Search Console, CrUX, GA4) | `/seo-google` |
| DataForSEO data (SERP, keywords, live data) | `/seo-dataforseo` |
| Image SEO and OG images | `/seo-images` |
| Hreflang / international SEO | `/seo-hreflang` |
| Programmatic SEO planning | `/seo-programmatic` |
| Competitor pages | `/seo-competitor-pages` |
| Performance (Core Web Vitals lab data) | `/seo-performance` |
| SEO strategy and planning | `/seo-plan` |

## UI blocks index

- [ui-blocks/CATALOG.md](ui-blocks/CATALOG.md)
- [ui-blocks/FETCH.md](ui-blocks/FETCH.md)

Regenerate block indexes after library changes:

```bash
python3 ui-blocks/scripts/regenerate-catalog.py
```

## Project routing

Copy or merge [CLAUDE.md](CLAUDE.md) into an application repository so agents pick the right Emmi sub-skill.
