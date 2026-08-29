# Approval Policy

## Decision rules

Level 0 actions may proceed automatically. Level 1 actions may proceed only in an approved development workspace. Level 2 actions require a recorded REVIEWER PASS before execution. Level 3 actions require explicit user approval for the exact action and target before execution.

## Approval record

For every Level 2 or 3 action, record the task ID, target project/environment, requested action, risk, reviewer result, user approval where required, actor, timestamp, and outcome. The authoritative log location is `<TO_BE_DEFINED>`.

## Examples

| Action | Level | Gate |
|---|---|---|
| Inspect a repository status | 0 | None |
| Edit code in a development workspace | 1 | Workspace scope |
| Merge a reviewed branch | 2 | REVIEWER PASS |
| Push to a remote | 2 | REVIEWER PASS |
| Change a production credential | 3 | Explicit user approval |
| Delete production data or force-push | 3 | Explicit user approval |

If scope, environment, or impact is unclear, stop and request clarification; do not infer approval.
