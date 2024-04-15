from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home, name='home'),
    path('recipes/new/', views.add_recipe, name='add_recipe'),
    path('recipes/all/', views.all_recipes, name='all_recipes'),
    path('recipes/<recipe_id>/detail/', views.recipe_detail, name='recipe_detail'),
    path('recipes/<recipe_id>/update/', views.update_recipe, name='update_recipe'),
    path('recipes/<recipe_id>/delete/', views.delete_recipe, name='delete_recipe'),
    path('recipes/search/', views.search, name='search'),
    path('recipes/contact_us/', views.contact, name='contact'),
    path('recipes/contact_us/messages', views.messages, name='message'),
    path("reviews/<recipe_id>/add/", views.add_review, name="add_review"),
]