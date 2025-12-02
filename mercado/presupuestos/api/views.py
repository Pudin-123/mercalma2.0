from rest_framework import generics
from presupuestos.models import Presupuesto
from .serializers import PresupuestoSerializer
from presupuestos.utils import enviar_a_telegram
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from presupuestos.models import TelegramLog
from .serializers import TelegramLogSerializer


class PresupuestoCreate(generics.CreateAPIView):
    queryset = Presupuesto.objects.all()
    serializer_class = PresupuestoSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        # Enviar mensaje a Telegram
        mensaje = (
            f"📢 <b>Nuevo presupuesto recibido</b>\n\n"
            f"📦 Producto: {instance.producto}\n"
            f"📧 Email: {instance.email}\n"
            f"📝 Mensaje: {instance.mensaje}\n"
            f"⏰ Fecha: {instance.creado_en.strftime('%d-%m-%Y %H:%M')}"
        )
        enviar_a_telegram(mensaje)
# Create your views here.
class IsStaffUser(permissions.BasePermission):
    """Permiso personalizado: solo usuarios staff"""
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_staff)


class PresupuestoList(generics.ListAPIView):
    queryset = Presupuesto.objects.all().order_by("-creado_en")
    serializer_class = PresupuestoSerializer
    permission_classes = [permissions.IsAuthenticated, IsStaffUser]

class UltimoTelegramLog(APIView):
    def get(self, request):
        ultimo = TelegramLog.objects.order_by("-recibido_en").first()
        if not ultimo:
            return Response({"detail": "No hay mensajes registrados aún."}, status=404)
        return Response(TelegramLogSerializer(ultimo).data)
