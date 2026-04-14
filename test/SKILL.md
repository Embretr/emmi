---
name: emmi-test
description: >-
  Emmi testing and CI/CD: strategy and implementation for unit, integration, system, UAT, regression, functional,
  performance, security, usability, and smoke tests. Use when adding tests, fixing flaky CI, or designing a test pyramid.
---

# Test

## Layers (know the terms)

| Layer | Role |
|-------|------|
| **Unit** | Smallest units in isolation (pure logic, single component). |
| **Integration** | Modules/services together (DB, API + handler, queue consumer). |
| **System** | Full app against real or near-real dependencies. |
| **UAT / acceptance** | Product-defined readiness; often scenario-based. |
| **Regression** | Guard existing behavior after changes (automate high-value suites). |
| **Functional** | Requirements mapped to behavior (UI, API, DB). |
| **Performance** | Latency, throughput, load, stress; budgets and profiling. |
| **Security** | Vulnerabilities and abuse cases (baseline scanning + targeted tests). |
| **Usability** | Task success, clarity (often mixed manual + instrumentation). |
| **Smoke** | Fast gate on main paths after build or deploy. |

## Opinionated defaults

- **Pyramid:** many unit, fewer integration, selective E2E.  
- **CI:** run unit + integration on every PR; smoke on deploy candidate; nightly heavier jobs if needed.  
- **Flakes:** fix or quarantine with owner; no silent retries without tracking.  
- **Coverage:** chase meaningful branches, not percentage vanity.

## CI/CD

- Pin tool versions; cache deps; fail fast on lint + typecheck + tests.  
- Separate **preview** and **production** deploys; migrations gated.  
- Artifacts: test reports, Playwright traces on failure.

## Deliverables

Test plan snippet (what runs where), added tests, CI config edits, and how to run locally.
