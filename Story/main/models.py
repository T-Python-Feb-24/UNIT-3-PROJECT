from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Story(models.Model):
    CATEGORY_CHOICES = [
        ('Fun', 'Fun'),
        ('Fair', 'Fair'),
        ('Adventure', 'Adventure'),
        ('Romance', 'Romance'),
        ('Mystery', 'Mystery'),
        ('Sci-Fi', 'Science Fiction'),
        ('Horror', 'Horror'),
    ]

    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)  # Added description field
    content = models.TextField()
    image = models.ImageField(upload_to="images/")
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
    
class Comment(models.Model):
    Story = models.ForeignKey(Story, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.plant.name}"