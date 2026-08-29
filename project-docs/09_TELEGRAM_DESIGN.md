# Telegram Design

Telegram is the primary remote command interface. It transports requests to MASTER Hermes and returns scoped task updates or results.

## Required controls

- Use a private bot and allow only explicitly authorized Telegram user IDs.
- Reject or ignore unauthorized users without exposing system details.
- Do not send credentials, secrets, or sensitive logs through Telegram.
- Require normal review and approval gates; Telegram access does not elevate authority.
- Log authentication decisions and task references without retaining unnecessary sensitive content.

## Validation path

1. Configure authorized IDs without recording them in Git.
2. Verify an authorized Telegram → Hermes → Telegram exchange.
3. Unauthorized-user negative testing is deferred to Phase 6 security validation and was not executed as part of Phase 2.
4. Dangerous-action negative testing is deferred to Phase 6 security validation and was not executed as part of Phase 2.

## Validated baseline

Phase 2 validation passed using Hermes on WSL2 Ubuntu: the private allowlisted Telegram route completed successful round trips. The WSL2 systemd gateway is the preferred runtime. Telegram user IDs, bot tokens, and other credentials are intentionally not recorded here. The Windows Native Telegram Gateway is retained only as a non-primary fallback because it was unstable.
