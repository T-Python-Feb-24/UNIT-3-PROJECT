from django.contrib import admin
from .models import Contact
# Register your models here.
class contact_us(admin.ModelAdmin):
    list_display=["username","email","subject","message","created_at"]
admin.site.register(Contact,contact_us)