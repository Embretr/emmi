# Emmi

My heavily opinionated Claude Code skill kit. Built around my own workflows, preferences, and opinions — sole purpose is to get the best possible results from day-to-day work with Claude Code.

**Repo:** https://github.com/Embretr/emmi

---

## Install

**Option 1 — paste into Claude Code:**

```
Install Emmi: run
git clone --single-branch --depth 1 https://github.com/Embretr/emmi.git ~/emmi && cd ~/emmi && ./bin/setup

Then restart Claude Code or start a new session so the skills load.

If the user wants routing for their current project, offer to append the "Emmi skill routing" section from ~/.claude/skills/emmi/CLAUDE.md to that project's CLAUDE.md.
```

**Option 2 — shell:**

```bash
git clone --single-branch --depth 1 https://github.com/Embretr/emmi.git ~/emmi
cd ~/emmi && ./bin/setup
```

`./bin/setup` symlinks `~/.claude/skills/emmi` to your clone. Override the target:

```bash
EMMI_SKILLS_HOME=/path/to/.claude/skills ./bin/setup
```

---

## Update

```bash
cd ~/emmi && git pull && ./bin/emmi-update-check
```

If output shows `UPGRADE_AVAILABLE`, restart your Claude Code session to pick up the new skills.

---

## What's inside

| Path | Role |
|------|------|
| `SKILL.md` | Kit router — read first |
| `*/SKILL.md` | Sub-skills |
| `ui-ux/SKILL.md` | UI/UX rules, design system, interaction patterns |
| `ferdig-ferdig/SKILL.md` | Production-readiness QA, four gates |
| `ui-blocks/` | Block library and `CATALOG.md` |
| `rules/` | Patterns to avoid (local entries gitignored) |
| `evaluators/` | Quality signals (local entries gitignored) |
| `bin/setup` | Symlink installer |
| `bin/emmi-update-check` | Compare local clone to remote HEAD |
| `CLAUDE.md` | Routing block to merge into project repos |

---

## License

MIT
