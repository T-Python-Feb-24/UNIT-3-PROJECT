from django.contrib import admin

from .models import Place, Contact

class PlaceAdmin(admin.ModelAdmin):
    list_display = ['name', 'category' ]
    list_filter =  ['category']

admin.site.register(Place, PlaceAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", 'email', 'created_at']
    list_filter = ['created_at']
    
admin.site.register(Contact, ContactAdmin)
