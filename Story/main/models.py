from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Story(models.Model):
    CATEGORY_CHOICES = [
        ('Fun','Fun'),
        ('Fair','Fair'),

    ]

    name = models.CharField(max_length=200)
    content= models.TextField()
    image = models.ImageField(upload_to="images/")
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    create_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
    
class Comment(models.Model):
    Story = models.ForeignKey(Story, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.plant.name}"