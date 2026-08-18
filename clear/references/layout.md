# Layout Pillar — CLEAR Framework

A good layout lets people scan and understand the information by grouping, positioning, and aligning elements that belong together. When the structure is clear, people don't have to search for what they want — they follow your cues.

Layout is how you create clarity without shouting.

## 1. PRE-CHECK

- **Content priority must be clear.** The Copywriting pass usually resolves this. If it didn't, ASK: *"Of the content on this screen, which is the single most important thing to see first?"*
- **For dashboards / complex UIs:** *"What's the primary task the user is here to do on this screen?"*

## 2. DIAGNOSE

Use Gestalt principles as a grouping checklist:

- **Proximity** — items that belong together should be near each other; unrelated items should be separated by space
- **Similarity** — items doing the same job should look the same (breaks scannability otherwise)
- **Common region** — related items enclosed together (container / card / section)
- **Continuity / alignment** — misaligned edges create visual noise; align to a grid
- **Figure / ground** — foreground should lift away from background
- **Closure** — avoid incomplete shapes that create ambiguity

And the course's 3 common layout mistakes:

| Mistake | Problem | Solution |
|---|---|---|
| Sloppy spacing | Spacing inconsistent or missing | Start with "too much" padding, then adjust to a consistent rhythm |
| Border bloat | Overreliance on borders to define regions | Define areas with subtle container / surface colors instead |
| Content cramming | Squeezing too much info in | Remove elements (via Copywriting) or use progressive disclosure |

List specific findings, e.g.:
- "Price and monthly cost are misaligned across the three plan cards — can't compare at a glance"
- "Every form section has a heavy border, making the whole screen feel boxy"
- "Header menu isn't aligned with the content grid — creates visual noise"

## 3. DECIDE

**Ask the user if:**
- Two+ plausible layouts genuinely compete (e.g., stacked vs columnar dashboard cards — affects density and scanning direction)
- Progressive disclosure tradeoffs — what stays visible vs what collapses is a judgment call

**Decide alone if:**
- Padding / margin micro-adjustments
- Aligning to an existing grid
- Replacing borders with subtle container colors (within brand tokens)
- Fixing obvious proximity violations

## 4. PRODUCE

- Apply Gestalt grouping: use SPACE to group, not borders
- Establish a consistent spacing rhythm from the brand tokens (e.g., 4/8/16/24/32)
- For cramming: apply progressive disclosure (collapse, tabs, accordion, "see more" links, tooltips for secondary info)
- For borders: replace with `surface` or `muted` background tokens from the brand
- Align interactive elements (CTAs, comparable values) to the same grid columns

**Code input:** edit CSS / Tailwind classes in source. Use existing spacing tokens; don't introduce new ones.

**Screenshot / URL input:** update the mockup's layout. **Keep copy from the C pass untouched** — that was finalized.

## 5. VERIFY

- Can the eye follow the screen in a single top-to-bottom pass without backtracking?
- Are related items visually grouped (by proximity, enclosure, or similarity)?
- Is spacing on a consistent rhythm?
- **Re-scan the Copywriting pass** — is all copy still in a sensible place? Any copy hidden, cropped, or orphaned?

## Psychology: Cognitive Load

Working memory is limited. Every extra visual mismatch forces people to re-interpret what they're seeing. Good layout turns messy pixels into predictable structure — that's the cost savings. Clutter isn't just ugly; it's costly.

## Gestalt Principles (deeper dive)

People don't read UIs like documents. They first perceive structure through grouping signals (proximity, similarity, common region), then assign meaning. Gestalt principles are rules of human perception — how our brains group visual elements into unified wholes.

Use them proactively: when you want "these go together," pick one or two Gestalt principles to express that. Don't rely solely on borders.
