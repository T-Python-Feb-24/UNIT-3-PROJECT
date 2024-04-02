# Generated by Django 5.0.3 on 2024-04-02 10:22

import account.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('prodect', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.prodect')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prodect', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.prodect')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=10, unique=True)),
                ('avatar', models.ImageField(default='images/profiles/user-defualt.svg', upload_to=account.models.group_based_upload_to)),
                ('gender', models.CharField(choices=[('', 'Null'), ('Male', 'Male'), ('Female', 'Female')], default='', max_length=22)),
                ('nationality', models.CharField(choices=[('Saudi Arabia', 'Sa'), ('United Arab Emirates', 'Uae')], default='Saudi Arabia', max_length=20)),
                ('address', models.TextField()),
                ('about', models.TextField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
