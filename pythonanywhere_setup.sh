#!/bin/bash
# Script de configuración para PythonAnywhere
# Ejecutar con: bash pythonanywhere_setup.sh

echo "=== Configurando proyecto Mercalma en PythonAnywhere ==="

# 1. Crear directorio del proyecto
echo "1. Verificando directorio del proyecto..."
cd /home/Pudindechocolate

# 2. Si no existe el proyecto, clonarlo (ajusta la URL de tu repo)
# git clone https://github.com/tuusuario/mercalma.git
# cd mercalma

# 3. Crear y activar entorno virtual
echo "2. Creando entorno virtual..."
mkvirtualenv --python=/usr/bin/python3.11 mercalma_env

# 4. Instalar dependencias
echo "3. Instalando dependencias..."
pip install -r requirements.txt

# 5. Crear archivo .env con configuración de PythonAnywhere
echo "4. Configurando variables de entorno..."
cp .env.pythonanywhere .env

# 6. Crear directorio para archivos estáticos y media
echo "5. Creando directorios..."
mkdir -p mercado/staticfiles
mkdir -p mercado/media

# 7. Migrar base de datos
echo "6. Ejecutando migraciones..."
cd mercado
python manage.py migrate

# 8. Crear superusuario (cambiar credenciales)
echo "7. Creando superusuario..."
python manage.py createsuperuser --no-input --username admin --email admin@example.com

# 9. Recopilar archivos estáticos
echo "8. Recopilando archivos estáticos..."
python manage.py collectstatic --noinput

echo ""
echo "=== ¡Configuración completada! ==="
echo ""
echo "Próximos pasos:"
echo "1. Ve a https://www.pythonanywhere.com/user/Pudindechocolate/webapps/"
echo "2. Crea una nueva Web App"
echo "3. Selecciona 'Manual configuration'"
echo "4. Elige Python 3.11"
echo "5. Configura el WSGI file con los detalles del repositorio"
echo ""
