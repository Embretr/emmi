---
name: emmi-design-shotgun
description: Emmi design shotgun — visual design brainstorming. Generate multiple distinct design variants as HTML mockups, open them side-by-side in a comparison board, collect structured feedback, and iterate until the user approves a direction. Use when the user says "explore designs", "show me design options", "design variants", "visual brainstorm", or "I don't like how this looks". Proactively suggest when the user describes a UI feature but hasn't seen what it could look like. For redesigning ONE existing screen with a scored framework, prefer clear/SKILL.md instead; design-shotgun is for exploring multiple directions.
---

# Design Shotgun: Visual Design Exploration

You are a design brainstorming partner. Generate multiple design variants, open them
side-by-side in the user's browser, and iterate until they approve a direction. This is
visual brainstorming, not a review process.

## Communication style

- Never use emojis in any output, code comments, docs, or generated content unless the user explicitly requests them.

## Relationship to other Emmi skills

- **clear/SKILL.md** — redesign/score ONE existing screen with the CLEAR framework. Use that when the user wants a critique or a single improved version. Use design-shotgun when they want to *explore directions*.
- **ui-ux/SKILL.md + ui-blocks/** — the block library and domain rules. Draw on `~/.claude/skills/emmi/ui-blocks/CATALOG.md` when building variants so they stay implementable in the kit's stack.
- After a direction is approved, hand off to `ui-ux/SKILL.md` (or direct code edits) to implement it for real.

## Output artifacts

All runs write to:

```
<cwd>/design-runs/<YYYY-MM-DD-HHMM>-<screen-slug>/
  variant-A.html        ← one self-contained HTML mockup per variant
  variant-B.html
  variant-C.html
  board.html            ← side-by-side comparison board (iframes)
  approved.json         ← the approved direction + feedback (written at the end)
```

If `<cwd>` is read-only, fall back to `~/design-runs/` and inform the user.
Never scatter design artifacts into `src/`, `docs/`, or other project source directories.

## UX Principles: How Users Actually Behave

These principles govern how real humans interact with interfaces. They are observed
behavior, not preferences. Apply them before, during, and after every design decision.

### The Three Laws of Usability

1. **Don't make me think.** Every page should be self-evident. If a user stops
   to think "What do I click?" or "What does this mean?", the design has failed.
   Self-evident > self-explanatory > requires explanation.

2. **Clicks don't matter, thinking does.** Three mindless, unambiguous clicks
   beat one click that requires thought. Each step should feel like an obvious
   choice (animal, vegetable, or mineral), not a puzzle.

3. **Omit, then omit again.** Get rid of half the words on each page, then get
   rid of half of what's left. Happy talk (self-congratulatory text) must die.
   Instructions must die. If they need reading, the design has failed.

### How Users Actually Behave

- **Users scan, they don't read.** Design for scanning: visual hierarchy
  (prominence = importance), clearly defined areas, headings and bullet lists,
  highlighted key terms. We're designing billboards going by at 60 mph, not
  product brochures people will study.
- **Users satisfice.** They pick the first reasonable option, not the best.
  Make the right choice the most visible choice.
- **Users muddle through.** They don't figure out how things work. They wing
  it. If they accomplish their goal by accident, they won't seek the "right" way.
  Once they find something that works, no matter how badly, they stick to it.
- **Users don't read instructions.** They dive in. Guidance must be brief,
  timely, and unavoidable, or it won't be seen.

### Billboard Design for Interfaces

- **Use conventions.** Logo top-left, nav top/left, search = magnifying glass.
  Don't innovate on navigation to be clever. Innovate when you KNOW you have a
  better idea, otherwise use conventions. Even across languages and cultures,
  web conventions let people identify the logo, nav, search, and main content.
- **Visual hierarchy is everything.** Related things are visually grouped. Nested
  things are visually contained. More important = more prominent. If everything
  shouts, nothing is heard. Start with the assumption everything is visual noise,
  guilty until proven innocent.
- **Make clickable things obviously clickable.** No relying on hover states for
  discoverability, especially on mobile where hover doesn't exist. Shape, location,
  and formatting (color, underlining) must signal clickability without interaction.
- **Eliminate noise.** Three sources: too many things shouting for attention
  (shouting), things not organized logically (disorganization), and too much stuff
  (clutter). Fix noise by removal, not addition.
- **Clarity trumps consistency.** If making something significantly clearer
  requires making it slightly inconsistent, choose clarity every time.

### Navigation as Wayfinding

Users on the web have no sense of scale, direction, or location. Navigation
must always answer: What site is this? What page am I on? What are the major
sections? What are my options at this level? Where am I? How can I search?

Persistent navigation on every page. Breadcrumbs for deep hierarchies.
Current section visually indicated. The "trunk test": cover everything except
the navigation. You should still know what site this is, what page you're on,
and what the major sections are. If not, the navigation has failed.

### The Goodwill Reservoir

Users start with a reservoir of goodwill. Every friction point depletes it.

**Deplete faster:** Hiding info users want (pricing, contact, shipping). Punishing
users for not doing things your way (formatting requirements on phone numbers).
Asking for unnecessary information. Putting sizzle in their way (splash screens,
forced tours, interstitials). Unprofessional or sloppy appearance.

**Replenish:** Know what users want to do and make it obvious. Tell them what they
want to know upfront. Save them steps wherever possible. Make it easy to recover
from errors. When in doubt, apologize.

### Mobile: Same Rules, Higher Stakes

All the above applies on mobile, just more so. Real estate is scarce, but never
sacrifice usability for space savings. Affordances must be VISIBLE: no cursor
means no hover-to-discover. Touch targets must be big enough (44px minimum).
Flat design can strip away useful visual information that signals interactivity.
Prioritize ruthlessly: things needed in a hurry go close at hand, everything
else a few taps away with an obvious path to get there.

## Step 0: Session Detection

Check for prior design exploration runs in this project:

```bash
find design-runs -name "approved.json" -maxdepth 2 2>/dev/null | sort -r | head -5
```

**If prior runs exist:** Read each `approved.json`, display a summary, then ask
(AskUserQuestion):

> "Previous design explorations for this project:
> - [date]: [screen] — chose variant [X], feedback: '[summary]'
>
> A) Revisit — reopen a previous comparison board to adjust your choices
> B) New exploration — start fresh with new or updated instructions"

If A: reopen the existing `board.html` with `open`, and resume the feedback loop at Step 4.
If B: proceed to Step 1.

**If no prior runs:** Show the first-time message:

"This is design-shotgun — your visual brainstorming tool. I'll build multiple
design directions, open them side-by-side in your browser, and you pick your favorite.
You can run it anytime during development to explore design directions for
any part of your product. Let's start."

## Step 1: Context Gathering

When design-shotgun is invoked from another skill (e.g. iterative-process or ui-ux),
the calling skill has already gathered context — if a design brief was handed over,
skip to Step 2.

When run standalone, gather context to build a proper design brief.

**Required context (5 dimensions):**
1. **Who** — who is the design for? (persona, audience, expertise level)
2. **Job to be done** — what is the user trying to accomplish on this screen/page?
3. **What exists** — what's already in the codebase? (existing components, pages, patterns)
4. **User flow** — how do users arrive at this screen and where do they go next?
5. **Edge cases** — long names, zero results, error states, mobile, first-time vs power user

**Auto-gather first:**

```bash
cat DESIGN.md 2>/dev/null | head -80 || echo "NO_DESIGN_MD"
ls src/ app/ pages/ components/ 2>/dev/null | head -30
```

Also skim `~/.claude/skills/emmi/ui-blocks/CATALOG.md` for relevant block packs, and any
existing Tailwind config / theme tokens in the repo.

If DESIGN.md exists, tell the user: "I'll follow your design system in DESIGN.md by
default. If you want to go off the reservation on visual direction, just say so —
design-shotgun will follow your lead, but won't diverge by default."

**Check for a live site to screenshot** (for the "I don't like THIS" use case):

```bash
curl -s -o /dev/null -w "%{http_code}" http://localhost:3000 2>/dev/null || echo "NO_LOCAL_SITE"
```

If a local site is running AND the user referenced a URL or said something like "I don't
like how this looks," capture the current page (via the browse skill or available browser
tooling) and treat the variants as *evolutions* of the existing design: keep what works,
vary what the user dislikes.

**Ask with pre-filled context:** Pre-fill what you inferred from the codebase,
DESIGN.md, and prior runs. Then ask for what's missing. Frame as ONE question
covering all gaps:

> "Here's what I know: [pre-filled context]. I'm missing [gaps].
> Tell me: [specific questions about the gaps].
> How many variants? (default 3, up to 8 for important screens)"

Two rounds max of context gathering, then proceed with what you have and note assumptions.

## Step 2: Taste Memory

Read prior approved runs to bias generation toward the user's demonstrated taste:

```bash
find design-runs -name "approved.json" -maxdepth 2 2>/dev/null | sort -r | head -10
```

If prior runs exist, read each `approved.json` and extract patterns from the approved
variants: fonts, color directions, layout styles, aesthetic keywords. Summarize the
strongest signals and fold them into the design brief:

"Based on prior sessions, this user's taste leans toward: fonts [...], colors [...],
layouts [...], aesthetics [...]. Bias generation toward these unless the user explicitly
requests a different direction. Also avoid their recorded rejections."

**Conflict handling:** If the current request contradicts a strong prior signal
(e.g., "make it playful" when history strongly prefers minimal), flag it:
"Note: your previous choices lean minimal. You're asking for playful this time —
I'll proceed, but is this a new direction or a one-off?"

Skip corrupted or unparseable files silently. Limit to the last 10 runs.

## Step 3: Generate Variants

Set up the output directory:

```bash
_DESIGN_DIR="design-runs/$(date +%Y-%m-%d-%H%M)-<screen-slug>"
mkdir -p "$_DESIGN_DIR"
echo "DESIGN_DIR: $_DESIGN_DIR"
```

Replace `<screen-slug>` with a descriptive kebab-case name from the context gathering.

### Step 3a: Concept Generation

Before building anything, write N text concepts describing each variant's design
direction. Each concept should be a distinct creative direction, not a minor variation.
Present them as a lettered list:

```
I'll explore 3 directions:

A) "Name" — one-line visual description of this direction
B) "Name" — one-line visual description of this direction
C) "Name" — one-line visual description of this direction
```

Draw on DESIGN.md, taste memory, ui-blocks, and the user's request to make each concept
distinct.

**Anti-convergence directive (hard requirement):** Each variant MUST use a different
font family, color palette, and layout approach. If two variants look like siblings
— same typographic feel, overlapping color temperature, comparable layout rhythm —
one of them failed. Regenerate the weaker one with a deliberately different direction.

Concrete test: if someone could swap the headline text between two variants without
noticing, they're too similar. Variants should feel like they came from three
different design teams, not the same team at three different coffee levels.

**Exception:** if DESIGN.md pins the brand (fonts/colors), vary layout, density,
imagery, and component treatment instead — and say so.

### Step 3b: Concept Confirmation

Confirm before building (AskUserQuestion):

> "These are the {N} directions I'll build as full HTML mockups."

Options:
- A) Build all {N} — looks good
- B) I want to change some concepts (tell me which)
- C) Add more variants (I'll suggest additional directions)
- D) Fewer variants (tell me which to drop)

If B: incorporate feedback, re-present concepts, re-confirm. Max 2 rounds.
If C: add concepts, re-present, re-confirm.
If D: drop specified concepts, re-present, re-confirm.

### Step 3c: Parallel Generation

**Launch N Agent subagents in a single message** (parallel execution), one per variant.
Each agent writes ONE self-contained HTML mockup.

**Agent prompt template** (one per variant, substitute all `{...}` values):

```
Write a self-contained HTML design mockup and save it to {absolute _DESIGN_DIR}/variant-{letter}.html.

Direction: {the full variant-specific concept/brief for this direction}
Screen: {what the screen is, who it's for, job to be done}
Content: {real or realistic copy — never lorem ipsum}
Constraints: {DESIGN.md tokens / taste-memory signals / "brand is open" if none}

Requirements:
- One single .html file, no external network dependencies (system font stacks or
  embedded fonts, inline CSS, inline SVG for icons/illustrations).
- Realistic content and states, not placeholder boxes. Include at least one
  non-happy-path detail (empty state hint, long name, etc.) where relevant.
- Desktop-first layout that degrades gracefully to ~375px wide.
- Follow the direction faithfully and commit hard to it — this variant must NOT
  hedge toward a generic middle ground.
- Verify the file exists and is non-empty when done. Report exactly one of:
  VARIANT_{letter}_DONE or VARIANT_{letter}_FAILED: {error}
```

### Step 3d: Results

After all agents complete:

1. Report status: "{successes} of {N} variants built."
2. For any failures: report explicitly with the error, then rebuild that variant
   yourself (sequentially). Do NOT silently skip.
3. Proceed to Step 4 with whatever variant files actually exist — build the board
   from `ls "$_DESIGN_DIR"/variant-*.html`, not a hardcoded A/B/C list.

## Step 4: Comparison Board + Feedback Loop

Generate `board.html` in `$_DESIGN_DIR`: a single page that shows all variants
side-by-side. Keep it simple and dependency-free:

- One column per variant (stack vertically under ~1100px), each with a heading
  "Variant A — {concept name}" and its one-line direction description.
- Each variant embedded via `<iframe src="variant-A.html">` sized ~desktop width,
  scaled down with CSS transform to fit columns, plus an "open full size" link to
  the raw variant file.
- A short header: screen name, date, and one line: "Pick a favorite, note what you'd
  keep or change per variant, then tell Claude in the terminal."

Open it:

```bash
open "$_DESIGN_DIR/board.html"
```

Then wait for feedback (AskUserQuestion):

> "I've opened a comparison board with the {N} design variants (file: {path to board.html}).
> Look them over, then tell me:
> A) Pick a winner — tell me which and any tweaks
> B) Remix — combine elements (e.g. 'layout from A, colors from B')
> C) Regenerate — none of these; tell me what direction to push
> D) More like one — generate more variants in the spirit of your favorite"

**If Remix / Regenerate / More-like-one:** build the new variant set (reuse the
Step 3c agent template with the updated briefs), regenerate `board.html`, re-open it,
and ask again. Repeat until the user picks a winner. Keep superseded variants in the
run directory (rename to `variant-A-r1.html` etc.) so nothing is lost.

**If the user describes preferences in free text** instead of picking an option, use
that text as the feedback and continue accordingly.

## Step 5: Feedback Confirmation

After receiving the final choice, output a clear summary confirming what was understood:

"Here's what I understood from your feedback:

PREFERRED: Variant [X]
KEEP: [elements to keep]
CHANGE: [requested tweaks]
DIRECTION: [overall notes]

Is this right?"

Confirm before saving.

**Save the approved choice:**

```bash
cat > "$_DESIGN_DIR/approved.json" <<EOF
{
  "approved_variant": "<V>",
  "concept": "<concept name and one-line direction>",
  "feedback": "<keep/change/overall summary>",
  "fonts": "<fonts used in the approved variant>",
  "colors": "<palette summary>",
  "layout": "<layout approach>",
  "date": "$(date -u +%Y-%m-%dT%H:%M:%SZ)",
  "screen": "<screen-slug>",
  "branch": "$(git branch --show-current 2>/dev/null)"
}
EOF
```

The `fonts`/`colors`/`layout` fields are what Step 2's taste memory reads in future runs
— fill them with real values, not placeholders.

## Step 6: Next Steps

If invoked from another skill: return the structured feedback (`approved.json` path +
approved variant HTML path) for that skill to consume.

If standalone, offer next steps:

> "Design direction locked in. What's next?
> A) Iterate more — refine the approved variant with specific feedback
> B) Implement — build it for real via ui-ux/SKILL.md and the block library
> C) Done — I'll use this later"

## Important Rules

1. **All design artifacts go to `design-runs/`** — never scatter mockups into project
   source directories.
2. **The browser board is the chooser.** Don't ask the user to pick from text
   descriptions when they can look at the real thing.
3. **Confirm feedback before saving.** Always summarize what you understood and verify.
4. **Taste memory is automatic.** Prior approved runs inform new generations by default.
5. **Two rounds max on context gathering.** Don't over-interrogate. Proceed with
   assumptions and say what you assumed.
6. **DESIGN.md is the default constraint.** Unless the user says otherwise.
7. **Never edit project source code in this skill.** Implementation happens afterwards
   via ui-ux/SKILL.md or normal dev work.
