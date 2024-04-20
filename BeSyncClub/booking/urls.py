from django.urls import path
from . import views

app_name  = "booking"

urlpatterns = [
    path("book/<event_id>/", views.book_ticket_view, name="book_ticket_view"),
    path("user/favorites/", views.user_booking_view, name="user_booking_view")
]