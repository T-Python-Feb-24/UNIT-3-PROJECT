from django.urls import path
from . import views

app_name='main'

urlpatterns=[
    path("",views.index_page,name="index_page"),
    path("about/",views.about_page,name="about_page"),
    path("contact/" ,views.contact_page,name="contact_page"),
]