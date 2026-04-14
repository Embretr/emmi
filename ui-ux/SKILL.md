---
name: emmi-ui-ux
description: >-
  Emmi UI/UX: implement or refine interfaces using the ui-blocks library plus domain-specific rules for ecommerce,
  marketing, and application UIs. Use for landing pages, shops, dashboards, design polish, Tailwind layout work,
  or "make it match our kit".
---

# UI / UX

## Communication style

- Never use emojis in any output, code comments, docs, or generated content unless the user explicitly requests them.

## Design system (required before any UI work)

**Never start UI work without a design system.** Before writing a single component:

1. Check the repo root for `DESIGN_SYSTEM.md` (or equivalent: `design-system.md`, `docs/design-system.md`, `design/DESIGN_SYSTEM.md`).
2. If it exists — read it. All decisions in it take precedence over these skill defaults.
3. If it does not exist — create it at the repo root using the template below before proceeding. Fill in every section. Do not leave placeholders unless assets are genuinely not yet decided, in which case mark them `TBD` and note what is needed.

A design system is not optional and not a nice-to-have. Every color, font, spacing value, shadow, and radius used in the UI must trace back to a token defined in it.

---

### Template: `DESIGN_SYSTEM.md`

Copy this template verbatim and fill it in. Delete no sections — mark undecided values as `TBD`.

The design system is the single source of truth. When build-out is complete, it produces three real output files that must be kept in sync with it:
- `globals.css` — all CSS custom properties (shadcn convention)
- `tailwind.config.ts` — extends Tailwind with the same tokens
- `lib/tokens.ts` — typed token exports for use in JS/TS (animations, z-index, etc.)

````markdown
# Design System

## Overview

| Property | Value |
|----------|-------|
| Product name | |
| Brand personality | (e.g. "Calm, precise, professional" / "Bold, energetic, direct") |
| Target audience | |
| UI mode default | Light / Dark / System |
| Primary framework | Next.js + shadcn/ui + Tailwind CSS v4 |
| Icon library | Lucide React |
| Last updated | |

> Brand rationale: explain the personality choices and what they should communicate to the target audience.

---

## Typography

### Font families

| Role | Family | CSS variable | Fallback stack |
|------|--------|-------------|----------------|
| Display / heading | | `--font-display` | system-ui, sans-serif |
| Body | | `--font-body` | system-ui, sans-serif |
| Mono | | `--font-mono` | ui-monospace, monospace |

> Rationale: why these fonts, and what do they communicate about the brand?

### Type scale

All sizes defined as CSS custom properties and extended in `tailwind.config.ts`.

| Token | CSS var | Size | Line height | Weight | Letter spacing | Usage |
|-------|---------|------|-------------|--------|----------------|-------|
| `display-2xl` | `--text-display-2xl` | 4.5rem | 1.1 | 600 | -0.02em | Hero headlines |
| `display-xl` | `--text-display-xl` | 3.75rem | 1.2 | 600 | -0.02em | Section headlines |
| `display-lg` | `--text-display-lg` | 3rem | 1.25 | 600 | -0.01em | Page titles |
| `display-md` | `--text-display-md` | 2.25rem | 1.3 | 600 | -0.01em | Card titles |
| `display-sm` | `--text-display-sm` | 1.875rem | 1.35 | 600 | 0 | Sub-section titles |
| `text-xl` | `--text-xl` | 1.25rem | 1.75 | 400 | 0 | Large body, intros |
| `text-lg` | `--text-lg` | 1.125rem | 1.75 | 400 | 0 | Body default |
| `text-md` | `--text-md` | 1rem | 1.5 | 400 | 0 | UI text, paragraphs |
| `text-sm` | `--text-sm` | 0.875rem | 1.5 | 400 | 0 | Secondary labels, captions |
| `text-xs` | `--text-xs` | 0.75rem | 1.5 | 400 | 0 | Timestamps, metadata |

---

## Color system

### Primitives (raw palette — never reference these directly in components)

```css
/* Gray */
--gray-25:  #FCFCFD;
--gray-50:  #F9FAFB;
--gray-100: #F2F4F7;
--gray-200: #EAECF0;
--gray-300: #D0D5DD;
--gray-400: #98A2B3;
--gray-500: #667085;
--gray-600: #475467;
--gray-700: #344054;
--gray-800: #1D2939;
--gray-900: #101828;
--gray-950: #0C111D;

/* Brand — fill in */
--brand-25:  ;
--brand-50:  ;
--brand-100: ;
--brand-200: ;
--brand-300: ;
--brand-400: ;
--brand-500: ; /* primary */
--brand-600: ;
--brand-700: ;
--brand-800: ;
--brand-900: ;

/* Semantic status */
--error-50: ; --error-300: ; --error-500: ; --error-600: ; --error-700: ;
--warning-50: ; --warning-300: ; --warning-500: ; --warning-600: ; --warning-700: ;
--success-50: ; --success-300: ; --success-500: ; --success-600: ; --success-700: ;
```

### Semantic tokens → `globals.css` (shadcn convention)

These are the tokens components use. They map primitives to roles and flip in dark mode.

```css
@layer base {
  :root {
    /* Backgrounds */
    --background:        ; /* page background */
    --background-subtle: ; /* section / card background */
    --background-muted:  ; /* inset, inputs */

    /* Foregrounds */
    --foreground:        ; /* primary text */
    --foreground-muted:  ; /* secondary text */
    --foreground-subtle: ; /* placeholder, metadata */

    /* shadcn core tokens */
    --card:              ;
    --card-foreground:   ;
    --popover:           ;
    --popover-foreground:;
    --primary:           ; /* brand primary — buttons, links */
    --primary-foreground:;
    --secondary:         ;
    --secondary-foreground:;
    --muted:             ;
    --muted-foreground:  ;
    --accent:            ;
    --accent-foreground: ;
    --destructive:       ;
    --destructive-foreground:;
    --border:            ;
    --input:             ;
    --ring:              ; /* focus ring */

    /* Status */
    --success:           ;
    --success-foreground:;
    --warning:           ;
    --warning-foreground:;
    --error:             ; /* alias for --destructive */

    /* Radius base — all component radii derive from this */
    --radius: 0.5rem;
  }

  .dark {
    /* Mirror all tokens above with dark-mode values */
    --background:        ;
    --background-subtle: ;
    --background-muted:  ;
    --foreground:        ;
    --foreground-muted:  ;
    --foreground-subtle: ;
    --card:              ;
    --card-foreground:   ;
    --popover:           ;
    --popover-foreground:;
    --primary:           ;
    --primary-foreground:;
    --secondary:         ;
    --secondary-foreground:;
    --muted:             ;
    --muted-foreground:  ;
    --accent:            ;
    --accent-foreground: ;
    --destructive:       ;
    --destructive-foreground:;
    --border:            ;
    --input:             ;
    --ring:              ;
    --success:           ;
    --success-foreground:;
    --warning:           ;
    --warning-foreground:;
  }
}
```

---

## Spacing scale

Base unit: 4px. Tailwind's default scale covers this — do not override it. Use the standard scale.

| Usage | Value | Tailwind class |
|-------|-------|----------------|
| Section vertical padding (desktop) | 80px | `py-20` |
| Section vertical padding (mobile) | 48px | `py-12` |
| Card internal padding | 24px | `p-6` |
| Form field gap | 20px | `gap-5` |
| Inline element gap | 8px | `gap-2` |

---

## Border radius

Shadcn derives all radii from `--radius`. Define component radii as multiples.

| Token | CSS var | Value | Usage |
|-------|---------|-------|-------|
| none | — | 0 | Full-bleed, tables |
| xs | `calc(var(--radius) - 6px)` | ~2px | Badges, chips |
| sm | `calc(var(--radius) - 4px)` | ~4px | Inputs, small buttons |
| md | `var(--radius)` | 8px | Cards, dropdowns (default) |
| lg | `calc(var(--radius) + 4px)` | ~12px | Large cards, panels |
| xl | `calc(var(--radius) + 8px)` | ~16px | Sheets, drawers |
| full | 9999px | — | Pills, avatars, toggles |

Set `--radius` in `:root` to shift the entire UI's roundness at once.

---

## Shadows and elevation

```css
/* Add to globals.css or tailwind.config.ts boxShadow extension */
--shadow-xs:  0 1px 2px hsl(0 0% 0% / 0.05);
--shadow-sm:  0 1px 3px hsl(0 0% 0% / 0.10), 0 1px 2px hsl(0 0% 0% / 0.06);
--shadow-md:  0 4px 8px -2px hsl(0 0% 0% / 0.10), 0 2px 4px -2px hsl(0 0% 0% / 0.06);
--shadow-lg:  0 12px 16px -4px hsl(0 0% 0% / 0.08), 0 4px 6px -2px hsl(0 0% 0% / 0.03);
--shadow-xl:  0 20px 24px -4px hsl(0 0% 0% / 0.08), 0 8px 8px -4px hsl(0 0% 0% / 0.03);
--shadow-2xl: 0 24px 48px -12px hsl(0 0% 0% / 0.18);
```

| Token | Usage |
|-------|-------|
| `shadow-xs` | Inputs, subtle lift |
| `shadow-sm` | Cards at rest |
| `shadow-md` | Hovered cards, dropdowns |
| `shadow-lg` | Modals, popovers |
| `shadow-xl` | Drawers, command palette |
| `shadow-2xl` | Full-screen overlays |

---

## Motion tokens → `lib/tokens.ts`

```ts
export const duration = {
  fast:   100, // micro-interactions: button press, checkbox, badge
  normal: 200, // tooltips, small state changes, icon swaps
  slow:   300, // modals, drawers, page transitions
  enter:  200, // elements entering the DOM
  exit:   150, // elements leaving — always shorter than enter
} as const

export const easing = {
  enter:  'cubic-bezier(0.0, 0.0, 0.2, 1)', // ease-out
  exit:   'cubic-bezier(0.4, 0.0, 1, 1)',   // ease-in
  inOut:  'cubic-bezier(0.4, 0.0, 0.2, 1)', // ease-in-out
} as const
```

No animation exceeds 400ms. Exit is always faster than enter.

---

## Breakpoints → `tailwind.config.ts`

```ts
screens: {
  sm:  '390px',   // standard mobile
  md:  '768px',   // tablet
  lg:  '1024px',  // laptop
  xl:  '1280px',  // desktop
  '2xl': '1536px', // wide desktop
  '3xl': '1920px', // superwide — always constrain max-width here
},
```

Max content width: `max-w-screen-xl` (1280px). Wide variant: `max-w-screen-2xl`.

---

## Z-index scale → `tailwind.config.ts`

```ts
zIndex: {
  base:     '0',
  raised:   '10',
  dropdown: '100',
  sticky:   '200',
  overlay:  '300',
  modal:    '400',
  toast:    '500',
  tooltip:  '600',
},
```

---

## `tailwind.config.ts` — full extension block

```ts
import type { Config } from 'tailwindcss'

const config: Config = {
  darkMode: ['class'],
  content: ['./app/**/*.{ts,tsx}', './components/**/*.{ts,tsx}'],
  theme: {
    extend: {
      colors: {
        background:  'hsl(var(--background) / <alpha-value>)',
        foreground:  'hsl(var(--foreground) / <alpha-value>)',
        card: {
          DEFAULT:    'hsl(var(--card) / <alpha-value>)',
          foreground: 'hsl(var(--card-foreground) / <alpha-value>)',
        },
        popover: {
          DEFAULT:    'hsl(var(--popover) / <alpha-value>)',
          foreground: 'hsl(var(--popover-foreground) / <alpha-value>)',
        },
        primary: {
          DEFAULT:    'hsl(var(--primary) / <alpha-value>)',
          foreground: 'hsl(var(--primary-foreground) / <alpha-value>)',
        },
        secondary: {
          DEFAULT:    'hsl(var(--secondary) / <alpha-value>)',
          foreground: 'hsl(var(--secondary-foreground) / <alpha-value>)',
        },
        muted: {
          DEFAULT:    'hsl(var(--muted) / <alpha-value>)',
          foreground: 'hsl(var(--muted-foreground) / <alpha-value>)',
        },
        accent: {
          DEFAULT:    'hsl(var(--accent) / <alpha-value>)',
          foreground: 'hsl(var(--accent-foreground) / <alpha-value>)',
        },
        destructive: {
          DEFAULT:    'hsl(var(--destructive) / <alpha-value>)',
          foreground: 'hsl(var(--destructive-foreground) / <alpha-value>)',
        },
        success: {
          DEFAULT:    'hsl(var(--success) / <alpha-value>)',
          foreground: 'hsl(var(--success-foreground) / <alpha-value>)',
        },
        warning: {
          DEFAULT:    'hsl(var(--warning) / <alpha-value>)',
          foreground: 'hsl(var(--warning-foreground) / <alpha-value>)',
        },
        border: 'hsl(var(--border) / <alpha-value>)',
        input:  'hsl(var(--input) / <alpha-value>)',
        ring:   'hsl(var(--ring) / <alpha-value>)',
      },
      borderRadius: {
        sm:   'calc(var(--radius) - 4px)',
        md:   'var(--radius)',
        lg:   'calc(var(--radius) + 4px)',
        xl:   'calc(var(--radius) + 8px)',
      },
      fontFamily: {
        display: ['var(--font-display)', 'system-ui', 'sans-serif'],
        body:    ['var(--font-body)',    'system-ui', 'sans-serif'],
        mono:    ['var(--font-mono)',    'ui-monospace', 'monospace'],
      },
      screens: {
        sm:    '390px',
        md:    '768px',
        lg:    '1024px',
        xl:    '1280px',
        '2xl': '1536px',
        '3xl': '1920px',
      },
      zIndex: {
        raised:   '10',
        dropdown: '100',
        sticky:   '200',
        overlay:  '300',
        modal:    '400',
        toast:    '500',
        tooltip:  '600',
      },
      boxShadow: {
        xs:   'var(--shadow-xs)',
        sm:   'var(--shadow-sm)',
        md:   'var(--shadow-md)',
        lg:   'var(--shadow-lg)',
        xl:   'var(--shadow-xl)',
        '2xl':'var(--shadow-2xl)',
      },
    },
  },
  plugins: [require('tailwindcss-animate')],
}

export default config
```

---

## Component defaults

### Buttons

Uses shadcn `Button` with `variant` prop. Do not create custom button primitives.

| Variant | Token mapping | Usage |
|---------|--------------|-------|
| `default` | `primary` bg, `primary-foreground` text | Main CTA — one per section |
| `secondary` | `secondary` bg, `secondary-foreground` text | Secondary actions |
| `outline` | `border` border, `background` bg | Tertiary |
| `ghost` | transparent, hover `accent` bg | Icon buttons, subtle actions |
| `destructive` | `destructive` bg | Delete, remove, irreversible |
| `link` | transparent, `primary` text, underline on hover | Inline text actions |

Sizes: `sm` (h-8), `default` (h-10), `lg` (h-11). Minimum touch target 44px on mobile.

### Form inputs

Uses shadcn `Input`, `Select`, `Textarea`. State tokens:

| State | Ring / border | Background |
|-------|--------------|-----------|
| Default | `border` | `background` |
| Focus | `ring` (2px `ring` color) | `background` |
| Error | `destructive` ring | `background` |
| Disabled | `muted` border | `muted` bg |

Label above input, always visible. Error message inline below field in `destructive` color.

### Badges and status indicators

| Variant | Token | Usage |
|---------|-------|-------|
| Default | `secondary` | Neutral, draft, inactive |
| Outline | `border` | Subtle, informational |
| Destructive | `destructive` | Error, rejected, failed |
| Success | `success` | Completed, live |
| Warning | `warning` | Pending, expiring |

Always pair color with a text label. Never color alone.

---

## Icon system

| Property | Value |
|----------|-------|
| Library | Lucide React (`lucide-react`) |
| Inline UI size | 16px (`size-4`) |
| Standalone size | 20px (`size-5`) |
| Stroke width | 1.5 (Lucide default) |
| Color | `currentColor` — inherits from parent text |

`aria-hidden="true"` by default. Add `aria-label` only when the icon is the sole label of an interactive element.

---

## Grid and layout

| Property | Value |
|----------|-------|
| Max content width | `max-w-screen-xl` (1280px), centered |
| Wide variant | `max-w-screen-2xl` (1536px) |
| Page margin (desktop) | `px-8` (32px) inside container |
| Page margin (mobile) | `px-4` (16px) inside container |
| Section padding (desktop) | `py-20` (80px) |
| Section padding (mobile) | `py-12` (48px) |

---

## Voice and copy style

| Property | Guideline |
|----------|-----------|
| Tone | TBD |
| CTA style | Verb-first: "Start free trial", "View details", "Save changes" |
| Error messages | State what failed and what to do next. Never "Something went wrong." |
| Empty states | Explain what goes here and provide a primary action to fill it. |
| Loading states | Skeleton screens. Progress label for async actions over 2 seconds. |

---

## Changelog

| Date | Change |
|------|--------|
| | Initial design system |
````

---

### Building the design system with the user

Never fill in the design system with assumptions. When `DESIGN_SYSTEM.md` does not exist, enter an interactive build-out flow before writing any UI:

1. **Ask questions in focused batches** — 4 to 6 questions per message, grouped by theme. Do not dump everything at once.
2. **Cover every section** — work through brand personality, typography, color, spacing, motion, and component defaults until nothing is `TBD`.
3. **Make recommendations, not blanks** — for each question, offer a concrete default or example and ask the user to confirm, adjust, or replace it. This is faster than asking open-ended questions.
4. **Derive what you can** — if the user gives you a brand color, derive the full primitive palette and semantic tokens. If they give you a personality ("calm, minimal"), recommend font pairings that match.
5. **Write the file incrementally** — after each batch, update the relevant sections in `DESIGN_SYSTEM.md`. The user can course-correct before you proceed to the next batch.
6. **Do not start building UI until the file has no `TBD` entries in the core sections** (typography, color, spacing, radius). Motion, icons, and voice can be filled in later.

All UI work after this point — every component, every layout, every block — must reference tokens from `DESIGN_SYSTEM.md`. No raw hex values, no arbitrary spacing, no one-off font sizes in component code.

### After creating the file

- Commit it immediately: `git add DESIGN_SYSTEM.md && git commit -m "docs: add design system"`
- All subsequent UI work references tokens from it by name — no raw hex values or arbitrary spacing in component code.
- When a new pattern is established in code that isn't in the design system, update the file in the same PR.

## Block library

Kit root sibling **`ui-blocks/`**:

- [CATALOG.md](../ui-blocks/CATALOG.md) — master map  
- Per-pack indexes: `ui-blocks/marketing/BLOCKS.md`, `ecommerce`, `application`, `components`

**Fetch flow:** read **BLOCKS.md** for the right pack, then **Read** only the `.jsx` / `.tsx` files you need. Adapt to app tokens, routing, and data.

## Mode selection

Before any design or implementation work, identify which mode applies. Ask if unclear.

| Mode | When to use |
|------|-------------|
| **Marketing** | Landing pages, campaign pages, content-heavy public pages |
| **Application** | Dashboards, SaaS UIs, admin panels, authenticated flows |
| **Ecommerce** | Product listings, PDPs, cart, checkout, order management |
| **Mobile / App** | Expo + NativeWind native screens (iOS/Android) |

Hybrid is allowed — state which modes are active and apply both rule sets.

**Mobile / App sub-mode:** Mobile is not a standalone rule set. When the platform is mobile/native, first identify the category (Marketing, Application, or Ecommerce) and apply those same domain rules — adapted for native constraints: touch targets, native navigation patterns, NativeWind, and no browser-based responsive breakpoints.

## Responsive design (always required)

Every web UI must work across the full screen-size spectrum without exception:

- **Superwide (1920px+):** constrain max-width, prevent content from sprawling; use the extra space intentionally (wider columns, sidebars, richer layouts).
- **Desktop (1280–1920px):** primary design target for application and ecommerce.
- **Laptop (1024–1280px):** watch for nav and sidebar collisions.
- **Tablet (768–1024px):** consider touch targets; decide whether to show mobile or desktop nav.
- **Mobile (390–768px):** thumb reach for primary CTAs; stack columns; full-width inputs.
- **Small phone (320–390px):** test that nothing breaks or overflows at minimum widths.

Use Tailwind responsive prefixes (`sm:`, `md:`, `lg:`, `xl:`, `2xl:`) throughout. Never hardcode pixel widths that break at extreme ends. Test or review at both extremes before marking work done.

## Interaction economy (all modes, always)

**The preemptive principle:** always act on the user's behalf as early as possible. Do the thing, then give them a way to undo it — do not ask for permission first. A Back button costs nothing. A Next button costs a click, a read, a decision, and a moment of friction on every single use.

Every interaction the user performs must be absolutely required. If an action can be eliminated, inferred, automated, or defaulted — it must be. The goal is the minimum number of interactions to reach the outcome.

**Patterns — implement these wherever they apply:**

- **Auto-advance after single selection.** User picks one option, move on immediately. No Next button. Back button to undo.
- **Pre-fill everything you already know.** User is logged in — you have their name, email, address. Don't ask again. Pre-fill and let them correct.
- **Inline editing.** Click the text to edit it. No separate edit mode, no edit page for simple values.
- **Smart defaults on date pickers.** If context implies "today" or "next week", pre-select it. Never open a date picker on a blank state when the answer is obvious.
- **Auto-format as you type.** Phone numbers, card numbers, IBANs, sort codes — format them in real time. Never instruct the user on format; enforce it silently.
- **Dismiss on outside click.** Modals, dropdowns, popovers — clicking outside closes them. A close button is a fallback, not the primary dismiss method.
- **Auto-select all on focus.** If the user is likely replacing the value rather than appending to it, select the full contents on focus.
- **Skip steps that don't apply.** Conditional flows must hide irrelevant steps entirely — not grey them out, not show them as disabled. If step 2 makes step 4 irrelevant, step 4 does not appear.
- **Remember last used option.** Sort order, filter state, view mode, tab selection — restore it on next visit. Users set preferences once; they do not re-set them every session.
- **Single-click confirm for low-stakes actions.** "Are you sure?" dialogs on reversible actions are unnecessary friction. Use inline undo instead. Reserve confirmation dialogs for genuinely irreversible, high-consequence actions.
- **Search triggers on type.** No search button. Results update as the user types, with appropriate debounce. A search button exists only as an accessible fallback.
- **Tab order matches reading order.** Keyboard users must never have to reach for the mouse because the focus sequence is wrong.
- **Clipboard detection.** If the user has a URL, code, or recognisable value copied, detect it and offer to pre-fill. Especially valuable on first-load of an input that commonly receives pasted values.
- **Return key submits the obvious action.** In a single-field form or on the last field of a form, Enter submits. Never require the user to move to the submit button.
- **Infinite scroll where pagination adds nothing.** If the only reason for a Next Page button is to load more items in a list, replace it with scroll-triggered loading. Pagination is justified when page position is meaningful or shareable.

**Advanced patterns — apply where relevant:**

- **Sticky context.** User is deep in a flow — always show where they are and what they're doing. Breadcrumb, step indicator, or at minimum a persistent title. Never leave the user disoriented.
- **Preserve scroll position.** User clicks into a detail, hits back, lands exactly where they were — not the top of the list.
- **Optimistic UI.** Assume the action succeeds, update the UI instantly, roll back silently if it fails. Never make the user wait for confirmation of a fast operation.
- **Bulk actions appear on selection.** Do not show bulk controls until the user has selected more than one item. They are noise until they are relevant.
- **Drag handles appear on hover.** Reorderable lists show handles only on hover. Persistent handles add visual clutter for a capability most users use rarely.
- **Filter state persists in the URL.** Active filters, sort order, and view mode are reflected in the URL so the user can share, bookmark, or refresh and land in the same state.
- **Destructive actions require directional intent.** Swipe-to-delete requires a deliberate directional swipe, not incidental contact. Prevents accidental deletion.
- **Command palette.** Power users skip navigation entirely. `Cmd+K` or `/` opens a command palette to reach any action or page. Non-negotiable for any application UI.
- **Contextual help inline.** A `?` icon or tooltip adjacent to a confusing field. Help lives next to the thing that needs it — not in a docs page the user will never visit.
- **Mark optional fields, not required.** Most fields are required. Label the exceptions with "(optional)" instead of marking every required field with an asterisk.
- **Shift+click multi-select.** Standard OS behaviour. Users expect it. Do not reinvent selection mechanics.
- **Show password toggle.** One icon, always present on password inputs. Eliminates the most common login frustration.
- **Autosave with a quiet indicator.** "Saved 2s ago" in a corner. Removes anxiety without interrupting the user's flow.
- **Expandable rows instead of new pages.** Detail that is useful but not always needed belongs in an inline expansion, not a navigation event.
- **Highlight what changed.** After a save or update, briefly highlight the affected element. Confirms the action worked without a toast or modal.
- **Input masks that guide, not block.** Show the format as placeholder text as the user types. Never reveal a format error only after submission.
- **Persist table preferences.** Column widths, column order, row density — if the user configures it, remember it across sessions.
- **Double-click to edit.** Natural for table cells and inline list values. No separate edit button required.
- **Typeahead on every dropdown over 5 items.** No user should scroll a list of countries, timezones, or currencies. Filter-as-you-type is the minimum.
- **Drag to reorder with live preview.** Show the item's final position as the user drags, not only after they drop.

**Tables:**

- **Sticky headers always.** User scrolls down a long table — headers stay visible. No exceptions.
- **Sort indicator on hover, persisted on active.** Do not show sort arrows on every column at all times. Show on hover, keep visible on the active sort column.
- **Freeze first column on wide tables.** When the table requires horizontal scroll, the row identifier column stays locked. Users must always know which row they are on.
- **Export matches the filtered view.** If the user has filtered a table, export that exact view — not the full dataset. Exporting more than what is visible is a trust violation.
- **Pagination shows total context.** "Page 2 of 14" or "Showing 20 of 340 results." Users need to understand the scale of what they are working with.
- **Jump-to-page input on large paginated sets.** For datasets where next/prev paging is impractical, provide a "Go to page ___" input.

**Forms:**

- **Inline validation on blur, not on submit.** Validate each field when the user leaves it. Never let them submit and receive 6 errors at once.
- **Never clear a form on error.** If submission fails, all input stays exactly as the user left it. Losing filled data on a failed submit is unforgivable.
- **Show character count before the limit, not after.** Counter appears when the user is approaching the limit — not only when they have exceeded it.
- **Disabled buttons explain why on hover.** A tooltip on every disabled button: "Complete step 1 first", "Enter a valid email", etc. A disabled button with no explanation is a dead end.
- **Loading state on the button itself.** Spinner replaces the button label on submit. Not a separate page-level spinner.
- **Prevent double submit.** Disable the button immediately on first click. Prevents duplicate orders, duplicate posts, duplicate charges.
- **Tab between fields without losing state.** Tabbing away does not reset, revalidate aggressively, or clear input.
- **Section-level save in long forms.** Do not force users to scroll to a single save button at the bottom of a long form.
- **Warn before leaving with unsaved changes.** "You have unsaved changes" on any navigation away from a dirty form.
- **Multi-step forms show a summary before final submit.** Let the user review everything before committing. Especially required for financial, legal, or irreversible submissions.
- **Smart paste in multi-field inputs.** Paste a full phone number, date, or OTP into the first field — it splits across fields automatically.
- **OTP fields auto-advance.** Type a digit, cursor moves to the next field. Never require the user to click each individual box.
- **Correct keyboard type on mobile.** `inputmode="numeric"` for numbers, `inputmode="email"` for email, `inputmode="tel"` for phone. No excuse not to.
- **Address autocomplete.** Never ask users to type full addresses manually. Use an autocomplete API, pre-fill city and postcode from partial input.
- **Country auto-detected from IP.** Pre-select the user's country in country dropdowns. They can correct it, but start correct.
- **Currency and units match locale.** Detect locale and show the appropriate currency and unit system. Do not show imperial to metric users or USD to European users without detection.

**Notifications:**

- **Badge clears after viewing.** Notification badges disappear after the user has seen the content. Persisting a badge they have already addressed destroys trust in the badge.
- **Mark all as read.** Always present. Never force the user to open every individual notification to clear a count.
- **Group notifications by type or source.** 3 grouped notifications beats 40 individual ones every time.

**Settings:**

- **Settings search for panels with more than 20 options.** Nobody browses a long settings list. A search field is the minimum.

**Onboarding:**

- **Teach by doing, not by touring.** Onboarding is a real task that naturally exercises the key features — not a modal carousel pointing at UI elements.
- **Onboarding progress persists across sessions.** If onboarding spans multiple steps, remember exactly where the user left off. Never restart from step 1.

**Accessibility and keyboard:**

- **Focus trap in modals.** Tab cycles only within the open modal. Users must never be able to accidentally tab into content behind it.
- **Escape always closes.** Modals, drawers, dropdowns, tooltips — Escape closes them. No exceptions, no custom overrides.
- **Back button closes modal before leaving page.** Intercept the browser back event to dismiss open overlays first. Only navigate back if nothing is open.

**Mobile-native behaviour:**

- **Pull to refresh.** Any screen with live data supports pull-to-refresh. It is a standard mobile expectation, not an enhancement.
- **Swipe to go back.** Never block or override native swipe-back gestures. Work with them.
- **Long press for secondary actions.** Mobile equivalent of right-click context menu. Surface it where desktop would use a context menu.
- **Haptic feedback on significant actions.** Confirm, delete, toggle — subtle haptic response makes interactions feel real and complete.
- **Pinch to zoom on images and maps.** Never block default touch behaviour unless you are replacing it with something unambiguously better.
- **Voice input on search fields.** The OS provides it. Enable it with the correct input attributes. A microphone icon signals availability.

**Copy, paste, and URLs:**

- **Copy on click for codes and IDs.** Invite codes, API keys, tracking numbers, wallet addresses — one click copies, brief inline confirmation appears. No copy button, no instructions.
- **Paste and go for URL fields.** Detect paste into a URL input and trigger the action immediately without requiring the user to press Enter or a button.

**Network and performance:**

- **Smart retry on failure.** Network error — show a retry button inline, exactly where the failure occurred. Not a full page reload, not a toast with no action.
- **Graceful degradation on slow connections.** Show cached or stale data with a quiet "might be outdated" indicator rather than a blank screen or spinner.
- **Lazy load images with blur-up.** Low-resolution placeholder that sharpens as the full image loads. Never a blank rectangle.

**Navigation and long pages:**

- **Anchor links on long pages.** A sticky table of contents or jump links for any page where the user might need to navigate sections rather than scroll the full length.
- **Hover preview on links.** Tooltip showing destination or a content preview before the user commits to clicking.

**Search:**

- **Recent searches in search dropdown.** Surface the user's last few searches on focus. They retype the same queries constantly — save them the effort.
- **Grouped search results.** Split results by category (users, documents, actions, pages). Faster to scan than a flat list.
- **Keyboard shortcut hints in tooltips.** Show `⌘K` next to "Search", `⌘S` next to "Save". Teaches shortcuts passively without documentation.

**Feedback and state:**

- **Undo toast instead of confirm dialog.** "Deleted. Undo?" for 5 seconds is always better than "Are you sure?" before the action. Faster, less anxious, fully recoverable.
- **Focusable empty states with a CTA.** The primary action on an empty state is pre-focused and ready. Empty states are not dead ends.
- **Time-relative timestamps.** "2 hours ago" not "Apr 14 2026 09:32". Switch to absolute date on hover for precision when needed.

**Input polish:**

- **Truncate filenames in the middle.** `myverylongfi...ument.pdf` not `myverylongfilename...`. The extension and start are both meaningful.
- **Auto-resize textarea.** Grows with content as the user types. Fixed-height textareas with internal scroll are never acceptable.
- **Number inputs with +/− buttons on mobile.** Tap-editing a small number field is error-prone. Increment/decrement buttons solve it.

For every interaction in a flow, ask: what happens if this step does not exist? If the outcome is unchanged — the step should not exist.

## Modals, sheets, and drawers vs navigation (all modes)

**Use a modal, sheet, or drawer when:**
- The task is short and self-contained (quick edit, confirm, filter, share).
- The user needs context from the page behind it — the overlay preserves that context.
- Breaking navigation flow would feel disruptive (inline action, form with 2–4 fields).
- No sub-navigation, no nested state, no deep-linking needed.

**Use a new page / full navigation when:**
- The task is complex or multi-step — multiple sections, its own form flow.
- The user will spend real time there; the overlay would feel cramped.
- The destination has its own sub-navigation or meaningful internal state.
- The URL must be deep-linkable or shareable.
- It's a primary entity view (user profile, order detail, settings page).

**Rules that apply in both cases:**
- Sheets and drawers on mobile, modals on desktop — full-screen overlays on small viewports feel like navigation anyway, so treat them as such.
- Modals must be dismissible via Escape, backdrop click, and an explicit close control. No exceptions.
- Never stack modals. If a modal action needs confirmation, use an inline warning within the same modal, not a second modal on top.
- Drawers slide in from the side (filters, secondary panels). Sheets slide up from the bottom (mobile actions, quick forms). Modals are centered and block interaction.

## Visual polish (all modes, always)

**Gradients**
- Avoid full-section gradient backgrounds with multiple saturated colors. They read as AI-generated and undermine visual credibility.
- Gradients are allowed when subtle: single-hue shifts, very low saturation transitions, or dark-to-transparent overlays on images.
- Acceptable uses: a faint noise-textured gradient on a hero, a monochromatic depth effect, a transparent-to-color fade on a photo overlay.
- If in doubt, use a flat color. A well-chosen flat background with strong typography will always look more intentional than a colorful gradient.

**Typography**
- Do not default to Inter without thought. It is the most overused font in software UI — it signals zero typographic decision-making. Pick a font that fits the brand. Inter is acceptable only when it genuinely fits, not as a fallback.
- Do not apply gradient text to headings. It was a trend, it is now a cliché, and it immediately reads as AI-generated output. Use it at most once, on one word, when the brand explicitly calls for it.
- Do not use all-caps small labels as section headings or eyebrow text (e.g. "OUR FEATURES", "WHY US", "TRUSTED BY"). This pattern is AI-generated output made visible. Use normal-weight, normal-case text with size and spacing to create hierarchy instead.

**Color**
- Do not default to purple as a brand or accent color. It is the AI/tech industry default and carries no meaning anymore. If the brand has no defined color, ask or choose something intentional. Any color chosen deliberately beats the purple default.
- Be sparing with color across the entire UI. The default state of any surface — card, section, panel — is the design system background. Color is not decoration; it communicates something specific: a status, a brand moment, a destructive or affirmative action.
- Never assign each card or feature block its own background color. A row of cards each with a different tinted background is one of the clearest AI-generated UI tells. Cards in a set share a background. Differentiation comes from content, hierarchy, and spacing — not color.
- The only surfaces that earn a non-neutral background are: a hero or CTA section making a deliberate brand statement, a status banner (error, warning, success), or a highlighted/selected state. Everything else is neutral.

**Images and photography (marketing)**
- Marketing pages should include real imagery. A page without photos feels unfinished and generic.
- Use free stock photography from Unsplash or Pexels when real product images are unavailable. Only include images that fit the tone and subject — don't force it.
- When implementing without final assets, use a clearly-marked placeholder (`https://images.unsplash.com/...` or a sized placeholder block) rather than leaving the section empty. A placeholder communicates intent; an empty section does not.

## Motion and interaction (all modes, always)

**Animation**
- Every animation should be noticeable but only just — the threshold is "felt, not watched." If you can describe what the animation did, it's probably too much.
- Use animation on entry, exit, and state transitions (morphing, layout shifts, appearing/disappearing elements). These are the moments that make an interface feel alive.
- Never animate for decoration. Animate to communicate: something appeared, something changed, something completed.
- Duration: fast (100–200ms for micro-interactions, 200–350ms for transitions). Nothing should feel sluggish. Ease-out for entries, ease-in for exits, ease-in-out for morphs.
- Reduce or eliminate animation for users who have `prefers-reduced-motion` set.

**Interactivity**
- Every interactive element must respond on interaction — no exceptions. Buttons depress, links underline or shift, cards lift or highlight, inputs focus visibly.
- Hover, active, and focus states are all required. A component without all three is unfinished.
- Response must be immediate (no perceptible delay before the visual change). If an action takes time, the element changes state instantly and the async result resolves later.

## Platform integration (all modes, always)

Every UI should feel native to the platform it runs on. Use what the platform already provides — don't rebuild it.

**Web**
- **Click-to-copy** on any value the user might want: IDs, codes, URLs, addresses, keys. One click, silent confirmation (brief "Copied" tooltip, no modal).
- **Native share** via the Web Share API where supported. Fall back to copy-link only.
- **Native inputs where they exist:** `<input type="date">`, `<input type="file">`, color pickers, `<select>` on mobile. Override with custom UI only when the native control is genuinely insufficient.
- **Drag-and-drop** for file upload, list reordering, and kanban-style interactions where the mental model fits.
- **Browser autofill.** Never break it. Correct `autocomplete` attributes on every form field.
- **Deep-linkable URLs.** Every meaningful state (open modal, active tab, applied filter, selected record) should be shareable as a URL.
- **Keyboard shortcuts** for frequent actions. Follow platform conventions (Cmd/Ctrl+S, Cmd/Ctrl+K for search/command palette).

**Mobile / native (Expo + NativeWind)**
- **Share sheet** via `expo-sharing` or `Share.share()` wherever content is shareable.
- **Haptic feedback** on significant interactions: confirmations, errors, destructive actions.
- **Native pickers and modals** over custom-built equivalents: `DateTimePicker`, `ActionSheet`, bottom sheets.
- **System fonts and dynamic type.** Respect the user's font size setting.
- **Deep links and universal links.** Navigation state must be URL-addressable.
- **Biometric auth** where available and appropriate (`expo-local-authentication`).

**Principle:** if the platform offers it for free, use it. Custom implementations of native behaviors add maintenance cost and always feel slightly wrong.

## Domain rules (opinionated defaults)

### Marketing

**Hero and above the fold**
- **Hero does one job.** Single headline, single CTA. No split attention, no secondary actions competing in the first viewport.
- **Lead with the outcome, not the feature.** "Save 10 hours a week" over "Automated scheduling system." The user buys the result.
- **Specificity over vague claims.** "Used by 12,400 teams" beats "Trusted by thousands." Concrete numbers are credible; generic claims are ignored.
- **Social proof above the fold.** Logos, stats, or a sharp quote — establish credibility before the user has a reason to leave.
- **Visual consistency with the product.** The page should feel like a preview of what they're buying, not a separate brand experience.

**Conversion and CTAs**
- **One primary CTA per section.** Multiple competing CTAs create paralysis. Decide the winner and commit to it.
- **Answer objections inline.** If users wonder "is this safe?" or "can I cancel?", answer it at the point of friction — adjacent to the CTA, not buried in the footer.
- **Reduce form fields to the minimum.** Every extra field reduces conversion. Ask only for what is immediately necessary.
- **Exit-intent or scroll-triggered CTA.** One final prompt before the user leaves — not spammy if it's non-intrusive and relevant.

**Performance**
- **Optimize for fast load.** Every 100ms of delay has a measurable conversion cost. Compress images, lazy-load below the fold, no render-blocking resources above it.
- **Mobile-first layout.** Most traffic is mobile. Design and test on the smallest target screen first, then scale up.

**Pricing pages**
- **Three tiers maximum.** Highlight the recommended tier visually. Make the difference between tiers immediately obvious — no hunting through feature lists.
- **Scannable comparison.** Users compare on price and two or three key differentiators. Surface those; hide the rest behind a details toggle.

**Footer and objection handling**
- **FAQ near the bottom.** Catches users who scrolled but didn't convert. Kills last objections before they close the tab.
- Footer: legal, product links, contact — nothing more.

### Application (dashboard / SaaS)

**Density and layout**
- **Tight, purposeful UIs.** Buttons sized to their label, not oversized. Spacing follows a 4px/8px grid — enough breathing room to read, not so much it feels empty. Packed with action, yet clear.
- **Shell consistency:** navigation, page title, and primary action in the same position on every screen.
- **Visual hierarchy:** most important information largest and boldest. Users scan — structure for scanning, not reading.
- **Group related things spatially.** Proximity signals relationship. If two things belong together, they live near each other.
- Prefer patterns from `ui-blocks/application/` before inventing layout.

**Interaction and feedback**
- **Feedback on every action.** Button press, form submit, data save — always confirm something happened.
- **Skeleton screens over spinners.** Perceived load time drops; layout stays stable.
- **Actionable errors.** Never "Something went wrong." Say what failed and what the user should do next.
- **Let users undo.** Reduces fear of interacting. Required for all destructive actions.
- **Keyboard navigation and shortcuts.** Power users depend on it; it signals quality to everyone.

**Defaults and disclosure**
- **Surface the right defaults.** Most users never touch settings — the default should be correct for 80% of them.
- **Progressive disclosure.** Show only what the current task needs. Advanced options go behind expansion, modals, or secondary screens.
- **Useful empty states.** Never a blank screen. Explain what belongs there and how to add it.

**Color and status**
- **Color signals status, not decoration.** Red = error/destructive, green = success/safe. Use sparingly elsewhere.
- Never rely on color alone — pair with icon, label, or pattern for accessibility.

**Forms**
- Labels always visible (no placeholder-only). Errors inline, adjacent to the field. Loading and disabled states on every interactive element.

### Ecommerce

**Product detail page (PDP)**
- **Multiple product images are mandatory.** Multiple angles, zoom capability, at least one lifestyle shot. Images carry the sale — never use a single static photo.
- **Price and Add-to-Cart always visible.** Sticky or above the fold at all times. Never make the user scroll to find the buy action.
- **Show real stock levels.** "Only 3 left" is honest urgency — use it. Don't fabricate scarcity.
- **Shipping cost on the PDP.** Surprise fees at checkout are the primary cause of cart abandonment. Surface shipping cost before the user commits.
- **Trust signals adjacent to the buy button.** Secure payment badge, return policy, warranty — right there, not in the footer.
- **Reviews on the page, not buried.** Real reviews with photos where possible. Star rating visible near the price.
- **Clear return policy linked near the CTA.** Reduces purchase anxiety at the exact moment it matters.

**Cart and checkout**
- **Guest checkout is required.** Forcing account creation before purchase kills conversions. Let the user buy first, offer account creation after.
- **Progress indicator throughout checkout.** Users must always know how many steps remain.
- **Save cart across sessions.** Users research on mobile and buy on desktop. Cross-session cart persistence is not optional.
- **Mobile checkout is a distinct design problem.** Large tap targets, autofill support on all address and payment fields, Apple Pay / Google Pay as primary payment options on mobile.

**Discovery and browsing**
- **Search must be smart.** Typo tolerance, synonym matching, filterable results. Poor search is a direct revenue loss.
- **Recently viewed and related products.** Keeps users browsing rather than bouncing. Place below the fold on PDP and in the cart.

**Post-purchase**
- **Order confirmation does three things in order:** reassure (order received, details correct), set expectations (delivery estimate, tracking), upsell once (one relevant recommendation — no more).

**Empty and error states**
- Empty search results, empty cart, and out-of-stock states all need a useful next action — never a dead end.

### Components / primitives

- Use `ui-blocks/components/` for low-level pieces; align with Tailwind + React patterns already in the block.

## Process

1. **Select mode** — identify Marketing, Application, Ecommerce, or Mobile/App (or hybrid). For Mobile/App, also identify the category. State both explicitly.
2. Pull 1–3 reference blocks; list deltas for brand and data.
3. Implement with full responsive coverage (superwide to small phone).
4. Run **ferdig-ferdig** or **browse** for critical flows.
