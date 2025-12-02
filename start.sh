#!/usr/bin/env bash
set -e

echo "Starting Mercalma on Render..."
echo "Current directory: $(pwd)"
echo "Listing mercado directory:"
ls -la mercado/

cd mercado
echo "Changed to mercado directory: $(pwd)"

echo "Python version:"
python --version

echo "Attempting to import config.wsgi..."
python -c "from config.wsgi import application; print('SUCCESS: config.wsgi imported')" || exit 1

echo "Starting gunicorn..."
gunicorn config.wsgi:application --bind 0.0.0.0:$PORT --workers 2 --timeout 30
