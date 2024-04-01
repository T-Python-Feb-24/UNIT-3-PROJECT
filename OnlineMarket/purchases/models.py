from django.db import models
from django.contrib.auth.models import User
from product.models import Product
from creditcards.models import CardNumberField ,CardExpiryField ,SecurityCodeField
# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


#يحتاج تعديل
class Order(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    cart=models.ForeignKey(Cart, on_delete=models.CASCADE)
    order_date=models.DateTimeField()
    is_finished= models.BooleanField(default=False)
    #payment=models.ForeignKey(Payment)

class OrderDetail(models.Model):
   Product=models.ForeignKey(Product, on_delete=models.CASCADE)
   order=models.ForeignKey(Order,on_delete=models.CASCADE)
   price=models.DecimalField(max_digits=6, decimal_places=2)
   quantity=models.IntegerField()
  
   @property
   def total(self):
       return self.price* self.quantity
   def __str__(self):
       return f"{self.quantity}{self.product.name}for order #{self.order.id}"   


class Payment(models.Model):
    order= models.ForeignKey(Order, on_delete=models.CASCADE)
    shipment_address=models.CharField(max_length=150)
    shipment_phone=models.CharField(max_length=150)
    card_number=CardNumberField()
    expire=CardExpiryField()
    security_code= SecurityCodeField()
    