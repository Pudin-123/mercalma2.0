from django.conf import settings
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from categorias.models import Category
User = get_user_model()

class Product(models.Model):
    seller = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="sold_products")
    title = models.CharField(max_length=200, verbose_name="Título")
    description = models.TextField(blank=True, verbose_name="Descripción")
    marca = models.CharField(max_length=100, blank=True, default="Generico", verbose_name="Marca")
    price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Precio")
    stock = models.PositiveIntegerField(default=1, verbose_name="Stock")
    image = models.ImageField(upload_to="product_images/", blank=True, null=True, verbose_name="Imagen")
    active = models.BooleanField(default=True, verbose_name="Activo")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Categoría")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Última actualización")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """Retorna la URL del detalle del producto"""
        return reverse('market:product_detail', args=[self.pk])

    def is_available(self):
        return self.active and self.stock > 0
from django.contrib.auth import get_user_model
User = get_user_model()
class Cart(models.Model):
    # campos del carrito
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def total(self):
        return sum(item.subtotal() for item in self.items.all())

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def subtotal(self):
        return self.product.price * self.quantity

    @property
    def total_price(self):
        return self.product.price * self.quantity

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = "Categorías"

    def __str__(self):
        return self.name


