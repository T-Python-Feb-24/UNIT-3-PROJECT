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
    description = models.TextField(blank=True, null=True)  
    content = models.TextField()
    image = models.ImageField(upload_to="images/")
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    created_at = models.DateTimeField(default=timezone.now)
    saved_by = models.ManyToManyField(User, related_name='saved_stories', blank=True)

    def __str__(self):
        return self.name
    
class Comment(models.Model):
    Story = models.ForeignKey(Story, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.plant.name}"
    
class ContactMessage(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.created_at}"