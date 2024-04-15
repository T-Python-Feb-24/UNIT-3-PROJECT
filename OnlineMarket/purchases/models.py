from django.db import models
from django.contrib.auth.models import User
from product.models import Product
from creditcards.models import CardNumberField ,CardExpiryField ,SecurityCodeField
# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    quantity=models.PositiveBigIntegerField(default=1)




    