# Approval Policy

## Decision rules

Level 0 actions may proceed automatically. Level 1 actions may proceed only in an approved development workspace. Level 2 actions require a recorded REVIEWER PASS before execution. Level 3 actions require explicit user approval for the exact action and target before execution.

## Mandatory merge sequence

A merge may occur only after this exact sequence:

1. Runtime REVIEWER returns PASS.
2. STOP.
3. ChatGPT Control Plane independently reviews the current GitHub repository/PR head SHA.
4. ChatGPT explicitly issues `REVIEWER PASS` / `REVIEW_PASS`.
5. STOP.
6. Project Owner explicitly approves the exact PR merge.
7. The merge may then occur.

No earlier step authorizes a later step. Absence of any step invalidates merge authorization.

## Non-authoritative signals

These are never merge approval and cannot be inferred as such:
- prior approval of a different action;
- task state, labels, comments, or memory;
- Telegram, Desktop, or workflow progression.

## Approval record

For every Level 2 or 3 action, record the task ID, target project/environment, requested action, risk, reviewer result, user approval where required, actor, timestamp, and outcome. The authoritative log location is `project-docs/GOVERNANCE_INCIDENTS.md`.

## Role restrictions

- Runtime REVIEWER cannot issue repository `REVIEWER PASS` / `REVIEW_PASS`.
- MASTER cannot infer or manufacture Control Plane `REVIEWER PASS` / `REVIEW_PASS`.
- Owner implementation approval is not merge approval.

## Examples

| Action | Level | Gate |
|---|---|---|
| Inspect a repository status | 0 | None |
| Edit code in a development workspace | 1 | Workspace scope |
| Merge a reviewed branch | 3 | Full merge sequence above |
| Push to a remote | 2 | REVIEWER PASS |
| Change a production credential | 3 | Explicit user approval |
| Delete production data or force-push | 3 | Explicit user approval |

If scope, environment, or impact is unclear, stop and request clarification; do not infer approval.
