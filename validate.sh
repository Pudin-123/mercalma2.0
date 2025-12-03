#!/usr/bin/env bash
# Validation script to test WSGI import locally before Render deploy

set -e

echo "=== VALIDATION SCRIPT FOR RENDER DEPLOY ==="
echo ""
echo "1. Testing Python path setup..."
cd "$(dirname "$0")"
echo "Current directory: $(pwd)"
ls -la

echo ""
echo "2. Testing WSGI import (same as Render will do)..."
python3 -c "
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname('$PWD'), 'mercado'))
print('✓ Path setup successful')
print(f'  sys.path: {sys.path[:3]}')
"

echo ""
echo "3. Testing Django config import..."
python3 -c "
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
import django
django.setup()
print('✓ Django setup successful')
"

echo ""
echo "4. Testing WSGI app import (from root wsgi.py)..."
python3 -c "
import wsgi
print(f'✓ wsgi module imported successfully')
print(f'  wsgi.app = {wsgi.app}')
"

echo ""
echo "5. Testing gunicorn can load the app..."
python3 -c "
import sys
import os
sys.path.insert(0, os.getcwd())
from wsgi import app
print(f'✓ gunicorn can load wsgi:app')
print(f'  app type: {type(app)}')
"

echo ""
echo "=== ALL VALIDATIONS PASSED ==="
