# Generated by Django 4.2.3 on 2023-07-12 03:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CaosNewsApp', '0019_detallenoticia'),
    ]

    operations = [
        migrations.RenameField(
            model_name='detallenoticia',
            old_name='id',
            new_name='id_detalle',
        ),
    ]