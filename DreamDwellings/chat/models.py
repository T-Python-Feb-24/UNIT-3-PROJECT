from django.db import models
from django.contrib.auth.models import User
from main.models import Place
# Create your models here.

class Chat (models.Model):
    content = models.CharField(max_length=1000)
    timestamp = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Place = models.ForeignKey(Place, on_delete=models.CASCADE)
    room = models.ForeignKey('ChatRoom',on_delete=models.CASCADE)
    
class ChatRoom (models.Model):
    name = models.CharField(max_length=1000)