#!/usr/bin/env bash
# exit on error
set -o errexit

echo "======================================"
echo "📦 Installing dependencies..."
echo "======================================"

# Upgrade pip
pip install --upgrade pip

# Install wheel for better package building
pip install wheel

# Install dependencies
pip install -r requirements.txt

echo "======================================"
echo "🔧 Building Django project..."
echo "======================================"

# Navigate to Django project directory
cd mercado

# Run migrations
echo "Running database migrations..."
python manage.py autofix_db

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --no-input

echo "======================================"
echo "✅ Build completed successfully!"
echo "======================================"
