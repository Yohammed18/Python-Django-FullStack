# Generated by Django 4.1 on 2024-02-24 02:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('temp_app', '0003_rename_principal_school_principle'),
    ]

    operations = [
        migrations.RenameField(
            model_name='school',
            old_name='principle',
            new_name='principal',
        ),
    ]
