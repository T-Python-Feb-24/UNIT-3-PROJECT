from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    
    content = models.TextField()
    published_at = models.DateTimeField(auto_now_add=True)
    poster = models.ImageField(upload_to="images/", default="images/default.jpeg")


    #string representation
    def __str__(self):
        return self.title
    


class Comment(models.Model):

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.full_name} - {self.post.title}"
