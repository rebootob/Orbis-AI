# Telegram Design

Telegram is the planned primary remote command interface, introduced in Phase 2. It transports requests to MASTER Hermes and returns scoped task updates or results.

## Required controls

- Use a private bot and allow only explicitly authorized Telegram user IDs.
- Reject or ignore unauthorized users without exposing system details.
- Do not send credentials, secrets, or sensitive logs through Telegram.
- Require normal review and approval gates; Telegram access does not elevate authority.
- Log authentication decisions and task references without retaining unnecessary sensitive content.

## Validation path

1. Configure authorized IDs as `<TO_BE_DEFINED>`.
2. Verify an authorized Telegram → Hermes → Telegram exchange.
3. Verify unauthorized access is denied.
4. Verify dangerous actions still require explicit human approval.

No Telegram configuration is present in this Phase 0 repository.
