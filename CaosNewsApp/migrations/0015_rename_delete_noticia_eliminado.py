# Generated by Django 4.2.1 on 2023-07-01 06:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CaosNewsApp', '0014_alter_usuario_options_usuario_role_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='noticia',
            old_name='delete',
            new_name='eliminado',
        ),
    ]
