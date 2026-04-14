# Emmi

Opinionated Claude Code skill kit: planning, UI, QA, tests, deploy, stack conventions, and team workflows. Ships with a **`ui-blocks/`** library (marketing, ecommerce, application, UI primitives). **Rules** and **evaluators** hold local guardrails (gitignored entries are person-specific; only each `README.md` is tracked).

Replace `https://github.com/<org>/emmi.git` with this repository’s URL once it exists on GitHub.

---

## Step 1: Install on your machine

Open **Claude Code**, paste the block below, and send it. Claude runs the clone and setup (same idea as [gstack’s install](https://github.com/garrytan/gstack), but **this repo is only Emmi** — no gstack bundled here).

```
Install Emmi: run
git clone --single-branch --depth 1 https://github.com/<org>/emmi.git ~/emmi && cd ~/emmi && ./bin/setup

Then restart Claude Code or start a new session so skills load.

If the user wants routing for **their current project**, offer to append the "Emmi skill routing" section from ~/.claude/skills/emmi/CLAUDE.md (or this repo’s CLAUDE.md) to that project’s CLAUDE.md. Do not add anything about gstack unless the user asks for gstack separately.
```

---

## Install (shell only)

```bash
git clone --single-branch --depth 1 https://github.com/<org>/emmi.git ~/emmi
cd ~/emmi && ./bin/setup
```

`./bin/setup` symlinks `~/.claude/skills/emmi` → your clone. Override:

```bash
EMMI_SKILLS_HOME=/path/to/.claude/skills ./bin/setup
```

## Update

```bash
cd ~/emmi && git pull && ./bin/emmi-update-check
```

If you see `UPGRADE_AVAILABLE`, you pulled new commits; restart the session. (`emmi-update-check` needs a git remote and upstream.)

## Layout

| Path | Role |
|------|------|
| `SKILL.md` | Main router |
| `*/SKILL.md` | Sub-skills |
| `ui-blocks/` | Block library + `CATALOG.md` |
| `rules/` | Things to avoid (local entries gitignored) |
| `evaluators/` | Quality signals (local entries gitignored) |
| `bin/setup` | Global install symlink |
| `bin/emmi-update-check` | Compare local clone to remote |
| `CLAUDE.md` | Emmi-only routing to merge into app repos |

## License

Add your license when you publish the repo.
