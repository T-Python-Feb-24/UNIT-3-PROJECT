from django.urls import path
from . import views

app_name = 'rooms'

urlpatterns = [
    path('all/rooms/', views.all_rooms_view, name='all_rooms_view')
]