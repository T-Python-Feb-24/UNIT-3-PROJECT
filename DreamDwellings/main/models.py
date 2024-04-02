# from django.conf import settings
# from django.db import models

# from django.db import models



# class Place(models.Model):
#     CATEGORY_CHOICES = (
#         ('For Sale', 'For Sale'),
#         ('For Rent', 'For Rent'),
#     )
#     RIYADH_NEIGHBORHOOD_CHOICES = (
#         ('Downtown', 'Downtown'),
#         ('Al-Murabba', 'Al-Murabba'),
#         ('Al-Olaya', 'Al-Olaya'),
#         ('Al-Malaz', 'Al-Malaz'),
#         ('Al-Wadi', 'Al-Wadi'),
#     )

#     name = models.CharField(max_length=100)
#     neighborhood = models.CharField(max_length=50, choices=RIYADH_NEIGHBORHOOD_CHOICES)
#     latitude = models.DecimalField(max_digits=9, decimal_places=6)
#     longitude = models.DecimalField(max_digits=9, decimal_places=6)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     address = models.CharField(max_length=255)
#     image = models.ImageField(upload_to="images/")  
#     category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
#     for_rent = models.BooleanField(default=False)  
#     for_sale = models.BooleanField(default=False)  

#     def __str__(self):
#         return self.name
from django.db import models


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

    name = models.CharField(max_length=100)
    neighborhood = models.CharField(max_length=50, choices=RIYADH_NEIGHBORHOOD_CHOICES)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    address = models.CharField(max_length=255)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    for_rent = models.BooleanField(default=False)
    for_sale = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class PlaceImage(models.Model):
    place = models.ForeignKey(Place, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images/")

    def __str__(self):
        return f"Image for {self.place.name}"


    
# class Contact(models.Model):
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     email = models.EmailField()
#     message = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.first_name} {self.last_name} - {self.email}"
