# OpenRelief Security

- Form and record values are allowlisted and validated by exact form version on both offline creation and server acceptance.
- Mutation IDs prevent duplicated submissions after ambiguous network failures.
- Base versions prevent silent lost updates; conflicts preserve both copies.
- Resolution requires coordinator/admin permission and records strategy, actor, time, and resulting version.
- File writes use a mode-600 temporary file and atomic rename.
- The container runs non-root, read-only, with dropped capabilities and `no-new-privileges`.

The `x-user-*` headers are a development adapter only. Production must authenticate identities cryptographically, authorize project/site assignments, define offline session expiry, encrypt devices and transport, isolate tenants, protect exports/backups, redact logs, and support loss/revocation procedures. IndexedDB is not application-level encryption.
