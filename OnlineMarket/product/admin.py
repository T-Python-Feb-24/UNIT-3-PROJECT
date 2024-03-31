from django.contrib import admin
from .models import Product,Comment,Review
# Register your models here.
admin.site.register(Product)
admin.site.register(Comment)

class ReviewAdmin(admin.ModelAdmin):
   list_display=('product','user','rating')
admin.site.register(Review, ReviewAdmin)