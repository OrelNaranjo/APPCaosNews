# Generated by Django 4.2.1 on 2023-06-27 16:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('CaosNewsApp', '0012_alter_usuario_groups'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='groups',
        ),
        migrations.AddField(
            model_name='usuario',
            name='groups',
            field=models.ForeignKey(blank=True, help_text='The group this user belongs to.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='custom_user_set', related_query_name='custom_user', to='auth.group', verbose_name='group'),
        ),
    ]