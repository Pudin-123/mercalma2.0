"""
Snippet WSGI para PythonAnywhere. Copia el contenido en el archivo WSGI que ofrece PythonAnywhere (UI Web -> WSGI file).
Sustituye `tu_usuario` si tu directorio/home difiere.
"""

import os
import sys

# Ajusta este path a donde clonaste el proyecto en PythonAnywhere
project_home = '/home/tu_usuario/mercalma2.0/mercado'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
