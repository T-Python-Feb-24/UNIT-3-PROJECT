from django.db import models
from django.contrib.auth.models import User
from product.models import Product
# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


#يحتاج تعديل
class Order(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    cart=models.ForeignKey(Cart, on_delete=models.CASCADE)
    #payment=models.ForeignKey(Payment)
class Payment(models.Model):
 pass