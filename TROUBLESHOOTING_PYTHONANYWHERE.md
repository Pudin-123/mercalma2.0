# 🐛 Troubleshooting Guide - PythonAnywhere

## Errores Comunes y Soluciones

---

## 1. ❌ "ModuleNotFoundError: No module named 'django'"

### Síntomas:
- Error 500 en la web
- Log dice: `ModuleNotFoundError: No module named 'django'`

### Causas:
- Virtualenv no instaló paquetes
- Ruta de virtualenv incorrecta

### Solución:

**a) Reinstalar paquetes:**
```bash
workon mercalma_env
pip install --upgrade pip
pip install -r /home/Pudindechocolate/mercalma/requirements.txt
```

**b) Verificar virtualenv en Web:**
- Ve a Web → Virtualenv
- Debe ser: `/home/Pudindechocolate/.virtualenvs/mercalma_env`
- Click en Reload

**c) Si sigue sin funcionar:**
```bash
rmvirtualenv mercalma_env
mkvirtualenv --python=/usr/bin/python3.11 mercalma_env
pip install -r requirements.txt
```

---

## 2. ❌ "database connection refused"

### Síntomas:
- Error 500
- Log: `psycopg2.OperationalError: could not connect to server`

### Causas:
- DATABASE_URL incorrecto en .env
- BD PostgreSQL no existe
- Contraseña incorrecta

### Solución:

**a) Verificar DATABASE_URL:**
```bash
cat /home/Pudindechocolate/mercalma/mercado/.env | grep DATABASE_URL
```

Debe ser algo como:
```
postgres://Pudindechocolate:PASSWORD@Pudindechocolate.postgres.pythonanywhere-services.com/Pudindechocolate$mercalma
```

**b) Verificar que BD existe:**
- Ve a Databases en PythonAnywhere
- Verifica que existe: `Pudindechocolate$mercalma`

**c) Probar conexión:**
```bash
cd /home/Pudindechocolate/mercalma/mercado
python manage.py dbshell
```

Si funciona, debería abrir prompt de PostgreSQL.

---

## 3. ❌ "No module named 'config'"

### Síntomas:
- Error en logs: `ModuleNotFoundError: No module named 'config'`

### Causas:
- Ruta incorrecta en sys.path del WSGI
- Carpeta mercado no está en el path

### Solución:

**Editar WSGI configuration file:**

Ve a Web → WSGI configuration file y asegúrate que dice:

```python
import os
import sys
from pathlib import Path

# Ruta correcta al proyecto
path = '/home/Pudindechocolate/mercalma'
if path not in sys.path:
    sys.path.insert(0, path)

# Ruta correcta a la carpeta mercado (donde está manage.py)
path_mercado = '/home/Pudindechocolate/mercalma/mercado'
if path_mercado not in sys.path:
    sys.path.insert(0, path_mercado)

os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings'

from pathlib import Path
from dotenv import load_dotenv

env_path = Path('/home/Pudindechocolate/mercalma/mercado/.env')
if env_path.exists():
    load_dotenv(env_path)

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

Luego haz click en Reload.

---

## 4. ❌ "Static files (404 Not Found)"

### Síntomas:
- El sitio funciona pero CSS/JS no cargan
- Imágenes muestran 404

### Causas:
- Ruta incorrecta en Static files
- `collectstatic` no fue ejecutado

### Solución:

**a) Ejecutar collectstatic:**
```bash
cd /home/Pudindechocolate/mercalma/mercado
python manage.py collectstatic --noinput
```

**b) Verificar rutas en Static files:**

Ve a Web → Static files:
- `/static/` debe apuntar a `/home/Pudindechocolate/mercalma/mercado/staticfiles`
- `/media/` debe apuntar a `/home/Pudindechocolate/mercalma/mercado/media`

**c) Verificar permisos:**
```bash
chmod -R 755 /home/Pudindechocolate/mercalma/mercado/staticfiles
chmod -R 755 /home/Pudindechocolate/mercalma/mercado/media
```

---

## 5. ❌ "OperationalError: no such table"

### Síntomas:
- Error 500
- Log: `OperationalError: no such table: auth_user`

### Causas:
- Las migraciones no fueron ejecutadas
- BD vacía

### Solución:

```bash
cd /home/Pudindechocolate/mercalma/mercado
python manage.py migrate
```

Luego haz click en Reload.

---

## 6. ❌ "SECRET_KEY is not set"

### Síntomas:
- Error: `ImproperlyConfigured: The SECRET_KEY setting must not be empty`

### Causas:
- Archivo .env no existe o no tiene SECRET_KEY
- Variable no se cargó

### Solución:

**a) Verificar .env existe:**
```bash
ls -la /home/Pudindechocolate/mercalma/mercado/.env
```

**b) Si no existe, crear:**
```bash
cp /home/Pudindechocolate/mercalma/.env.pythonanywhere \
   /home/Pudindechocolate/mercalma/mercado/.env
```

**c) Generar nueva SECRET_KEY:**
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

**d) Editar .env y pegar la clave:**
```bash
nano /home/Pudindechocolate/mercalma/mercado/.env
```

Busca `SECRET_KEY=` y reemplaza el valor.

---

## 7. ❌ "DisallowedHost" error

### Síntomas:
- Error 400
- Log: `DisallowedHost at /`

### Causas:
- El dominio no está en ALLOWED_HOSTS

### Solución:

**Editar settings.py:**
```bash
nano /home/Pudindechocolate/mercalma/mercado/config/settings.py
```

Busca ALLOWED_HOSTS y asegúrate que tenga:
```python
ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
    '.onrender.com',
    '.pythonanywhere.com',
    'Pudindechocolate.pythonanywhere.com'
]
```

Luego recarga la app.

---

## 8. ❌ "Permission denied"

### Síntomas:
- Log: `Permission denied`
- No puede escribir archivos

### Causas:
- Permisos de carpeta incorrectos

### Solución:

```bash
# Cambiar permisos
chmod -R 755 /home/Pudindechocolate/mercalma
chmod -R 755 /home/Pudindechocolate/mercalma/mercado/media
chmod -R 755 /home/Pudindechocolate/mercalma/mercado/staticfiles

# Cambiar propietario si es necesario
chown -R Pudindechocolate:Pudindechocolate /home/Pudindechocolate/mercalma
```

---

## 9. ❌ "CSRF verification failed"

### Síntomas:
- Error 403 al enviar formularios
- Log: `CSRF verification failed`

### Causas:
- DEBUG=True en producción
- CSRF_TRUSTED_ORIGINS no configurado

### Solución:

**a) Asegurar DEBUG=False:**
```bash
nano /home/Pudindechocolate/mercalma/mercado/.env
```
Cambiar a: `DEBUG=False`

**b) Agregar dominio a settings.py:**
```python
CSRF_TRUSTED_ORIGINS = [
    'https://Pudindechocolate.pythonanywhere.com',
]
```

---

## 10. ❌ "EMAIL: Connection refused"

### Síntomas:
- Error al enviar emails
- Log: `Connection refused`

### Causas:
- Credenciales de email incorrectas
- Contraseña vs App Password

### Solución:

**Si usas Gmail:**
1. Ve a https://myaccount.google.com/security
2. Busca "Contraseñas de aplicación"
3. Copia la contraseña generada
4. En .env, usa: `EMAIL_HOST_PASSWORD=la-contraseña-de-app`

**Prueba:**
```bash
python manage.py shell
>>> from django.core.mail import send_mail
>>> send_mail('Test', 'Message', 'from@gmail.com', ['to@example.com'])
```

---

## 11. ❌ "Timeout" en requests largos

### Síntomas:
- Error 504 Gateway Timeout
- Procesos que tardan mucho

### Causas:
- Operaciones muy lentas
- Límite de tiempo de PythonAnywhere

### Solución:

1. Optimiza el código (mejor query, caching)
2. Usa Celery para tareas en background
3. Aumenta plan en PythonAnywhere
4. Considera usar periodic tasks

---

## 12. ❌ "Error while unloading application"

### Síntomas:
- Error al recargar
- Aplicación no responde

### Causas:
- Código con errores de sintaxis
- Imports incorrectos

### Solución:

**a) Verificar sintaxis:**
```bash
cd /home/Pudindechocolate/mercalma/mercado
python manage.py check
```

**b) Ver errores completos:**
```bash
python manage.py runserver 0.0.0.0:8000
```

(Para testing local en PythonAnywhere, aunque no es ideal)

---

## 🔍 Cómo Revisar Logs

### En PythonAnywhere:
1. Ve a **Web**
2. Click en tu app
3. Scroll hasta **Log files**
4. Click en **error_log.log**

### En consola:
```bash
# Ver últimas líneas
tail -f /var/log/Pudindechocolate.pythonanywhere.com.error.log

# Ver últimas 50 líneas
tail -50 /var/log/Pudindechocolate.pythonanywhere.com.error.log

# Buscar palabra clave
grep "ERROR" /var/log/Pudindechocolate.pythonanywhere.com.error.log
```

---

## 🔧 Checklist de Debug

- [ ] Verificar logs en Web → Log files
- [ ] Verificar virtualenv está correctamente asignado
- [ ] Verificar que requirements.txt fue instalado
- [ ] Verificar .env existe con SECRET_KEY
- [ ] Verificar DATABASE_URL es correcto
- [ ] Verificar BD PostgreSQL existe
- [ ] Ejecutar: `python manage.py check`
- [ ] Ejecutar: `python manage.py migrate`
- [ ] Hacer: `python manage.py collectstatic --noinput`
- [ ] Hacer: Reload (botón verde)
- [ ] Revisar logs de nuevo

---

## 🆘 Si Nada Funciona

1. **Elimina todo y empieza de nuevo:**
```bash
cd /home/Pudindechocolate
rm -rf mercalma
git clone TU_REPO mercalma
cd mercalma
# Sigue los pasos del DESPLIEGUE_PYTHONANYWHERE.md
```

2. **Contacta soporte:**
   - PythonAnywhere Help: https://www.pythonanywhere.com/help/
   - Django Docs: https://docs.djangoproject.com/

3. **Busca en Google:** Copia el mensaje de error completo

---

**Nota:** Guarda este archivo para futuras referencias! 📚
