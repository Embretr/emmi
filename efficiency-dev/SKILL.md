---
name: emmi-efficiency-dev
description: >-
  Emmi efficiency work: improve load times, runtime performance, cost, and scaling characteristics. Use for Core Web Vitals,
  bundle size, DB query cost, caching, queue backpressure, and capacity planning.
---

# Efficiency dev

## Web

- Measure: **LCP, INP, CLS**; server **TTFB**.  
- **Bundle:** analyze chunks, dynamic import, remove duplicate deps.  
- **Images:** correct sizes, modern formats, priority hints.  
- **Data:** avoid over-fetching; pagination; caching headers or CDN.

## Backend

- **Queries:** indexes, N+1 elimination, explain plans.  
- **Caching:** Redis or edge where safe; TTL and invalidation explicit.  
- **Queues:** rate limits, dead letter, idempotency.

## Mobile

- Startup time, JS thread work, list virtualization, image decode cost.

## Output

Before/after metrics, bottleneck summary, and concrete changes with risk notes.
