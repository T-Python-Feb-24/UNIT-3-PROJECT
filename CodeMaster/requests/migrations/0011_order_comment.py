# Generated by Django 5.0.2 on 2024-04-13 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requests', '0010_alter_order_rate'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='comment',
            field=models.TextField(default='', max_length=250),
        ),
    ]
