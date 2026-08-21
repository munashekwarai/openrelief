# OpenRelief Threat Model

| Threat | Implemented control | Production requirement |
|---|---|---|
| Submission loss while offline | IndexedDB-first queue and cached shell | Device backup/management and storage monitoring |
| Duplicate after timeout | Stable processed mutation IDs | Database uniqueness across replicas |
| Silent overwrite | Base-version conflict detection | Transactional compare-and-swap storage |
| Malicious conflict resolution | Role check and audited explicit strategy | Strong identity, assignment authorization, review |
| Invalid/stale form values | Exact form-version validation | Form migration and retirement governance |
| Lost/stolen field device | Browser storage only | Full-disk encryption, lock, remote wipe, offline expiry |
| Identity spoofing | None in development header adapter | Replace with cryptographic authentication before deployment |
| Cross-tenant disclosure | Single-project reference | Tenant keys and authorization on every query/mutation |
| Local/server data tampering | Atomic file replacement and audit evidence | Encrypted transactional store and immutable audit export |
| Resource exhaustion | HTTP body and schema bounds | Rate limits, quotas, attachment controls |

The platform cannot determine which conflicting observation is factually correct. Eventual consistency makes temporary divergence expected. Device compromise, coerced users, false field observations, and physical safety procedures remain outside software-only guarantees.
