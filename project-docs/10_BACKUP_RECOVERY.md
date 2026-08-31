# Backup and Recovery

## Backup scope

Back up Hermes configuration/state, Git repositories, n8n workflows/configuration, and relevant system configuration. Do not include plaintext secrets in repository backups.

## Policy

- Daily: quick backup.
- Weekly: full backup.
- Event-driven: before upgrades and major configuration changes.

## Implementation status

WP-005C Backup/Recovery: PARTIAL COMPLETE

Completed:
- runtime inventory / backup design
- external credential recovery verification
- backup execution / manifest validation

Merged evidence:
- PR #17 → `3e7b990f1fb88724f0266f5bd2fbcb7d6303bb44`
- PR #18 → `a7789317931894366dba8f8d3e4b04d659ee6d4f`
- PR #19 → `6ca8d28ee43bb20569a9e328204aa1c9ff003753`

Restore/DR:
DEFERRED BY PROJECT OWNER

RESTORE_VALIDATION=NOT_STARTED
MIGRATION=NOT_STARTED
CUTOVER=NOT_STARTED

Do not claim full DR validation, tested restore, migration readiness, or cutover readiness.

## Recovery procedure

1. Stop further changes and identify the affected component.
2. Select the last known-good backup or Git revision.
3. Restore in a non-production or otherwise approved environment first.
4. Validate state, access controls, task continuity, and integration health.
5. Obtain Level 3 approval before production restoration if applicable.
6. Record the incident, restoration point, validation results, and follow-up actions.

The V1 acceptance gate requires a documented recovery test that proves important task state survives a restart and recovery path.
