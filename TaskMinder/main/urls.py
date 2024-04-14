from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.home_page, name="home_page"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("tasks/", views.task_list, name="tasks"),
    path('create/', views.create_task, name='create_task'),
    # path("tasks/search/", views.task_search, name="task_search"),
    path("task/detail/", views.task_detail, name="task_detail"),
    path("add/comment/<project_id>", views.add_comment, name="add_comment"),
    path("journal", views.journal, name="journal"),
    path("reading/list/", views.reading_list, name="reading_list"),
    path("notes/", views.notes, name="notes"),
    path("yearly/goals/", views.yearly_goals, name="yearly_goals"),
    # path('send/email/', views.send_email, name='send_email'),
]