#!/usr/bin/env bash
#
# Entry point script for Docker during development
set -euo pipefail

# We need to wait for the database to be ready until we can run migrations.
# To do this, retry up to 15 times to run the migrations. Once that worked,
# we can assume that the database is up and ready.
success=0
retries=15
for i in $(seq $retries); do
    echo "Running migrations…"
    ./manage.py migrate && success=1 && break || true
    echo "Database not yet ready, waiting ($i/$retries)…"
    sleep 1
done
if [ "$success" -eq 1 ]; then
    echo "Database is up, all migrations applied"
else
    echo "Timed out waiting for database"
    exit 1
fi

echo "Collect static files…"
./manage.py collectstatic --noinput

echo "Start dev server…"
./manage.py runserver 0.0.0.0:8000 --force-color
