from django.db import models
from product.models import Product
from django.contrib.auth.models import User
from main import validator


class Comments(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   product = models.ForeignKey(Product, on_delete=models.CASCADE)
   content = models.TextField(blank=False)
   commented_at = models.DateTimeField(auto_now_add=True)


class Contactus(models.Model):
   username = models.CharField(max_length=50)
   email = models.EmailField(null=False, validators=[validator.validate_email])
   phone = models.CharField(max_length=10, validators=[
                            validator.validate_phone])
   subject = models.CharField(max_length=200, blank=False, null=False)
   content = models.TextField(blank=False, null=False)
   created_at = models.DateTimeField(auto_now_add=True)

   def __str__(self):
      return self.subject
