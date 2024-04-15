from django.urls import path
from . import views

app_name  = "favorites"

urlpatterns = [
    path("add/<recipes_id>/", views.add_remove_favorites, name="add_remove_favorites"),
    path("user/<recipes_id>/favorites/", views.user_favorites, name="user_favorites")
]