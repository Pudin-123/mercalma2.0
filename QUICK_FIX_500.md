# ⚡ SOLUCIÓN RÁPIDA - Error 500 en mercalma.onrender.com

## 🎯 CAUSA MÁS PROBABLE:

La variable de entorno **DATABASE_URL** no está configurada en Render.

---

## ✅ SOLUCIÓN INMEDIATA:

### PASO 1: Crear Base de Datos PostgreSQL

1. Ve a https://dashboard.render.com
2. Click en **"New +"** en la parte superior
3. Selecciona **"PostgreSQL"**
4. Configura:
   ```
   Name: mercalma-db
   Database: mercalma
   User: mercalma
   Region: Same as your web service (Oregon, etc.)
   PostgreSQL Version: 16
   Plan: Free
   ```
5. Click en **"Create Database"**
6. Espera 1-2 minutos a que se cree

### PASO 2: Copiar la Database URL

1. Una vez creada la base de datos, estarás en su página
2. Busca la sección **"Connections"**
3. Copia el valor de **"Internal Database URL"**
   - Debería verse así: `postgresql://mercalma:xxxxx@dpg-xxxxx-a/mercalma`
   - ⚠️ **USA "Internal Database URL", NO "External Database URL"**

### PASO 3: Configurar DATABASE_URL en el Web Service

1. Ve a tu **Web Service** (mercalma)
2. Click en **"Environment"** en el menú lateral
3. Click en **"Add Environment Variable"**
4. Agrega:
   ```
   Key: DATABASE_URL
   Value: [pega la Internal Database URL que copiaste]
   ```
5. Click en **"Save Changes"**

### PASO 4: Esperar el Redeploy

Render reiniciará automáticamente tu aplicación.
Esto tomará 2-3 minutos.

---

## 📋 VERIFICAR OTRAS VARIABLES DE ENTORNO

Mientras esperas, asegúrate de tener TODAS estas variables configuradas:

### Variables OBLIGATORIAS:

```
✓ SECRET_KEY = [tu clave del archivo SECRET_KEYS_FOR_RENDER.txt]
✓ DEBUG = False
✓ DATABASE_URL = [Internal Database URL de PostgreSQL]
```

### Variables Opcionales (según tu app):

```
ALLOWED_HOSTS = .onrender.com (opcional, ya está en settings.py)
SITE_URL = https://mercalma.onrender.com
MERCADOPAGO_ACCESS_TOKEN = [tu token]
MERCADOPAGO_PUBLIC_KEY = [tu clave]
EMAIL_HOST_USER = [tu email]
EMAIL_HOST_PASSWORD = [tu password]
TELEGRAM_BOT_TOKEN = [tu token]
TELEGRAM_CHAT_ID = [tu chat id]
```

---

## 🔍 SI EL ERROR PERSISTE DESPUÉS DEL REDEPLOY:

### Opción 1: Ejecutar Migraciones Manualmente

1. En tu Web Service en Render
2. Click en **"Shell"** en el menú
3. Ejecuta estos comandos:
   ```bash
   cd mercado
   python manage.py migrate
   python manage.py collectstatic --no-input
   ```

### Opción 2: Habilitar DEBUG temporalmente

Para ver el error exacto:

1. En Environment Variables, cambia:
   ```
   DEBUG = True
   ```
2. Espera el redeploy
3. Recarga tu sitio en el navegador
4. Verás el error completo de Django
5. **IMPORTANTE**: Después de diagnosticar, vuelve a poner `DEBUG = False`

### Opción 3: Revisar los Logs

1. En tu Web Service, click en **"Logs"**
2. Busca líneas rojas con "ERROR" o "Exception"
3. Copia y comparte el error para ayuda específica

---

## 🎯 FLUJO COMPLETO DE CONFIGURACIÓN:

```
1. PostgreSQL Database creada ✓
   └─> Copiar "Internal Database URL"

2. Web Service → Environment Variables ✓
   ├─> SECRET_KEY = [tu clave]
   ├─> DEBUG = False
   └─> DATABASE_URL = [Internal URL]

3. Redeploy automático ✓
   └─> Esperar 2-3 minutos

4. Verificar en navegador ✓
   └─> https://mercalma.onrender.com
```

---

## 📸 DÓNDE ENCONTRAR TODO:

### Para crear PostgreSQL:
```
Dashboard Render → New + → PostgreSQL
```

### Para copiar Internal Database URL:
```
Dashboard → PostgreSQL (mercalma-db) → Connections → Internal Database URL
```

### Para agregar variables de entorno:
```
Dashboard → Web Service (mercalma) → Environment → Add Environment Variable
```

### Para ver logs:
```
Dashboard → Web Service (mercalma) → Logs
```

### Para abrir Shell:
```
Dashboard → Web Service (mercalma) → Shell
```

---

## ⏱️ TIEMPO ESTIMADO:

- Crear PostgreSQL: 2 minutos
- Configurar DATABASE_URL: 1 minuto
- Redeploy automático: 2-3 minutos
- **TOTAL: ~5-6 minutos**

---

## ✅ RESULTADO ESPERADO:

Después de configurar DATABASE_URL y esperar el redeploy:

✓ El sitio debería cargar correctamente
✓ No más Error 500
✓ Aplicación funcionando en https://mercalma.onrender.com

---

## 🆘 SI NECESITAS AYUDA:

Comparte:
1. Screenshot de tus Environment Variables (oculta los valores)
2. Los últimos logs del deploy
3. El error completo si habilitas DEBUG=True

---

**ACCIÓN INMEDIATA: Crear PostgreSQL y configurar DATABASE_URL ahora ↑**
