# Generated by Django 5.0.3 on 2024-04-01 07:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_recipes_chfe_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipes',
            old_name='chfe_name',
            new_name='chef_name',
        ),
    ]
