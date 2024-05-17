#!/bin/bash

# Collect static files
echo "Collect static files"
python3.9 manage.py collectstatic --noinput

# Migrate database
echo "Apply database migrations"
python3.9 manage.py migrate
