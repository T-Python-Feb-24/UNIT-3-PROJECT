from django.urls import path
from . import views

app_name  = "accounts"

urlpatterns = [
    path("signup/", views.sign_up, name="sign_up"),
    path("signin/", views.sign_in, name="sign_in"),
    path("logout/", views.logout_user, name="logout_user"),
    path("profile/<user_name>/", views.user_profile, name="user_profile"),
    path("update/", views.update_profile , name="update_profile")
]