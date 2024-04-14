from django.db import models
from django.contrib.auth.models import User 


# Create your models here.

class Recipe(models.Model):
    
    categories = models.TextChoices("Category", ["Mix","Carbs", "Vegetarian" , "Protien"])

    title=models.CharField(max_length = 64)
    about= models.TextField()
    ingredients=models.TextField()
    quantity=models.IntegerField()
    fat=models.IntegerField()
    protien=models.IntegerField()
    carb=models.IntegerField()
    calories=models.IntegerField()
    image=models.ImageField(upload_to="images/", default="images/default.jpg")
    category=models.CharField(max_length = 64 , choices=categories.choices)





class Comment(models.Model):
    recipe= models.ForeignKey(Recipe, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User , on_delete=models.CASCADE)



class Contact(models.Model):
    name=models.CharField(max_length = 64)
    email=models.EmailField(max_length=254)
    message=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    image=models.ImageField(upload_to="images/", default="images/user.png")


