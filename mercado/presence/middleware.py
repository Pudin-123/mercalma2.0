from django.utils import timezone
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.db import OperationalError
from .models import UserActivity
import logging

logger = logging.getLogger(__name__)

class AutoLogoutMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            now_ts = timezone.now().timestamp()
            last = request.session.get("last_activity", now_ts)
            # 30 minutos = 1800 segundos
            if now_ts - last > 1800:
                logout(request)
                # después de logout, opcionalmente redirigir a página informativa
                return redirect("session_expired")
            request.session["last_activity"] = now_ts
        return self.get_response(request)
# Agregar 'mercado.presence.middleware.AutoLogoutMiddleware' a MIDDLEWARE en settings.py

class UpdateLastSeenMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            try:
                # Solo actualizar si han pasado al menos 30 segundos desde la última actualización
                last_update = request.session.get("last_activity_update")
                now = timezone.now().timestamp()
                
                if last_update is None or (now - last_update) > 30:
                    UserActivity.objects.update_or_create(
                        user=request.user, 
                        defaults={"last_seen": timezone.now()}
                    )
                    request.session["last_activity_update"] = now
            except OperationalError as e:
                # Si la base de datos está bloqueada, simplemente ignoramos
                logger.warning(f"Database locked while updating UserActivity for {request.user}: {str(e)}")
            except Exception as e:
                # Cualquier otro error no debería bloquear la solicitud
                logger.error(f"Error updating UserActivity: {str(e)}", exc_info=True)
        
        return self.get_response(request)
# Agregar 'mercado.presence.middleware.UpdateLastSeenMiddleware' a MIDDLEWARE en settings.py