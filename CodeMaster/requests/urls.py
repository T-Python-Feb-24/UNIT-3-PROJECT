from django.urls import path
from . import views

app_name='requests'

urlpatterns=[
    path("order/",views.order_page,name="order_page"),
]