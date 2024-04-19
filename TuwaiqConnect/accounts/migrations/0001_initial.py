# Generated by Django 5.0.2 on 2024-04-01 10:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collage_name', models.CharField(max_length=100)),
                ('graduation_year', models.IntegerField()),
                ('major', models.CharField(max_length=100)),
                ('GPA', models.DecimalField(decimal_places=3, max_digits=5)),
                ('CV', models.FileField(upload_to='files/')),
                ('approved', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
