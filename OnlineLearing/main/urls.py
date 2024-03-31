from . import views
from django.urls import path


app_name  = "main"

urlpatterns = [
    path("", views.index_view, name="index_view"),
    path("post/add/",views.add_courses_view, name="add_courses_view"),
    path("post/about/",views.add_about_view, name="add_about_view"),



    


    
]