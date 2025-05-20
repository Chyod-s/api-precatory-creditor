#!/bin/bash
set -e

echo "Aguardando o Postgres ficar disponível..."

while ! nc -z postgres 5432; do
  sleep 1
done

echo "Banco de dados está pronto!"

# alembic revision --autogenerate -m "init migrations"
cd /app

alembic -c alembic.ini upgrade head

exec python -m src.api_main.main
