from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Student(models.Model):

    majors = models.TextChoices("Major", ["Software Engineering", "Computer Science", "Data Science", "Network and Computer Engineering", "Cyber Security"])

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=50)
    major = models.CharField(max_length=64, choices=majors.choices)
    
    def __str__(self) -> str:
        return f"{self.user.username}" - {self.major}
    

class Profile(models.Model):
        
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to="images/", default="images/avatar.png")
    birthdate = models.DateField(auto_now=False, auto_now_add=False)
    bio = models.TextField()
    linkedin_link = models.URLField(blank=True)
    github_link = models.URLField(blank=True)

    def __str__(self) -> str:
        return f"{self.user.username} profile"

    





               
