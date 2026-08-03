# Issue-First Automation Policy

This repository converts eligible bot-created pull requests into reviewable GitHub issues and records actionable CI failures as issues.

## Security invariants

1. The privileged `pull_request_target` job is metadata-only. It must never check out, build, import, source, or execute code from a pull request.
2. Third-party and GitHub-maintained actions must be pinned to a full immutable commit SHA.
3. Workflow permissions are denied by default and granted per job only when required.
4. A pull request is treated as bot-created only when both the webhook sender type is `Bot` and the actor login ends in `[bot]`.
5. The original pull-request URL, head branch, and head commit SHA are preserved in the generated issue for auditability.
6. Duplicate markers prevent repeated events from creating duplicate tracking issues.
7. Cancelled workflow runs do not create failure issues. Existing CI issues close only after a successful verification run for the same workflow and branch key.
8. Repository protections and required checks must not be bypassed to merge this automation.

## Maintainer workflow

1. Validate the underlying problem or dependency update.
2. Define acceptance criteria and regression risk in the issue.
3. Add `approved-for-fix` only after review.
4. Implement the smallest safe change on a human-reviewed branch.
5. Require repository validation, security checks, and portfolio-security checks to pass.
6. Record the successful run or merged pull request before closing the issue.

## Emergency exception

Apply `allow-bot-pr` only when the original bot pull request must remain open for native update or compatibility behavior. The label is an explicit exception, not the default path.
