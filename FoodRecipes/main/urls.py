from django.urls import path
from . import views

app_name = "main"

urlpatterns  = [
    path("", views.home, name="home"),
    path("add/recipes/",views.add_recipes,name="add_recipes"),
    path("all/recipes/",views.all_recipes,name="all_recipes"),
    path("detail/<recipes_id>/recipes/",views.detail_recipes,name="detail_recipes"),
    path("suggestions/<recipes_id>/",views.suggestions,name="suggestions"),
    path("recipes/search",views.recipes_search,name="recipes_search"),
    path("comments/add/<recipes_id>/", views.add_comment, name="add_comment"),
    path("plants/<recipes_id>/update/", views.update_recipes, name="update_recipes"),
    path("plants/<recipes_id>/delete/", views.delete_recipes, name="delete_recipes"),
    path("suggestions/msg", views.suggestions_msg, name="suggestions_msg"),
    # path('recipes/<int:recipe_id>/repost/', views.repost_recipe, name='repost_recipe'),

    ]