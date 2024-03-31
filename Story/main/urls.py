from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from main.views import home

app_name  = "main"

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_story, name='add_story'),
    path('story/<int:pk>/', views.show_story, name='show_story'), 
    path('all_stories/', views.all_stories, name='all_stories'),

]