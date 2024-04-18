from django.db import models
from django.contrib.auth.models import User



# Task  
class Task(models.Model):

    title = models.CharField(max_length=200)
    description = models.TextField()
    deadline = models.DateField()

    def __str__(self):
        return self.title


# Notes 
class Note(models.Model):

    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    context = models.TextField()

    def __str__(self) -> str:
        return self.title
    


# Journal
class Journal(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    context = models.TextField()

    def __str__(self):
        return self.title


# Task  
class ReadingList(models.Model):

    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title
    

# Yearly Goals   
class YearlyGoal(models.Model):

    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title
    

