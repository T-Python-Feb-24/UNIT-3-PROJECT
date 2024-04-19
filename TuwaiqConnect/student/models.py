from django.db import models
from accounts.models import Student
# Create your models here.

class Project (models.Model):
    types = models.TextChoices("types",["unit","final","personal"])
    
    Student = models.ForeignKey(Student,on_delete=models.CASCADE)
    project_type = models.CharField(max_length=100,choices=types.choices)
    # put a default image
    screenshot = models.ImageField(upload_to ="images/")
    name = models.CharField(max_length=100)
    desc = models.TextField()
    link = models.URLField()

