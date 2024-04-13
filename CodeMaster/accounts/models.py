from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone=models.CharField(max_length=255,blank=True)
    info=models.TextField(default="")
    instagram = models.URLField(blank=True)
    linked_in = models.URLField(blank=True)
    
    def __str__(self) -> str:
        return self.user.username
    
