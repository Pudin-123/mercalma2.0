# Guía para agentes AI en MERCALMA

## Visión general
MERCALMA es un marketplace construido con Django y Django REST Framework, con una arquitectura modular orientada a la claridad y la colaboración. El frontend sugerido es React, pero el backend es el núcleo del repositorio.

## Estructura principal
- `core/`, `market/`, `categorias/`, `perfil/`, `presupuestos/`, `quotes/`, `simple_chat/`, `presence/`: apps Django separadas, cada una con modelos, vistas, urls y migraciones propias.
- `config/`: configuración global del proyecto Django (settings, urls, wsgi/asgi).
- `backend_utils/`: utilidades y comandos de gestión personalizados.
- `media/`, `static/`, `templates/`: recursos estáticos y plantillas globales.

## Flujos de desarrollo
- **Migraciones:**
  - `python manage.py makemigrations`
  - `python manage.py migrate`
- **Servidor local:**
  - `python manage.py runserver`
- **Entorno virtual:**
  - Windows: `.venv\Scripts\activate`
  - Linux/Mac: `source env/bin/activate`
- **Dependencias:**
  - `pip install -r requirements.txt`

## Convenciones y patrones
- Cada app Django sigue la estructura estándar: `models.py`, `views.py`, `urls.py`, `admin.py`, `tests.py`, `migrations/`.
- Las utilidades y comandos personalizados se ubican en `backend_utils/management/commands/`.
- Las plantillas HTML se agrupan en `templates/<app>/`.
- Los archivos estáticos se organizan en `static/` y `staticfiles/`.
- La autenticación se gestiona con Django Allauth y/o JWT.
- La base de datos principal es PostgreSQL (en desarrollo puede usarse SQLite).

## Integraciones y comunicación
- El backend expone APIs RESTful desde cada app, siguiendo la convención de Django REST Framework.
- El frontend (no incluido aquí) consume estas APIs.
- El despliegue se realiza en Railway/Vercel/Docker.

## Ejemplo de flujo de trabajo
1. Crear una nueva app: `python manage.py startapp <nombre_app>`
2. Definir modelos en `<app>/models.py` y registrar en `admin.py`.
3. Crear migraciones y aplicarlas.
4. Implementar vistas y rutas en `<app>/views.py` y `<app>/urls.py`.
5. Agregar tests en `<app>/tests.py`.
6. Actualizar documentación en `/docs` y/o Trello.

## Reglas específicas
- Cada Pull Request debe incluir una descripción emocional del cambio y documentación clara.
- Los cambios visuales deben acompañarse de capturas.
- La documentación vive en `/docs` y en el tablero Trello.

## Archivos clave
- `manage.py`: punto de entrada para comandos Django.
- `config/settings.py`: configuración global.
- `requirements.txt`: dependencias Python.
- `README.md`: visión y guía rápida.

---

Para dudas sobre flujos, convenciones o integración, consulta `/docs` o el README. Colabora con intención y claridad.
