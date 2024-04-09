from django.contrib import admin
from .models import Comments, Contactus
from product.models import Product, ProductImage
from account.models import Profile, Cart
from favorites.models import Favorite


class ImageInline(admin.TabularInline):
   model = ProductImage
   extra = 1


class productAdmin(admin.ModelAdmin):
   inlines = [
       ImageInline,
   ]


admin.site.register(Product, productAdmin)
admin.site.register(Comments)
admin.site.register(Contactus)
admin.site.register(Profile)
admin.site.register(Cart)
admin.site.register(Favorite)
