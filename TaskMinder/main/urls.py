from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.home_page, name="home_page"),
    path("my/tasks/", views.tasks, name="tasks"),
    path("tasks/search/", views.task_search, name="task_search"),
    path("task/detail/", views.task_detail, name="task_detail"),
    path("add/comment/<project_id>", views.add_comment, name="add_comment"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path('send/email/', views.send_email, name='send_email'),
    path('create/', views.create_task, name='create_task'),

]