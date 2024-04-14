from django.urls import path
from . import views

app_name = "main"

urlpatterns  = [
    path("", views.index_view, name="index_view"),
    
    path("add/event/", views.add_event_view, name="add_event_view"),
    path("edit/event/<event_id>/", views.edit_event_view, name="edit_event_view"),
    path("event/detail/<event_id>/", views.event_detail_view, name="event_detail_view"),
    path("event/delete/<event_id>/", views.delete_event_view, name="delete_event_view"),
    path("all/events/", views.all_events_view, name="all_events_view"),
    path("search/events/", views.search_events_view, name="search_events_view"),

]