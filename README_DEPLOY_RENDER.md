# Despliegue en Render — MERCALMA

Este archivo contiene los pasos finales y comandos para desplegar el proyecto en Render.

---

## 1) Preparar el repo local

1. Asegúrate de que todos los cambios locales estén guardados y probados.
2. Comprueba que `render.yaml` está en la raíz del repo (ya está actualizado) y que contiene los comandos correctos (`./build.sh` y start con `$PORT`).
3. Verifica que `mercado/config/settings.py` usa variables de entorno para `SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS` (ya aplicado).

Comandos (PowerShell) para commitear y pushear a GitHub:

```powershell
cd C:\Users\PudinSensual\Desktop\Mercalma\MERCALMA
git add .
git commit -m "Preparo despliegue en Render: render.yaml, settings.py, README despliegue"
git push origin main
```

(Sustituye `main` por la rama que uses.)

---

## 2) Crear el servicio en Render (UI)

Opción A — Usar `render.yaml` (recomendado):
- En Render Dashboard → New → `Web Service` → `Deploy from Git` → conecta con GitHub → selecciona tu repositorio/branch.
- Render detectará `render.yaml` y propondrá crear los servicios (web + db) especificados.

Opción B — Crear manualmente desde la UI:
- New → Web Service → Connect Repo → selecciona repo y branch.
- **Root Directory:** deja vacío (si `render.yaml` está en la raíz) o `.`
- **Build Command:** `./build.sh`
- **Start Command:** `cd mercado && gunicorn config.wsgi:application --bind 0.0.0.0:$PORT`
- **Environment:** Python 3.11 (o 3.x compatible)
- **Region** según prefieras.

---

## 3) Variables de entorno obligatorias (añadir en Environment → Environment Variables)

- `SECRET_KEY` = (valor seguro; si usas `render.yaml` puede generarlo Render)
- `DEBUG` = `False`
- `ALLOWED_HOSTS` = ejemplo: `.onrender.com,tu-servicio.onrender.com` (puedes usar CSV)
- `SITE_URL` = `https://<tu-servicio>.onrender.com`

Variables opcionales según funcionalidades usadas:
- `DATABASE_URL` (si creas DB manualmente; si usas la DB admin de Render, se crea automáticamente)
- `MERCADOPAGO_ACCESS_TOKEN`, `MERCADOPAGO_PUBLIC_KEY`
- `EMAIL_HOST_USER`, `EMAIL_HOST_PASSWORD`
- Cualquier otra credencial externa que uses.

---

## 4) Base de datos

- Si `render.yaml` incluye la sección `databases`, Render puede crear la DB y poner `DATABASE_URL` automáticamente.
- Si creas la DB en la UI, copia la `DATABASE_URL` y pégala en las Environment Variables.
- `build.sh` ejecuta `python manage.py autofix_db`; si tu comando de migración es distinto, ajusta `build.sh`.

---

## 5) Media (archivos subidos)

- El filesystem de la instancia no es persistente para uploads. Configura almacenamiento externo (S3/DigitalOcean Spaces) para `MEDIA` en producción.
- Si quieres, puedo añadir `django-storages` y la configuración en `settings.py`.

---

## 6) Comprobaciones y troubleshooting

- Si ves `ModuleNotFoundError: No module named 'app'`: asegúrate de que Start Command es `cd mercado && gunicorn config.wsgi:application --bind 0.0.0.0:$PORT` o `gunicorn mercado.config.wsgi:application --bind 0.0.0.0:$PORT`.
- Logs útiles en Render: Build Logs y Live/App Logs (Runtime)
- Si hay fallos durante `pip install`, revisa Build Logs: puede faltar una dependencia del sistema (p. ej. para `lxml` o `Pillow`).

---

## 7) Forzar redeploy / ejecutar comandos ad-hoc

- Desde la UI: Logs → Shell (Shell del Service) para ejecutar comandos manualmente `python manage.py migrate` o `python manage.py createsuperuser`.
- Opcional: instalar `render` CLI y hacer `render services update` — ver docs de Render.

---

## 8) Comandos locales para probar antes de deploy

```powershell
# Desde la raíz del repo
$env:SECRET_KEY='mi-secreto-local'
$env:DEBUG='True'
cd .\mercado
python -m pip install -r ..\requirements.txt
python manage.py collectstatic --no-input
python manage.py runserver
```

Para comprobar importación WSGI:

```powershell
# desde la raíz del repo
python -c "import importlib; importlib.import_module('mercado.config.wsgi'); print('OK')"
```

---

## 9) Qué haré si quieres que lo haga yo

Puedo:
- Crear la configuración S3 + `django-storages` y actualizar `requirements.txt`.
- Ejecutar pruebas locales (si me das permiso para ejecutar comandos en tu entorno; de lo contrario te doy los comandos).
- Revisar logs de despliegue si me pegas aquí los errores de Render.

---

Si necesitas, te guío paso a paso por la UI de Render mientras despliegas.
