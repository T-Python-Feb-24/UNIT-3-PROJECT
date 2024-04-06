from django.urls import path
from . import views

app_name="student"

urlpatterns = [
    path("<student_username>/profile",views.student_profile,name="student_profile"),
    path("new/project/",views.new_project,name="new_project"),
    path("update/<student_username>/profile",views.update_student,name="update_student")
    
]

