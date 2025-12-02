#!/usr/bin/env python
"""
Script para preparar la configuración de PythonAnywhere
Ejecutar desde la carpeta del proyecto: python prepare_pythonanywhere.py
"""

import os
import subprocess
from pathlib import Path

def main():
    print("=" * 60)
    print("🚀 Preparando proyecto para PythonAnywhere")
    print("=" * 60)
    print()
    
    # Crear archivos necesarios
    print("✅ Verificando archivos...")
    
    files_to_check = [
        '.env.pythonanywhere',
        'pythonanywhere_wsgi.py',
        'pythonanywhere_setup.sh',
        'DESPLIEGUE_PYTHONANYWHERE.md'
    ]
    
    for file in files_to_check:
        if os.path.exists(file):
            print(f"  ✓ {file}")
        else:
            print(f"  ✗ FALTA: {file}")
    
    print()
    print("=" * 60)
    print("📋 INSTRUCCIONES FINALES")
    print("=" * 60)
    print()
    print("1. Lee el archivo: DESPLIEGUE_PYTHONANYWHERE.md")
    print()
    print("2. Datos de acceso:")
    print("   Usuario: Pudindechocolate")
    print("   Contraseña: 8Avmr8DiDUQ9zsh")
    print()
    print("3. En PythonAnywhere, en la consola ejecuta:")
    print()
    print("   cd /home/Pudindechocolate")
    print("   git clone TU_REPOSITORIO.git mercalma")
    print("   cd mercalma")
    print("   mkvirtualenv --python=/usr/bin/python3.11 mercalma_env")
    print("   pip install -r requirements.txt")
    print()
    print("4. Sigue los pasos del archivo DESPLIEGUE_PYTHONANYWHERE.md")
    print()
    print("=" * 60)
    print()

if __name__ == '__main__':
    main()
