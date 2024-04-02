from django.db import models
from django.contrib.auth.models import User
from main.models import Recipe 
from interactive.models import UserRecipe

# Create your models here.


class Favorite(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(UserRecipe, on_delete=models.CASCADE)



class RecipeFavorite(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)


