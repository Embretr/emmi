# Reward Pillar — CLEAR Framework

Reward is how the screen makes people feel after a meaningful moment — not just points or confetti. The emotional outcome of a screen.

Best reward is **contextual + proportional**: right feeling, right moment, right intensity.

Sometimes reward is the main differentiator for an entire business (Gusto for payroll, Duolingo for learning).

## The Reward Trifecta

From Self-Determination Theory — humans are motivated by three core psychological needs:

1. 🛡️ **Control** — "I'm safe / certain / in charge"
2. 🌱 **Competence** — "I'm improving / I can do this"
3. 🤝 **Recognition** — "My work is recognized / I feel seen"

An emotional outcome can be a blend — a screen can land anywhere on the triangle.

## 1. PRE-CHECK

**Always ask if emotional job is unclear.** Wrong reward flavor is the most common mistake.

Use the screen-type prior as the starting suggestion (see `references/screen-type-priors.md`), but confirm with the user:

> *"On this screen, what should users feel? Control ('Did this go through / am I safe'), Competence ('I nailed that decision / I'm making progress'), or Recognition ('I'm seen / I belong')? The screen-type prior suggests [X] but confirm."*

Typical defaults by moment:
- Post-purchase / confirmation → Control
- Task completion → Completion (Competence)
- Long multi-step flows → Progress (Competence)
- After friction / errors → Control + Competence
- Social / collaborative → Recognition

## 2. DIAGNOSE

Three common mistakes:

| Mistake | Problem | Fix |
|---|---|---|
| **Wrong Reward** | Delivering a payoff the user doesn't care about in that moment (e.g., "Congrats!" when they're anxious) | Match the dominant emotion first. Anxiety → Control. Effort → Competence. Pride → Recognition. |
| **Shy Reward** | Reward exists (time saved, status updated, recognition earned) but it's not visible enough, or it's generic praise with no real meaning | Surface the payoff explicitly: "Saved 1 hour", "Delivered today", "Share credential". Use Emphasis principles. Make it concrete. |
| **Over-Reward** | Intensity or frequency mismatched — giant fullscreen confetti for tiny actions feels spammy | Keep it proportional. Save big celebrations for real milestones. |

Also check: **is there a reward at all, or is this an emotional dead-spot?** Not every screen needs a celebration — but every screen has an emotional job.

## 3. DECIDE

**Always ask the user:** reward flavor (Control / Competence / Recognition). Drives everything else.

**Decide alone:** specific moves (copy, motion, placement, visualization, size, color) — constrained by the chosen flavor and brand tokens.

## 4. PRODUCE — by flavor

### 🛡️ Control — "I'm safe / certain / in charge"

Reduced uncertainty + perceived agency. Three subcategories:

| Subcategory | Definition | In UI terms |
|---|---|---|
| **Safety** | Reducing perceived threat, vulnerability, or potential loss | Reassurance cues: protection, privacy, fraud prevention, guarantees ("you're covered") |
| **Certainty** | Increasing predictability; clarifying state and likely outcomes | Status, ETAs, confirmations, "what's happening now + what happens next" |
| **Agency** | Perceived ability to influence / reverse | Undo / cancel / edit, preferences, branching choices, "I can still change this" |

Typical moments: post-action (checkout, submit, payment), waiting (shipping, processing, approvals), high-stakes (money, privacy, irreversible), recovery (errors, edge cases, "uh-oh" moments).

### 🌱 Competence — "I'm improving / I can do this"

Visible effectiveness — progress, skill, moving closer to the goal. Three subcategories:

| Subcategory | Definition | In UI terms |
|---|---|---|
| **Completion** | Clear evidence that a task or step is finished | "Done" states, checkmarks, receipts, submitted/sent, "You're all set" |
| **Progress** | Evidence of forward movement toward a goal | Milestones, progress bars, streaks, level/step indicators, "X% complete" |
| **Mastery** | Signals that you're getting better, faster, more accurate | Tips that improve performance, personal bests, quality scores |

Typical moments: task completion (submit, send, checkout, publish), long / multi-step flows (onboarding, setup, forms), performance feedback (analytics, habits, learning), after friction (fixes, retries, hard actions).

### 🤝 Recognition — "My work is seen / I feel seen"

Social acknowledgment — signals that work, identity, or contribution has been noticed. Three subcategories:

| Subcategory | Definition | In UI terms |
|---|---|---|
| **Acknowledgment** | Explicit feedback that your action counts socially | Praise, badges, credentials, "verified", shareable proof, endorsements |
| **Belonging** | Cues that you're part of a group, role, or identity — and that it matters | Teams / spaces, roles, cohort markers, community language ("Welcome back") |
| **Reciprocity** | Signals that another person saw you and responded | Replies, reactions, accepts, comments, "seen", "merged", "assigned" |

Typical moments: after an outcome (publish, submit, ship), social surfaces (profiles, feeds, leaderboards), group spaces (teams, communities, classrooms), collaboration loops (requests, reviews, handoffs).

## Key psychology

- **Concreteness Effect** — concrete words / images beat abstract. "Saved 2 hours" beats "Efficient." Turning "Clear History" into a literal burning-file visual makes the invisible action feel real.
- **Commitment & Consistency** — visible streaks turn past efforts into a promise (e.g., GitHub's green-squares grid nudges you to keep shipping).
- **Post-Purchase Dissonance** — spending causes anxiety. Translate spend into tangible gain: "2 hours saved" after a grocery delivery reframes the payment.
- **Labor Perception Effect** — people trust a service more when they can see it working. For high-stakes actions (decrypt, move money), a short "doing work" animation reassures.
- **Data Visualization** — charts shape how people feel. Progress that looks flat kills motivation; rising deltas reinforce effort.

## 5. VERIFY

- Is the payoff visible, not buried? (Guard against Shy Reward — apply Emphasis principles: size, placement, space.)
- Is intensity proportional to the moment? (Guard against Over-Reward — no fullscreen confetti for trivial actions.)
- Does the Copywriting from the earlier pass reinforce the chosen flavor? If flavor is Control but copy shouts "Amazing!", revisit Copywriting.
- Full CLEAR re-scan: Reward is the last pillar, so verify no upstream breakage — Copy still clear, Layout still grouped, Emphasis still dominant, Accessibility still met. This runs alongside (not instead of) the standard step 3.7 UPSTREAM RE-SCAN and covers all prior pillars, not just the immediately preceding one.

## The 2-step process (course summary)

1. Pick the feeling(s) that best match the customer's desires for this screen.
2. Apply the tactics above to those specific feelings.
