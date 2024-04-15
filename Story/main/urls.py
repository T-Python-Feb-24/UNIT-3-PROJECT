from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static
from main.views import home

app_name  = "main"

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_story, name='add_story'),
    path('story/<int:pk>/', views.show_story, name='show_story'), 
    path('all_stories/', views.all_stories, name='all_stories'),
    path('story/<int:pk>/update/', views.update_story, name='update_story'),
    path('story/<int:pk>/delete/', views.delete_story, name='delete_story'),
    path('story/<int:story_id>/comment/', views.add_comment, name='add_comment'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path("mode/dark/", views.dark_mode, name="dark_mode"),
    path("mode/light/", views.light_mode, name="light_mode"),
    path('contact_us_messages/', views.contact_us_messages, name='contact_us_messages'),
    path('save_contact_message/', views.save_contact_message, name='save_contact_message'),
    path('comment/<int:comment_id>/delete/<int:story_id>/', views.delete_comment, name='delete_comment'),
    path('category/<str:category_name>/', views.category_stories, name='category_stories'),
    path('no_access/', views.no_access, name='no_access'),
    path('about-us/', views.about_us, name='about_us'),
    path('faq/', views.faq, name='faq'),
    path('help/', views.help_page, name='help'),
]