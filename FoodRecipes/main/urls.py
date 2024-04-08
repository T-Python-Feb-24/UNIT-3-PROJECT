from django.urls import path
from . import views

app_name = "main"

urlpatterns  = [
    path("", views.home, name="home"),
    path("all/recipes/",views.all_recipes,name="all_recipes"),
    path("add/recipes/",views.add_recipes,name="add_recipes"),
    path("comments/add/<recipes_id>/", views.add_comment, name="add_comment"),
    path("detail/<recipes_id>/recipes/",views.detail_recipes,name="detail_recipes"),
    path("plants/<recipes_id>/update/", views.update_recipes, name="update_recipes"),
    path("plants/<recipes_id>/delete/", views.delete_recipes, name="delete_recipes"),
    path("recipes/search",views.recipes_search,name="recipes_search"),
    path("suggestions/<recipes_id>/",views.suggestions,name="suggestions"),
    path("suggestions/msg", views.suggestions_msg, name="suggestions_msg"),
    

    ]