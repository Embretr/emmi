---
name: emmi-test
description: >-
  Emmi testing strategy: regression-proof over coverage metrics. Vitest for unit and integration,
  Playwright for E2E. Tests gate the Railway build. No React component tests. Write the failing test
  before fixing production bugs.
---

# Test

## Philosophy

The goal of tests is not coverage — it is making the application regression-proof. A test exists to catch a future breakage before it reaches production. If a test would not catch anything that could realistically break, it should not exist.

**Write tests when:**
- The logic is complex enough that a future change could silently break it.
- A production bug has been found — write the failing test first, then fix.
- A tRPC procedure has non-trivial logic, auth checks, or side effects.
- A utility function has edge cases that are easy to get wrong.

**Do not write tests for:**
- React components — no component unit tests.
- Simple CRUD procedures with no logic beyond DB read/write.
- Things that TypeScript already guarantees at compile time.
- Implementation details that will change.

---

## Stack

| Layer | Tool | When |
|-------|------|------|
| Unit / integration | Vitest | Complex logic, tRPC procedures, utilities |
| E2E | Playwright | Critical user flows end-to-end |
| Error monitoring | PostHog | Production regressions that tests didn't catch |

---

## Unit and integration tests (Vitest)

### What to test

- **Pure logic functions** with multiple code paths or edge cases.
- **tRPC procedures** — call through the full HTTP stack, not the procedure function directly. Test the real request/response cycle including auth middleware and input validation.
- **Utilities and validators** — any shared Zod schema or helper that is used in multiple places.
- **Auth-gated procedures** — verify that unauthenticated and unauthorised calls are rejected with the correct `TRPCError` code.

### DB in tests

Use a mock DB or in-memory DB. Never test against the real development or production database.

Options in order of preference:
1. **Vitest mocks** for the Prisma client — mock `db` at the module level, return shaped fixtures.
2. **In-memory SQLite** via Prisma's `datasource` override — fast, real Prisma behaviour, no external dependency.

```ts
// vitest.setup.ts — mock Prisma client
vi.mock('~/server/db', () => ({
  db: {
    user: {
      findUnique: vi.fn(),
      create: vi.fn(),
      // add methods as needed per test file
    },
  },
}))
```

### Test structure

```
src/
  server/
    api/
      routers/
        posts.ts
        posts.test.ts   // co-located with the router
  lib/
    utils.ts
    utils.test.ts
```

Co-locate test files with the code they test. No separate `__tests__` directory.

### Vitest config

```ts
// vitest.config.ts
import { defineConfig } from 'vitest/config'
import tsconfigPaths from 'vite-tsconfig-paths'

export default defineConfig({
  plugins: [tsconfigPaths()],
  test: {
    environment: 'node',
    setupFiles: ['./vitest.setup.ts'],
    coverage: {
      provider: 'v8',
      reporter: ['text', 'json-summary'],
    },
  },
})
```

---

## E2E tests (Playwright)

### What to test

Critical user flows only — the paths that, if broken, make the product unusable:

- Sign up and sign in.
- The primary happy path for each core feature.
- Any flow involving payment, destructive actions, or data that is hard to recover.

Do not write Playwright tests for edge cases or error states — those belong in Vitest procedure tests.

### Setup

```ts
// playwright.config.ts
import { defineConfig, devices } from '@playwright/test'

export default defineConfig({
  testDir: './e2e',
  fullyParallel: true,
  forbidOnly: !!process.env.CI,
  retries: process.env.CI ? 1 : 0,
  reporter: process.env.CI ? 'github' : 'list',
  use: {
    baseURL: process.env.PLAYWRIGHT_BASE_URL ?? 'http://localhost:3000',
    trace: 'on-first-retry',
  },
  projects: [
    { name: 'chromium', use: { ...devices['Desktop Chrome'] } },
    { name: 'mobile', use: { ...devices['Pixel 7'] } },
  ],
})
```

### E2E file structure

```
e2e/
  auth.spec.ts
  [feature].spec.ts
```

---

## CI/CD

### GitHub Actions — runs on every push to `main`

```yaml
# .github/workflows/ci.yml
name: CI

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  ci:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: oven-sh/setup-bun@v2

      - name: Install dependencies
        run: bun install --frozen-lockfile

      - name: Typecheck
        run: bun run typecheck

      - name: Lint
        run: bun run lint

      - name: Unit and integration tests
        run: bun run test

      - name: Build
        run: bun run build
```

Tests run on every PR and every push to main. A failing test blocks merge.

### Railway build gate

Tests also run as part of the Railway build process. If tests fail, the build fails and the deploy does not happen.

Add to Railway's build command:

```bash
bun run test && bun run build
```

This means broken tests block both CI and deploy. There is no path to production with a failing test.

### No preview environments by default

Start with staging + production only. Add preview environments per project if needed — not a default.

---

## Production bug workflow

When a bug is found in production:

1. **Reproduce it** — understand the exact input or sequence that triggers it.
2. **Write a failing test** — a Vitest test for procedure bugs, a Playwright spec for flow bugs. The test must fail before the fix.
3. **Fix the bug** — the test should now pass.
4. **Commit both together** — the test and the fix in the same commit or PR.

This ensures the bug can never silently reappear without a test catching it.

PostHog error tracking surfaces production issues. When PostHog flags an error, treat it as a bug and follow this workflow.

---

## `package.json` scripts

```json
{
  "scripts": {
    "test": "vitest run",
    "test:watch": "vitest",
    "test:coverage": "vitest run --coverage",
    "test:e2e": "playwright test",
    "test:e2e:ui": "playwright test --ui",
    "typecheck": "tsc --noEmit",
    "lint": "eslint . --ext .ts,.tsx"
  }
}
```

`test` runs Vitest in CI mode (single run, no watch). `test:watch` for local development.
