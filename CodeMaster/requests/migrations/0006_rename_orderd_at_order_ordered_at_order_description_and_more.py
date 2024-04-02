# Generated by Django 5.0.2 on 2024-04-02 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requests', '0005_remove_order_file_order_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='orderd_at',
            new_name='ordered_at',
        ),
        migrations.AddField(
            model_name='order',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='order',
            name='subject',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
