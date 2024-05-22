from django.urls import path
from . import views


app_name = 'main'

urlpatterns = [
    path('', views.home, name='home'),
    path('surveys/', views.survey_list, name='survey_list'),
    path('survey/<int:id>/', views.survey_detail, name='survey_detail'),
    path('create/', views.create_survey, name='create_survey'),
    path('results/<int:survey_id>/', views.survey_results, name='survey_results'),
    path('submit/<int:survey_id>/', views.submit_survey, name='submit_survey'),
    path('delete_survey/<int:survey_id>/', views.delete_survey, name='delete_survey'),
    path('manage_users/', views.manage_users, name='manage_users'),
    path('learn_more/', views.learn_more, name='learn_more'),
]

