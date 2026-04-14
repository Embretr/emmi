---
name: emmi-web-dev
description: >-
  Emmi web stack: Next.js App Router, tRPC, Prisma, Better Auth, Tailwind, TanStack Query, Zod, React Hook Form.
  Opinionated conventions for structure, data fetching, auth, forms, errors, and env.
---

# Web dev

## Stack overview

The stack is T3-derived with Better Auth replacing NextAuth and Prisma as the ORM.

| Layer | Technology | Role |
|-------|-----------|------|
| Framework | Next.js (App Router) | Routing, RSCs, middleware |
| API | tRPC | Type-safe procedures, all server communication |
| ORM | Prisma | Schema, DB access, `db push` workflow |
| Auth | Better Auth | Sessions, providers, roles |
| Validation | Zod | Input schemas on tRPC procedures and forms |
| Forms | React Hook Form + Zod | Form state, validation, error surfaces |
| Data fetching | TanStack Query (via tRPC) | Client-side queries, mutations, optimistic updates |
| Styling | Tailwind CSS + shadcn/ui | See ui-ux skill |
| Env | `@t3-oss/env-nextjs` | Validated, typed env vars |

---

## How each technology fits together

### Next.js App Router

Every route is a React Server Component by default. RSCs run on the server — they can read the DB, access env vars, and call Better Auth directly without going through tRPC. `"use client"` is added only when a component needs interactivity, browser APIs, or TanStack Query hooks.

The App Router handles routing via the filesystem under `app/`. Layouts wrap routes and stay mounted across navigations. Middleware runs before any route and is where auth protection lives.

### tRPC

tRPC creates a fully type-safe API layer between client and server. Procedures are defined with a Zod input schema and a resolver. The TypeScript types flow automatically to the client — no code generation, no REST contracts.

The client uses TanStack Query under the hood. `trpc.feature.action.useQuery()` is a TanStack Query query. `trpc.feature.action.useMutation()` is a TanStack Query mutation. All TanStack Query capabilities (optimistic updates, cache invalidation, `useUtils`) are available.

Server-side, tRPC procedures can be called directly without HTTP using the server-side caller. Use this in RSCs when you need procedure logic but are already on the server.

### Prisma

Prisma defines the DB schema in `schema.prisma`. Types are generated from the schema and used throughout the codebase. `prisma db push` syncs the schema to the DB without a migration history — this is the preferred workflow.

The Prisma client is a singleton instantiated in `lib/db.ts` and imported directly wherever needed.

### Better Auth

Better Auth handles session creation, validation, and providers. On the server, access the session directly via Better Auth's server helpers — no need to go through tRPC for session reads in RSCs or middleware. On the client or inside tRPC procedures, use the provided hooks and context.

Email/password is the default provider. Additional providers (OAuth, magic link, etc.) are added on demand per project.

### Zod

Zod is the single validation layer. Every tRPC procedure input is a Zod schema. Every form is validated with a Zod schema via React Hook Form's `zodResolver`. Never write manual validation — Zod handles it.

### React Hook Form

All forms use React Hook Form with `zodResolver`. The form schema is a Zod object. Errors from validation surface inline at the field level. Errors from tRPC mutations surface as both a toast (global feedback) and inline on the relevant field where possible.

### TanStack Query

TanStack Query manages all client-side server state — loading, error, stale, refetch. Access it through the tRPC client. Direct TanStack Query usage (outside tRPC) is for third-party APIs only.

### @t3-oss/env-nextjs

All env vars are defined and validated in `env.ts` at the project root. Server-only vars in `server`, public vars in `client`. Import `env` from there throughout the codebase — never `process.env` directly.

---

## Project structure

```
app/
  (auth)/             # auth routes group — sign in, sign up, etc.
  (app)/              # protected routes group
    dashboard/
    [feature]/
  api/
    trpc/[trpc]/      # tRPC HTTP handler
  layout.tsx
  middleware.ts       # auth protection lives here

components/           # top-level shared components
  ui/                 # shadcn primitives
  [feature]/          # feature-specific components

server/
  api/
    routers/          # one file per feature: posts.ts, users.ts, etc.
    root.ts           # merges all routers
    trpc.ts           # context, middleware, procedure helpers
  auth.ts             # Better Auth server instance
  db.ts               # Prisma client singleton

lib/
  utils.ts
  validators/         # shared Zod schemas reused across procedures and forms

env.ts                # @t3-oss/env-nextjs schema
prisma/
  schema.prisma
```

---

## Conventions

### App Router

- **Always App Router.** Never Pages Router.
- **Default to RSC.** Add `"use client"` only when the component needs interactivity, browser APIs, or TanStack Query hooks. If in doubt, keep it server.
- **Middleware handles auth protection.** Never check session in layouts or pages as the primary auth guard. Middleware runs first and redirects unauthenticated users before the route renders.
- **Route groups for auth vs app.** `(auth)/` for public auth routes, `(app)/` for protected routes. Keeps layouts separate and middleware matching clean.

### tRPC

- **All client-server communication goes through tRPC.** No Server Actions, no raw `fetch` to internal routes.
- **Feature-based routers.** One file per feature domain (`posts.ts`, `users.ts`, `billing.ts`). Merged in `root.ts`. Never one large router file.
- **Every procedure input is a Zod schema.** No unvalidated inputs, no `z.any()`.
- **Throw `TRPCError` with specific codes.** `NOT_FOUND`, `UNAUTHORIZED`, `FORBIDDEN`, `BAD_REQUEST`, `INTERNAL_SERVER_ERROR`. Never throw generic errors from procedures.
- **Server-side caller for RSCs.** When an RSC needs data that goes through procedure logic, use the server-side caller — not a client fetch.

### Optimistic updates

- **Default to optimistic UI on mutations.** Update the cache immediately via `useUtils`, roll back on error.
- **Exception: forms and submits where the user expects to wait.** Show a loading state on the button itself (spinner replaces label), disable the button, prevent double submit.
- **Progressive loading where possible.** Skeleton screens over spinners. Partial data over blank states.

### Prisma

- **camelCase everywhere.** Model names, field names, relation names — all camelCase. No `@@map`, no snake_case DB columns.
- **`prisma db push` is the workflow.** No migration files. Push schema changes directly.
- **Prisma client is a singleton in `server/db.ts`.** Never instantiate it elsewhere.
- **Timestamps on every model.** `createdAt DateTime @default(now())` and `updatedAt DateTime @updatedAt` on every model without exception.
- **Import the Prisma client as `db`.** `import { db } from "~/server/db"`.

### Better Auth

- **Email/password is the default.** Other providers added per project on demand — never pre-installed speculatively.
- **Session access in RSCs and middleware via Better Auth server helpers directly.** No need to go through tRPC for a session read.
- **tRPC procedures use Better Auth context for session.** The tRPC context includes the session; procedures access it via `ctx.session`.
- **Use Better Auth's built-in roles.** Do not build a custom roles/permissions system — use what Better Auth provides.
- **Protect procedures at the procedure level.** Authenticated procedures check `ctx.session` and throw `UNAUTHORIZED` if missing. Never rely only on middleware for procedure-level auth.

### Forms

- **React Hook Form + Zod for every form.** `useForm` with `zodResolver(schema)`.
- **Errors are both inline and toast.** Validation errors show inline at the field. Mutation errors (from tRPC) show as a toast AND inline on the relevant field where the mapping is clear.
- **Never clear a form on error.** If a mutation fails, the form stays filled. The user corrects and resubmits.
- **Disable submit while pending.** Loading state on the button itself during submission.

### Env

- **All env vars go through `env.ts`.** Validated with `@t3-oss/env-nextjs`. Never access `process.env` directly in application code.
- **Server-only vars in `server`, public vars in `client`.** Accessing a server var on the client throws at build time.

### Error handling

- **tRPC procedures throw typed `TRPCError`.** The client receives a typed error with a code and message.
- **User-facing messages are safe.** Never expose stack traces, query details, or internal identifiers in error messages.
- **Errors surface two ways:** toast for global feedback ("Failed to save"), inline for field-level feedback ("Email already in use").

---

## Feature build pattern

Follow this order for every new feature:

1. **Schema** — add or update the Prisma model, run `prisma db push`.
2. **Zod validators** — define input schemas in `lib/validators/[feature].ts`.
3. **tRPC router** — create `server/api/routers/[feature].ts`, add procedures, wire into `root.ts`.
4. **Server component** — fetch initial data via server-side caller, pass to client components as props.
5. **Client components** — TanStack Query for mutations and reactive updates, React Hook Form for forms.
6. **Error and loading states** — every query has a loading skeleton, every mutation has a button loading state and error handling.
7. **Optimistic updates** — add `useUtils` cache updates to mutations unless the user expects a wait.
