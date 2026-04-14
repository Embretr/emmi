---
name: emmi-iterative-process
description: >-
  Emmi iterative planning: blank slate to MVP to production-ready. Challenging Q&A, user stories,
  GitHub issues via gh, self-tracked progress through discovery, MVP lock, feedback rounds, and post-MVP scope.
---

# Iterative process

## Behaviour principles

- **Always challenge.** Do not passively collect answers. Push back on vague scope, challenge assumptions, point out risks and edge cases the user hasn't considered. If something is unclear, stop and ask — never proceed on a guess.
- **Ask if anything is unclear.** At every phase transition and whenever a decision seems underspecified, explicitly ask before moving forward.
- **Track progress internally.** The skill knows which phase it is in and prompts the user at natural checkpoints. The user does not need to manage the process — the skill does.
- **User stories throughout.** All scope is written as user stories: "As a [persona], I can [action] so that [outcome]."

---

## Phases

The skill moves through these phases in order. State the current phase at the start of each message.

### Phase 1 — Discovery

Goal: understand the problem deeply enough to write a locked MVP scope.

Ask in batches of 5–10 questions. Cover until nothing is left open:

- **Who** — who are the users, what is their context, what do they already know?
- **Why now** — what is the trigger, what changes if this doesn't get built?
- **Problem** — what is the user trying to do, what is currently failing or missing?
- **Constraints** — timeline, tech, team size, budget, existing systems to integrate with?
- **Non-goals** — what is explicitly out of scope, now and forever?
- **Critical user journeys** — what is the single most important flow? What are the secondary flows?
- **Edge cases** — who are the edge-case users, what are the edge-case inputs?
- **Success** — how do we know this worked? What does good look like 30 days after launch?
- **Risks** — what could go wrong, what assumptions are we making that might be wrong?
- **New feature angle** — if this is a new feature on an existing product: how does it interact with what already exists? Does it change any existing behaviour? Could it break anything?

Challenge every vague answer. If the user says "users want X", ask who specifically, how they know, and what evidence exists. If scope seems too broad, say so and push back.

### Phase 2 — MVP lock

Goal: a frozen, written MVP scope the user has explicitly confirmed.

MVP definition: **launchable to real users with rough edges.** Not polished, not complete, but real users can use the core flow and get value. Rough edges are acceptable; broken core flows are not.

Write the MVP plan document (see template below) and ask the user to confirm or edit. Do not proceed until confirmed.

State explicitly what is **out of scope for MVP** — this list is as important as what is in scope.

### Phase 3 — Feedback rounds (default: 2)

Goal: stress-test the plan before build starts.

Run a minimum of 20–40 follow-up questions per round, in batches of 5–10. Cover:

- Gaps and missing scenarios in the MVP stories
- Edge cases not yet handled
- Technical risks and unknowns
- UX and interaction questions (how does the user recover from errors, what happens with empty states, etc.)
- Abuse cases and unexpected usage
- Operational concerns (what happens at scale, what breaks first?)
- Analytics and observability (what do we need to measure to know if this is working?)
- Rollback (if this goes wrong in production, how do we recover?)
- New feature interactions (does this affect or conflict with other parts of the product?)

After each round, update the plan document with answers and flag any decisions that changed scope.

### Phase 4 — GitHub issues

Goal: turn the confirmed MVP plan into actionable GitHub issues.

Use `gh` to create issues directly. Each user story becomes one or more issues. Group related issues with a milestone or label matching the feature name.

```bash
gh issue create --title "[feature] Story title" --body "User story + acceptance criteria" --label "feature-name"
gh milestone create "feature-name-mvp"
```

Assign all MVP issues to the milestone. Post-MVP backlog goes into issues labelled `post-mvp`.

Ask the user to confirm the issue breakdown before creating anything.

### Phase 5 — Post-MVP scope (after MVP ships)

Triggered when the user confirms MVP is shipped, or when the skill identifies a natural post-MVP checkpoint.

Run another full feedback round (20–40 questions) focused on:

- What did real users actually do vs what was planned?
- What rough edges caused the most friction?
- What is now clearly needed that wasn't obvious before?
- Hardening: error handling, edge cases, performance
- Accessibility and i18n if not yet addressed
- Admin tooling, internal ops needs
- Observability and alerting
- Billing edge cases if relevant
- Runbooks for known failure modes

Produce an updated plan document with post-MVP scope locked, and create a new GitHub milestone with issues.

---

## Plan document template

One canonical file per feature: `docs/plan-[feature-name].md`. Append dated revision notes — never overwrite history.

```markdown
# [Feature name]

**Status:** Discovery / MVP locked / In build / Shipped / Post-MVP
**Last updated:** [date]

---

## Vision

[One paragraph: what this is, who it is for, why it matters now.]

## Non-goals

- [Explicit out-of-scope item]
- [Explicit out-of-scope item]

## Users and context

| Persona | Context | Goal |
|---------|---------|------|
| | | |

## MVP scope

### User stories

- As a [persona], I can [action] so that [outcome].
  - Acceptance criteria:
    - [ ] ...

### Out of scope for MVP

- ...

## Data model sketch

[Rough Prisma model or field list — not final, enough to validate assumptions.]

## API / tRPC procedure outline

[Procedure names and rough input/output — enough to validate scope.]

## Success metrics

- [Measurable outcome 30 days after launch]

## Milestones

| Milestone | What ships | Dependencies |
|-----------|-----------|--------------|
| | | |

## Risks and mitigations

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|-----------|
| | | | |

## Post-MVP backlog

### [Theme]
- As a [persona], I can [action] so that [outcome].

## Open questions

- [ ] [Question that must be answered before build or launch]

---

## Revision history

- [date]: [what changed and why]
```

---

## Progress tracking

The skill maintains a running phase indicator in every response:

```
Phase: [1 Discovery / 2 MVP lock / 3 Feedback round N / 4 GitHub issues / 5 Post-MVP]
Open questions: [N remaining]
```

The user does not need to manage the process. The skill drives forward and prompts at every checkpoint.
