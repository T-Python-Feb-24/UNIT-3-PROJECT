from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Contact(models.Model):
    username=models.CharField(max_length=2048)
    email=models.EmailField()
    subject=models.CharField(max_length=2048)
    message=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)




  