# 🚀 Instrucciones para Subir Mercalma a PythonAnywhere

## Datos de tu Cuenta
```
Usuario: Pudindechocolate
Contraseña: 8Avmr8DiDUQ9zsh
URL Final: https://Pudindechocolate.pythonanywhere.com
```

---

## PASO 1: Acceder a PythonAnywhere
1. Ve a https://www.pythonanywhere.com
2. Inicia sesión con tu usuario y contraseña
3. Ve al panel de control
2
---

## PASO 2: Subir tu Proyecto (Elige una opción)

### 🔧 OPCIÓN A: Usando Git (Recomendado)
Si tu proyecto está en GitHub:

1. Abre una **Bash console** en PythonAnywhere:
   ```bash
   cd /home/Pudindechocolate
   git clone https://github.com/TU_USUARIO/TU_REPOSITORIO.git mercalma
   cd mercalma
   ```

2. Si el proyecto NO está en Git, sube los archivos manualmente o copialos con SCP.

### 📁 OPCIÓN B: Subida Manual
1. En PythonAnywhere, ve a **Files**
2. Sube el archivo `mercalma.zip` que tienes
3. Descomprime en `/home/Pudindechocolate/mercalma`

---

## PASO 3: Crear Entorno Virtual

En la consola de PythonAnywhere:

```bash
mkvirtualenv --python=/usr/bin/python3.11 mercalma_env
pip install --upgrade pip
pip install -r /home/Pudindechocolate/mercalma/requirements.txt
```

**Esto tardará 3-5 minutos...**

---

## PASO 4: Configurar Variables de Entorno

### A) Copiar archivo de configuración
```bash
cp /home/Pudindechocolate/mercalma/.env.pythonanywhere \
   /home/Pudindechocolate/mercalma/mercado/.env
```

### B) Editar el archivo .env
```bash
nano /home/Pudindechocolate/mercalma/mercado/.env
```

**Edita estos valores:**
```
SECRET_KEY=generar-una-clave-aleatoria-aqui
DATABASE_URL=postgres://Pudindechocolate:8Avmr8DiDUQ9zsh@Pudindechocolate.postgres.pythonanywhere-services.com/Pudindechocolate$mercalma
EMAIL_HOST_USER=tu-email@gmail.com
EMAIL_HOST_PASSWORD=tu-contraseña-de-app
```

Para generar SECRET_KEY abre otra consola y ejecuta:
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Luego presiona Ctrl+O para guardar, Enter, y Ctrl+X para salir de nano.

---

## PASO 5: Crear Base de Datos PostgreSQL

1. Ve a **Databases** en PythonAnywhere
2. Haz click en **"Create a new database"**
3. Selecciona **PostgreSQL**
4. Nombre: `Pudindechocolate$mercalma`
5. Anota la contraseña que se genera

---

## PASO 6: Ejecutar Migraciones

```bash
cd /home/Pudindechocolate/mercalma/mercado
workon mercalma_env
python manage.py migrate
```

Crea un superusuario:
```bash
python manage.py createsuperuser
```

Sigue los pasos interactivos.

---

## PASO 7: Recopilar Archivos Estáticos

```bash
python manage.py collectstatic --noinput
```

---

## PASO 8: Crear la Web App

1. Ve a **Web** en PythonAnywhere
2. Click en **"Add a new web app"**
3. Selecciona **Manual configuration**
4. Selecciona **Python 3.11**

---

## PASO 9: Configurar el WSGI

En la página de Web (después de crear la app):

1. Click en **"WSGI configuration file"** (es el archivo `/var/www/...`)
2. Reemplaza TODO el contenido con esto:

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

3. Guarda (Ctrl+S)

---

## PASO 10: Configurar Archivos Estáticos

En **Web** → **Static files:**

Agrega 2 líneas:

| URL      | Directory                                            |
|----------|------------------------------------------------------|
| /static/ | /home/Pudindechocolate/mercalma/mercado/staticfiles |
| /media/  | /home/Pudindechocolate/mercalma/mercado/media       |

---

## PASO 11: Configurar el Virtualenv

En **Web** → **Virtualenv:**

```
/home/Pudindechocolate/.virtualenvs/mercalma_env
```

---

## PASO 12: Recargar la Aplicación

1. Vuelve a la página principal de **Web**
2. Busca el botón verde **"Reload"**
3. Haz click

**¡Espera 10-30 segundos!**

---

## ✅ Verificar que Funciona

1. Ve a: https://Pudindechocolate.pythonanywhere.com
2. Si ves tu aplicación Django: **¡Éxito!** 🎉
3. Admin: https://Pudindechocolate.pythonanywhere.com/admin/

---

## 🐛 Si Hay Errores

### Ver logs:
En **Web** → **Log files**
- **error_log.log** - Errores del servidor
- **access_log.log** - Historial de accesos

### Errores Comunes:

**"ModuleNotFoundError: No module named..."**
- Reinstala: `pip install -r requirements.txt`
- Recarga la web app

**"Database connection refused"**
- Verifica DATABASE_URL en .env
- Verifica que la BD PostgreSQL existe

**"Static files not found (404)"**
- Ejecuta: `python manage.py collectstatic --noinput`
- Verifica rutas en Static files config

**"Permission denied"**
- Verifica permisos: `chmod -R 755 /home/Pudindechocolate/mercalma`

---

## 📝 Archivos Incluidos

He preparado estos archivos para ti:

1. **`.env.pythonanywhere`** - Plantilla de variables (ya configurada)
2. **`pythonanywhere_wsgi.py`** - Configuración WSGI correcta
3. **`pythonanywhere_setup.sh`** - Script automático (opcional)
4. **Este archivo** - Guía paso a paso

---

## 🔒 Seguridad

**⚠️ IMPORTANTE:**
- Cambia `SECRET_KEY` por uno aleatorio
- No subas el archivo `.env` a Git (agrega a `.gitignore`)
- Cambia credenciales de email en producción
- En PythonAnywhere, DEBUG siempre debe ser `False`

---

## 📧 Contacto Soporte

Si tienes problemas:
1. Revisa los logs en PythonAnywhere
2. Verifica que la BD PostgreSQL existe
3. Asegúrate de que el virtualenv está activado
4. Intenta recargar la web app (botón verde)

**¡Buena suerte! 🚀**
