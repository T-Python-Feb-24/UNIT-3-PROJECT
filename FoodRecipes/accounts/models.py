from django.db import models
from django.contrib.auth.models import User

from main.models import Recipes

# Create your models here.
class ProfileUser(models.Model):
    recipes  = models.ForeignKey(Recipes, on_delete=models.CASCADE,null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    about = models.TextField()
    avatar = models.ImageField(upload_to="images/", default="images/istockphoto-1300845620-612x612.jpg")
   
    
