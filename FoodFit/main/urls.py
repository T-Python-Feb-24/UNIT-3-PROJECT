
from django.urls import path
from . import views

app_name = "main"

urlpatterns  = [
   path("",views.home,name="home"),
   path("all/recipe/",views.all_recipe,name="all_recipe_page"),
   path("add/recipe/",views.add_recipe,name="add_recipe_page"),
   path("update/<recipe_id>/recipe/",views.update_recipe,name="update_recipe_page"),
   path("delete/<recipe_id>/recipe/",views.delete_recipe,name="delete_recipe_view"),
   path("detail/<recipe_id>/recipe/",views.detail_recipe,name="detail_recipe_page"),
   path("search/recipe/",views.search_recipe,name="search_recipe_page"),
   path("contact/us/",views.contact_us,name="contact_us_page"),
   path("user/message/",views.user_message,name="user_message_page"),
   path("delete/<msg_id>/message/",views.delete_message,name="delete_message_view"),
   path("comments/<recipe_id>/",views.comments,name="comments_view"),
   path("not/allowed/",views.allowed,name="not_allowed_page"),
   path("search/food/",views.search_food,name="search_food_page"),


]
