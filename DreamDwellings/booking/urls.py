from django.urls import path
from . import views

app_name = 'booking'

urlpatterns = [
    
    path('buy-now/<int:place_id>/', views.buy_now, name='buy_now'),
    path('book-now/<int:place_id>/', views.book_now, name='book_now'),
    path('buy-success/', views.buy_success, name='buy_success'),
    path('book-success/', views.book_success, name='book_success'),
]
