# Copywriting Pillar — CLEAR Framework

Copy answers one question: **"Why should I care, right now?"**

It's how your product talks. Get the words right, then use Layout, Emphasis, Accessibility, and Reward to make that message easier to see.

## 1. PRE-CHECK

Before rewriting copy, verify strategic clarity. If any of the following are unclear from the input or Stage 1 scan, ASK the user now — framed as a design finding, not a request for input:

- **Value proposition** — *"The current hero doesn't land a specific promise. What's the one thing this screen should make stick? E.g., 'cheapest coverage', 'fastest claims', 'honest pricing'."*
- **Target audience** — *"I can't tell who this is for from the current copy. New shoppers? Existing customers renewing? Comparison-shoppers?"*
- **Tone** — *"Tone reads inconsistent on this screen. Should it lean formal/confident or warm/casual? Any forbidden phrases?"*
- **Reassurance points** — *"Before I polish the CTA, what doubts might the reader have here? Any fears, blockers, or hesitations worth addressing?"*

*This is the canonical list for the Copywriting pre-check. SKILL.md stage 3.2 may cite a shorter summary — this file governs.*

## 2. DIAGNOSE

Run these detection rules against current copy:

- **Too long** — copy blocks > ~30 words, or multiple dense paragraphs where a line would do
- **Too generic** — headline restates what the product IS instead of what it DOES for the reader (e.g., "Welcome to [Product]", "The best way to [X]")
- **Unnecessary / duplicated** — information restated in body that's already in the headline; multiple near-synonym CTAs
- **WIIFM missing** — benefit to reader isn't obvious in 1–2 seconds
- **No reassurance** — any high-stakes action (purchase, commitment, data share) without at least one reassurance line
- **Tone inconsistency** — formal and casual phrasings mixed on the same screen
- **Strategic clarity issues** — surface any gaps found in PRE-CHECK as design findings

List specific findings, e.g.:
- "H1 'Welcome to Rebil' doesn't communicate what Rebil is or why to care"
- "Subheader is 4 lines long — can be 1 sentence"
- "No reassurance near the primary CTA despite it being a commitment action"

## 3. DECIDE

For each finding, decide:

**Ask the user if:**
- Two+ plausible headline angles genuinely diverge (e.g., "cheapest" vs "fastest claims") — different takes, different implications
- Tone needs selection (formal/confident vs warm/casual) and isn't settled
- A reassurance point requires product knowledge (e.g., "Is there a money-back guarantee?")
- The screen's primary message is contested

**Decide alone if:**
- Word-level polish ("utilize" → "use")
- Removing obvious duplication
- Trimming excessive length to a tight sentence
- Converting passive voice to active
- Adding obvious reassurances that don't need product facts ("No commitment required" when self-evident)

## 4. PRODUCE

Apply the 4 practical tips:

1. **What's in it for me?** — Every headline and CTA must answer this in 1–2 seconds. If not, rewrite.
2. **Reassure** — Surface one reassurance near any committal moment. "You can change this later", "No prep needed", "Free to start."
3. **Use specific & action words** — Clear verbs + concrete outcomes. "Start saving in 2 minutes" beats "Get started today."
4. **Talk like a real person** — Read it out loud. If it sounds like a brochure, rewrite. Say it as you'd say it to a friend.

**Code input:** edit strings in the source files directly. Preserve template delimiters, i18n keys, accessibility attributes.

**Screenshot / URL input:** update `<h1>`, `<h2>`, `<p>`, and CTA labels in the HTML mockup. **Keep visual layout unchanged** — that's the Layout pass's job.

## 5. VERIFY

- Read the new hero aloud. Does it answer *"why should I care right now?"* in <2 seconds?
- Does every CTA have a specific verb + concrete outcome?
- Is there at least one reassurance per committal moment?
- No generic phrases ("Welcome", bare "Get started") in primary positions
- Tone consistent across the whole screen

If any fail, loop back to section 4 for that element before advancing.

## Common mistakes recap

| Mistake | Problem | Solution |
|---|---|---|
| Too long | People skim or leave | Shorter, denser. Aim for one scannable line per idea. |
| Too generic | Leaves readers guessing | Specific outcomes, concrete language |
| Unnecessary & duplicated | Adds noise, slows reading | Cut it. If it appears twice, remove one. |
