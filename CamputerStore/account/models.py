from django.db import models
from main.models import Product
from django.contrib.auth.models import User
from main import validator
User._meta.get_field('email')._unique = True
User._meta.get_field('email').validators = [
    validator.validate_email]
User._meta.get_field('username').validators = [
    validator.validate_username]


def group_based_upload_to(instance, filename):
   return "profiles/images/{}/{}".format(instance.user.id, filename)


class Profile(models.Model):
   class nationality_choices(models.TextChoices):
      SA = "Saudi Arabia"
      UAE = "United Arab Emirates"

   class gender_choices(models.TextChoices):
      null = ""
      Male = "ذكر"
      Female = "انثى"

   user = models.OneToOneField(User, on_delete=models.CASCADE)
   phone = models.CharField(max_length=10, unique=True, validators=[
                            validator.validate_phone])
   avatar = models.ImageField(
       upload_to=group_based_upload_to, default="profiles/images/user-defualt.svg")
   gender = models.CharField(max_length=22,
                             choices=gender_choices.choices,
                             default=gender_choices.null)
   nationality = models.CharField(max_length=20,
                                  choices=nationality_choices.choices,
                                  default=nationality_choices.SA)
   address = models.TextField()
   about = models.TextField()

   def __str__(self) -> str:
      return f"{self.user.username} profile"





class Cart(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   product = models.ForeignKey(Product, on_delete=models.CASCADE)
   quantity = models.IntegerField()
