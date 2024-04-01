from django.urls import path
from . import views

app_name = "main"

urlpatterns  = [
    path("", views.index_view, name="index_view"),
    
    # path("add/club/", views.add_club_view, name="add_club_view"),
    # path("edit/club/<club_id>/", views.edit_club_view, name="edit_club_view"),
    # path("club/detail/<club_id>/", views.club_detail_view, name="club_detail_view"),

    path("add/event/", views.add_event_view, name="add_event_view"),
    path("edit/event/<event_id>/", views.edit_event_view, name="edit_event_view"),
    path("event/detail/<event_id>/", views.event_detail_view, name="event_detail_view"),
]