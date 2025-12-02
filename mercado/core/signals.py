
import logging
from django.conf import settings
from django.db import connections
from django.db.models.signals import post_migrate
from django.dispatch import receiver

logger = logging.getLogger(__name__)

@receiver(post_migrate)
def enable_sqlite_wal(sender, **kwargs):
    dbs = getattr(settings, "DATABASES", {})
    for alias, cfg in dbs.items():
        if "sqlite3" in cfg.get("ENGINE", ""):
            try:
                conn = connections[alias]
                cursor = conn.cursor()
                cursor.execute("PRAGMA journal_mode=WAL;")
                result = cursor.fetchone()
                cursor.close()
                # Para depuración rápida, además del logger, podés usar print:
                print(f"Modo WAL activado para '{alias}': {result}")
                logger.info("Modo WAL activado para '%s': %s", alias, result)
            except Exception as e:
                logger.warning("No se pudo activar WAL para '%s': %s", alias, e)
