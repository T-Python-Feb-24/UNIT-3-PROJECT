# Generated by Django 5.0.3 on 2024-04-02 07:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_remove_recipes_chef_name_recipes_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='evaluation',
            field=models.PositiveIntegerField(null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
