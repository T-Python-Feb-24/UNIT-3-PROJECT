from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Property(models.Model):
    
    # categories = models.TextChoices("Category", ["rent", "buy", "Flower", "Herb","Tree"])
       
    # agent = models.ForeignKey()
    name = models.CharField(max_length=2048)
    about = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to="images/", default="images/pexels-photo-1423600.jpeg")
    # category = models.CharField(max_length=64, choices=categories.choices)
    agent_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
# class Contact(models.Model):
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     email = models.EmailField()
#     message = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.first_name} {self.last_name} - {self.email}"
