---
name: emmi-web-dev
description: >-
  Emmi preferred web stack: Next.js, Better Auth, Prisma, Tailwind CSS, tRPC. Use for app setup, features, API design,
  auth flows, server/client boundaries, and conventions in that stack.
---

# Web dev

## Stack

- **Framework:** Next.js (App Router unless project already Pages).  
- **Auth:** Better Auth (sessions, providers, server-side checks).  
- **DB:** Prisma schema, migrations, typed queries.  
- **API:** tRPC routers, Zod input validation, shared types with client.  
- **UI:** Tailwind; compose from **ui-blocks** when building marketing or app shells.

## Conventions

- **Server vs client:** default server components; `"use client"` only when needed.  
- **Data:** fetch on server where possible; avoid waterfall client fetches for initial page.  
- **Errors:** user-safe messages; log server detail.  
- **Env:** `DATABASE_URL`, auth secrets, public vs server-only keys.

## Feature pattern

1. Prisma model + migration  
2. tRPC procedure + Zod  
3. Server component or thin client wrapper  
4. Tests at integration level for procedures when non-trivial

Cross-check **rules/** and **evaluators/** before merging patterns that affect many files.
