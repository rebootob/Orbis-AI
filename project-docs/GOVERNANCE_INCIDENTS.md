# Governance Incidents

This file records governance violations for audit. Each record preserves evidence and does not alter repository history.

## INCIDENT-2026-08-31-WP006

| Field | Value |
|---|---|
| INCIDENT_ID | INCIDENT-2026-08-31-WP006 |
| DATE | 2026-08-31 |
| WORK_PACKAGE | WP-006 — Security Gates, Approvals, and Audit Logging |
| REPOSITORY | rebootob/Orbis-AI |
| VIOLATION | PREMATURE_MERGE_BEFORE_CONTROL_PLANE_REVIEW_PASS |
| AUTHOR | MASTER / CODER |
| ACTOR | Hermes runtime / user workflow |
| EVIDENCE | GitHub PR #22 merged into `develop` before ChatGPT Control Plane explicitly issued `REVIEWER PASS` / `REVIEW_PASS` for the repository state. |
| ROOT CAUSE | Merge occurred without explicit Control Plane review authorization and without explicit Project Owner approval of the exact PR merge. |
| IMPACT | Governance gate bypass; merge authority was inferred from task progression rather than explicit authorization. |
| REMEDIATION | Required merge gate invariant restored; this incident preserved as audit evidence; no revert of merged content. |
| STATUS | RECORDED |
| NEXT_WP_GATE | Blocked until explicit Control Plane instruction. |

## Audit Notes

- PR #22 merged content remains in `develop` as approved implementation evidence.
- This incident does not authorize rollback, Restore/DR, or expansion of scope.
- WP-007 Issue #24 and PR #25 remain open as unauthorized-start evidence and must not be merged.
