#!/bin/bash
# Load testing script to simulate traffic and trigger SLO burn

APP_URL=${1:-"http://localhost:8000"}
REQUESTS=${2:-100}

echo "Sending $REQUESTS requests to $APP_URL"

for i in $(seq 1 $REQUESTS); do
  curl -s "$APP_URL/api/data" > /dev/null
  curl -s "$APP_URL/health" > /dev/null
  curl -s "$APP_URL/api/error" > /dev/null
  sleep 0.1
done

echo "Done. Check Prometheus for metrics."