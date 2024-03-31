from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserRecipe(models.Model):
    
    categories = models.TextChoices("Category", ["All", "Carbs", "Vegetarian" , "Protien"])

    user=models.ForeignKey(User , on_delete=models.CASCADE)
    title=models.CharField(max_length = 64)
    about= models.TextField()
    calories=models.IntegerField()
    image=models.ImageField(upload_to="images/", default="images/default.jpg")
    category=models.CharField(max_length = 64 , choices=categories.choices)
