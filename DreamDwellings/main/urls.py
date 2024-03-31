from django.urls import path
from . import views

app_name = "main"

urlpatterns  = [
    path("", views.index_view, name="index_view"),
    path('about/', views.about, name='about'),
#     path('contact/success/', views.contact_success, name='contact_success'),
]