from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.splash_screen_view, name='splash_screen_view'),
    path('home/', views.index_view, name='index_view')
]