# 📋 INVENTARIO DE ARCHIVOS DE DEPLOYMENT

Estos son todos los archivos que he creado/modificado para tu despliegue en PythonAnywhere:

## 📂 ARCHIVOS CREADOS

### 🌟 PRINCIPALES (Lee en este orden)

| Archivo | Descripción | Acción |
|---------|-------------|--------|
| `START_HERE.md` | Punto de entrada - resumen de todo | **👈 EMPIEZA AQUI** |
| `DESPLIEGUE_PYTHONANYWHERE.md` | Guía paso a paso completa con comandos | **Sigue esta** |
| `README_DEPLOYMENT.txt` | Resumen visual en formato ASCII | Referencia rápida |

### 🔧 CONFIGURACIÓN

| Archivo | Descripción | Ubicación |
|---------|-------------|-----------|
| `.env.pythonanywhere` | Plantilla de variables de entorno | Raíz del proyecto |
| `pythonanywhere_wsgi.py` | Configuración WSGI correcta | Raíz del proyecto |
| `.env` (después de copiar) | Variables de ambiente en producción | `mercado/.env` |

### 📖 DOCUMENTACIÓN

| Archivo | Descripción |
|---------|-------------|
| `CHECKLIST_SEGURIDAD.md` | Lista de verificación de seguridad |
| `TROUBLESHOOTING_PYTHONANYWHERE.md` | Solución de problemas comunes |
| `COMANDOS_PYTHONANYWHERE.sh` | Comandos útiles listos para usar |

### 🐍 SCRIPTS

| Archivo | Descripción |
|---------|-------------|
| `pythonanywhere_setup.sh` | Script automático de setup (opcional) |
| `prepare_pythonanywhere.py` | Script de verificación pre-deploy |

---

## ✏️ ARCHIVOS MODIFICADOS

### `mercado/config/settings.py`
```python
# Cambio realizado:
ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '.onrender.com', '.pythonanywhere.com', 'Pudindechocolate.pythonanywhere.com']
# Agregué soporte para PythonAnywhere
```

### `requirements.txt`
```
# Cambio realizado:
psycopg2-binary==2.9.11  # (Actualizado de 2.9.9)
# Para compatibilidad con Windows en PythonAnywhere
```

---

## 🎯 FLUJO DE DEPLOYMENT

```
1. START_HERE.md
   ↓
2. DESPLIEGUE_PYTHONANYWHERE.md
   ├─→ Paso 1-4: Setup virtualenv
   ├─→ Paso 5: Variables de entorno
   ├─→ Paso 6-7: Base de datos
   ├─→ Paso 8-11: Web app config
   └─→ Paso 12: Reload
   ↓
3. Verificar: https://Pudindechocolate.pythonanywhere.com
   ↓
4. Si hay problemas:
   └─→ TROUBLESHOOTING_PYTHONANYWHERE.md
   └─→ CHECKLIST_SEGURIDAD.md
   └─→ COMANDOS_PYTHONANYWHERE.sh
```

---

## 📦 TAMAÑO TOTAL

```
START_HERE.md                          ~3 KB
DESPLIEGUE_PYTHONANYWHERE.md          ~8 KB
README_DEPLOYMENT.txt                  ~4 KB
.env.pythonanywhere                    ~1 KB
pythonanywhere_wsgi.py                 ~1 KB
CHECKLIST_SEGURIDAD.md                ~6 KB
TROUBLESHOOTING_PYTHONANYWHERE.md     ~10 KB
COMANDOS_PYTHONANYWHERE.sh             ~8 KB
pythonanywhere_setup.sh                ~3 KB
prepare_pythonanywhere.py              ~2 KB
─────────────────────────────────────────
TOTAL DOCUMENTACIÓN:                  ~46 KB
```

---

## ✅ CHECKLIST: ANTES DE DESPLEGAR

- [ ] He leído START_HERE.md
- [ ] He leído DESPLIEGUE_PYTHONANYWHERE.md completamente
- [ ] Tengo mis credenciales listas:
  - Usuario: Pudindechocolate
  - Contraseña: 8Avmr8DiDUQ9zsh
- [ ] Mi código está en GitHub (o listo para subir manualmente)
- [ ] He guardado las contraseñas de email en lugar seguro
- [ ] Tengo abierto un navegador en PythonAnywhere

---

## 🚀 PASOS RÁPIDOS

```bash
# En PythonAnywhere Bash console:

# 1. Clonar proyecto
cd /home/Pudindechocolate
git clone TU_REPO mercalma
cd mercalma

# 2. Crear virtualenv
mkvirtualenv --python=/usr/bin/python3.11 mercalma_env

# 3. Instalar paquetes
pip install -r requirements.txt

# 4. Configurar .env
cp .env.pythonanywhere mercado/.env
nano mercado/.env  # Editar valores

# 5. Migrar BD
cd mercado
python manage.py migrate
python manage.py createsuperuser

# 6. Archivos estáticos
python manage.py collectstatic --noinput

# 7. En PythonAnywhere Web:
# - Crear Web App (Manual + Python 3.11)
# - Configurar WSGI (copiar contenido de pythonanywhere_wsgi.py)
# - Configurar Static files (/static/ y /media/)
# - Configurar Virtualenv
# - Click Reload
```

---

## 🎓 REFERENCIA RÁPIDA

| Necesito... | Archivo |
|------------|---------|
| Comenzar | `START_HERE.md` |
| Instrucciones paso a paso | `DESPLIEGUE_PYTHONANYWHERE.md` |
| Verificación de seguridad | `CHECKLIST_SEGURIDAD.md` |
| Solucionar problemas | `TROUBLESHOOTING_PYTHONANYWHERE.md` |
| Comandos útiles | `COMANDOS_PYTHONANYWHERE.sh` |
| Variables de entorno | `.env.pythonanywhere` |
| Configuración WSGI | `pythonanywhere_wsgi.py` |

---

## 💾 DÓNDE GUARDAR ESTOS ARCHIVOS

Todos los archivos están en la raíz del proyecto:
```
C:\Users\PudinSensual\Desktop\Mercalma\MERCALMA\
├── START_HERE.md
├── DESPLIEGUE_PYTHONANYWHERE.md
├── README_DEPLOYMENT.txt
├── CHECKLIST_SEGURIDAD.md
├── TROUBLESHOOTING_PYTHONANYWHERE.md
├── COMANDOS_PYTHONANYWHERE.sh
├── .env.pythonanywhere
├── pythonanywhere_wsgi.py
├── pythonanywhere_setup.sh
├── prepare_pythonanywhere.py
├── mercado/
│   ├── config/settings.py (✏️ MODIFICADO)
│   └── .env (crear desde .env.pythonanywhere)
└── requirements.txt (✏️ MODIFICADO)
```

---

## 🌐 ENLACES IMPORTANTES

- **Panel PythonAnywhere**: https://www.pythonanywhere.com
- **Mi cuenta**: https://www.pythonanywhere.com/user/Pudindechocolate/
- **Web apps**: https://www.pythonanywhere.com/user/Pudindechocolate/webapps/
- **Bases de datos**: https://www.pythonanywhere.com/user/Pudindechocolate/databases/
- **Django Docs**: https://docs.djangoproject.com/
- **PostgreSQL Docs**: https://www.postgresql.org/docs/

---

## 🆘 SOPORTE

1. Revisa logs en PythonAnywhere
2. Consulta TROUBLESHOOTING_PYTHONANYWHERE.md
3. Lee CHECKLIST_SEGURIDAD.md
4. Usa comandos de COMANDOS_PYTHONANYWHERE.sh
5. Contacta soporte de PythonAnywhere si es necesario

---

**Última actualización:** 2 de diciembre de 2025
**Estado:** ✅ TODO LISTO PARA DEPLOYMENT
**Próximo paso:** Lee START_HERE.md 👈

