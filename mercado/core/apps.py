
from django.apps import AppConfig

class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'   # <- IMPORTANTE: 'core' porque core está al mismo nivel que manage.py

    def ready(self):
        import core.signals  # importa las señales usando el path correcto
