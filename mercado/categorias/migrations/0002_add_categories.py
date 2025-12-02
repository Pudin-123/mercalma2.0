from django.db import migrations

def create_categories(apps, schema_editor):
    Category = apps.get_model('categorias', 'Category')
    Category.objects.create(name="Alimentos")
    Category.objects.create(name="Ropa")
    Category.objects.create(name="Electrónica")
    Category.objects.create(name="Hogar")
    Category.objects.create(name="Juguetes")
    Category.objects.create(name="Deportes")
    Category.objects.create(name="Libros")
    Category.objects.create(name="Salud y Belleza")
    Category.objects.create(name="Automotriz")
    Category.objects.create(name="Otros")

class Migration(migrations.Migration):

    dependencies = [
    ('categorias', '0001_initial'),
]

operations = [
        migrations.RunPython(create_categories),
    ]
