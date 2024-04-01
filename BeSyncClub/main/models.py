from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class club(models.Model):

    university_name = models.CharField(max_length=2000)
    about_club = models.TextField()
    club_email = models.EmailField()
    club_header = models.ImageField(upload_to="images/", default="images/default.jpeg")
    x_link = models.URLField(blank=True)
    join_at = models.DateTimeField(auto_now_add=True)


    #string representation
    def __str__(self):
        return self.university_name
    

    

