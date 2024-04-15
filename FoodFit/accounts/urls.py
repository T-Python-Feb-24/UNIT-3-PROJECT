from django.urls import path
from . import views

app_name  = "accounts"

urlpatterns = [
    path("register/", views.register_user_view, name="register_user_view"),
    path("login/", views.login_user_view, name="login_user_view"),
    path("logout/", views.logout_user_view, name="logout_user_view"),
    path("profile/<user_id>/", views.user_profile, name="user_profile_page"),
    path("update/profile/<user_id>/", views.update_user_profile, name="update_user_profile_view"),
]