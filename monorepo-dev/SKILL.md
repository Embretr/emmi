---
name: emmi-monorepo-dev
description: >-
  Emmi Turborepo monorepo: pnpm workspaces, Next.js + Expo, shared tRPC routers and Prisma only.
  Start monorepo immediately when both web and mobile are known from the start.
---

# Monorepo dev

## When to use

Start a monorepo **immediately** when you know the project will have both a web app and a mobile app. Do not start single-repo and migrate later — that migration is painful. If both are planned from day one, set up the monorepo on day one.

---

## Stack

| Tool | Role |
|------|------|
| Turborepo | Task pipeline, local caching |
| pnpm workspaces | Package manager and workspace linking |
| `apps/web` | Next.js (see web-dev skill) |
| `apps/mobile` | Expo (see mobile-dev skill) |
| `packages/api` | tRPC router definitions only |
| `packages/db` | Prisma schema and client |
| `packages/config` | Shared tsconfig, eslint config |

---

## Package layout

```
apps/
  web/               # Next.js app — owns its own tRPC server setup, Next config, env
  mobile/            # Expo app — owns its own app.json, babel, metro config

packages/
  api/               # tRPC router definitions only — no server setup, no context
  db/                # Prisma schema, client singleton, generated types
  config/            # Shared tsconfig base, eslint config
    tsconfig/
      base.json
      nextjs.json
      expo.json
    eslint/
      base.js
      nextjs.js
      expo.js

pnpm-workspace.yaml
turbo.json
package.json        # root — dev dependencies, turbo, scripts only
```

---

## What is shared and what is not

**Shared (`packages/`):**
- tRPC router definitions and Zod input schemas (`packages/api`)
- Prisma client and generated types (`packages/db`)
- TypeScript and ESLint config (`packages/config`)

**Not shared:**
- UI components — web and mobile cannot share components. Web uses React DOM, mobile uses React Native. Keep UI entirely separate in each app.
- Auth setup — Better Auth is configured per app. The same backend is called, but the client setup differs.
- Environment variables — each app has its own `.env`. No leakage between apps.

---

## `packages/api` — routers only

`packages/api` contains tRPC router definitions and Zod schemas. Nothing else.

```
packages/api/
  src/
    routers/
      posts.ts
      users.ts
    root.ts       # mergeRouters — the AppRouter type lives here
    index.ts      # exports AppRouter type and individual routers
  package.json
  tsconfig.json
```

The tRPC server setup (context, middleware, `createTRPCRouter`) lives in each app:
- `apps/web/src/server/api/trpc.ts`
- `apps/mobile/src/lib/api/trpc.ts`

This way `packages/api` has no dependency on Next.js or Expo — it is framework-agnostic.

---

## `packages/db` — Prisma only

```
packages/db/
  prisma/
    schema.prisma
  src/
    index.ts      # exports db (Prisma client singleton)
  package.json
  tsconfig.json
```

Both apps import `db` from `@repo/db`. The Prisma client is instantiated once in the package and shared.

`prisma db push` is run from the `packages/db` directory or via a root script:

```bash
pnpm --filter @repo/db db:push
```

---

## `pnpm-workspace.yaml`

```yaml
packages:
  - 'apps/*'
  - 'packages/*'
```

---

## `turbo.json`

T3 default pipeline with local caching only. No remote cache.

```json
{
  "$schema": "https://turbo.build/schema.json",
  "globalDependencies": ["**/.env.*local"],
  "pipeline": {
    "build": {
      "dependsOn": ["^build"],
      "outputs": [".next/**", "!.next/cache/**", "dist/**"]
    },
    "lint": {
      "outputs": []
    },
    "typecheck": {
      "dependsOn": ["^build"],
      "outputs": []
    },
    "test": {
      "dependsOn": ["^build"],
      "outputs": []
    },
    "dev": {
      "cache": false,
      "persistent": true
    },
    "db:push": {
      "cache": false
    }
  }
}
```

`^build` means a task depends on the `build` of all its dependencies first — `packages/db` and `packages/api` build before `apps/web` or `apps/mobile`.

---

## Root `package.json` scripts

```json
{
  "scripts": {
    "dev": "turbo dev",
    "dev:web": "turbo dev --filter=web",
    "dev:mobile": "turbo dev --filter=mobile",
    "build": "turbo build",
    "lint": "turbo lint",
    "typecheck": "turbo typecheck",
    "test": "turbo test",
    "db:push": "pnpm --filter @repo/db db:push",
    "db:studio": "pnpm --filter @repo/db studio"
  }
}
```

---

## Version alignment

Keep these dependencies on the same version across all packages:

- `react` and `react-dom`
- `typescript`
- `zod`
- `@trpc/server` and `@trpc/client`

Use pnpm's `overrides` in the root `package.json` to enforce a single version when needed:

```json
{
  "pnpm": {
    "overrides": {
      "zod": "^3.23.0"
    }
  }
}
```

---

## CI (GitHub Actions)

```yaml
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

      - uses: pnpm/action-setup@v4
        with:
          version: latest

      - uses: actions/setup-node@v4
        with:
          node-version: 20
          cache: 'pnpm'

      - name: Install dependencies
        run: pnpm install --frozen-lockfile

      - name: Typecheck
        run: pnpm typecheck

      - name: Lint
        run: pnpm lint

      - name: Test
        run: pnpm test

      - name: Build
        run: pnpm build --filter=web  # mobile builds locally, not in CI
```

Mobile builds are done locally and distributed via TestFlight — not in CI.

---

## New monorepo checklist

```
[ ] pnpm-workspace.yaml created
[ ] packages/config — base tsconfig and eslint
[ ] packages/db — Prisma schema, client, db:push script
[ ] packages/api — tRPC router definitions, AppRouter type exported
[ ] apps/web — Next.js, imports @repo/api and @repo/db
[ ] apps/mobile — Expo, imports @repo/api types
[ ] turbo.json pipeline configured
[ ] Root package.json scripts wired up
[ ] pnpm overrides set for shared critical deps
[ ] CI pipeline running on main
[ ] Railway deployed for apps/web
```
