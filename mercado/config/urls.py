from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from market.views import ProductViewSet
from market.views import create_preference
from core.views import home
from django.conf import settings
from django.conf.urls.static import static


# Swagger imports
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router = routers.DefaultRouter()
router.register(r"products", ProductViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="MERCALMA API",
        default_version="v1",
        description="API para manejar productos de MERCALMA (compra, venta, trueque).",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="tuemail@ejemplo.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path('', include('core.urls', namespace='core')),

    # Swagger endpoints
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),

    path("", home, name="home"),  # inicio
    path('market/', include(('market.urls', 'market'), namespace='market')), # mercado
    path("accounts/", include("allauth.urls")),  # login/signup
    path('', include('perfil.urls')),
    path("pago/<int:product_id>/", create_preference, name="crear-preferencia"),
    path("", include("presence.urls")),
    path("presence/", include("presence.urls", namespace="presence")),
    path("chat/", include("simple_chat.urls", namespace="simple_chat")),
    path("quotes/", include("quotes.urls", namespace="quotes")),
    path("api/presupuestos/", include("presupuestos.api.urls")),
    path("presupuestos/", include("presupuestos.urls")),
    path('categorias/', include('categorias.urls', namespace='categorias')),
    path('notifications/', include('notifications.urls', namespace='notifications')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)