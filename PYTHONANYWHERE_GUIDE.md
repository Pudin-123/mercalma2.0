# Guía de Despliegue en PythonAnywhere

## Información de tu cuenta
- **Usuario:** Pudindechocolate
- **Contraseña:** 8Avmr8DiDUQ9zsh
- **URL:** https://Pudindechocolate.pythonanywhere.com

## Pasos de Despliegue

### 1. Acceder a PythonAnywhere
1. Ve a https://www.pythonanywhere.com
2. Inicia sesión con usuario: `Pudindechocolate`
3. Contraseña: `8Avmr8DiDUQ9zsh`

### 2. Subir el proyecto

**Opción A: Usando Git (Recomendado)**
```bash
# En la consola de PythonAnywhere
cd /home/Pudindechocolate
git clone https://github.com/tuusuario/tu-repo.git mercalma
cd mercalma/mercado
```

**Opción B: Manualmente**
- Descarga tu proyecto como ZIP
- En PythonAnywhere, usa File editor para subir archivos

### 3. Crear entorno virtual
```bash
# En consola de PythonAnywhere
mkvirtualenv --python=/usr/bin/python3.11 mercalma_env
pip install -r /home/Pudindechocolate/mercalma/requirements.txt
```

### 4. Configurar variables de entorno
```bash
# Copiar el archivo de configuración
cp /home/Pudindechocolate/mercalma/.env.pythonanywhere /home/Pudindechocolate/mercalma/mercado/.env

# Editar y completar credenciales
nano /home/Pudindechocolate/mercalma/mercado/.env
```

**Variables importantes a configurar:**
```
SECRET_KEY=algo-muy-secreto
DATABASE_URL=postgres://Pudindechocolate:PASSWORD@Pudindechocolate.postgres.pythonanywhere-services.com/Pudindechocolate$mercalma
EMAIL_HOST_USER=tu_email@gmail.com
EMAIL_HOST_PASSWORD=tu_app_password
```

### 5. Configurar la base de datos

**Crear base de datos PostgreSQL:**
1. Ve a https://www.pythonanywhere.com/user/Pudindechocolate/databases/
2. Crea una nueva base de datos PostgreSQL
3. Nombre: `Pudindechocolate$mercalma`

**Ejecutar migraciones:**
```bash
cd /home/Pudindechocolate/mercalma/mercado
workon mercalma_env
python manage.py migrate
python manage.py createsuperuser
python manage.py collectstatic --noinput
```

### 6. Configurar Web App

**En PythonAnywhere Web Panel:**
1. Ve a **Web** → **Add a new web app**
2. Selecciona **Manual configuration** (no framework)
3. Elige **Python 3.11**

### 7. Configurar WSGI

En **Web** → **WSGI configuration file**, reemplaza el contenido con:

```python
import os
import sys
from pathlib import Path

path = '/home/Pudindechocolate/mercalma'
if path not in sys.path:
    sys.path.insert(0, path)

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

### 8. Configurar Archivos Estáticos

En **Web** → **Static files:**

| URL              | Directory                                          |
|------------------|----------------------------------------------------|
| /static/         | /home/Pudindechocolate/mercalma/mercado/staticfiles/ |
| /media/          | /home/Pudindechocolate/mercalma/mercado/media/    |

### 9. Configurar Virtualenv

En **Web** → **Virtualenv:**
```
/home/Pudindechocolate/.virtualenvs/mercalma_env
```

### 10. Recargar la aplicación

Haz click en el botón **Reload** (verde) en la página de Web Apps.

## Verificación

1. Ve a https://Pudindechocolate.pythonanywhere.com
2. Deberías ver tu aplicación Django funcionando
3. Accede al admin en https://Pudindechocolate.pythonanywhere.com/admin/

## Troubleshooting

**Error: ModuleNotFoundError**
- Verifica que el virtualenv esté correctamente apuntado
- Reinstala los requirements

**Error: Database connection**
- Verifica la URL de la base de datos en .env
- Asegúrate de que la base de datos existe

**Error: Static files no cargan**
- Ejecuta `python manage.py collectstatic --noinput`
- Verifica las rutas en Static files configuration

**Error 500 en logs**
- Ve a **Web** → **Log files**
- Revisa error_log.log para detalles

## Archivos de configuración incluidos

1. **`.env.pythonanywhere`** - Plantilla de configuración
2. **`pythonanywhere_setup.sh`** - Script automático
3. **`pythonanywhere_wsgi.py`** - Configuración WSGI correcta

## Próximas optimizaciones

- [ ] Configurar CDN para static files
- [ ] Agregar dominio personalizado
- [ ] Configurar SSL/HTTPS
- [ ] Backup automático de BD
- [ ] Monitoring y alertas

¡Éxito con tu despliegue! 🚀
