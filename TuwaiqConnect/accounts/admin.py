from django.contrib import admin
from .models import Student,Orgnization

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
   list_display = ("user","collage_name","graduation_year","major","approved")
    
admin.site.register(Student,StudentAdmin)

class OrgnizationAdmin(admin.ModelAdmin):
    # list_display =("user","about")
    pass