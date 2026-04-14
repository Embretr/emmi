---
name: emmi-analytics
description: >-
  Emmi analytics: PostHog-first product analytics, feature flags, session replay, error tracking, and experiment hygiene.
  Use for instrumentation plans, funnel definitions, dashboards, or cleaning up events and flags.
---

# Analytics

## PostHog (primary)

- **Product events:** name conventions, properties, user vs group keys.  
- **Feature flags:** naming, rollout rules, stale flag review.  
- **Funnels and retention:** define steps with engineering alignment.  
- **Session replay:** sampling, privacy masking (PII).  
- **Errors:** source maps, release tracking, ownership.

## Other tools

When the stack includes GA4, Plausible, or custom warehouses: map the **same conceptual model** (who, what, when, experiment variant) and avoid duplicate conflicting definitions.

## Governance

- Document events in-repo (`docs/analytics.md` or similar).  
- **Do not** log secrets or raw PII in event properties.

Cross-check **evaluators/** for metric quality bars the org cares about.
