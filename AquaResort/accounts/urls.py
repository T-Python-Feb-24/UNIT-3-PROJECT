from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('sign/up/', views.sign_up_view, name='sign_up_view'),
    path('login/', views.login_view, name='login_view'),
    path('logout/', views.logout_view, name='logout_view'),
    path('profile/<user_name>/', views.profile_view, name='profile_view')
]