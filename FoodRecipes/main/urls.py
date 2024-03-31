from django.urls import path
from . import views

app_name = "main"

urlpatterns  = [
    path("", views.home, name="home"),
    path("add/recipes/",views.add_recipes,name="add_recipes"),
    path("all/recipes/",views.all_recipes,name="all_recipes")
    ]