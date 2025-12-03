"""
Main WSGI app for Render deployment.
Imports the actual WSGI app from mercado.config module.
Named 'app.py' with 'app' variable to match Render's default expectations (gunicorn app:app).
"""
import os
import sys

# Asegura que mercado esté en el path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'mercado'))

# Importa la aplicación WSGI de Django
from config.wsgi import application

# Exporta como 'app' que es lo que Render busca por defecto
app = application

if __name__ == "__main__":
    try:
        from waitress import serve
        serve(application, host='0.0.0.0', port=int(os.environ.get('PORT', 8000)))
    except ImportError:
        import gunicorn.app.wsgiapp
        gunicorn.app.wsgiapp.run()
