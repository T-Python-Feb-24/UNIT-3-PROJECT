# Generated by Django 5.0.3 on 2024-04-06 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_blog_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='category',
            field=models.CharField(choices=[('Nature', 'Nature'), ('Arts', 'Arts'), ('Daily Life', 'Daily Life'), ('Food', 'Food')], max_length=64),
        ),
    ]
