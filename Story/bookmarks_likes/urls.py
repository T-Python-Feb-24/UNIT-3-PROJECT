from django.urls import path
from . import views

app_name = 'bookmarks_likes'

urlpatterns = [
    path('story/<int:story_id>/bookmark/', views.toggle_bookmark, name='toggle_bookmark'),
    path('story/<int:story_id>/like/', views.toggle_like, name='toggle_like'),
    path('saved_stories/', views.saved_stories, name='saved_stories'),
]