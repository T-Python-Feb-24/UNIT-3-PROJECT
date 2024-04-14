from django.urls import path
from . import views

app_name="bootcamp"

urlpatterns = [
    path("Bootcamps/",views.all_bootcamps,name="all_bootcamps"),
    path("add/bootcamp/",views.add_bootcamp,name="add_bootcamp"),
    path("<bootcamp_id>/bootcamp/students/",views.bootcamp_details,name="bootcamp_details"),
    path("<bootcamp_id>/students/evaluation",views.students_evaluation,name="students_evaluation")

]

