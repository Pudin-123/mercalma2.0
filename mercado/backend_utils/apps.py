from django.apps import AppConfig

class BackendUtilsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'backend_utils'

    def ready(self):
        try:
            from . import signals  # noqa
        except Exception:
            pass
