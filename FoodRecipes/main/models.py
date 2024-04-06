from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator      
from django.contrib.auth.models import User

# Create your models here.
class Recipes(models.Model):
    categories = models.TextChoices("Category", ["Breakfast","Lunch", "Dinner"])
  
    name = models.CharField(max_length=2048)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    published_at = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=64,choices=categories.choices)
    time_coocking=models.CharField(max_length=2048)
    number_people=models.CharField(max_length=2048)
    image=models.ImageField(upload_to="images/",default="images/kagyana-2955466_1280.jpg")
    
class Comment(models.Model):

    Recipes= models.ForeignKey(Recipes, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    published_at = models.DateTimeField(auto_now_add=True)
    evaluation = models.PositiveIntegerField( validators=[MinValueValidator(1), MaxValueValidator(5)],null=True) 
    
class Suggestions(models.Model):
    Recipes= models.ForeignKey(Recipes, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    published_at = models.DateTimeField(auto_now_add=True)
    


    
def __str__(self):
    return self