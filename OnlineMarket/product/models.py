from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Product(models.Model):

    #catergories choices
    categories = models.TextChoices("Category", ["Iphone", "Airbods", "Mackbook", "Ipad","Apple watch"])

    name = models.CharField(max_length=2048)
    description = models.TextField()
    published_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="images/")
    price=models.DecimalField(max_digits=10,decimal_places=2)
    quantity=models.IntegerField()
    category = models.CharField(max_length=64, choices=categories.choices)


    #string representation
    def __str__(self):
        return self.name
    


class Comment(models.Model):

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Review(models.Model):

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating=models.IntegerField(choices=[(i,i) for i in range (1,6)])   

