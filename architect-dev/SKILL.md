---
name: emmi-architect-dev
description: >-
  Emmi architecture: decisions within the established stack, ADRs, background jobs, multi-tenancy,
  real-time, file storage. Opinionated defaults for robust systems from the start.
---

# Architect dev

## Philosophy

Architecture decisions are made once and lived with for years. Make them deliberately, document them, and build for change. The goal is a system that is easy to reason about, easy to change, and hard to break silently.

- **Stay in the stack.** The default answer to any infrastructure question is "can the existing stack handle it?" Before adding a service, a queue, or a database, exhaust what Postgres, Railway, and Next.js can do.
- **Boring is good.** Choose the technology with the largest surface area of known failure modes over the one that is theoretically optimal but unfamiliar.
- **Build for the next order of magnitude, not ten.** Design for 10x current scale. Do not design for 1000x — that is premature and wrong.

---

## Architecture decision records (ADRs)

Every significant architectural decision gets an ADR. Significant means: a decision that is hard to reverse, affects multiple parts of the system, or where reasonable people would disagree.

Location: `docs/adr/`

```markdown
# ADR-001: [Decision title]

**Date:** [date]
**Status:** Accepted / Superseded by ADR-XXX

## Context
[What is the situation, what problem are we solving?]

## Decision
[What we decided to do.]

## Alternatives considered
[What else was considered and why it was rejected.]

## Consequences
[What becomes easier, what becomes harder, what risks are accepted.]
```

---

## System boundaries

Always produce a context diagram before implementation. Minimal version:

```
[User] → [Next.js app] → [tRPC API layer] → [Prisma] → [Postgres]
                       → [Better Auth]
                       → [File storage (R2)]
                       → [Worker service] → [Postgres]
```

Document: every user-facing entry point, every data store, every external service, every async boundary.

---

## Background processing

**Default: Railway cron service or worker service.**

- Simple scheduled jobs (nightly reports, cleanup): Railway cron service with a dedicated script.
- Queue-based work (email, webhooks, processing pipelines): a separate `apps/worker` service on Railway consuming a Postgres-backed queue (use `pg-boss` — it uses Postgres directly, no Redis required for basic queuing).

```
Railway services:
  web     → Next.js
  worker  → Node.js process consuming pg-boss queue
  db      → Postgres (shared)
```

`pg-boss` is the default queue. It stores jobs in Postgres — no extra infrastructure. Add Redis-backed queues only when throughput exceeds what Postgres can handle (rarely needed).

---

## Multi-tenancy

Default pattern: **row-level tenancy with `orgId`**.

Every resource that belongs to an organisation has an `orgId` field. Every query that reads or writes tenant data includes `orgId` in the `where` clause. Procedures enforce this through the tRPC context — the session includes the active `orgId` and it is applied automatically.

```prisma
model Project {
  id        String   @id @default(cuid())
  orgId     String
  org       Org      @relation(fields: [orgId], references: [id])
  createdAt DateTime @default(now())
  updatedAt DateTime @updatedAt
}
```

```ts
// tRPC context — orgId is always injected
const orgProcedure = protectedProcedure.use(({ ctx, next }) => {
  if (!ctx.session.orgId) throw new TRPCError({ code: 'FORBIDDEN' })
  return next({ ctx: { ...ctx, orgId: ctx.session.orgId } })
})
```

Never rely on the client to send `orgId`. Always derive it from the session on the server.

---

## Real-time

**Default: polling with TanStack Query.**

`refetchInterval` on queries that need live data. Simple, zero infrastructure, works everywhere.

```ts
const { data } = trpc.notifications.list.useQuery(undefined, {
  refetchInterval: 5000, // poll every 5s
})
```

**When polling is not enough: Server-Sent Events (SSE).**

SSE is one-directional (server → client), works over HTTP, no WebSocket infrastructure needed. Use for live feeds, activity streams, progress updates.

**WebSockets only when:** true bidirectional real-time is required (collaborative editing, live chat). Add only when SSE or polling demonstrably cannot meet the requirement.

---

## File storage

**Default: Cloudflare R2 via Uploadthing.**

Uploadthing handles the upload flow, presigned URLs, file type validation, and size limits. Files are stored in R2. No S3 setup, no CORS configuration, no presigned URL management.

```ts
import { createUploadthing } from 'uploadthing/next'

const f = createUploadthing()

export const uploadRouter = {
  imageUploader: f({ image: { maxFileSize: '4MB' } })
    .middleware(async ({ req }) => {
      const session = await auth.api.getSession({ headers: req.headers })
      if (!session) throw new Error('Unauthorized')
      return { userId: session.user.id }
    })
    .onUploadComplete(async ({ metadata, file }) => {
      // save file URL to DB
    }),
}
```

---

## Failure modes

For every significant feature, document:

| Failure | Behaviour | Detection |
|---------|-----------|-----------|
| DB unavailable | App returns 500, no data loss | Railway alerts + PostHog errors |
| Worker crashes | Jobs remain in queue, retry on restart | pg-boss retry policy |
| File upload fails | User sees error, no partial state | Uploadthing error callback |
| Auth service down | Users cannot sign in, existing sessions work | PostHog errors |

Design every mutation to be **idempotent** — safe to retry. Use `cuid()` IDs generated client-side when needed so retried creates do not duplicate data.

---

## Observability

- **Errors:** PostHog error tracking on all unhandled exceptions.
- **Logs:** structured `console.log` with JSON on Railway. Include `userId`, `orgId`, `requestId` on every log line in request context.
- **Health:** `/api/health` endpoint on every service. Railway health checks configured.
- **Alerts:** Railway service restart alerts. PostHog error rate alerts.

---

## What to keep simple

- **One database.** Postgres handles 99% of use cases. Do not add a second database technology without a compelling measured reason.
- **One deployment target.** Railway. No Vercel, no Lambda, no edge functions unless there is a specific measured need.
- **No microservices.** Everything in the Next.js app unless it is genuinely a separate concern (background worker). Microservices add latency, deployment complexity, and distributed systems failure modes. Avoid until pain demands it.
