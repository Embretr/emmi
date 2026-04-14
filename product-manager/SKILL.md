---
name: emmi-product-manager
description: >-
  Emmi product management: scope, prioritisation, outcomes over output, knowing when to cut.
  Use when defining what to build, why, and in what order.
---

# Product manager

## Philosophy

- **Outcomes over output.** A shipped feature nobody uses is waste. Define success before building.
- **The best feature is often the one you don't build.** Every feature adds maintenance surface. Default to cutting scope until you can defend what remains.
- **Talk to users before writing code.** Assumptions about what users want are usually wrong. Validate before building, not after.
- **Small bets, fast feedback.** Ship the smallest thing that tests the hypothesis. Expand what works, cut what doesn't.

---

## Prioritisation

For any backlog decision, evaluate on two axes — impact and effort:

| | Low effort | High effort |
|--|-----------|------------|
| **High impact** | Do first | Plan carefully, break down |
| **Low impact** | Do if trivially fast | Cut or defer indefinitely |

When stuck: "What is the most important thing the user cannot do right now?" That goes next.

---

## Defining a feature

Every feature needs these answered before work starts. Unknown answers are the first thing to resolve — not a reason to start building anyway.

- **Problem:** What is failing or missing for the user right now?
- **User:** Who specifically? A named persona with real context, not "users."
- **Success:** How do we know this worked? A measurable outcome, not "users will like it."
- **MVP:** What is the smallest version that tests whether this solves the problem?
- **Non-goals:** What are we explicitly not building? As important as what we are building.
- **Risk:** What assumption might be wrong, and what happens if it is?

---

## Scoping rules

- **Cut the nice-to-haves.** If a feature is still useful without a capability, cut it for MVP.
- **One core flow per MVP.** Solves one problem for one persona. Secondary flows come after validation.
- **No speculative features.** Build for real users you have or will have at launch, not hypothetical future ones.
- **Edge cases are not MVP scope** unless they affect the majority of users or are legally required.

---

## When to kill a feature

Kill a feature when:
- Adoption is consistently low with no clear improvement path.
- Maintenance cost outweighs value to the users who use it.
- It conflicts with a more important user goal.
- The assumption it was built on turned out to be wrong and cannot be fixed cheaply.

Killing a feature is a success. It reduces complexity.

---

## Communicating decisions

Every significant product decision gets a written rationale — one paragraph in the plan doc or GitHub issue. Cover:
- What was decided.
- What was rejected and why.
- What would change the decision.

The decision must be findable later.

---

## Metrics

Track the minimum set that tells you if the product is working:

- **Activation:** did the user complete the core action that delivers value?
- **Retention:** do they come back?
- **Core action frequency:** how often do active users do the thing the product is for?

Do not use sign-ups or page views as primary success signals. Instrument these three in PostHog before launching a feature, not after. Tie to the iterative-process plan doc.
