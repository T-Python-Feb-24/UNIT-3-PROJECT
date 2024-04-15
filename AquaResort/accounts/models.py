from django.db import models
from django.contrib.auth.models import User
from phone_field import PhoneField
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = PhoneField(blank=True)
    points = models.IntegerField(blank=True, default=0)