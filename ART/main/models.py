from django.db import models

class Blog(models.Model):

    name =  models.CharField(max_length=200)
    about = models.TextField()
    image = models.ImageField(upload_to='images/', default='images/default_img.jpg')
    is_published = models.BooleanField()
    Categories = models.TextChoices('Category', ["Ornamental drawing","Pointillism", "Cartoon drawing"]) 
    category = models.CharField(max_length = 64, choices = Categories.choices)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
# comment
class Comment(models.Model):
    
    Blog= models.ForeignKey(Blog, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

#Contact

    class Contact(models.Model):
    first_name=models.CharField(max_length = 64)
    last_name=models.CharField(max_length = 64)
    email=models.EmailField(max_length=254)
    message=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)


