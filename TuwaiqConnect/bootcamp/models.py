from django.db import models
from django.contrib.auth.models import User
from accounts.models import Student

# Create your models here.

class Bootcamp(models.Model):
    bootcamp_name = models.CharField(max_length=100)
    students = models.ManyToManyField(Student)
    staff = models.ManyToManyField(User)
    desc = models.TextField()
    objectives =models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.bootcamp_name
    

class Evaluation(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    bootcamp = models.ForeignKey(Bootcamp, on_delete=models.CASCADE)
    attendance_rate = models.FloatField()
    grades_rate = models.FloatField()
    
    