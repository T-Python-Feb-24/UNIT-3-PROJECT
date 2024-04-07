from django.urls import path
from . import views

app_name = "main"

urlpatterns  = [
    path("", views.index_view, name="index_view"),
    path('about/', views.about, name='about'),
    path('contact/', views.contact_view, name='contact'),
    path("place/add/", views.add_place, name="add_place_view"),
    path('place/<int:place_id>/', views.place_detail, name='place_detail'),
    path('place/add/main/success_page/', views.success_page_view, name='success_page'),
    path('services/', views.services_page, name='services_page'),
    path('places/', views.all_places_view, name='all_places'),
    path("ad/", views.ad, name="ad"),
    path('place/<int:place_id>/update/', views.update_place, name='update_place'),
    path('place/<int:place_id>/delete/', views.delete_place, name='delete_place'),
]