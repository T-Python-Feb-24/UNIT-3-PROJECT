from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Club(models.Model):

    member = models.ForeignKey(User, on_delete=models.CASCADE) 
    university_name = models.CharField(max_length=200)
    about_club = models.TextField()
    club_email = models.EmailField()
    club_header = models.ImageField(upload_to="images/", default="images/default.jpeg")
    x_link = models.URLField(blank=True)
    join_at = models.DateTimeField(auto_now_add=True)

    #string representation
    def __str__(self):
        return self.university_name
    

class ContactClub(models.Model):
    club = models.OneToOneField(Club, on_delete=models.CASCADE)  
    message_content = models.TextField()
    message_date_time = models.DateTimeField(auto_now_add=True)

class Event(models.Model):

    #themes choices
    themes = models.TextChoices("Theme", ["DataScience", "NetWork", "CyberSecurity", "SoftwareEngineering", "ArtificialIntelligence"])

    event_title = models.CharField(max_length=30) 
    event_description = models.TextField()
    objective = models.TextField()
    event_img = models.ImageField(upload_to="images/", default="images/event-default.png")
    on_site = models.BooleanField()
    theme = models.CharField(max_length=64, choices=themes.choices)
    event_date_time = models.DateTimeField()

     #string representation
    def __str__(self):
        return self.event_title
