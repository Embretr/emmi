# Emphasis Pillar — CLEAR Framework

Use size, color, contrast, movement, and space so people can't miss the **one thing** you don't want them to miss. That also means turning the volume DOWN on other elements so the key element stands out first.

- Emphasis is how you control attention — not how you decorate.
- Hierarchy is relative: one element can only stand out if others step back.
- You create hierarchy with 6 simple dials (see below).

## The 6 Emphasis Dials

1. **Size** — bigger draws the eye
2. **Color** — a brand-colored element vs neutral surroundings
3. **Contrast** — stronger text/background contrast pulls attention
4. **Movement** — subtle motion is a powerful attention magnet (use sparingly)
5. **Space** — isolated elements get disproportionate attention
6. **Position** — top-left and center get seen first on Western reading orders

Most hierarchy comes from what you turn DOWN, not what you turn up.

## 1. PRE-CHECK

- **What is THE ONE thing that matters on this screen?** If not obvious, ASK:
  - General: *"What should this screen make unmissable? The primary CTA? A data point? A status change?"*
  - Dashboard: *"What should the user notice first at a glance — the top-line KPI? An anomaly? A quick action?"*

Without a defined lead, Emphasis has nothing to anchor. Do not proceed without it.

## 2. DIAGNOSE

Check for the 3 common mistakes:

| Mistake | Problem | Solution |
|---|---|---|
| Wrong Dial | Solving with color when the real issue is placement or space | Diagnose first: what's competing? Pick the dial that actually changes attention for that context (often placement + space beats color). |
| Weak Dial | "Kind of" adjusting everything; nothing stands out | Make one dial clearly different. Fewer changes, but bolder. |
| Screaming Dial | Cranking multiple dials to max (giant + neon + shadow + animation) | Establish a calm baseline, then lead with 1–2 dials. Most hierarchy comes from what you turn DOWN. |

Also check:
- **Does the lead element have at least 2 dials clearly tuned for it**, and are competing elements' dials turned DOWN?
- **Is there a calm baseline** for the rest of the screen?

## 3. DECIDE

**Ask the user if:**
- Which element leads? Always ask if ambiguous — this is the pass's defining choice.
- Trade-off between aggressive emphasis and brand calm (e.g., muted brand vs need for bold CTA).

**Decide alone if:**
- Which dial(s) to use once the lead is chosen. (Size + space is usually stronger than color alone.)
- Magnitude of adjustments, as long as within brand tokens.

## 4. PRODUCE

- For the LEAD element: turn UP 1–2 dials boldly (e.g., size + color; or size + position). Don't turn up more than 2 — that's screaming.
- For COMPETING elements: turn DOWN visually (smaller, muted, pushed to a secondary region). "Relative emphasis" matters more than absolute values.
- Apply **Reactance** principle: don't pressure users with visual aggression. Give autonomy and a clear path.

**Code input:** adjust class-level properties (font-size, color, margin, position) using existing brand tokens only.

**Screenshot / URL input:** update the HTML mockup accordingly.

## 5. VERIFY — Squint Test (MANDATORY)

Run automatically after every Emphasis pass. This is the pass's signature verification.

### Squint Test mechanics

```
Step 1: Open the current mockup (or rendered code) in a Chrome tab
        via mcp__chrome-devtools.
        - For mockup: mcp__chrome-devtools__new_page with file://
          path to mockup.html (new_page creates a fresh tab; use
          this for local file paths)
        - For code with dev server: mcp__chrome-devtools__navigate_page
          to the component's URL (navigate_page moves an existing
          tab; use this for http/https URLs)

Step 2: Apply the blur filter:
        mcp__chrome-devtools__evaluate_script:
          () => { document.body.style.filter = 'blur(10px)'; }

Step 3: Take a screenshot:
        mcp__chrome-devtools__take_screenshot

Step 4: Analyze the screenshot:
        - Is the intended primary element (declared in section 1
          PRE-CHECK) still the dominant shape?
        - Are competing elements visually quieter?

Step 5:
  PASS → remove the filter:
         mcp__chrome-devtools__evaluate_script:
           () => { document.body.style.filter = ''; }
         → advance to Accessibility.

  FAIL → identify the element that's still competing.
         Propose a specific dial adjustment ("reduce secondary
         button size by 20%", "mute the subtitle color").
         Loop back to section 3 (DECIDE) and 4 (PRODUCE).
         Re-run squint.
```

**Escape valve:** if 3 iterations fail, stop and surface the situation to the user. They may need to rethink content priorities or unlock brand constraints.

**If `mcp__chrome-devtools` is unavailable:** fall back to manual mode — describe what a blurred view of the mockup should reveal (blur softens detail, leaving only size / contrast / position / space signals), and ask the user: *"When you view the mockup and squint, is [your declared primary element] still the most prominent? If not, what's competing?"* Proceed based on their answer. Note in the final report that the automated Squint Test was unavailable.

## Psychology

- **Foggy Glasses Test** — blurring removes details, leaving only size/contrast/position/spacing. The lead should still be obvious. The Squint Test is this, mechanized.
- **Relative Emphasis** — importance is perceived as contrast, not absolute values. A button isn't "big" by itself — it's big *relative to* its surroundings.
- **Reactance** — if a UI pushes too hard, users push back. Paradox: if everything is emphasized, nothing stands out. Avoid extremes. Give users autonomy, clear options, and an obvious path to follow.
