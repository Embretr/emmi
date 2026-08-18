# Scorecard

The 0–5 scorecard starts conversations. It's not a verdict — it's a tool to align on which pillars need work first and to show progress at the end.

## Rubric per pillar

### Copywriting

| Score | What it looks like |
|---|---|
| 0 | Value prop indeterminable; copy is noise |
| 1 | You can guess the product from context, but the screen doesn't help |
| 2 | Value prop inferable but buried; tone passable but inconsistent |
| 3 | Value prop visible on the page; some copy works, some doesn't |
| 4 | Value prop lands fast; reassurances present; mostly consistent tone |
| 5 | Value prop lands in <2s, tone is consistent and honest, every word earns its place, every committal moment has a reassurance |

**Strategic clarity modifier:** if value prop, audience, or tone is unclear from the copy, deduct 1 point from the Copywriting score. (Course keeps 5 pillars — this is a modifier, not a 6th pillar.)

### Layout

| Score | What it looks like |
|---|---|
| 0 | Chaotic, no alignment, unclear grouping |
| 1 | Some alignment, but proximity/grouping issues are obvious |
| 2 | Mostly aligned; spacing rhythm uneven; borders define regions instead of grouping |
| 3 | Groupings read well; rhythm okay; some cramming or border bloat remains |
| 4 | Clean rhythm; groupings read naturally; progressive disclosure used where needed |
| 5 | Eye follows top-to-bottom without backtracking; Gestalt grouping is effortless |

### Emphasis

| Score | What it looks like |
|---|---|
| 0 | Nothing stands out, OR everything shouts (same visual effect) |
| 1 | Primary element is vaguely more prominent; too many competitors |
| 2 | Some hierarchy; lead element identifiable but not dominant at a glance |
| 3 | Hierarchy is clear but Squint Test uncertain |
| 4 | Hierarchy holds under Squint Test; one clear lead, competitors step back |
| 5 | Hierarchy is obvious in <1s; passes Squint Test with room to spare; feels calm not aggressive |

### Accessibility

| Score | What it looks like |
|---|---|
| 0 | Multiple failures (contrast, target size, color-only meaning) |
| 1 | Some issues fixable; clear failures remain |
| 2 | WCAG AA mostly met; tap targets or affordances problematic |
| 3 | WCAG AA met; targets adequate; a few patterns competing |
| 4 | Good on all three principles (visible / operable / actionable); minor issues only |
| 5 | Exceeds AA contrast; generous targets; clear affordances; non-color redundancy; error prevention |

### Reward

| Score | What it looks like |
|---|---|
| 0 | Emotional dead-spot; wrong reward flavor or none at all |
| 1 | Some attempt but wrong flavor or shy |
| 2 | Right flavor but buried (Shy Reward) |
| 3 | Right flavor visible; intensity roughly right |
| 4 | Right flavor; visible; concrete (translates gain into something tangible) |
| 5 | Right flavor + right intensity + reinforced in copy + proportional to moment |

## Screen-type weights

Multiply each pillar score by the type-specific weight, then sum for a weighted total:

| Type | C | L | E | A | R |
|---|---|---|---|---|---|
| Landing page | 2 | 1 | 2 | 1 | 2 |
| Dashboard | 1 | 2 | 2 | 2 | 1 |
| Mobile app screen | 2 | 1 | 1 | 2 | 2 |
| Complex UI / form | 2 | 2 | 1 | 2 | 1 |
| Confirmation / receipt | 2 | 1 | 1 | 1 | 2 |
| Onboarding / setup | 2 | 1 | 2 | 1 | 2 |

The max weighted total varies by screen type. Report both raw and weighted.

## BEFORE → AFTER delta format

Final scorecard output format:

```
BEFORE                                AFTER
───────────────                       ───────────────
C  2  [weight 2 = 4]                  C  4  [weight 2 = 8]
L  3  [weight 1 = 3]                  L  4  [weight 1 = 4]
E  2  [weight 2 = 4]                  E  4  [weight 2 = 8]
A  3  [weight 1 = 3]                  A  4  [weight 1 = 4]
R  1  [weight 2 = 2]                  R  4  [weight 2 = 8]
───────────────                       ───────────────
Total: 16 / 40 (weighted)             Total: 32 / 40 (weighted)
                                      Δ: +16 points
```

Always show:
1. Raw pillar scores (0–5 each)
2. Weighted totals (raw × weight)
3. Per-pillar improvement notes — e.g., "C: clarified value prop, removed duplicate body copy; L: established 8px rhythm, replaced borders with surface tokens; ..."

## How to score

- Be opinionated — give a number even if you're unsure
- Explain the gap: "this is a 2 because X; it'd be a 4 if Y"
- Don't optimize for "accuracy" — optimize for starting the right conversation
- Re-score after every major change so the delta is visible
