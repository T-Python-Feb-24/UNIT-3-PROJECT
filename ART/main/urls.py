from.import views
from django.urls import path
from django.contrib.auth.models import User

app_name  = "main"

urlpatterns=[
    path('', views.home, name='home'),
    path('images/new/', views.add_images, name='add_images'),
    path('images/all/', views.all_images, name='all_images'),
    path('images/<blog_id>/detail/', views.detail_images, name='detail_images'),
    path('images/<blog_id>/delete/', views.delete_images, name='delete_images'),
    path('images/search/', views.search, name='search'),
    path("comments/add/<blog_id>/", views.add_comment, name="add_comment"),
    path("images/contact/",views.contact_us,name="contact"),
    path("users/massage/",views.user_message,name="user_message"),
   
]