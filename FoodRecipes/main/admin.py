from django.contrib import admin
from .models import Recipes,Comment,Suggestions
 
class RecipesAdmin(admin.ModelAdmin):
    
    list_display = ['name','content','published_at','image','time_coocking','number_people','category']
    
    list_filter =  ['name',]

admin.site.register(Recipes, RecipesAdmin)
admin.site.register(Comment)
admin.site.register(Suggestions)

