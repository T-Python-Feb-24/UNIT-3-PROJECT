from django.urls import path
from . import views
app_name = "product"

urlpatterns  = [
    path("", views.home_view, name="home_view"),
    path("product/all/", views.product_list_view, name="product_list_view"),
    path("product/add/", views.product_add_view, name="product_add_view"),
    path("product/detail/<product_id>/", views.product_detail_view, name="product_detail_view"),
    path("produt/edite/<product_id>/", views.product_edit_view, name="product_edit_view"),
    path("product/delete/<product_id>/", views.product_delete_view, name="product_delete_view"),
    path("comments/add/<product_id>/", views.add_comment_view, name="add_comment_view"),
    path("rating/add/<product_id>/", views.add_rating_view, name="add_rating_view"),
    path("posts/search/", views.product_search_view, name="product_search_view")
    ]