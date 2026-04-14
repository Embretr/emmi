---
name: emmi-analytics
description: >-
  Emmi analytics: PostHog-first. Product events, feature flags, session replay, error tracking, funnels.
  Instrument before launch, not after. Document events in the repo.
---

# Analytics

## Stack

PostHog is the single analytics platform. It covers product events, feature flags, session replay, error tracking, and A/B experiments. Do not add a second analytics tool unless PostHog demonstrably cannot cover the use case.

---

## Instrumentation timing

**Instrument before launch, not after.** Analytics added retroactively are missing data for the period that matters most — right after launch when you need to know if things are working.

For every feature, define and instrument the following before shipping:
1. The activation event — the action that means "the user got value."
2. The core action event — the repeatable thing the feature is built around.
3. Any error or failure states that matter.

---

## Event naming

Consistent naming makes events queryable without guessing. Follow this convention:

```
[noun]_[past_tense_verb]

Examples:
  project_created
  file_uploaded
  payment_completed
  onboarding_step_completed
  search_performed
  invite_sent
```

- Lowercase, underscores only.
- Past tense — the event happened.
- Noun first — groups related events together in the PostHog UI.

---

## Properties

Every event should include:
- `userId` — automatically captured by PostHog identify, not sent manually.
- `orgId` — for multi-tenant apps, always include organisation context.
- Relevant entity IDs (`projectId`, `fileId`, etc.).
- Relevant state at the time (`plan`, `role`, `featureFlag`).

Never include:
- PII beyond what PostHog already captures (name, email are in the person profile — not in event properties).
- Secrets, tokens, or internal system values.
- Raw user content (message bodies, file contents).

---

## Web instrumentation (Next.js)

```ts
// lib/analytics.ts
import posthog from 'posthog-js'

export function trackEvent(event: string, properties?: Record<string, unknown>) {
  posthog.capture(event, properties)
}

export function identifyUser(userId: string, traits?: Record<string, unknown>) {
  posthog.identify(userId, traits)
}

export function resetUser() {
  posthog.reset()
}
```

Initialise PostHog in the root layout. Identify the user immediately after sign-in. Reset on sign-out.

Session replay: enable with PII masking on all input fields containing sensitive data (`data-ph-mask` attribute or global input masking config).

---

## Mobile instrumentation (Expo)

Use `posthog-react-native`. Same event naming conventions. Identify on sign-in, reset on sign-out.

```ts
import { usePostHog } from 'posthog-react-native'

const posthog = usePostHog()
posthog.capture('project_created', { projectId, orgId })
```

---

## Feature flags

- **Name:** `snake_case`, descriptive of the feature. `new_dashboard`, `billing_v2`.
- **Never hardcode feature flag keys as strings in multiple places.** Define them once:

```ts
// lib/flags.ts
export const FLAGS = {
  newDashboard: 'new_dashboard',
  billingV2: 'billing_v2',
} as const
```

- **Review stale flags.** A flag that has been fully rolled out or permanently off for 30+ days should be removed. Clean up the flag and the conditional code together.
- **Flags are temporary.** They are a rollout mechanism, not a permanent configuration system.

---

## Error tracking

PostHog error tracking captures unhandled exceptions automatically when configured. Additionally:

- Wrap critical flows in try/catch and call `posthog.captureException(error)` with context.
- Include `userId` and `orgId` in error context so errors are attributable.
- Set up PostHog alerts for error rate spikes on key flows.

---

## Funnels and dashboards

Define funnels for every core user journey before launch:

- Sign up → Activation (complete core action for first time)
- Core action funnel (start → complete)
- Any paid conversion funnel

Create a PostHog dashboard per feature area. Share the dashboard link in the plan doc.

---

## Documentation

Every tracked event is documented in `docs/analytics.md`:

```markdown
# Analytics events

## [Feature name]

| Event | When | Key properties |
|-------|------|---------------|
| `project_created` | User creates a new project | `projectId`, `orgId`, `template` |
| `project_deleted` | User deletes a project | `projectId`, `orgId` |
```

Update this file in the same PR as the instrumentation code. Undocumented events become unqueryable noise within months.
