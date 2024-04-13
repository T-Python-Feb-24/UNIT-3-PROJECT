from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ContactClub(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message_content = models.TextField()
    message_date_time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f"{self.user.username} - {self.message_content}"


class Event(models.Model):

    #themes choices
    themes = models.TextChoices("Theme", ["DataScience", "NetWork", "CyberSecurity", "SoftwareEngineering", "ArtificialIntelligence"])
    types = models.TextChoices("Type", ["Workshop", "Program", "Meeting", "Challenges"])
    

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    event_title = models.CharField(max_length=30) 
    event_description = models.TextField()
    objective = models.TextField()
    event_img = models.ImageField(upload_to="images/", default="images/event-default.png")
    on_site = models.BooleanField()
    theme = models.CharField(max_length=64, choices=themes.choices)
    event_type = models.CharField(max_length=64, choices=types.choices)
    event_date = models.DateField(auto_now=False, auto_now_add=False)
    time_start = models.TimeField(auto_now=False, auto_now_add=False)
    time_end = models.TimeField(auto_now=False, auto_now_add=False)


     #string representation
    def __str__(self):
        return self.event_title
