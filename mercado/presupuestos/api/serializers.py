from rest_framework import serializers
from presupuestos.models import Presupuesto
from presupuestos.models import Presupuesto, TelegramLog

class PresupuestoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Presupuesto
        fields = ["id", "producto", "email", "mensaje", "creado_en"]

class PresupuestoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Presupuesto
        fields = ["id", "producto", "email", "mensaje", "creado_en"]

class TelegramLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelegramLog
        fields = ["id", "chat_id", "username", "mensaje", "recibido_en"]

# Create your serializers here.