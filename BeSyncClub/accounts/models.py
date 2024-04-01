from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=50)
    university = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.user.username
    





               
