FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN apt-get update && apt-get install -y netcat-openbsd && apt-get clean

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

COPY src/api_main/entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh