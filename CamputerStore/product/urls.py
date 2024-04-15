from django.urls import path
from . import views


app_name = "product"
urlpatterns = [
    path("search/", views.search_product_view, name="search_product_view"),
    path("add/", views.add_product_view, name="add_product_view"),
    path("update/<product_id>/", views.update_product_view, name="update_product_view"),
    path("delete/<product_id>/", views.delete_product_view, name="delete_product_view"),
    path("<category>/", views.product_by_category, name="product_by_category"),
    path("prod/<product_id>/", views.product_detail_view,
         name="product_detail_view"),

]
