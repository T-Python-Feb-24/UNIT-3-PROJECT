from django.contrib import admin
from .models import Recipe, Contact, Review

# Register your models here.
class PublisherAdmin(admin.ModelAdmin):
    list_display= ('title', 'category', 'created_at')

    list_filter= ('category', 'created_at',)

class PublisherCon(admin.ModelAdmin):
    list_display= ('first_name', 'last_name', 'email', 'created_at')

class PublisherRev(admin.ModelAdmin):
    list_display= ('recipe', 'user', 'created_at')

admin.site.register(Recipe, PublisherAdmin)
admin.site.register(Contact, PublisherCon)
admin.site.register(Review, PublisherRev)