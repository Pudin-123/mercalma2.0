"""
WSGI config para PythonAnywhere
Reemplaza el contenido del archivo WSGI que PythonAnywhere genera
en /var/www/Pudindechocolate_pythonanywhere_com_wsgi.py
"""

import os
import sys
from pathlib import Path

# Agregar el directorio del proyecto al path
path = '/home/Pudindechocolate/mercalma'
if path not in sys.path:
    sys.path.insert(0, path)

# Agregar subdirectorio mercado al path
path_mercado = '/home/Pudindechocolate/mercalma/mercado'
if path_mercado not in sys.path:
    sys.path.insert(0, path_mercado)

# Configurar variable de entorno para Django
os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings'

# Cargar variables de entorno desde .env
from pathlib import Path
from dotenv import load_dotenv

env_path = Path('/home/Pudindechocolate/mercalma/mercado/.env')
if env_path.exists():
    load_dotenv(env_path)

# Inicializar aplicación Django
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
