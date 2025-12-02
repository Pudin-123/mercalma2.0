from django.db import migrations

def add_supermercado_category(apps, schema_editor):
    Category = apps.get_model('categorias', 'Category')
    Category.objects.get_or_create(name="Supermercado")

def remove_supermercado_category(apps, schema_editor):
    Category = apps.get_model('categorias', 'Category')
    Category.objects.filter(name="Supermercado").delete()

class Migration(migrations.Migration):

    dependencies = [
        ('categorias', '0002_add_categories'),
    ]

    operations = [
        migrations.RunPython(add_supermercado_category, remove_supermercado_category),
    ]