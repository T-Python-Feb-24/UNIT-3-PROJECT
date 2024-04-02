from django.urls import path
from . import views

app_name = 'bidding'

urlpatterns = [
    path('bid/', views.bid_view, name='bid'),
    # Add more URL patterns as needed
]
