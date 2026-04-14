---
name: emmi-ferdig-ferdig
description: >-
  Emmi production-readiness QA: thorough feature testing, adversarial and unpredictable usage, technical weak-spot review,
  and usability hardening ("idiot proof"). Web: Playwright. Mobile: Maestro. Use before ship, after big changes,
  or when "try to break it".
---

# Ferdig ferdig (ship-quality QA)

## Scope

Whole app, a feature slice, or a PR surface. State which.

## Web (Playwright)

- **Happy paths** for every acceptance criterion.  
- **Adversarial:** double clicks, rapid navigation, back button, refresh mid-flow, invalid input, huge payloads, slow network simulation where possible.  
- **Auth:** logged out, expired session, wrong role.  
- **Accessibility smoke:** focus order, keyboard on primary flows, critical ARIA.  
- **Visual:** key pages at mobile and desktop widths.

## Mobile (Maestro)

- Same intent as web: flows, interruptions, permissions denied, offline if relevant, deep links.

## Technical review

- Error boundaries, loading states, race conditions, optimistic UI rollback.  
- API failure handling and user-visible messages.  
- Security basics on the touched surface: XSS sinks, IDOR patterns, sensitive data in logs.

## Usability

- **Idiot-proofing:** fewest decisions, clear labels, undo where cheap, confirmations only for destructive actions.  
- Copy: no jargon without definition; errors say what to do next.

## Output

Structured report: **PASS / ISSUES** with repro steps, severity, file hints. Fix or file tickets before calling production-ready.
