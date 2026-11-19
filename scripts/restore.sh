#!/usr/bin/env bash
set -euo pipefail
if [[ $# -ne 1 ]]; then echo "Usage: $0 backups/file.sql"; exit 1; fi
cat "$1" | docker compose exec -T db psql -U "${POSTGRES_USER:-appuser}" "${POSTGRES_DB:-appdb}"
echo "Database restore completed."
