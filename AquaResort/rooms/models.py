from django.db import models

# Create your models here.
class Room(models.Model):
    rooms_status = models.TextChoices('state', ['availabe','occupied','under_maintenance'])
    rooms_type = models.TextChoices('type', ['standard', 'deluxe ', 'suite', 'villa', 'accessible'])

    room_availability = models.CharField(max_length=50, choices=rooms_status.choices)
    room_type = models.CharField(max_length=50, choices=rooms_type.choices)
    room_number = models.CharField(max_length=50)
    capacity = models.IntegerField()
    amenities = models.TextField()
    room_img = models.ImageField(upload_to="images/",default='images/signUp-bg3.jpg')
    price = models.CharField(max_length=50)
    

