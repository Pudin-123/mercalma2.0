#!/bin/bash
# Script para ejecutar en PythonAnywhere (BASH) dentro de tu cuenta
# Ajusta USERNAME y PROJECT_DIR según tu instalación si es necesario.

# CONFIG
USERNAME="Pudindechocolate"    # Cambia por tu usuario en PythonAnywhere si hace falta
PROJECT_DIR="/home/$USERNAME/mercalma2.0/mercado"
VENV_DIR="/home/$USERNAME/venv-mercalma"

set -e
echo "Usando proyecto: $PROJECT_DIR"

cd "$PROJECT_DIR"

echo "Comprobando encoding de requirements.txt..."
if command -v file >/dev/null 2>&1; then
  file -i requirements.txt || true
fi

# Intentar convertir a UTF-8 si detecta UTF-16 (no hace cambios si ya es utf-8)
python - <<'PY'
import sys
p = 'requirements.txt'
raw = open(p,'rb').read()
for enc in ('utf-8','utf-16','utf-16le','utf-16be'):
    try:
        s = raw.decode(enc)
        open(p,'w',encoding='utf-8').write(s)
        print('Converted requirements.txt from', enc)
        break
    except Exception:
        pass
PY

echo "Creando/activando virtualenv: $VENV_DIR"
python3.11 -m venv "$VENV_DIR" || true
source "$VENV_DIR/bin/activate"
pip install --upgrade pip

echo "Instalando dependencias desde requirements.txt"
pip install -r requirements.txt

echo "Instalando dj-database-url por si falta"
pip install dj-database-url || true

echo "Ejecutando migraciones"
python manage.py migrate --noinput

echo "Collectstatic"
python manage.py collectstatic --noinput

echo "Crea superusuario interactivo ahora (opcional)"
echo "Ejecuta: python manage.py createsuperuser"

echo "Listo. Recarga la app desde la pestaña Web de PythonAnywhere."
