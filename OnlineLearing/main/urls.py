from . import views
from django.urls import path


app_name  = "main"

urlpatterns = [
    path("", views.index_view, name="index_view"),
    path("post/add/",views.add_courses_view, name="add_courses_view"),
    path("post/about/",views.add_about_view, name="add_about_view"),
    path("post/all/",views.all_courses_view, name="all_courses_view"),
    path("post/detail/<post_id>/", views.post_detail_view, name="post_detail_view"),
    path("post/update/<post_id>/", views.update_post_view, name="update_post_view"),
    path("post/delete/<post_id>/", views.delete_post_view, name="delete_post_view"),
    path("post/register/" ,views.register_courses_view , name= "register_courses_view"),
    path("posts/search/", views.posts_search_view, name="posts_search_view"),
    

]