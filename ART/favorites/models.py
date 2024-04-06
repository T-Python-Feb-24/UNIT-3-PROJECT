from django.db import models
from django.contrib.auth.models import User
from main.models import Blog

# Create your models here.


class Favorite(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)