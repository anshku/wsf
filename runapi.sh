#!/bin/sh
source venv/bin/activate
python3 manage.py runserver &
cd frontend
npm run serve