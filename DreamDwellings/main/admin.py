from django.contrib import admin
from .models import Place
# Register your models here.
class PlaceAdmin(admin.ModelAdmin):
    
    list_display = ['name', 'category' ]
    
    list_filter =  ['category']

admin.site.register(Place, PlaceAdmin)