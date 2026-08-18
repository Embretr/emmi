# Screen-Type Priors

Screen type tunes the CLEAR framework: which pillars matter most, and what reward flavor to default to.

## Pillar weights + default reward flavor

| Screen type | C | L | E | A | R | Default reward flavor |
|---|---|---|---|---|---|---|
| Landing page | 2 | 1 | 2 | 1 | 2 | Control + Recognition |
| Dashboard | 1 | 2 | 2 | 2 | 1 | Competence |
| Mobile app screen | 2 | 1 | 1 | 2 | 2 | Depends on screen job |
| Complex UI / form | 2 | 2 | 1 | 2 | 1 | Control |
| Confirmation / receipt | 2 | 1 | 1 | 1 | 2 | Control (post-purchase) |
| Onboarding / setup | 2 | 1 | 2 | 1 | 2 | Competence + Control |

Weights are **multipliers for the scorecard totals** — higher weight means that pillar contributes more to the final score. Use the default reward flavor as a starting suggestion for the Reward pass; user confirms in that pillar's PRE-CHECK.

## Detection heuristics

Detect screen type from the input; present your guess **with evidence**; let the user correct.

### Landing page signals
- Single primary CTA above the fold
- Hero with value prop + supporting image/video
- Sections below: features, social proof, pricing, FAQ
- No user state indicators (not logged in, not mid-flow)
- URL often marketing root (`/`, `/product`, `/pricing`)

### Dashboard signals
- Multiple data widgets (charts, tables, KPI tiles)
- Time range selectors, filters, tabs
- Data-dense; low textual copy
- Logged-in user state assumed (avatar, account menu)

### Mobile app screen signals
- Viewport width ≤ 430px, portrait orientation
- Bottom tab bar, hamburger / nav-drawer patterns
- Stacked card layouts
- Touch-first affordances (large buttons, swipe hints)

### Complex UI / form signals
- Multi-field form or multi-step workflow
- Dense input controls, validation messaging
- Save/submit actions
- Sidebar + main content layout (enterprise-style)

### Confirmation / receipt signals
- Copy includes: "order", "thank you", "confirmed", "receipt", "your X has been"
- Order/reference number visible
- Summary of what was done + what happens next
- Usually one primary CTA ("Track order", "Continue")

### Onboarding / setup signals
- Progress indicator (step N of M)
- Brief forms, one choice per screen
- Copy: "Welcome", "Let's get started", "Almost done"
- Often branded illustration per step

## When signals conflict

Present the ranked top-2 guesses with evidence:

> "I see both dashboard and complex-UI signals — data widgets + a form-like sidebar. Which fits this screen best, or is it something else?"

## When signals are weak

Default by input type:
- Code input → complex UI (most components in codebases)
- URL input → landing (most public marketing URLs)
- Screenshot → ask the user outright

Always let the user override. The heuristic is a starting point, not a verdict.
