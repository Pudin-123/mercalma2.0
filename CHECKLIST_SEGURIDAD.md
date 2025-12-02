# Checklist de Seguridad para Despliegue en PythonAnywhere

## Antes de subir a producción

### 🔐 Seguridad
- [ ] Cambiar `SECRET_KEY` por una clave aleatoria y segura
- [ ] Establecer `DEBUG = False` en settings.py
- [ ] Cambiar contraseñas de email (usar App Passwords de Gmail)
- [ ] Usar HTTPS (habilitado por defecto en PythonAnywhere)
- [ ] Verificar que NO hay credenciales en el código
- [ ] Agregar `.env` a `.gitignore`

### 🗄️ Base de Datos
- [ ] Crear base de datos PostgreSQL en PythonAnywhere
- [ ] Ejecutar migraciones con `python manage.py migrate`
- [ ] Crear superusuario admin
- [ ] Hacer backup de BD antes de cambios importantes

### 📁 Archivos Estáticos
- [ ] Ejecutar `python manage.py collectstatic --noinput`
- [ ] Configurar rutas correctas de /static/ y /media/
- [ ] Verificar que WhiteNoise está en MIDDLEWARE
- [ ] Probar carga de imágenes y archivos

### 🔑 Variables de Entorno
```
DEBUG=False
SECRET_KEY=generar-nueva-clave
ALLOWED_HOSTS=Pudindechocolate.pythonanywhere.com
DATABASE_URL=postgres://usuario:contraseña@servidor/base_datos
SITE_URL=https://Pudindechocolate.pythonanywhere.com
```

### 📧 Email
- [ ] Configurar SMTP de Gmail
- [ ] Generar App Password (no usar contraseña normal)
- [ ] Probar envío de emails

### 🔒 Permisos
```bash
# En PythonAnywhere:
chmod -R 755 /home/Pudindechocolate/mercalma
chmod -R 755 /home/Pudindechocolate/mercalma/mercado/media
chmod -R 755 /home/Pudindechocolate/mercalma/mercado/staticfiles
```

### 🧪 Pruebas
- [ ] Probar login/logout
- [ ] Probar registro de usuarios
- [ ] Probar formularios
- [ ] Probar carga de imágenes
- [ ] Revisar logs de error

### 📊 Monitoreo
- [ ] Revisar logs regularmente
- [ ] Configurar alertas en PythonAnywhere
- [ ] Hacer backups semanales
- [ ] Monitorear uso de CPU/RAM

---

## Después del despliegue

### 🚀 Optimizaciones
1. **Caché:**
   ```python
   CACHES = {
       'default': {
           'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
       }
   }
   ```

2. **Compresión de archivos estáticos:**
   - Ya está con `WhiteNoise`

3. **Optimizar imágenes:**
   - Redimensionar antes de subir
   - Considerar CDN para media

4. **Minificación CSS/JS:**
   - Usar herramientas de build

### 🔄 Actualización de código
```bash
cd /home/Pudindechocolate/mercalma
git pull origin main
workon mercalma_env
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput
# Recargar web app en PythonAnywhere
```

### 📈 Escalado futuro
Si crece el proyecto:
- Considerar plan de pago en PythonAnywhere
- Agregar más workers
- Usar CDN para static files
- Considerar caché Redis
- Database optimization

---

## URLs Importantes

- Panel de control: https://www.pythonanywhere.com
- Mi cuenta: https://www.pythonanywhere.com/user/Pudindechocolate/
- Web apps: https://www.pythonanywhere.com/user/Pudindechocolate/webapps/
- Bases de datos: https://www.pythonanywhere.com/user/Pudindechocolate/databases/
- Consola: https://www.pythonanywhere.com/user/Pudindechocolate/consoles/

---

## Contactos de Soporte

- **PythonAnywhere Support:** https://www.pythonanywhere.com/help/
- **Django Docs:** https://docs.djangoproject.com/
- **PostgreSQL Docs:** https://www.postgresql.org/docs/

---

**Nota:** Revisa esta lista después de cada despliegue para asegurar mejor práctica y seguridad.
