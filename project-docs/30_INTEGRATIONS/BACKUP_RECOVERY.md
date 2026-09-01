# Backup and Recovery

## Backup scope

Back up Hermes configuration/state, Git repositories, n8n workflows/configuration, and relevant system configuration. Do not include plaintext secrets in repository backups.

## Policy

- Daily: quick backup.
- Weekly: full backup.
- Event-driven: before upgrades and major configuration changes.

## Implementation status

WP-005C / Phase 10 recovery path: COMPLETE FOR CURRENT RECOVERY SCOPE

Completed:
- runtime inventory / backup design
- external credential recovery verification
- backup execution / manifest validation
- isolated restore rehearsal / recovery validation: PASS
- corrective backup coverage: COMPLETE
- original accepted backup preserved: `20260830-231125`
- corrective backup: `20260830-231125-corrective`
- secret safety: PASS
- recovery isolation: PASS

Merged evidence:
- PR #46 → `49d17b88cfba4d7f3ab8f00a4066772d1252c4a4`

Current state:
RESTORE_VALIDATION=PASS
MIGRATION=NOT_STARTED
CUTOVER=NOT_STARTED

Do not claim migration or cutover readiness has been executed.

## Recovery procedure

1. Stop further changes and identify the affected component.
2. Select the last known-good backup or Git revision.
3. Restore in a non-production or otherwise approved environment first.
4. Validate state, access controls, task continuity, and integration health.
5. Obtain Level 3 approval before production restoration if applicable.
6. Record the incident, restoration point, validation results, and follow-up actions.

The V1 acceptance gate requires a documented recovery test that proves important task state survives a restart and recovery path.
