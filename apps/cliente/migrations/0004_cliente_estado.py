# Generated by Django 4.2.1 on 2023-09-08 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0003_alter_cliente_telefono_cliente'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='estado',
            field=models.BooleanField(default=True),
        ),
    ]
