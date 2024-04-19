from django.contrib import admin
from .models import Project 
# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("Student","name","project_type","screenshot")
    
admin.site.register(Project,ProjectAdmin)
    