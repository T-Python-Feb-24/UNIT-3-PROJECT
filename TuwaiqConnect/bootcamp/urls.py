from django.urls import path
from . import views

app_name="bootcamp"

urlpatterns = [
    
    path("Bootcamps/",views.all_bootcamps,name="all_bootcamps"),
    path("add/bootcamp/",views.add_bootcamp,name="add_bootcamp"),
    path("<bootcamp_id>/bootcamp/students/",views.bootcamp_details,name="bootcamp_details"),
    path("<bootcamp_id>/<student_id>/evaluation",views.students_evaluation,name="student_evaluation"),
    path("<staff_username>/staff/profile",views.staff_profile,name="staff_profile")

]

