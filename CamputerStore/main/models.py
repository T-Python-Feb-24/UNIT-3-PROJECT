from django.db import models
from django.contrib.auth.models import User


class categories_choices(models.TextChoices):
   PC = "PC"
   Laptop = "Laptop"
   Parts = "parts"
   Accessories = "accessories"
   Software = "Software"


class Prodect(models.Model):
   name = models.CharField(max_length=300, null=False)
   model = models.CharField(max_length=200)
   category = models.CharField(max_length=200,
                               choices=categories_choices.choices,
                               default=categories_choices.PC)
   price = models.FloatField(null=False)
   in_stock = models.IntegerField(null=False)
   created_at = models.DateTimeField(auto_now_add=True)


class Comments(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   prodect = models.ForeignKey(Prodect, on_delete=models.CASCADE)
   content = models.TextField(blank=False)
   commented_at = models.DateTimeField(auto_now_add=True)


class Contactus(models.Model):
   name = models.CharField(max_length=50)
   email = models.EmailField(null=False)
   phone = models.CharField(max_length=10)
   content = models.TextField(blank=False)
   created_at = models.DateTimeField(auto_now_add=True)
