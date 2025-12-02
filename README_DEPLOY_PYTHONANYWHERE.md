**Despliegue a PythonAnywhere**

Guía rápida y comandos listos para desplegar este proyecto en PythonAnywhere.

- **Clonar el repo (ya hecho)**: asegúrate de clonar en tu directorio home, por ejemplo `~/mercalma2.0`.

- **Crear y activar virtualenv** (ajusta la versión de Python disponible en PythonAnywhere):

```bash
python3.11 -m venv ~/venv-mercalma
source ~/venv-mercalma/bin/activate
```

- **Comprobar y convertir codificación de `requirements.txt`**

Si ves caracteres extraños (`^@`) al abrir `requirements.txt` en PythonAnywhere, conviértelo a UTF-8:

```bash
cd ~/mercalma2.0/mercado
file -i requirements.txt
# si reporta utf-16 o similar, usar iconv:
iconv -f UTF-16 -t UTF-8 requirements.txt > requirements.utf8.txt && mv requirements.utf8.txt requirements.txt
# alternativa Python (si no tienes iconv):
python - <<'PY'
import sys
raw = open('requirements.txt','rb').read()
for enc in ('utf-8','utf-16','utf-16le','utf-16be'):
    try:
        s = raw.decode(enc)
        open('requirements.txt','w',encoding='utf-8').write(s)
        print('Converted from', enc)
        break
    except Exception:
        pass
PY
```

- **Instalar dependencias** (incluye `dj-database-url` que se añadió a `requirements.txt`):

```bash
source ~/venv-mercalma/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

- **Variables de entorno (recomendado)**: en la pestaña *Web → Environment variables* de PythonAnywhere añade:
  - `SECRET_KEY` = tu_clave
  - `DEBUG` = `False`
  - `SITE_URL` = `https://TU_USUARIO.pythonanywhere.com`
  - `EMAIL_HOST_USER`, `EMAIL_HOST_PASSWORD`
  - `MERCADOPAGO_ACCESS_TOKEN`, `MERCADOPAGO_PUBLIC_KEY`, etc.
  - `DATABASE_URL` (si usas DB externa)

- **Configurar WSGI**: en el archivo WSGI que proporciona PythonAnywhere, pega este snippet (sustituye `tu_usuario` y ruta si es distinto):

```python
import os
import sys

project_home = '/home/tu_usuario/mercalma2.0/mercado'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

- **Static & Media (UI de PythonAnywhere)**:
  - URL `/static/` → Path `/home/tu_usuario/mercalma2.0/mercado/staticfiles`
  - URL `/media/`  → Path `/home/tu_usuario/mercalma2.0/mercado/media`

- **Migraciones y collectstatic**:

```bash
cd ~/mercalma2.0/mercado
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py createsuperuser
```

Script de ayuda
----------------
He añadido un script `mercado/pa_setup.sh` que automatiza la conversión de `requirements.txt`, crea/activa un virtualenv, instala dependencias y ejecuta migraciones y `collectstatic`.

Para usarlo en PythonAnywhere:

```bash
cd ~/mercalma2.0/mercado
chmod +x pa_setup.sh
./pa_setup.sh
```

Después del script puedes ejecutar `python manage.py createsuperuser` para crear el admin.

- **Recargar la app**: en la pestaña *Web* pulsa *Reload*.

- **Logs**: si hay errores revisa *Error log* y *Server log* desde la UI; también puedes verlos por consola:

```bash
tail -n 200 /var/log/tu_usuario.pythonanywhere.com.error.log
tail -n 200 /var/log/tu_usuario.pythonanywhere.com.server.log
```

Notas
- No subas secretos al repositorio. Usa variables de entorno o archivos `.env` fuera del control de versiones.
- Si necesitas Postgres/MySQL considera servicios externos o un plan de pago en PythonAnywhere.

Si quieres, puedo también generar un archivo WSGI con tu nombre de usuario ya colocado — dime tu usuario de PythonAnywhere y lo preparo.
