#!/usr/bin/env bash

if [ -n "${SCALINGO_POSTGRESQL_URL}" ]; then
	db_url="${PGCONTENTS_DB_URL:-"${SCALINGO_POSTGRESQL_URL}"}"

	# Replace "postgres://" prefix with "postgresql://":
	PGCONTENTS_DB_URL="${db_url/postgres:\/\//postgresql:\/\/}"
	export PGCONTENTS_DB_URL
fi
