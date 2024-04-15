from django.db import models
from django.contrib.auth.models import User
from main.models import Event

# Create your models here.


class Booking(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    booked_at = models.DateTimeField(auto_now_add=True)

