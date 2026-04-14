---
name: emmi-team-manager
description: >-
  Emmi team workflows: GitHub issues, branches, PRs, reviews, task splitting, release notes.
  Use for sprint planning, delegation, or process.
---

# Team manager

## GitHub workflow

### Issues

Every piece of work is a GitHub issue before it is code.

- **Title:** imperative, specific. "Add password reset flow" not "Auth improvements."
- **Body:** problem statement, acceptance criteria as a checklist, any relevant context or links.
- **Labels:** feature / bug / chore + size (xs / s / m / l). Size is effort estimate, not time.
- **Milestone:** the MVP or release this issue belongs to.

Create issues via CLI:
```bash
gh issue create --title "..." --body "..." --label "feature,s" --milestone "mvp"
gh issue list --milestone "mvp"
gh issue close 42
```

### Branches

- Short-lived. Merge within days, not weeks.
- Named: `feat/short-description`, `fix/short-description`, `chore/short-description`.
- Every branch links to an issue: reference `#42` in the PR body.
- Delete branches after merge.

### Pull requests

- **One concern per PR.** A PR that does two things is two PRs.
- **Vertical slices.** Each PR delivers end-user value where possible — schema + procedure + UI together, not separately.
- **PR body includes:** what this does, how to test it, screenshots for UI changes, issue reference.
- **Size:** aim for PRs reviewable in under 20 minutes. Large PRs get missed or rubber-stamped.

```bash
gh pr create --title "..." --body "..." --assignee "@me"
gh pr list
gh pr merge 42 --squash --delete-branch
```

### Reviews

Reviewers check:
- Does it solve the issue it references?
- Are there tests for non-trivial logic?
- Are there any obvious security issues (unvalidated input, missing auth check, exposed secrets)?
- UI changes: does it match the design system, does it work on mobile?
- No unnecessary complexity introduced.

Reviews are not style enforcement — that is what linters are for.

---

## Task splitting

- **Vertical slices first.** Split by user-visible outcome, not by layer (do not have separate issues for "add DB schema", "add API", "add UI" unless they are genuinely parallelisable).
- **Spike tasks explicit.** If a task requires research before implementation, create a spike issue with a timebox. Output is a decision, not code.
- **Blockers visible.** If an issue cannot start until another is done, note it explicitly in the issue body.
- **No tasks smaller than 30 minutes or larger than 2 days.** Too small = overhead, too large = hard to review and risky to merge.

---

## Releases

Every release to production gets a brief note documenting:
- What shipped.
- Any migration steps required.
- How to roll back if something goes wrong.
- Known issues or limitations.

Write it as a GitHub release or in the plan doc. One paragraph is enough for small releases.

```bash
gh release create v1.2.0 --title "v1.2.0" --notes "..."
```

---

## Communication defaults

- **Async first.** Decisions in writing (GitHub issues, PR comments) so they are searchable and don't require everyone online at the same time.
- **Decisions in the repo.** If it affects the code, the decision lives near the code — ADR, plan doc, or issue comment. Not in Slack or a meeting.
- **No drive-by architecture.** Technical decisions that affect multiple files or services go through the iterative-process or architect-dev skill — not a quick PR comment.
