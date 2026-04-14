---
name: emmi-deployment
description: >-
  Emmi deployment skill: Railway-first (services, env, databases, domains, rollbacks). May cover other hosts when needed.
  Use for ship, env vars, production debugging, or infra setup.
---

# Deployment

## Railway (default)

- **Services:** align build/start commands with monorepo package if applicable.  
- **Env:** document required vars in README or `docs/`; no secrets in repo.  
- **Databases:** managed Postgres/Redis; migration strategy (run migrations in deploy step or one-off).  
- **Domains / TLS:** verify apex and www if used.  
- **Rollback:** previous deploy + DB migration compatibility notes.

## Other platforms

When not Railway: map same checklist (build, env, data, networking, observability). Call out deltas explicitly.

## Checklist

- Health endpoint or equivalent smoke after deploy  
- Logs and errors visible (structured logging)  
- Background workers and cron if any  
- Cost and scaling knobs noted

## Output

Exact steps run, URLs, env names (not values), and follow-up risks.
