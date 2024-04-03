from django.contrib import admin
from .models import Bootcamp
# Register your models here.

class BootcampAdmin(admin.ModelAdmin):
    list_display=("bootcamp_name","desc")
    
admin.site.register(Bootcamp,BootcampAdmin)
