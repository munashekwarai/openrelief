# OpenRelief Deployment

```bash
npm ci && npm run typecheck && npm test && npm run build
OPENRELIEF_DATA=/var/lib/openrelief/openrelief.json HOST=127.0.0.1 PORT=3001 npm start
```

Or run `docker compose up --build -d`. Localhost permits service workers over HTTP; remote deployments require HTTPS. Replace development identity headers with an authenticated proxy or identity adapter before any remote or real-data use.

Back up the server state after quiescing writes or through a storage adapter snapshot. Recovery must verify forms, records, processed mutation IDs, unresolved conflicts, and audit ordering. Device recovery needs a separate operational plan because unsynchronized IndexedDB data exists only on that device.

For multi-instance use, implement the `Store` interface with a transactional database, unique mutation IDs, compare-and-swap record versions, durable audit, and tenant/project keys.
