from django.urls import path
from .views import telegram_webhook
from . import views


urlpatterns = [
    path("telegram/webhook/", telegram_webhook, name="telegram-webhook"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("lista-presupuestos/", views.lista_presupuestos, name="lista-presupuestos"),
]
