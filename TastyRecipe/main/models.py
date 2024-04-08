from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Recipe(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title =  models.CharField(max_length=200)
    brief = models.TextField()
    ingredients = models.TextField()
    instructions = models.TextField()
    time_estimate = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', default='images/logo.png')
    
    Categories = models.TextChoices('Category', ["Pasta", "Soup", "Chicken", "Salad"]) 
    category = models.CharField(max_length = 64, choices = Categories.choices)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Contact(models.Model):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Review(models.Model):

    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.recipe.title}"