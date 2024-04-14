from django.contrib import admin
from .models import Story

# Register your models here.
class Adminmain (admin.ModelAdmin):

   list_display=['name','category','content','content','created_at']

admin.site.register(Story , Adminmain)