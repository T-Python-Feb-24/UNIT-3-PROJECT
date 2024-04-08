from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from main import validator


class Product(models.Model):
   class categories_choices(models.TextChoices):
      PC = "اجهزة الكمبيوتر"
      Laptop = "اجهزة الكمبيوتر المحمول"
      Parts = "قطع الكمبيوتر"
      Accessories = "اكسسوارات"
      Software = "برامج"

   name = models.CharField(max_length=300, null=False)
   model = models.CharField(max_length=200, unique=True)
   category = models.CharField(max_length=200,
                               choices=categories_choices.choices,
                               default=categories_choices.PC)
   price = models.FloatField(null=False)
   discount = models.IntegerField(null=True, default=None)
   in_stock = models.IntegerField(null=False)
   created_at = models.DateTimeField(auto_now_add=True)

   def __str__(self):
      return self.name[:30] + "..."


def group_based_upload_to(instance, filename):
   return "product/image/{}/{}".format(instance.product.id, filename)


ext_validatod = [FileExtensionValidator(["png", "jpg", "jpeg"])]


class ProductImage(models.Model):
   product = models.ForeignKey(Product, on_delete=models.CASCADE)
   image = models.ImageField(
       upload_to=group_based_upload_to, null=False, validators=ext_validatod)


class Comments(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   product = models.ForeignKey(Product, on_delete=models.CASCADE)
   content = models.TextField(blank=False)
   commented_at = models.DateTimeField(auto_now_add=True)


class Contactus(models.Model):
   username = models.CharField(max_length=50)
   email = models.EmailField(null=False, validators=[validator.validate_email])
   phone = models.CharField(max_length=10, validators=[
                            validator.validate_phone])
   subject = models.CharField(max_length=200, blank=False, null=False)
   content = models.TextField(blank=False, null=False)
   created_at = models.DateTimeField(auto_now_add=True)

   def __str__(self):
      return self.subject
