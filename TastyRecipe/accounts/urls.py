from django.urls import path
from . import views

app_name  = "accounts"

urlpatterns = [
    path("register/", views.register_user_view, name="register"),
    path("login/", views.login_user_view, name="login"),
    path("logout/", views.logout_user_view, name="logout"),
    path("profile/<user_name>/", views.profile_view, name="profile"),
    path("profile/<user_name>/update", views.update_user, name="update_user"),
    path("add/<recipe_id>/", views.add_remove_saved_view, name="add_remove_saved_view"),
    path("user/saved/", views.user_saved_view, name="user_saved_view"),
]