---
name: emmi-monorepo-dev
description: >-
  Emmi Turborepo monorepo: combine Next.js (web-dev) and Expo (mobile-dev) with shared packages, tRPC, Prisma, and CI.
  Use for repo layout, turbo pipelines, shared config, and cross-package changes.
---

# Monorepo dev

## Layout (typical)

- `apps/web` — Next.js  
- `apps/mobile` — Expo  
- `packages/api` — tRPC routers, shared server logic  
- `packages/db` — Prisma schema and client  
- `packages/ui` or `packages/config` — shared UI tokens, eslint/tsconfig

## Turborepo

- **`turbo.json`:** pipeline dependsOn, outputs for build, test, lint.  
- **Caching:** correct outputs so CI benefits.  
- **Env:** per-app `.env` documented; no leakage across apps in logs.

## Shared code rules

- **Types and validators** live once; import from `packages/*`.  
- **Side-effect free** shared modules for RN and Node where possible.  
- **Version locks** aligned across apps for critical deps (React, NativeWind, etc.).

## CI

- Matrix or staged jobs: lint → test → build web → build mobile (or EAS on schedule).

Coordinate with **deployment** for which app deploys where.
