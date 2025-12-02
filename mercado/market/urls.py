from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "market"

urlpatterns = [
    path("", views.product_list, name="product_list"),
    path("product/<int:pk>/", views.product_detail, name="product_detail"),
    path("create/", views.create_product, name="create_product"),
    path("edit/<int:pk>/", views.product_edit, name="product_edit"),
    path("delete/<int:pk>/", views.product_delete, name="product_delete"),
    path("product/<int:pk>/edit/", views.edit_product, name="edit_product"),
    path("product/<int:pk>/delete/", views.delete_product, name="delete_product"),
    path("my_products/", views.my_products, name="my_products"),

    # --- Carrito ---
    path("cart/", views.cart_detail, name="cart_detail"),
    path("cart/add/<int:product_id>/", views.add_to_cart, name="add_to_cart"),
    path("cart/remove/<int:item_id>/", views.remove_from_cart, name="remove_from_cart"),
    path("cart/clear/", views.clear_cart, name="clear_cart"),
    path("cart/update/", views.update_cart, name="update_cart"),
    path("cart/update/ajax/", views.update_cart_ajax, name="update_cart_ajax"),




    # --- Crear orden ---
    path("order/create/", views.create_order, name="create_order"),

    # --- MercadoPago ---
    path("payment/create/<int:product_id>/", views.create_preference, name="create_preference"),
    path("payment/success/", views.payment_success, name="payment_success"),
    path("payment/cancel/", views.payment_cancel, name="payment_cancel"),
    path('mercadopago/create/<int:product_id>/', views.create_preference, name='create_preference'),
    path("payment/mercadopago/", views.mercadopago_checkout, name="mercadopago_checkout"),
]
