from django.db import models
from main.models import Prodect
from django.contrib.auth.models import User
User._meta.get_field('email')._unique = True


def group_based_upload_to(instance, filename):
   return "images/{}/{}".format(instance.user.id, filename)


class Profile(models.Model):
   class nationality_choices(models.TextChoices):
      SA = "Saudi Arabia"
      UAE = "United Arab Emirates"

   class gender_choices(models.TextChoices):
      Male = "Male"
      Female = "Female"

   user = models.OneToOneField(User, on_delete=models.CASCADE)
   phone = models.CharField(max_length=10, unique=True)
   avatar = models.ImageField(
       upload_to=group_based_upload_to, default="images/profiles/user-defualt.svg")
   gender = models.CharField(max_length=22,
                             choices=gender_choices.choices,
                             default=gender_choices.Male)
   nationality = models.CharField(max_length=20,
                                  choices=nationality_choices.choices,
                                  default=nationality_choices.SA)
   address = models.TextField()
   about = models.TextField()

   def __str__(self) -> str:
      return f"{self.user.username} profile"


class Favorite(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   prodect = models.ForeignKey(Prodect, on_delete=models.CASCADE)


class cart(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   prodect = models.ForeignKey(Prodect, on_delete=models.CASCADE)
   quantity = models.IntegerField()
