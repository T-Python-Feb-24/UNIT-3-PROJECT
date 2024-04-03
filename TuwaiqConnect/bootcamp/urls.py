from django.urls import path
from . import views

app_name="bootcamp"

urlpatterns = [
    path("Bootcamps/",views.all_bootcamps,name="all_bootcamps"),
    path("add/bootcamp/",views.add_bootcamp,name="add_bootcamp")
]

