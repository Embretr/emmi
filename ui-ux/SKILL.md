---
name: emmi-ui-ux
description: >-
  Emmi UI/UX: implement or refine interfaces using the ui-blocks library plus domain-specific rules for ecommerce,
  marketing, and application UIs. Use for landing pages, shops, dashboards, design polish, Tailwind layout work,
  or "make it match our kit".
---

# UI / UX

## Block library

Kit root sibling **`ui-blocks/`**:

- [CATALOG.md](../ui-blocks/CATALOG.md) — master map  
- Per-pack indexes: `ui-blocks/marketing/BLOCKS.md`, `ecommerce`, `application`, `components`

**Fetch flow:** read **BLOCKS.md** for the right pack, then **Read** only the `.jsx` / `.tsx` files you need. Adapt to app tokens, routing, and data.

## Domain rules (opinionated defaults)

### Ecommerce

- Prioritize **scannability**: price, variant, stock, shipping hints above the fold on PDP.  
- **Cart and checkout:** minimize steps; show trust (returns, security) near payment.  
- **Empty and error states** for cart, search, filters.  
- Mobile: thumb reach for primary CTA; sticky mini-cart or clear entry.

### Marketing

- **One primary CTA** per major section; repeat strategically down the page.  
- Social proof near conversion points; avoid generic filler testimonials.  
- Hero: headline, subcopy, CTA, proof or product visual in first viewport.  
- Footer: legal, product links, contact.

### Application (dashboard / SaaS)

- **Density with hierarchy:** tables readable, actions discoverable, destructive actions guarded.  
- **Shell consistency:** navigation, page title, primary action placement.  
- Forms: labels, errors inline, loading and disabled states.  
- Prefer patterns from `ui-blocks/application/` before inventing layout.

### Components / primitives

- Use `ui-blocks/components/` for low-level pieces; align with Tailwind + React patterns already in the block.

## Process

1. Confirm which domain applies (or hybrid).  
2. Pull 1–3 reference blocks; list deltas for brand and data.  
3. Implement; then run **ferdig-ferdig** or **browse** for critical flows.
