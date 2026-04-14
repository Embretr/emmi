---
name: emmi-architect-dev
description: >-
  Emmi architecture planning: boundaries, data flow, failure modes, scaling, and tradeoffs for Next.js, tRPC, Prisma,
  Expo, and monorepos. Use for greenfield structure, refactors, or "how should this fit together".
---

# Architect dev

## Deliverables

- **Context diagram** (users, apps, services, data stores).  
- **Key decisions** with alternatives rejected.  
- **Data model** sketch and consistency model (strong vs eventual).  
- **Failure modes:** what breaks, what degrades, how we detect it.  
- **Evolution:** what must be easy to change later.

## Checklist

- Auth and authorization story end-to-end  
- Multi-tenant or org model if relevant  
- Background work and scheduling  
- Observability (logs, metrics, traces)  
- Compliance and PII boundaries

Align with **web-dev**, **mobile-dev**, or **monorepo-dev** when implementing.
