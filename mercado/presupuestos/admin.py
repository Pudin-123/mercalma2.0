from django.contrib import admin
from presupuestos.models import Presupuesto

@admin.register(Presupuesto)
class PresupuestoAdmin(admin.ModelAdmin):
    list_display = ("producto", "email", "creado_en")
    search_fields = ("producto", "email")
# Register your models here.
