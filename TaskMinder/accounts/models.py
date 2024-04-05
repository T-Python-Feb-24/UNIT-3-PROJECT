from django.db import models
from django.contrib.auth.models import User
from django.templatetags.static import static


# Create your models here.

class Profile(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    about = models.TextField()
    avatar = models.ImageField(upload_to="images/", default="images/default.jpeg")

    def __str__(self) -> str:
        return f"{self.user.first_name} profile"
    


# class User(AbstractBaseUser):
#     GenderChoice = 
#     ('others', 'Others'),
#     ('male', 'Male'),
#     ('female' :'Female')

#     gender = models.CharField(choice=GenderChoice)
#     pro_pic = models.ImageField(upload_to ="", null=True)
#     default_pic_mapping = { 'others': '00.png', 'male': '01.png', 'female': '02.png'}

#     def get_profile_pic_url(self):
#         if not self.pro_pic:
#             return static('img/{}'.format(self.default_pic_mapping[self.gender]))
#         return self.pro_pic.url