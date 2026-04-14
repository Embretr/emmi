---
name: emmi-efficiency-dev
description: >-
  Emmi performance: easy wins applied by default, production-ready hardening on ship, deep work on request.
  No hard budgets — optimise what gives the best result.
---

# Efficiency dev

## When to do what

Performance work has three tiers. Know which tier applies before starting.

| Tier | When | What |
|------|------|------|
| **Easy wins** | Always — baked into normal development | Low-effort, high-impact habits applied by default |
| **Production-ready hardening** | When making something production-ready | Bundle analysis, query review, image audit |
| **Deep work** | On explicit request or when something is measurably slow | Caching strategy, Redis, query optimisation, profiling |

Never spend time on deep optimisation work unless asked or unless a specific slow point has been identified and measured. Optimise what gives the best result — not what is theoretically optimal.

---

## Tier 1 — Easy wins (always apply)

These cost little and should be in place from the start.

**Next.js / web**
- Use `next/image` for every image. Never a raw `<img>` tag. Set `width`, `height`, `priority` on above-the-fold images.
- Dynamic import (`next/dynamic`) for heavy components not needed on initial load.
- Keep client components small. Push as much as possible to RSCs — they don't ship JS to the browser.
- `loading="lazy"` on all below-the-fold images not using `next/image`.
- Avoid importing large libraries client-side (date libraries, charting, etc.) without checking the bundle cost first.

**Database (Prisma)**
- Add indexes on every foreign key and every field used in a `where` clause at schema design time — not after queries get slow.
- Use `select` to fetch only the fields needed. Never return full models to the client when a subset will do.
- Avoid N+1 — use `include` or batch queries. If a loop calls `db.*` on each iteration, that is an N+1.

**Mobile (Expo)**
- Hermes engine always enabled.
- FlashList over FlatList for any list with more than ~20 items.
- `expo-image` over the built-in `Image` for automatic caching and performance.
- Never run heavy computation on the JS thread — offload with `InteractionManager.runAfterInteractions` or a worker if needed.

---

## Tier 2 — Production-ready hardening (before ship)

Run these when preparing a feature or app for production.

**Bundle analysis**
```bash
ANALYZE=true pnpm build
```

Install `@next/bundle-analyzer` and configure in `next.config.ts`. Look for:
- Unexpectedly large chunks.
- Duplicate packages (two versions of the same lib).
- Client-side imports that should be server-only.
- Libraries that can be dynamically imported.

**Image audit**
- All images use `next/image` with correct `sizes` prop for responsive images.
- No uncompressed PNGs where WebP/AVIF would work.
- Hero and above-the-fold images have `priority={true}`.

**Query review**
- Run `prisma studio` or check Railway logs for slow queries.
- Confirm all `where` fields have indexes.
- Check for missing `select` — procedures returning more data than the client uses.

**Core Web Vitals check**
- Run Lighthouse or PageSpeed Insights on the production URL.
- LCP: largest image or text block loads fast. Usually fixed by `priority` on hero image and fast TTFB.
- CLS: no layout shifts. Usually caused by images without dimensions or fonts swapping.
- INP: interactions feel instant. Usually caused by heavy JS on the main thread.

**Mobile startup**
- Profile cold start time with Flipper or `expo-dev-client`.
- Defer anything not needed in the first 2 seconds.

---

## Tier 3 — Deep work (on request or measured bottleneck)

Only do this work when asked or when a specific, measured problem exists.

**Caching**
Choose the strategy that gives the best result for the specific data:

| Data type | Strategy |
|-----------|---------|
| Static or rarely changing | Next.js fetch cache or ISR with long revalidation |
| User-specific, frequently read | TanStack Query client cache with appropriate `staleTime` |
| Shared, frequently read, expensive to compute | Redis with explicit TTL and invalidation |
| Real-time | No cache — subscribe or poll |

Redis is added per project when needed. Not a default. Common use cases: rate limiting, session store, expensive aggregations, pub/sub.

**Database**
- Run `EXPLAIN ANALYZE` on slow queries.
- Consider read replicas for read-heavy workloads.
- Pagination: cursor-based for large datasets, offset for small ones.
- Connection pooling: PgBouncer or Railway's built-in pooling for high-concurrency.

**Bundle deep dive**
- Tree-shake or replace libraries with lighter alternatives.
- Route-level code splitting — each page loads only what it needs.
- Move constants and config to server-side so they don't ship to the client.

---

## Output

Always report before/after for any optimisation work:

```
Before: [metric and value]
After:  [metric and value]
Change: [what was done]
Risk:   [any regression risk or caveats]
```

No metric, no evidence it helped.
