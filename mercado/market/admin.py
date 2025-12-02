from django.contrib import admin
from .models import Product, Category

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "seller", "marca", "price", "active", "created_at")
    search_fields = ("title", "description", "marca", "seller__username")
    list_filter = ("active", "created_at", "seller")

admin.site.register(Category)
# Register your models here.
