from django.urls import path
from . import views

app_name="accounts"

urlpatterns=[
    path("login/" ,views.login_page ,name="login_page"),
    path("register/" ,views.register_page , name="register_page"),
    path("logout/", views.logout_user,name="logout_user"),
    path("dashborad/",views.dashborad_page,name="dashborad_page"),
    path("update/",views.update_profile_page,name="update_profile_page")
    
]