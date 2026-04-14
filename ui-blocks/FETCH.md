# Fetching blocks (for agents)

## Quick map

- **Master index:** [CATALOG.md](CATALOG.md)
- **Per-pack trees + flat lists:** [marketing/BLOCKS.md](marketing/BLOCKS.md), [ecommerce/BLOCKS.md](ecommerce/BLOCKS.md), [application/BLOCKS.md](application/BLOCKS.md), [components/BLOCKS.md](components/BLOCKS.md)

## Workflow

1. Decide pack: marketing site → `marketing`; shop → `ecommerce`; app/dashboard → `application`; low-level UI → `components`.
2. Open that pack’s **BLOCKS.md**, find the category (e.g. `sections/heroes/`).
3. Open specific files under `ui-blocks/<pack>/react/...` or `ui-blocks/components/typescript/...`.
4. Use as **inspiration and structure reference**; merge with the project’s components and tokens.

## Path pattern

- Marketing / ecommerce / application: `ui-blocks/<pack>/react/<area>/<category>/<NN-name>.jsx`
- Components: `ui-blocks/components/typescript/<component>.tsx`
