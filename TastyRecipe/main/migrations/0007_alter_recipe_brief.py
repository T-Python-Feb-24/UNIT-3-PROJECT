# Generated by Django 5.0.3 on 2024-04-08 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_recipe_brief'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='brief',
            field=models.TextField(),
        ),
    ]
