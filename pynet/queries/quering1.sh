#!/bin/bash

SQL_FILE="queries.sql"

psql -U "$DB_USER" -d "$DB_NAME" -p "$DB_PORT" -f "$SQL_FILE"
