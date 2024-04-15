from django.contrib import admin
from .models import Order,Rating
# Register your models here.
admin.site.register(Order)

class rate(admin.ModelAdmin):
    list_display=["user","order","rate","comment"]
admin.site.register(Rating,rate)