from django.urls import path
from .views import PresupuestoCreate, PresupuestoList, UltimoTelegramLog


urlpatterns = [
path("create/", PresupuestoCreate.as_view(), name="presupuesto-create"),
    path("list/", PresupuestoList.as_view(), name="presupuesto-list"),
    path("ultimo-telegram/", UltimoTelegramLog.as_view(), name="ultimo-telegram"),
]
# Create your urls here.