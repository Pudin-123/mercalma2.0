import os
from django.core.wsgi import get_wsgi_application
from django.core.management import call_command

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = get_wsgi_application()

# Auto-run migrations on app startup (safe for production)
try:
    call_command('migrate', '--noinput', verbosity=0)
except Exception as e:
    print(f'Warning: Could not run migrations on startup: {e}')