from pathlib import Path
import environ
import os
from pathlib import Path

env = environ.Env(DEBUG=(bool, True))
environ.Env.read_env()  # lee .env si existe

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = env("SECRET_KEY", default="dev-secret-no-usar-en-prod")
DEBUG = env("DEBUG", default=True)
ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '.onrender.com', '.pythonanywhere.com', 'Pudindechocolate.pythonanywhere.com']

INSTALLED_APPS = [
    'backend_utils',
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",  # <-- requerido por allauth
    "rest_framework",
    "drf_yasg",


    # Terceros
    "allauth",
    "allauth.account",  # núcleo
                        # cuentas locales (si querés)
    "allauth.socialaccount",
    "allauth.socialaccount.providers.google",
    "allauth.socialaccount.providers.github",

    # Apps locales
    "categorias",
    "core",
    "market",
    "perfil",
    "presence",
    "simple_chat",
    "quotes",
    "presupuestos",
    "notifications",

]

SITE_ID = 1

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
]

LOGIN_REDIRECT_URL = "core:home"
LOGOUT_REDIRECT_URL = "core:home"

# ACCOUNT CONFIG DE ALLAUTH
ACCOUNT_LOGIN_METHOD = "email"
ACCOUNT_SIGNUP_FIELDS = ["email", "username", "password1", "password2"]
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_PASSWORD = "password1"
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True

# SOCIALACCOUNT CONFIG
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        },
    },
    'github': {
        'SCOPE': [
            'user',
            'repo',
            'read:org',
        ],
    }
}

# Auto-conectar después de login social
SOCIALACCOUNT_AUTO_SIGNUP = True
SOCIALACCOUNT_EMAIL_VERIFICATION = 'none'

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "presence.middleware.AutoLogoutMiddleware",
    "allauth.account.middleware.AccountMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    'presence.middleware.AutoLogoutMiddleware',
    'presence.middleware.UpdateLastSeenMiddleware',
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],  # <-- carpeta de templates
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.csrf",
                "django.template.context_processors.static",
                "django.template.context_processors.request",  # <-- requerido por allauth
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"


BASE_DIR = Path(__file__).resolve().parent.parent

import dj_database_url

# Database configuration
# En producción (Render), usa PostgreSQL desde DATABASE_URL
# En desarrollo local, usa SQLite
if 'DATABASE_URL' in os.environ:
    DATABASES = {
        'default': dj_database_url.config(
            default=os.environ.get('DATABASE_URL'),
            conn_max_age=600,
            conn_health_checks=True,
        )
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
            'OPTIONS': {
                'timeout': 30,
                'isolation_level': None,
                'check_same_thread': False,
            },
            'ATOMIC_REQUESTS': False,
            'CONN_MAX_AGE': 0,
        }
    }

STATIC_URL = "static/"
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

MERCADOPAGO_ACCESS_TOKEN = env("MERCADOPAGO_ACCESS_TOKEN", default="APP_USR-7466105107689955-111112-d4728192d77290b704a1cac8e79ac691-2952577724")
MERCADOPAGO_PUBLIC_KEY = env("MERCADOPAGO_PUBLIC_KEY", default="APP_USR-35018119-c38f-4466-87d5-b99da322dc66")


SESSION_COOKIE_AGE = 30 * 60           # 30 minutos (en segundos)
SESSION_SAVE_EVERY_REQUEST = True      # cada request renueva el tiempo
SESSION_EXPIRE_AT_BROWSER_CLOSE = False

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'tu_correo@gmail.com'
EMAIL_HOST_PASSWORD = 'tu_contraseña_o_contraseña_de_aplicación'
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# Configuración de AutoLogout
AUTO_LOGOUT_DELAY = 15  # minutos
AUTO_LOGOUT_REDIRECT_URL = 'account_login'  # redirigir a la página de login después del logout automático

# --- Telegram ---
TELEGRAM_BOT_TOKEN = "8330684630:AAEU8Xv7Lzf-GmazTG200AAcfl8jw0mLG-E"
TELEGRAM_CHAT_ID = "6778150392"   # puede ser grupo o canal
TELEGRAM_ADMINS = ["6778150392"] # lista de IDs de administradores
# --- FIN Telegram ---

SITE_URL = env("SITE_URL", default="http://127.0.0.1:8000")

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.BasicAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
}

# Payment provider placeholders
STRIPE_SECRET_KEY = ''
STRIPE_PUBLISHABLE_KEY = ''
STRIPE_WEBHOOK_SECRET = ''

# Static files
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
    BASE_DIR / 'market' / 'static',
    BASE_DIR / 'mercado' / 'static',
]
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Backend utils logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {'console': {'class': 'logging.StreamHandler'}},
    'root': {'handlers': ['console'], 'level': 'INFO'},
}
