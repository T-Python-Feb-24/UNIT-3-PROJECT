from django.urls import path
from . import views

app_name  = "favorites"

urlpatterns = [
    path("add/<recipe_id>/", views.add_remove_favorites, name="add_remove_favorites_view"),
    path("user/favorites/", views.user_favorites, name="user_favorites_view"),
    path("recipe/<recipe_id>/favorites/", views.recipe_favorites, name="recipe_favorites_view"),
    
]