#!/usr/bin/env bash
set -euo pipefail
mkdir -p backups
docker compose exec -T db pg_dump -U "${POSTGRES_USER:-appuser}" "${POSTGRES_DB:-appdb}" > "backups/appdb-$(date +%Y%m%d-%H%M%S).sql"
echo "Database backup created."
