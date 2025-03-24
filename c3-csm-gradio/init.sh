#!/bin/bash
set -ex

python app.py &
APP_PID=$!

sleep 15

curl -X POST "http://localhost:7860/gradio_api/call/generate_conversation_audio" \
  -H "Content-Type: application/json" \
  -d '{
    "data": [
      null,
      "conversational_a", "Hello from speaker 0", null,
      "conversational_b", "Hello from speaker 1", null,
      "random_voice", "Hello from random speaker 2", null,
      "random_voice", "", null,
      "random_voice", "", null,
      "random_voice", "", null,
      "random_voice", "", null,
      "random_voice", "", null,
      "random_voice", "", null,
      "random_voice", "", null,
      0, 
      "[]", 
      0.7, 
      5, 
      1000
    ]
  }'

sleep 1200
kill $APP_PID
wait $APP_PID || true