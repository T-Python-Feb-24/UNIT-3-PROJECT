from django.db import models
from accounts.models import Orgnization,Student
# Create your models here.

class Candidate(models.Model):
    organization =models.ForeignKey(Orgnization,on_delete=models.CASCADE)
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
