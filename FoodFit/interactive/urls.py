from django.urls import path
from . import views

app_name  = "interactive"

urlpatterns = [
    path("recipe/",views.user_recipe,name="user_recipe_page"),
    path("add/recipe/",views.add_user_recipe,name="add_user_recipe_page"),
    path("recipe/detail/",views.user_recipe_detail,name="user_recipe_detail_page"),



]