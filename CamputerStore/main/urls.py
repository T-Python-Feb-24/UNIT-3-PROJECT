from django.urls import path
from . import views


app_name = "main"
urlpatterns = [
    path('', views.index_view, name="index_view"),
    path("contactus/", views.contactus_view, name="contactus_view"),
    path("about/", views.about_view, name="about_view"),
    path("search/", views.search_product_view, name="search_product_view"),
    path("add/product/", views.add_product_view, name="add_product_view"),
    path("product/<product_name>/", views.product_detail_view,
         name="product_detail_view"),

]
