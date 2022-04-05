#!/bin/sh
curl --location --request POST 'http://127.0.0.1:8000/players/' --header 'Content-Type: application/json' --data-raw '{
    "id": "3",
    "name": "axvd",
    "position": "Midfielder",
    "odds": 0.5,
    "margin": 0.1
}'