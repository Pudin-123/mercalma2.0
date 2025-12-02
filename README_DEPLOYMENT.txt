╔════════════════════════════════════════════════════════════════╗
║                  🚀 DEPLOY A PYTHONANYWHERE                     ║
║                    TODO ESTÁ LISTO PARA TI                      ║
╚════════════════════════════════════════════════════════════════╝

┌─ 👤 CREDENCIALES ─────────────────────────────────────────────┐
│                                                                 │
│  Usuario:     Pudindechocolate                                 │
│  Contraseña:  8Avmr8DiDUQ9zsh                                  │
│  URL Final:   https://Pudindechocolate.pythonanywhere.com      │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

┌─ 📚 ARCHIVOS DE CONFIGURACIÓN QUE PREPARÉ ─────────────────────┐
│                                                                 │
│  ✅ START_HERE.md                  ← EMPIEZA AQUÍ              │
│  ✅ DESPLIEGUE_PYTHONANYWHERE.md     ← GUÍA PASO A PASO        │
│  ✅ .env.pythonanywhere             ← VARIABLES DE ENTORNO     │
│  ✅ pythonanywhere_wsgi.py          ← CONFIGURACIÓN WSGI       │
│  ✅ CHECKLIST_SEGURIDAD.md          ← SEGURIDAD Y CHECKPOINTS  │
│  ✅ COMANDOS_PYTHONANYWHERE.sh      ← COMANDOS ÚTILES          │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

┌─ 🎯 PLAN DE ACCIÓN (5-10 MINUTOS) ─────────────────────────────┐
│                                                                 │
│  PASO 1: Lee START_HERE.md                                     │
│          └─> Te orienta en todo el proceso                     │
│                                                                 │
│  PASO 2: Lee DESPLIEGUE_PYTHONANYWHERE.md                      │
│          └─> Instrucciones detalladas con comandos             │
│                                                                 │
│  PASO 3: Ve a https://www.pythonanywhere.com                   │
│          └─> Inicia sesión con tus credenciales                │
│                                                                 │
│  PASO 4: Abre consola Bash                                     │
│          └─> Copia y pega los comandos del archivo             │
│                                                                 │
│  PASO 5: Configura Web App                                     │
│          └─> Sigue los pasos del archivo DESPLIEGUE            │
│                                                                 │
│  PASO 6: Recarga (botón verde)                                 │
│          └─> ¡Tu sitio estará online!                          │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

┌─ ✨ LO QUE YA HICE PARA TI ────────────────────────────────────┐
│                                                                 │
│  ✓ Actualicé config/settings.py                               │
│  ✓ Creé plantilla .env con tu usuario                          │
│  ✓ Preparé configuración WSGI correcta                         │
│  ✓ Escribí guía en español paso a paso                         │
│  ✓ Incluí checklist de seguridad                               │
│  ✓ Agregué comandos útiles listos para usar                    │
│  ✓ Configuré ALLOWED_HOSTS para PythonAnywhere                 │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

┌─ 🔧 CAMBIOS REALIZADOS EN TU PROYECTO ─────────────────────────┐
│                                                                 │
│  📝 mercado/config/settings.py:                                │
│     • Agregué .pythonanywhere.com a ALLOWED_HOSTS              │
│     • El proyecto soporta variables de entorno DATABASE_URL    │
│     • Configurado para PostgreSQL en producción                │
│                                                                 │
│  📝 requirements.txt:                                          │
│     • Actualizado a psycopg2-binary==2.9.11 (compatible)      │
│     • Todos los paquetes listos para instalar                  │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

┌─ ⚡ QUICK REFERENCE ───────────────────────────────────────────┐
│                                                                 │
│  Crear virtualenv:                                             │
│  $ mkvirtualenv --python=/usr/bin/python3.11 mercalma_env     │
│                                                                 │
│  Instalar dependencias:                                        │
│  $ pip install -r requirements.txt                             │
│                                                                 │
│  Migraciones:                                                  │
│  $ python manage.py migrate                                    │
│                                                                 │
│  Archivos estáticos:                                           │
│  $ python manage.py collectstatic --noinput                    │
│                                                                 │
│  Crear admin:                                                  │
│  $ python manage.py createsuperuser                            │
│                                                                 │
│  Ver logs:                                                     │
│  $ tail -f /var/log/error.log                                  │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

┌─ 🚨 IMPORTANTE ────────────────────────────────────────────────┐
│                                                                 │
│  ⚠️  Lee el archivo START_HERE.md primero                      │
│  ⚠️  No publiques el archivo .env en GitHub                    │
│  ⚠️  Cambia SECRET_KEY por una clave aleatoria                 │
│  ⚠️  Usa credenciales reales de email                          │
│  ⚠️  DEBUG debe ser False en producción                        │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

┌─ 📞 PROBLEMA? ─────────────────────────────────────────────────┐
│                                                                 │
│  1. Revisa los logs en PythonAnywhere                          │
│     Web → Log files → error_log.log                            │
│                                                                 │
│  2. Lee las soluciones en DESPLIEGUE_PYTHONANYWHERE.md        │
│     Sección: "Si hay errores"                                  │
│                                                                 │
│  3. Verifica que:                                              │
│     • DATABASE_URL esté correcto                               │
│     • Virtualenv esté activado                                 │
│     • BD PostgreSQL exista                                     │
│     • Permisos de carpeta sean correctos (755)                 │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

╔════════════════════════════════════════════════════════════════╗
║                                                                ║
║  🎉 FELICIDADES! TODO ESTÁ LISTO PARA DESPLEGAR              ║
║                                                                ║
║  Próximo paso: Lee START_HERE.md                              ║
║                                                                ║
║  ¡Tu sitio estará online en menos de 10 minutos! 🚀           ║
║                                                                ║
╚════════════════════════════════════════════════════════════════╝
