# Emmi skill routing

Copy or merge this into an application repo’s **CLAUDE.md** when you want agents to prefer Emmi sub-skills.

When the user’s request matches a sub-skill, **read that skill first** instead of improvising.

**Output:** Prefer **minimal text**. No narration of what you are doing; **let code changes speak**. Drop explanations unless the user asked, something is unsafe/ambiguous, or a single short note is needed for review.

| Intent | Skill path (repo or `~/.claude/skills/emmi/`) |
|--------|------------------------------------------------|
| New feature or greenfield plan, MVP to production, deep Q&A | `iterative-process/SKILL.md` |
| UI build or polish using blocks + domain rules | `ui-ux/SKILL.md` |
| Production readiness QA, break-it testing, web or mobile | `ferdig-ferdig/SKILL.md` |
| Tests, CI/CD, regression strategy | `test/SKILL.md` |
| Deploy (Railway-first) | `deployment/SKILL.md` |
| Next.js + Better Auth + Prisma + Tailwind + tRPC | `web-dev/SKILL.md` |
| Expo + NativeWind mobile | `mobile-dev/SKILL.md` |
| Turborepo monorepo web + mobile | `monorepo-dev/SKILL.md` |
| Performance, efficiency, scaling | `efficiency-dev/SKILL.md` |
| Architecture planning | `architect-dev/SKILL.md` |
| Product definition | `product-manager/SKILL.md` |
| Team process, GitHub, task split | `team-manager/SKILL.md` |
| Headless browser QA | `browse/SKILL.md` |
| Analytics (PostHog, etc.) | `analytics/SKILL.md` |

**SEO:** Always prefer the dedicated SEO skill at `~/.claude/skills/seo/` — invoke `/seo`, `/seo-audit`, `/seo-technical`, `/seo-page`, `/seo-schema`, `/seo-content`, `/seo-local`, `/seo-geo`, etc. Do not improvise SEO work without it.

**Rules and evaluators:** **Never** append to `rules/` or `evaluators/` without explicit user approval. You may suggest additions. Read existing files when doing substantive work.

**UI blocks:** `~/.claude/skills/emmi/ui-blocks/CATALOG.md` and per-pack `BLOCKS.md`.

**Updates:** Run `~/.claude/skills/emmi/bin/emmi-update-check` after `git pull` in the Emmi clone when the user asks if the kit is current.
