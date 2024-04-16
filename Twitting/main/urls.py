from django.urls import path
from . import views

app_name = "main"

urlpatterns  = [
    path("", views.index_view, name="index_view"),
    path("post/add/", views.add_post_view, name="add_post_view"),
    path("post/detail/<post_id>/", views.post_detail_view, name="post_detail_view"),
    path("post/update/<post_id>/", views.update_post_view, name="update_post_view"),
    path("post/delete/<post_id>/", views.delete_post_view, name="delete_post_view"),
    path("posts/search/", views.posts_search_view, name="posts_search_view"),
    path("comments/add/<post_id>/", views.add_comment_view, name="add_comment_view")
]