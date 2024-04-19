from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Student(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    collage_name = models.CharField(max_length=255)
    graduation_year = models.IntegerField()
    major = models.CharField(max_length=255)
    GPA =models.DecimalField(max_digits=5,decimal_places=2)
    CV = models.FileField(upload_to="files/")
    approved = models.BooleanField(default=False)
    
    def __str__(self):
        return self.user.username
    

class Orgnization(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    about = models.TextField()
    logo = models.ImageField(upload_to="images/")
    # approved = models.BooleanField(default=False)
    
