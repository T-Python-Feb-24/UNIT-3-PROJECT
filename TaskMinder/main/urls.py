from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.home_page, name="home_page"),
    path("my/tasks/", views.tasks, name="tasks"),
    path("tasks/search/", views.task_search, name="task_search"),
    path("task/detail/", views.task_detail, name="task_detail"),
    path("add/comment/", views.add_comment, name="add_comment"),
]