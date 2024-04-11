from django.urls import path
from . import views

app_name="orgnaization"

urlpatterns = [
    path("organization/",views.organization_home_page,name="organization_home_page"),
    path("students/acquisition/",views.students_acquisition,name="students_acquisition"),
]

