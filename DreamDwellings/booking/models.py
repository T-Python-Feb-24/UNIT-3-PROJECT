from django.db import models
from django.contrib.auth.models import User
from main.models import Place
from django.utils import timezone

class Booking(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)  
    check_in_date = models.DateField(default=timezone.now)  
    check_out_date = models.DateField(default=timezone.now() + timezone.timedelta(days=1))  
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=255)  
      
def __str__(self):
        return f'{self.user.username} - {self.place.name}'