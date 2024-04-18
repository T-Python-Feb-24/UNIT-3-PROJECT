from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.home_page, name="home_page"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("tasks/", views.task_list, name="tasks"),
    path("journal/", views.journal, name="journal"),
    path("reading/list/", views.reading_list, name="reading_list"),
    path("notes/", views.notes, name="notes"),
    path("yearly/goals/", views.yearly_goals, name="yearly_goals"),
]