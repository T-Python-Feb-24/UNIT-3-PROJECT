from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator      
from django.contrib.auth.models import User

# Create your models here.
class Recipes(models.Model):
    categories = models.TextChoices("Category", ["Breakfast","Lunch", "Dinner"])
  
    name = models.CharField(max_length=2048)
    content = models.TextField()
    published_at = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=64,choices=categories.choices)
    time_coocking=models.IntegerField()
    number_people=models.IntegerField(max_length=2048)
    image=models.ImageField(upload_to="images/",default="")
    
class Comment(models.Model):

    Recipes= models.ForeignKey(Recipes, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    published_at = models.DateTimeField(auto_now_add=True)
    evaluation = models.PositiveIntegerField( validators=[MinValueValidator(1), MaxValueValidator(5)]) 
    
class Suggestions(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    published_at = models.DateTimeField(auto_now_add=True)
    