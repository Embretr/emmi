# Brand Extraction

Two layers: **visual brand** and **strategic brand**. Both are extracted at Stage 1 of the runbook. The visual layer is a hard constraint on every pass. The strategic layer drives pillar pre-checks — especially Copywriting and Reward.

---

## Visual brand — priority cascade

### Case 1: Input is CODE

**The codebase is the brand source. Full stop.**

Read in this order until you have enough tokens:

1. **Tailwind config** — `tailwind.config.{js,ts,cjs,mjs}`
   - `theme.extend.colors` → primary, surface, muted, accent, state colors
   - `theme.extend.fontFamily` → typography stack
   - `theme.extend.borderRadius` → radius scale
   - `theme.extend.boxShadow` → shadow scale
2. **CSS custom properties** — search CSS files for `:root { --* }` declarations
3. **Design tokens** — `design-tokens.{json,yaml,ts}`, `theme.{ts,js}`, `styled-system/`
4. **1–2 neighboring components** — read to understand spacing rhythm, radius usage, typography scale in practice

**Fallback if no tokens found:** if the codebase has no theme file, no CSS custom properties, no design tokens, and no useful patterns in neighboring components (e.g., all styles are inline and ad-hoc), extract tokens from the actual computed or inline styles of the component being redesigned. Present the inferred token set to the user and ask them to confirm before any pass runs. Do not invent tokens outside what you observe.

**Hard constraint:** NEVER introduce tokens outside the codebase's existing vocabulary unless the user explicitly unlocks them. If a pillar pass suggests a new color / font / radius, surface it as a question:

> "This improvement would require a new token — add one to the design system, or keep within the existing vocabulary?"

### Case 2: Input is URL

1. `mcp__chrome-devtools__navigate_page` to the URL.
2. `mcp__chrome-devtools__take_screenshot` for visual reference (full page).
3. `mcp__chrome-devtools__evaluate_script` to query computed styles:
   - `getComputedStyle(document.body)` → background, font-family, color
   - Primary buttons: query `button, .btn, [role="button"]`, extract `backgroundColor`, `color`, `borderRadius`, `fontSize`, `padding`
   - Surfaces: query cards/containers for `backgroundColor`, `borderRadius`, `boxShadow`
   - Typography scale: query headings and body text for `fontSize`, `fontWeight`, `lineHeight`
4. Combine the visual capture + computed styles into brand tokens.

### Case 3: Input is SCREENSHOT

1. Extract visible tokens from the image:
   - Dominant colors: background, primary CTA, surfaces, accent
   - Typography family (best visual approximation — say what you think it is and tag as approximate)
   - Radius: from visible cards/buttons
   - Shadow style: flat / subtle / pronounced
   - Density: tight / medium / airy
2. Run the **completeness check**:
   - **Required (must have):** primary color, typography family, tone of voice
   - **Nice-to-have (improves quality):** secondary / surface / neutral scale, radius, shadow, iconography, density
3. If coverage is thin (< 70% of required + nice-to-have):
   - **First ask:** "What's the URL for this company? I'll pull brand tokens from the live site — that's the highest-signal source."
   - **If no URL:** "Do you have access to their codebase? Point me at the repo and I'll read theme files directly."
   - **If neither:** use user-provided tokens OR neutral professional defaults with **every assumption tagged ⚠️** in the brand sheet. Proceed, but make the user reconfirm before passes run.

---

## Strategic brand context

Scan the input for signals on these six fields:

| Field | Where to look |
|---|---|
| **Value proposition** | Hero, H1, primary CTA text, tagline |
| **Target audience** | Tone, vocabulary, visual style, featured imagery |
| **Positioning** | Explicit comparison language, differentiators, "unlike X..." phrasings |
| **Tone / voice** | Copy samples — formal/casual, serious/playful, warm/clinical |
| **Key messages** | What's emphasized, repeated, boxed out, illustrated |
| **Screen goal** | Primary CTA + surrounding context — what is the user supposed to do or feel here? |

**For each unclear field:** note the gap. DO NOT ask everything upfront. Let the gap surface at the relevant pillar's PRE-CHECK (mostly Copywriting and Reward).

**Exception:** if value prop is completely indeterminable from the input, ask at Stage 1 — you can't even score without knowing what the screen is trying to do.

---

## Brand-sheet preview

After extraction, render a one-screen summary for the user to confirm. Example structure:

```
┌──────────────────────────────────────────────────────────┐
│  BRAND SHEET — [Company name]                            │
├──────────────────────────────────────────────────────────┤
│  COLORS                                                  │
│    Primary        #XXXXXX                                │
│    Background     #XXXXXX                                │
│    Surface        #XXXXXX                                │
│    Text           #XXXXXX                                │
│    Muted          #XXXXXX                                │
│    [State colors] [hex values]  [⚠ if assumed]           │
│                                                          │
│  TYPOGRAPHY                                              │
│    Family         [e.g., Geist Sans]  [⚠ if approx]      │
│    Scale          [sizes used]                           │
│                                                          │
│  RADIUS & SHADOW                                         │
│    Radius         [values]                               │
│    Shadow         [style summary]                        │
│                                                          │
│  STRATEGIC                                               │
│    Value prop     "[extracted or ⚠ gap]"                 │
│    Audience       [extracted or ⚠ gap]                   │
│    Tone           [extracted or ⚠ gap]                   │
│    Screen goal    [extracted or ⚠ gap]                   │
│                                                          │
│  ⚠ Tagged as assumption — please confirm or correct      │
└──────────────────────────────────────────────────────────┘
```

Present inline as a text block in the conversation, OR write to `<run-folder>/brand-sheet.html` as an HTML preview opened in the browser.

User has final word. Their corrections become the brand constraint for the rest of the run.
