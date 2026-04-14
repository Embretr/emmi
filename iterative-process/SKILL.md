---
name: emmi-iterative-process
description: >-
  Emmi iterative planning for new features and greenfield projects: exhaustive Q&A from blank slate to MVP plan,
  then to production-ready scope, with configurable feedback rounds. Expect 20–40+ follow-ups per feedback round.
  Use for "plan the feature", "MVP then full product", roadmap workshops, or structured discovery before build.
---

# Iterative process

## Outcomes

Produce a **written plan** with: problem, users, MVP scope, success metrics, milestones, risks, and **post-MVP / production** scope. Plans must survive handoff to another engineer.

## Phases

1. **Discovery (nothing → MVP)**  
   Ask until empty: who, why now, constraints, non-goals, tech assumptions, data model sketch, critical user journeys, edge cases, launch definition for MVP.

2. **MVP lock**  
   Freeze MVP scope in the doc. List explicit **out of scope** items.

3. **Feedback round(s)**  
   User-configurable count (default: one round after MVP doc, one after first MVP ship). Each round: **minimum 20–40 follow-up questions** (can be batched in sets of 5–10 per message). Cover gaps, metrics, abuse cases, ops, support, analytics, rollback.

4. **Post-MVP (MVP → production-ready)**  
   After MVP is done (or agreed "MVP shipped"), run another feedback cycle, then expand the plan: hardening, perf, accessibility, i18n, admin, billing edge cases, observability, runbooks.

## Rules

- Prefer **one canonical plan file** in the repo (e.g. `docs/plan-<feature>.md`). Append dated revision notes rather than losing history.
- Every phase ends with **checklist acceptance**: user confirms or edits.
- If the user sets `feedback_rounds: N`, run **N** full rounds after MVP definition and **N** (or user-defined) after MVP delivery before locking "production" scope.
- Pull in **rules/** and **evaluators/** if they affect scope.

## Deliverable template (use as markdown structure)

- Vision and non-goals  
- Personas / jobs-to-be-done  
- MVP user stories + acceptance criteria  
- Data model and API outline  
- Milestones and dependencies  
- Risks and mitigations  
- Post-MVP backlog grouped by theme  
- Open questions (explicitly empty before sign-off)
