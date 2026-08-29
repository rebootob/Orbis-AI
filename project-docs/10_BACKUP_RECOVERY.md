# Backup and Recovery

## Backup scope

Back up Hermes configuration/state, Git repositories, n8n workflows/configuration, and relevant system configuration. Do not include plaintext secrets in repository backups.

## Policy

- Daily: quick backup.
- Weekly: full backup.
- Event-driven: before upgrades and major configuration changes.

Backup location, retention, encryption, ownership, and restore environment are `<TO_BE_DEFINED>`.

## Recovery procedure

1. Stop further changes and identify the affected component.
2. Select the last known-good backup or Git revision.
3. Restore in a non-production or otherwise approved environment first.
4. Validate state, access controls, task continuity, and integration health.
5. Obtain Level 3 approval before production restoration if applicable.
6. Record the incident, restoration point, validation results, and follow-up actions.

The V1 acceptance gate requires a documented recovery test that proves important task state survives a restart and recovery path.
