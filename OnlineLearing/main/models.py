from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=2048)
    age = models.BooleanField()
    number = models.CharField(max_length=20)  

    def _str_(self):
        return self.name



class Course(models.Model):
    COURSE_CATEGORIES = (
        ('education', 'Education'),
        ('icts', 'ICTs'),
        ('languages', 'Languages'),
        ('law', 'Law'),
    )

    coursename = models.CharField(max_length=2048)
    numberhours = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    startdate = models.DateTimeField(auto_now_add=True)
    expirydate = models.DateTimeField()
    poster = models.ImageField(upload_to="images/")
    categories = models.CharField(max_length=20, choices=COURSE_CATEGORIES)
    content = models.TextField()


    def _str_(self):
        return self.coursename
class Register(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    #course=
    #type=Doctor/student

    
class Doctor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    namedoctor = models.CharField(max_length=2048)
    salary = models.PositiveIntegerField()
    number = models.CharField(max_length=20)

    def _str_(self):
        return self.namedoctor
