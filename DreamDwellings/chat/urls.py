from django.urls import path
from . import views

app_name = "chat"

urlpatterns = [
    path('chat-rooms/', views.chat_rooms, name='chat_rooms'),
    path('chat-rooms/<int:room_id>/', views.chat_messages, name='chat_messages'),
]