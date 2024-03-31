
from django.urls import path
from . import views

app_name = "main"

urlpatterns  = [
   path("",views.home,name="home"),
   path("search/food/",views.search_food,name="search_food_page"),


]
