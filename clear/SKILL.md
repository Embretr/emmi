---
name: emmi-clear
description: Emmi CLEAR UI framework. Use when the user wants to redesign an existing UI screen (landing page, mobile app, complex UI, dashboard, onboarding, confirmation, etc.) using the CLEAR framework — Copywriting, Layout, Emphasis, Accessibility, Reward. Accepts screenshot, URL, or code as input. Produces an HTML mockup (for screenshot/URL inputs) or direct code edits (for code inputs) while preserving the company's existing brand. Also triggers on phrases like "improve this UI", "make this screen clearer", "apply CLEAR to this design", "score this UI", "redesign this page", "make this dashboard easier to scan", "critique this screen", "give me feedback on this UI".
---

# CLEAR UI Framework

## Communication style

- Never use emojis in any output, code comments, docs, or generated content unless the user explicitly requests them.

5 steps to craft clear interfaces — a repeatable redesign skill:

1. **C — Copywriting** — Tell people why to care, what to do, what happens next
2. **L — Layout** — Group, position, align so the screen is easy to scan
3. **E — Emphasis** — Make sure people can't miss the one thing that matters
4. **A — Accessibility** — Design for different abilities, devices, and contexts
5. **R — Reward** — Turn any boring interaction into something that feels good

You won't solve every problem in one pass. It's normal to solve one thing and notice a new opportunity in an earlier pillar.

## Hard constraints (non-negotiable)

- **Never design from scratch.** This skill redesigns an existing input. If the user has no starting point, decline and redirect.
- **Brand is a hard constraint.** Never introduce colors, fonts, radii, or shadows that aren't already in the input's token vocabulary unless the user explicitly unlocks them.
- **Ask before speculating.** When multiple meaningful directions exist, present alternatives and WAIT for the user to choose before rendering any artifact.
- **One pillar at a time.** Don't make copy changes during the Emphasis pass, or layout changes during Reward.
- **After each pillar, re-scan upstream.** Make sure previous wins weren't accidentally broken.
- **Squint test is mandatory.** Run it automatically after the Emphasis pass. If it fails, loop Emphasis before advancing.
- **Graceful degradation.** If `mcp__chrome-devtools` tools are unavailable, URL input and the automated Squint Test fall back to manual modes — describe a blurred view mentally and ask the user to inspect the mockup themselves. Inform the user what's unavailable; don't stall.
- **Mid-run pivots are allowed.** If the user changes scope mid-run ("skip Accessibility", "actually use this new primary color", "stop after Layout"), honor immediately. Scope changes update the current run's rules — note any brand-constraint overrides in the final report.

## Runbook

### Stage 1 — Intake

**1.1 Identify input type:** screenshot / URL / code. Ask if ambiguous.

**1.2 Extract brand tokens.** Load `references/brand-extraction.md` and follow the visual extraction cascade:
- Code input → codebase is the brand source. Read theme files first.
- URL input → navigate via `mcp__chrome-devtools`, pull computed styles.
- Screenshot input → extract what's visible, then completeness check. If thin, ask for URL first, then codebase access, then fall back.

**1.3 Extract strategic brand context** (same reference, strategic section). Scan the input for value prop, audience, positioning, tone, key messages, screen goal. Note gaps — do NOT ask everything upfront. Gaps surface at step 3.2 (PRE-CHECK) of the relevant pillar, not here. **Exception:** if value prop is completely indeterminable from the input, ask now — scoring is impossible without it.

**1.4 Detect screen type.** Load `references/screen-type-priors.md`. Present your guess (with evidence); let the user correct. Known types: landing, dashboard, mobile app, complex UI / form, confirmation / receipt, onboarding / setup.

**1.5 Confirm pillar scope.** Default: all 5 in CLEAR order. Honor "skip X" or "only C and L".

**1.6 Show brand-sheet preview.** Swatches, typography specimens, radius/shadow examples, tone descriptors, ⚠️ ASSUMPTION tags for anything inferred. User confirms or corrects before any pass runs.

### Stage 2 — Baseline scorecard

**2.1** Load `references/scorecard.md`.

**2.2** Score 0–5 per pillar-in-scope, weighted by the screen-type priors. Identify the weakest pillar.

**2.3** Present scorecard as findings — specific reasons each pillar is below 5, including strategic-clarity issues inside Copywriting (e.g., *"Copy: 2 — value prop isn't identifiable from the hero; tone mixes formal and casual"*).

**2.4** User confirms/adjusts scores. Scoring starts conversations, not verdicts.

**2.4.1 Score-only branch.** If the user only asked for a score ("score this UI", "critique this screen", "give me feedback on this"), STOP after 2.4. Present the scorecard with findings, then offer: "Would you like me to proceed with CLEAR passes to improve this, or is the scorecard all you needed?" Do not advance to Stage 3 without explicit request.

**2.5 Ask mode:** "Step-by-step (feedback after each pillar) or full cycle (one shot, feedback at end)?" — now that the user has seen the scorecard.

### Stage 3 — Pillar passes

For each pillar in scope, in CLEAR order:

**3.1** Load the per-pillar reference: `references/copywriting.md`, `references/layout.md`, `references/emphasis.md`, `references/accessibility.md`, or `references/reward.md`.

**3.2 PRE-CHECK** — does this pillar have the context it needs? If gaps exist from Stage 1's strategic scan, ASK now, framed as "here's what's weak about the current design, help me fix it."

**3.3 DIAGNOSE** — run the pillar's detection rules against the current screen. List specific findings.

**3.4 DECIDE** — for each finding:
- Meaningful alternatives (2+ plausible directions with tradeoffs) → present alternatives, WAIT for user choice.
- Tactical / preference-free → decide confidently alone.

**3.5 PRODUCE** — apply the fix:
- Code input → edit source files in place. Stay within existing token vocabulary.
- Screenshot / URL input → update the HTML mockup file.

**3.6 VERIFY** — pillar-specific check (see per-pillar details). **After Emphasis: run the Squint Test** (see `references/emphasis.md`).

**3.7 UPSTREAM RE-SCAN** — quick check that previous pillars' wins are still intact. Note any regressions.

**3.8 FEEDBACK GATE:**
- **Step-by-step mode:** show artifact + findings + decisions → wait for user. Refine on feedback; advance on approval.
- **Full cycle mode:** silently advance. Defer feedback to Stage 4.

### Stage 4 — Final scorecard + deliverable

**4.1** Re-score 0–5 per pillar using the rubric already loaded from `references/scorecard.md` in Stage 2. Show **BEFORE → AFTER** delta with screen-type-weighted totals.

**4.2** Summarize changes per pillar (what was changed, why).

**4.3** Present deliverable:
- Code input → list of files edited + diff summary. Run any type-check or lint the project has.
- Mockup → file path printed + opened in the user's default browser.

**4.4** If mode = full cycle: ask for feedback now. If feedback requires changes, re-enter Stage 3 at step 3.3 (DIAGNOSE) for the relevant pillar(s) — the per-pillar reference is already loaded, so skip 3.1.

**4.5 Stakeholder summary (optional).** After the deliverable is accepted, offer: *"Want a short non-technical summary you can share with stakeholders?"* If yes, generate a `summary.md` in the run folder with 4–5 bullets:
- Written in the same language as the design (match the screen's locale).
- No framework jargon — no "pillar", "squint test", "WCAG", "Gestalt", "emphasis dial", "reward flavor". Write as design rationale a product manager or founder would send to their team.
- Each bullet: **what** was changed → **why** it matters for the user or business. Lead with the user-facing impact, not the technique.
- Keep it general — describe the design direction, not specific copy or token values. The summary should still make sense if the final implementation tweaks details.
- Tone: confident and clear, not salesy. No hedging ("we think", "arguably") — state the reasoning directly.

## Output artifacts

**Screenshot / URL input runs:**
```
~/clear-runs/<project-slug>/<YYYY-MM-DD-HHMM>-<screen-slug>/
  mockup.html           ← the redesigned screen
  brand-sheet.html      ← extracted brand preview (optional — may be shown inline instead)
  report.md             ← scorecard before/after, per-pillar summaries
  summary.md            ← (optional) non-technical stakeholder summary
  original.png          ← input screenshot or URL capture
```

**Code input runs:** edits applied in place. Plus:
```
~/clear-runs/<project-slug>/<YYYY-MM-DD-HHMM>-<screen-slug>/
  report.md             ← scorecard before/after, list of files edited
  summary.md            ← (optional) non-technical stakeholder summary
  original-snapshot/    ← copies of edited files before changes (safety)
  preview.html          ← (optional) standalone render for visual review
```

`<project-slug>` is the working directory's basename (e.g. `my-app`). Run artifacts always live under `~/clear-runs/`, never inside the project repo — nothing from a run should end up committed. Code-input edits are the only files written into the repo.

## Non-goals

- Not for designing new screens from scratch
- Not a rebrand tool (brand is a hard constraint)
- Not a multi-page site audit
- Not a site crawler (one URL per run)
- Not a replacement for human judgment

## Iteration reminder

After each major change, re-scan the screen for what you may have affected upstream. Solving one pillar often reveals a new opportunity in an earlier one.
