#!/usr/bin/env bash

if [ "$DATABASE" = "postgres" ]
then
  echo "Waiting for postgres..."

  while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 3
  done

  echo "PostgreSQL started"

fi

exec "$@"