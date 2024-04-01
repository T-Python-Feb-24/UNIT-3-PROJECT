from django.contrib import admin
from .models import Event

# Register your models here.

#customizing the admin panel for a Model
class EventAdmin(admin.ModelAdmin):
    #list to customize the columns
    list_display = ['event_title', 'on_site', 'event_date_time', '']
    #adding fliters
    list_filter =  ['theme']

admin.site.register(Event, EventAdmin)
