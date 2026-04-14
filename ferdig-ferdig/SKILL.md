---
name: emmi-ferdig-ferdig
description: >-
  Emmi production-readiness QA: thorough feature testing, adversarial and unpredictable usage, technical weak-spot review,
  and usability hardening ("idiot proof"). Web: Playwright. Mobile: Maestro. Use before ship, after big changes,
  or when "try to break it".
---

# Ferdig ferdig (production-ready QA)

Ferdig ferdig means done done. A feature is not production-ready until it passes all four evaluation gates below. Work through them in order — a failure at any gate is a blocker, not a note.

## Scope

Whole app, a feature slice, or a PR surface. State which before starting.

---

## The four gates

### Gate 1 — Is it intuitive?

A feature passes this gate if someone with zero prior domain knowledge can understand and use it correctly on the first attempt, with no training and no documentation.

Evaluate by asking: if a stranger opened this right now, would they know what it does, how to use it, and what will happen when they do?

Failure modes to look for:
- Unlabelled or ambiguously labelled controls.
- Actions that require knowing what happened before this screen.
- Flows with no indication of where the user is or what comes next.
- UI that requires reading a tooltip or help text to understand the primary action.

If it fails: redesign the interaction. Add inline descriptions, contextual helpers, progressive disclosure, or clearer labels. Do not ship unclear UI with a tooltip as the fix — the base UI must be self-evident.

### Gate 2 — Can it be broken?

If a user can put the feature into a broken, inconsistent, or unrecoverable state — they will. Every failure state must be handled and explained.

Test everything adversarial:
- Double-click, rapid repeated actions, clicking submit before data loads.
- Back button, refresh, browser close mid-flow.
- Invalid, empty, oversized, and malformed input on every field.
- Slow or failed network: API timeout, 500, 429, network offline.
- Auth edge cases: logged out mid-session, expired token, insufficient permissions, wrong role.
- Race conditions: two tabs, optimistic UI that fails to commit.
- Empty states, zero results, first-time use before any data exists.

A feature passes this gate when every broken path either prevents the action with a clear explanation, or recovers gracefully and tells the user what happened and what to do next. "Something went wrong" is a gate failure.

### Gate 2.5 — Is every action necessary?

**The preemptive principle:** always act on the user's behalf as early as possible. Do the thing, then give them a way to undo it — do not ask for permission first. A Back button costs nothing. A Next button costs a click, a read, a decision, and a moment of friction on every single use.

Every interaction the user performs must be absolutely required. If an action can be eliminated, inferred, automated, or defaulted — it must be. Unnecessary steps are not a minor annoyance; they are a design failure.

Audit every interaction in the flow against this list. Each pattern that applies and is missing is a gate failure:

- **Auto-advance after single selection.** User picks one option, move on. No Next button. Back button to undo.
- **Pre-fill everything the system already knows.** Logged-in user — you have their name, email, address. Don't ask again.
- **Inline editing.** Click the text to edit it. No separate edit mode or page for simple values.
- **Smart defaults on date pickers.** If context implies "today" or "next week", it should be pre-selected.
- **Auto-format as you type.** Phone numbers, card numbers, IBANs — formatted in real time, never instructed.
- **Dismiss on outside click.** Modals, dropdowns, popovers close on backdrop click. Close button is a fallback.
- **Auto-select all on focus.** If the user is likely replacing the value, select all on focus.
- **Skip steps that don't apply.** Irrelevant conditional steps are hidden entirely, not disabled.
- **Remember last used option.** Sort order, filter, view mode — restored on next visit.
- **Single-click confirm for low-stakes actions.** No "Are you sure?" on reversible actions. Use undo instead.
- **Search triggers on type.** No search button. Results update as the user types.
- **Tab order matches reading order.** Keyboard users never forced to the mouse.
- **Clipboard detection.** Recognisable copied values (URL, code, ID) offered as pre-fill.
- **Return key submits.** Last field in a form or single-field form — Enter submits.
- **Infinite scroll where pagination adds no value.** Next Page exists only when page position is meaningful.

Also check for these patterns where applicable — missing implementations are gate failures:

- **Sticky context.** Deep flows always show where the user is: breadcrumb, step indicator, or title.
- **Scroll position preserved on back.** Back navigation restores position, not top of page.
- **Optimistic UI.** Fast actions update instantly with silent rollback on failure.
- **Bulk actions appear on selection only.** Not visible until multiple items are selected.
- **Drag handles appear on hover only.** Not persistently visible on reorderable lists.
- **Filter state in URL.** Filters, sort, and view mode survive refresh and can be shared.
- **Destructive swipe requires directional intent.** Not triggered by incidental contact.
- **Command palette present.** `Cmd+K` or `/` in any application UI.
- **Contextual help inline.** `?` or tooltip adjacent to fields that need explanation.
- **Optional fields labelled, not required ones.** Asterisks mark exceptions, not the rule.
- **Shift+click multi-select.** Standard selection mechanics, not reinvented.
- **Show password toggle.** Present on all password inputs.
- **Autosave with quiet indicator.** "Saved Xs ago" — no modal, no toast.
- **Expandable rows for secondary detail.** Not a navigation event.
- **Changed element highlighted after save.** Brief highlight confirms the action worked.
- **Input masks guide as the user types.** Format never revealed as a post-submission error.
- **Table preferences persisted.** Column widths and order survive sessions.
- **Double-click to edit.** Table cells and inline values, no separate edit button.
- **Typeahead on dropdowns over 5 items.** No scrolling long lists.
- **Drag reorder shows live final position.** Preview during drag, not only after drop.

Tables:
- **Sticky headers** on all scrollable tables.
- **Sort arrows on hover only**, persisted on active column.
- **First column frozen** on horizontally scrollable tables.
- **Export matches filtered view**, not full dataset.
- **Pagination shows total context** ("Page 2 of 14", "20 of 340 results").
- **Jump-to-page input** on large paginated datasets.

Forms:
- **Inline validation on blur**, not on submit.
- **Form input preserved on error** — never cleared on failed submission.
- **Character count shown before limit**, not after exceeding it.
- **Disabled buttons have a tooltip** explaining why.
- **Loading state on the submit button itself**, not a page spinner.
- **Double submit prevented** — button disabled immediately on first click.
- **Tab between fields doesn't lose state.**
- **Section-level save** on long forms.
- **Unsaved changes warning** on navigation away.
- **Summary screen** before final submit on multi-step forms.
- **Smart paste** splits across multi-field inputs automatically.
- **OTP fields auto-advance** on digit entry.
- **Correct `inputmode`** set on all mobile inputs.
- **Address autocomplete** — no manual full-address typing.
- **Country pre-selected from IP.**
- **Currency and units match detected locale.**

Notifications:
- **Badge clears after viewing.**
- **Mark all as read** always present.
- **Notifications grouped** by type or source.

Settings:
- **Settings search** present if panel has more than 20 options.

Onboarding:
- **Teaches by doing**, not a modal tour.
- **Progress persists across sessions** — never resets to step 1.

Accessibility and keyboard:
- **Focus trapped in modals.** Tab never escapes to content behind an open modal.
- **Escape closes everything.** Modals, drawers, dropdowns, tooltips — no exceptions.
- **Back button closes overlay before navigating.** Browser back dismisses open overlays first.

Mobile:
- **Pull to refresh** on any screen with live data.
- **Swipe back not blocked.** Native gesture works as expected.
- **Long press exposes secondary actions** where desktop would use a context menu.
- **Haptic feedback** on confirm, delete, toggle.
- **Pinch to zoom not blocked** on images and maps.
- **Voice input enabled** on search fields.

Copy, paste, URLs:
- **Copy on click** for codes, keys, IDs — with inline confirmation.
- **Paste and go** on URL fields — action triggers on paste.

Network and performance:
- **Inline retry on failure** — not a full page reload.
- **Stale data shown with indicator** rather than blank screen on slow connection.
- **Blur-up lazy loading** on images — no blank rectangles.

Navigation:
- **Anchor links / jump nav** on long pages.
- **Hover previews** on links.

Search:
- **Recent searches** shown on focus.
- **Grouped results** by category.
- **Shortcut hints in tooltips** (`⌘K`, `⌘S`, etc.).

Feedback and state:
- **Undo toast** instead of confirm dialog for reversible deletions.
- **Empty state CTA is pre-focused.**
- **Timestamps are relative** ("2 hours ago"), absolute on hover.

Input polish:
- **Filenames truncated in the middle**, not the end.
- **Textarea auto-resizes** with content.
- **Number inputs have +/− buttons** on mobile.

For each interaction in the flow, ask: what happens if this step does not exist? If the answer is "nothing breaks and the user still reaches the outcome" — the step should not exist.

### Gate 3 — Is it worth using?

The feature must justify the time and energy it asks of the user. The value delivered must obviously exceed the friction required to deliver it.

Ask: would a real user, under realistic conditions, choose to use this? Or would they abandon it, work around it, or feel it wasn't worth the effort?

Evaluate:
- How many steps, decisions, and inputs does the happy path require?
- Is each step necessary, or is any of it waste?
- Does the outcome feel proportionate to the effort?
- Would reducing input (fewer fields, smarter defaults, better prefill) make it significantly better?
- Would increasing output (more useful result, better formatting, actionable next step) make it worth the friction?

If the answer is "I wouldn't bother using this the way it is" — redesign before shipping. Optimize for minimum input, maximum output.

### Gate 4 — Is it 100% clear what it does?

Every action must have a predictable, understandable outcome. No surprises, no side effects the user didn't anticipate.

Check:
- Does every button, link, and control communicate exactly what it will do before the user commits?
- Are destructive or irreversible actions guarded with a confirmation that describes the consequence?
- Are there any side effects (data changes, notifications sent, state updated elsewhere) that the user isn't told about?
- Does the post-action state make it obvious what just happened?

If a user could reasonably be surprised by the result of their action — the gate fails. Make consequences visible before the action, not after.

---

## Technical hardening

Run alongside the four gates, not instead of them.

- Error boundaries on every async surface. No unhandled promise rejections visible to the user.
- Loading, empty, error, and success states implemented for every data-dependent component.
- API failure paths: 400, 401, 403, 404, 429, 500 — each produces a user-visible, actionable message.
- Optimistic UI has a rollback path on failure.
- Security basics on the touched surface: XSS sinks, IDOR patterns, sensitive data in logs or URLs.
- Accessibility: focus order correct, keyboard navigable on primary flows, critical ARIA in place.

## Testing execution

**Web:** Playwright — happy paths, adversarial paths, auth edge cases, mobile and desktop viewports.

**Mobile:** Maestro — same flows adapted for native: interruptions (calls, notifications), permissions denied, offline mode, deep links, background/foreground transitions.

---

## Output

A structured report with a verdict for each gate:

```
Gate 1 — Intuitive:   PASS / FAIL
Gate 2 — Unbreakable: PASS / FAIL
Gate 3 — Worth using: PASS / FAIL
Gate 4 — Clear:       PASS / FAIL
Technical:            PASS / ISSUES

Overall: PRODUCTION READY / NOT READY
```

For every FAIL or ISSUE: repro steps, severity (blocker / major / minor), and file or component hint. Nothing ships until all four gates pass and all blockers are resolved.
