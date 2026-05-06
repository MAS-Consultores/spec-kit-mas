# Moodle 3.x — Legacy Security Guidance (Exception Track)

Moodle 3.x is **not** an approved company stack. Work on Moodle 3 MUST be treated as a **documented exception** in the implementation plan (rationale, scope, approver, and migration path).

## Policy

**MUST**

- Record `Deviation / Exception Needed` in the plan with approver and sunset date for migration to Moodle 5.
- Apply only security patches from the vendor-supported line for the exact minor version in use; track build numbers.
- Isolate the instance (network segmentation, dedicated credentials, separate backups from production Moodle 5 estates).
- Restrict administrative access; enforce MFA at the identity provider or VPN layer when Moodle 3 lacks native MFA.
- Validate capabilities and contexts on every entrypoint (`require_login`, `require_capability`) for the Moodle 3 API surface in use.
- Use Moodle database APIs with placeholders; never concatenate user input into SQL.
- Use `format_string` / `format_text` for output; never echo raw user input.
- Use the Files API and `pluginfile.php` for user content; declare Privacy API metadata where personal data is stored.

**MUST NOT**

- Ship new privileged features on Moodle 3 without executive security sign-off.
- Install unmaintained third-party plugins without a documented risk acceptance.

## Migration

**SHOULD**

- Attach a milestone-level migration plan to Moodle 5 with data and capability mapping.

## Evidence

Plans MUST reference this document when the feature targets Moodle 3 and MUST list compensating controls (patch level, isolation, monitoring, migration date).
