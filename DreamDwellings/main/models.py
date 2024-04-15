from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import Avg

class Place(models.Model):
    CATEGORY_CHOICES = (
        ('For Sale', 'For Sale'),
        ('For Rent', 'For Rent'),
    )
    
    RIYADH_NEIGHBORHOOD_CHOICES = (
        ('Downtown', 'Downtown'),
        ('Al-Murabba', 'Al-Murabba'),
        ('Al-Olaya', 'Al-Olaya'),
        ('Al-Malaz', 'Al-Malaz'),
        ('Al-Wadi', 'Al-Wadi'),
    )
    AVAILABILITY_CHOICES = (
        ('Available', 'Available'),
        ('Booked', 'Booked'),
        ('Sold', 'Sold'),
    )
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user_id')
    name = models.CharField(max_length=100)
    description = models.TextField()
    neighborhood = models.CharField(max_length=50, choices=RIYADH_NEIGHBORHOOD_CHOICES)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    offer_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    address = models.CharField(max_length=255)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    
    def __str__(self):
        return self.name

    def __str__(self):
        return self.name

class PlaceImage(models.Model):
    place = models.ForeignKey(Place, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images/")

    def __str__(self):
        return f"Image for {self.place.name}"


    
class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"
    
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'place')
    
