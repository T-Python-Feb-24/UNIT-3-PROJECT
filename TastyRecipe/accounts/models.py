from django.db import models
from django.contrib.auth.models import User

from main.models import Recipe
# Create your models here.

class Profile(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to="images/", default="images/avatar.webp")
    instagram_link = models.URLField(blank=True)
    youtube_link = models.URLField(blank=True)

    def __str__(self) -> str:
        return f"{self.user.username} profile"

class Saved(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)