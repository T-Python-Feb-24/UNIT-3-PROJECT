from django.urls import path
from . import views


app_name = "product"
urlpatterns = [
    path("search/", views.search_product_view, name="search_product_view"),
    path("add/", views.add_product_view, name="add_product_view"),
    path("<category>/", views.product_by_category, name="product_by_category"),
    path("prod/<product_name>/", views.product_detail_view,
         name="product_detail_view"),

]
