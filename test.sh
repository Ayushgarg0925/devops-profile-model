#!/bin/bash

echo "Testing API..."

curl -X GET http://localhost:8000/

echo ""
echo "Generating text..."

# curl -X POST http://localhost:8000/generate \
# -H "Content-Type: application/json" \
# -d '{"prompt":"Hello DevOps"}'
curl -X 'POST' \
  'http://localhost:8000/generate' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "prompt": "Hello DevOps"
}'

echo ""