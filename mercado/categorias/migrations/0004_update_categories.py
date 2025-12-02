from django.db import migrations

def update_categories(apps, schema_editor):
    Category = apps.get_model('categorias', 'Category')
    # Primero, eliminamos todas las categorías existentes
    Category.objects.all().delete()
    
    # Creamos las nuevas categorías que coinciden con el menú
    categories = [
        "Ofertas",
        "Supermercado",
        "Tecnología",
        "Hogar",
        "Moda",
        "Deportes"
    ]
    
    for cat_name in categories:
        Category.objects.create(name=cat_name)

def reverse_categories(apps, schema_editor):
    Category = apps.get_model('categorias', 'Category')
    Category.objects.all().delete()

class Migration(migrations.Migration):

    dependencies = [
        ('categorias', '0003_add_supermercado_category'),
    ]

    operations = [
        migrations.RunPython(update_categories, reverse_categories),
    ]