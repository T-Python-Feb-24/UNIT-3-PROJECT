# Generated by Django 5.0.2 on 2024-04-13 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requests', '0009_order_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='rate',
            field=models.IntegerField(default=None),
        ),
    ]
