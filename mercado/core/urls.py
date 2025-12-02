from django.urls import path, include
from . import views

app_name = "core"
urlpatterns = [
    path("", views.home, name="home"),
    path("market/", include("market.urls", namespace="market")),
    path("perfil/", include("perfil.urls", namespace="perfil")),
]