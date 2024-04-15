from django.urls import path
from . import views

app_name  = "interactive"

urlpatterns = [
    path("recipe/",views.users_recipe,name="users_recipe_page"),
    path("add/recipe/",views.add_user_recipe,name="add_user_recipe_page"),
    path("recipe/<recipe_id>/detail/",views.user_recipe_detail,name="user_recipe_detail_page"),
    path("user/<recipe_id>/comment",views.comments,name="comments_view"),
    path("update/<recipe_id>/recipe/",views.update_recipe,name="update_recipe_page"),
    path("delete/<recipe_id>/recipe/",views.delete_recipe,name="delete_recipe_view"),
    path("delete/<com_id>/comment/",views.delte_comment,name="delete_comment_view"),

]