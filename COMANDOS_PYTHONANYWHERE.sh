#!/bin/bash
# Comandos útiles para PythonAnywhere
# Copia y pega cada sección en la consola Bash de PythonAnywhere

echo "=== COMANDOS ÚTILES PARA PYTHONANYWHERE ==="
echo ""

# ==========================================
# SETUP INICIAL
# ==========================================
echo "📋 SETUP INICIAL"
echo "=========================================="
echo "# Crear entorno virtual"
echo "mkvirtualenv --python=/usr/bin/python3.11 mercalma_env"
echo ""
echo "# Instalar dependencias"
echo "pip install -r /home/Pudindechocolate/mercalma/requirements.txt"
echo ""
echo "# Activar entorno"
echo "workon mercalma_env"
echo ""

# ==========================================
# MIGRACIONES Y DATOS
# ==========================================
echo "🗄️ MIGRACIONES Y BASE DE DATOS"
echo "=========================================="
echo "# Ejecutar migraciones"
echo "cd /home/Pudindechocolate/mercalma/mercado"
echo "python manage.py migrate"
echo ""
echo "# Crear superusuario"
echo "python manage.py createsuperuser"
echo ""
echo "# Ver usuarios"
echo "python manage.py shell"
echo ">>> from django.contrib.auth.models import User"
echo ">>> User.objects.all()"
echo ">>> exit()"
echo ""

# ==========================================
# ARCHIVOS ESTÁTICOS
# ==========================================
echo "📁 ARCHIVOS ESTÁTICOS"
echo "=========================================="
echo "# Recopilar static files"
echo "python manage.py collectstatic --noinput"
echo ""
echo "# Limpiar y recopilar"
echo "python manage.py collectstatic --clear --noinput"
echo ""

# ==========================================
# LOGS Y DEPURACIÓN
# ==========================================
echo "🔍 LOGS Y DEPURACIÓN"
echo "=========================================="
echo "# Ver logs de error (última línea)"
echo "tail -f /var/log/Pudindechocolate.pythonanywhere.com.error.log"
echo ""
echo "# Ver logs de acceso"
echo "tail -f /var/log/Pudindechocolate.pythonanywhere.com.access.log"
echo ""
echo "# Ver logs de la web app"
echo "tail -f /home/Pudindechocolate/.pythonanywhere-logs/Pudindechocolate.pythonanywhere.com.error.log"
echo ""

# ==========================================
# VARIABLES DE ENTORNO
# ==========================================
echo "🔐 VARIABLES DE ENTORNO"
echo "=========================================="
echo "# Crear/editar archivo .env"
echo "nano /home/Pudindechocolate/mercalma/mercado/.env"
echo ""
echo "# Ver contenido del .env"
echo "cat /home/Pudindechocolate/mercalma/mercado/.env"
echo ""
echo "# Generar nueva SECRET_KEY"
echo "python -c \"from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())\""
echo ""

# ==========================================
# GESTIÓN DE ARCHIVOS
# ==========================================
echo "📂 GESTIÓN DE ARCHIVOS"
echo "=========================================="
echo "# Cambiar permisos"
echo "chmod -R 755 /home/Pudindechocolate/mercalma"
echo ""
echo "# Ver tamaño de carpetas"
echo "du -sh /home/Pudindechocolate/mercalma/*"
echo ""
echo "# Listar archivos grandes"
echo "find /home/Pudindechocolate/mercalma -type f -size +10M"
echo ""

# ==========================================
# GIT
# ==========================================
echo "🔄 GIT - ACTUALIZAR CÓDIGO"
echo "=========================================="
echo "# Clonar repositorio"
echo "cd /home/Pudindechocolate"
echo "git clone https://github.com/TU_USUARIO/TU_REPO.git mercalma"
echo ""
echo "# Actualizar código (pull)"
echo "cd /home/Pudindechocolate/mercalma"
echo "git pull origin main"
echo ""
echo "# Ver estado"
echo "git status"
echo ""

# ==========================================
# SHELL DE DJANGO
# ==========================================
echo "🐍 SHELL DE DJANGO"
echo "=========================================="
echo "# Abrir shell"
echo "python manage.py shell"
echo ""
echo "# Dentro del shell:"
echo ">>> from django.contrib.auth.models import User"
echo ">>> u = User.objects.first()"
echo ">>> u.email = 'newemail@example.com'"
echo ">>> u.save()"
echo ">>> exit()"
echo ""

# ==========================================
# MANTENIMIENTO
# ==========================================
echo "🔧 MANTENIMIENTO"
echo "=========================================="
echo "# Limpiar cache"
echo "python manage.py clear_cache"
echo ""
echo "# Hacer backup de BD"
echo "# (Usar interfaz de PythonAnywhere)"
echo ""
echo "# Ver configuración de Django"
echo "python manage.py diffsettings"
echo ""

# ==========================================
# RECARGAR APLICACIÓN
# ==========================================
echo "🚀 RECARGAR APLICACIÓN"
echo "=========================================="
echo "# Presionar botón Reload en Web Apps"
echo "# O desde consola:"
echo "touch /var/www/Pudindechocolate_pythonanywhere_com_wsgi.py"
echo ""

# ==========================================
# UTILIDADES
# ==========================================
echo "🛠️ UTILIDADES"
echo "=========================================="
echo "# Ver versión de Python"
echo "python --version"
echo ""
echo "# Ver paquetes instalados"
echo "pip list"
echo ""
echo "# Ver información del virtualenv"
echo "which python"
echo ""
echo "# Probar conexión a BD"
echo "python manage.py dbshell"
echo ""

echo ""
echo "=== FIN DE COMANDOS ÚTILES ==="
