from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    states = models.TextChoices("State", ["Under review", "Accepted", "Rejected"],)
    subject = models.CharField(max_length=255)
    description = models.TextField(default="")
    file = models.FileField(upload_to="media/files/", blank=True)  
    ordered_at = models.DateTimeField(auto_now_add=True)
    state = models.CharField(max_length=64, choices=states.choices, default='Under review')

    

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order=models.OneToOneField(Order,on_delete=models.CASCADE)
    comment=models.TextField(max_length=250 ,default="")
    rate=models.IntegerField(default=None)