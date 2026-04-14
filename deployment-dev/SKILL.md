---
name: emmi-deployment
description: >-
  Emmi deployment: Railway-first, CLI-first. Managed Postgres, multiple services, staging + prod environments.
  Instant rollback. Set everything up so it can be operated from the Railway CLI.
---

# Deployment

## Core principle

**CLI-first.** Everything that can be done from the Railway CLI should be set up to be done from the Railway CLI. When setting up a project, configuring services, or deploying — reach for `railway` before the dashboard. The dashboard is for env vars and one-time visual checks only.

---

## Stack

| Tool | Role |
|------|------|
| Railway | Hosting, managed Postgres, services, environments |
| Railway CLI | Deploy, logs, run, link, status — primary interface |
| GitHub Actions | CI gate (tests + typecheck) before Railway deploys |
| PostHog | Error tracking in production |

---

## Railway CLI setup

Install and authenticate first:

```bash
npm install -g @railway/cli
railway login
railway link   # link to existing project, or:
railway init   # create new project
```

Key commands used daily:

```bash
railway status                        # current project and environment
railway up                            # deploy current directory
railway logs                          # tail logs for linked service
railway logs --service web            # logs for a specific service
railway run <command>                 # run a command in the Railway environment (with env vars injected)
railway shell                         # open a shell with Railway env vars
railway variables                     # list env vars for current environment
railway environment                   # switch environments (staging / production)
railway domain                        # generate or view domain
railway rollback                      # instant rollback to previous deploy
```

---

## Project structure

### Services

Split into multiple services per project as the app warrants. Common pattern:

| Service | Role |
|---------|------|
| `web` | Next.js app |
| `worker` | Background jobs (if needed) |
| `cron` | Scheduled tasks (if needed) |
| `db` | Railway managed Postgres |

Each service has its own build and start command. Add services via CLI:

```bash
railway service create
```

### Environments

Default to **staging** and **production** per project. Local development uses a local DB or `railway run` with staging vars.

```bash
railway environment staging    # switch to staging
railway environment production # switch to production
```

Never develop against production. Staging is the integration environment — it should match production as closely as possible.

---

## Database

Use Railway's managed Postgres. The connection string is injected automatically as `DATABASE_URL` when the service is linked.

### Prisma on deploy

Run `prisma db push` as part of the Railway start command — not the build command. This ensures schema is synced before the app starts serving traffic.

```bash
# Railway start command for web service
npx prisma db push && node server.js
# or with bun:
bunx prisma db push && bun run start
```

This runs on every deploy. `db push` is idempotent — safe to run repeatedly.

---

## Environment variables

Managed directly in the Railway dashboard. Never committed to the repo.

**Required vars to document** in `docs/env.md` (names only, never values):

```markdown
# Environment variables

## Required (all environments)
- `DATABASE_URL` — injected by Railway Postgres service
- `BETTER_AUTH_SECRET` — random 32-char string
- `NEXT_PUBLIC_APP_URL` — full URL of the deployment

## Required (production only)
- [list any prod-only keys]

## Optional
- [list with description]
```

Use `@t3-oss/env-nextjs` in code — a missing or invalid var fails the build, not at runtime.

Copy vars between environments via CLI where Railway supports it, otherwise set manually in the dashboard.

---

## Deploy flow

1. Push to `main` → GitHub Actions runs typecheck, lint, tests.
2. On pass → Railway auto-deploys `main` to staging.
3. Manual promote to production via Railway dashboard or CLI:

```bash
railway up --environment production
```

Or configure Railway to auto-deploy `main` to production if staging is not needed as a gate.

**Build command:**
```bash
bun run test && bun run build
```

Tests failing blocks the build and the deploy.

---

## Domains and TLS

Per project. Railway generates a `*.up.railway.app` URL for each service by default — use this for staging.

For production, add a custom domain via CLI:

```bash
railway domain
```

Then point your DNS to Railway's provided CNAME. TLS is automatic. Verify both apex and `www` if used.

---

## Rollback

Instant rollback to the previous deploy via Railway CLI:

```bash
railway rollback
```

This redeploys the previous build image. Database changes made by `db push` are not rolled back — design schema changes to be backwards compatible with the previous app version so rollback is always safe.

**Rule:** before any schema change that removes or renames a column, ensure the running app version does not depend on that column. Ship the app change first, then the schema cleanup.

---

## Observability

- **Logs:** Railway's built-in log viewer and `railway logs` CLI. Structured logging (`console.log` with JSON objects) makes logs filterable.
- **Errors:** PostHog error tracking. All unhandled errors and caught exceptions surface there.
- **Uptime:** Railway provides basic uptime monitoring per service. For production, add a health endpoint:

```ts
// app/api/health/route.ts
export function GET() {
  return Response.json({ status: 'ok' })
}
```

Configure Railway's health check to hit `/api/health`.

---

## New project checklist

```
[ ] railway init or railway link
[ ] Create services: web, db (managed Postgres), worker/cron if needed
[ ] Set environment variables in dashboard (staging first, then production)
[ ] Configure build command: bun run test && bun run build
[ ] Configure start command: bunx prisma db push && bun run start
[ ] Add /api/health route and configure Railway health check
[ ] Set up staging environment, verify deploy
[ ] Add custom domain on production, verify TLS
[ ] Document required env vars in docs/env.md
[ ] Confirm railway rollback works on staging
```
