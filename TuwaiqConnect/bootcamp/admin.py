from django.contrib import admin
from .models import Bootcamp,Evaluation
# Register your models here.

class BootcampAdmin(admin.ModelAdmin):
    list_display=("bootcamp_name","desc")
    
admin.site.register(Bootcamp,BootcampAdmin)

class EvaluationAdmin(admin.ModelAdmin):
    list_display = ("student","bootcamp","attendance_rate","grades_rate")
    
admin.site.register(Evaluation, EvaluationAdmin)
