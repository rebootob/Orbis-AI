# Approval Policy

## Decision Rules

Level 0 read actions may normally proceed automatically.

Level 1 development writes may proceed only inside the explicitly approved development scope or workspace.

A normal non-protected development-branch push may occur when the current Work Package authorizes it and the push is required to create reviewable evidence.

That push does not authorize merge, deployment, production change, or repository `REVIEW_PASS`.

For repository integration such as merge:

1. Runtime REVIEWER independently reviews the implementation.
2. Runtime REVIEWER returns PASS or FAIL evidence.
3. After runtime PASS, ChatGPT Control Plane independently determines repository `REVIEW_PASS`.
4. Explicit Project Owner approval is required before merge.

Level 3 production, destructive, credential, permission, migration, or force-push actions always require explicit Project Owner approval for the exact action and target.

Runtime REVIEWER PASS and repository `REVIEW_PASS` are separate decisions.

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

## Approval Record

For actions requiring review or explicit owner approval, retain sufficient evidence to identify:

- Task ID
- Target project or environment
- Requested action
- Permission or risk level
- Runtime REVIEWER result where applicable
- ChatGPT Control Plane repository review decision where applicable
- Project Owner approval where required
- Actor
- Timestamp
- Outcome

During Phase 5 and Phase 6 the GitHub task Issue and linked Git / Pull Request evidence provide the canonical workflow and audit record.

Future Project Registry work may add cross-project indexing but does not replace the Phase 5/6 task record.

## Owner Approval Gates

- Merge requires explicit Project Owner approval even after ChatGPT Control Plane `REVIEW_PASS`.
- Approval evidence must record Task ID, requested action, permission/risk level, actor, timestamp, and outcome.
- Level 3 actions require explicit Project Owner approval for the exact action and target.
- Runtime REVIEWER PASS does not replace Project Owner approval.

## Examples

| Action | Level / Type | Gate |
|---|---|---|
| Inspect repository or task status | Level 0 | None |
| Edit files in approved development scope | Level 1 | Approved Work Package |
| Push authorized development branch for review | Level 2 workflow | Work Package + diff/secret checks |
| Runtime implementation review | Review | REVIEWER PASS/FAIL |
| Repository `REVIEW_PASS` | Review | ChatGPT Control Plane |
| Merge reviewed work | Level 2 integration | Control Plane `REVIEW_PASS` + explicit Project Owner approval |
| Production deployment or production change | Level 3 | Explicit Project Owner approval |
| Production credential or permission change | Level 3 | Explicit Project Owner approval |
| Production data deletion or force-push protected history | Level 3 | Explicit Project Owner approval |

Review PASS never authorizes deployment automatically.

If scope, environment, authority, or impact is unclear, stop and request clarification. Do not infer approval.
