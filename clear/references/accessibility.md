# Accessibility Pillar — CLEAR Framework

Accessibility is about making your product usable for more people in more situations. It's not just a compliance thing — when you design with different abilities, devices, and contexts in mind, your interface becomes more forgiving for everyone.

## Design for 3 realities

1. **Permanent** — long-term limitations (vision, motor, hearing, cognitive)
2. **Temporary** — short-term (broken arm, eye surgery, sleep-deprived)
3. **Situational** — "life is happening" (bright sun, subway, holding a baby, distracted)

## 1. PRE-CHECK

- Target device / context clear? Mobile, desktop, kiosk, outdoor? Affects contrast and target sizing standards.
- If unclear, ASK: *"Where will this primarily be used? Any known constraints — older users, outdoor sunlight, one-handed use?"*

## 2. DIAGNOSE

### 7 common accessibility mistakes

- **🐜 Tiny & close targets** — <44px tap targets on mobile; dense clickable areas
- **👓 Low contrast text** — below WCAG AA (4.5:1 for normal text, 3:1 for large text)
- **▶️ Actions that don't look clickable** — text-only "buttons", no hover state, no visual affordance
- **👻 Missing hints** — primary actions hidden in three-dot menus or behind hover
- **🟢🔴 Color-only meaning** — status by color alone, no icon or label
- **🔀 Too many patterns in one view** — tabs + pills + chips + toggles all competing
- **💭 "They'll figure it out" assumptions** — hidden interactions, dense tooltips, no affordances

### Also check: Error prevention

- Are invalid states preventable?
- Is undo available for reversible actions?
- Are destructive / irreversible actions confirmed?

## 3. DECIDE

**Mostly decide alone.** Accessibility is rule-based, not preference-based.

**Only ask the user if:**
- A brand token fails accessibility (e.g., light-gray secondary text fails WCAG AA). Propose two paths:
  - (a) override the brand for this screen
  - (b) introduce an on-brand *accessible* variant to the token set
  This is the only case where brand vs accessibility requires a user judgment call.

## 4. PRODUCE

Apply the 3 principles from the course:

### 1. Visible without searching
Primary action visible on load — no scrolling, no digging, no guessing. Can you see the main action without hunting?

### 2. Operable without precision
Can you hit it easily even with reduced precision (thumb, motion, fatigue)?
- ≥44px touch targets on mobile
- ≥32px on desktop
- Adequate spacing between interactive elements

### 3. Actionable without guessing
Do actions look like actions?
- Buttons have button affordances (background, shadow, or border)
- Links look clickable (distinct color + underline on hover)
- Disabled states differ clearly from enabled

### Non-color redundancy
If status uses color, add an icon and/or label.

### Error prevention
- Disable invalid states instead of letting people submit into failure
- Always offer undo for reversible actions
- Confirm destructive / irreversible actions

**Code input:** update component styles, ARIA attributes, roles. Keep within brand tokens (except when unlocking for an accessibility-required adjustment via step 3).

**Screenshot / URL input:** update mockup spacing, contrast, affordances.

## 5. VERIFY

Automated checks (on mockup or rendered code):

- **Contrast ratios** — compute for every critical text/UI pair. Target: WCAG AA minimum (4.5:1 normal text, 3:1 large text / UI components). Use a contrast checker script in the browser console or a calculation against computed styles.
- **Target sizes** — measure clickable areas in rendered pixels. Target: 44px mobile, 32px desktop.
- **Color-only meaning** — scan for status indicators relying solely on color. Every state should have a secondary signal.

**Re-scan the Emphasis pass** — did any accessibility fix (darker gray, bolder outline) break hierarchy? If so, flag and rework that element.

## Psychology

- **First Impression Bias** — first interactions set the tone. If the start feels confusing, users assume the whole product is hard. Simple, obvious first actions create "I get this" quickly.
- **Error Prevention** — most accessibility failures are slip-ups, not cognitive failures. People know what to do, but the UI makes it easy to do the wrong thing. Preventing mistakes beats helpful error messages.
