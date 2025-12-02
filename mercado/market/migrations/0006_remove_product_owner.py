from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('market', '0005_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='owner',
        ),
    ]