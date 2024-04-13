from django.urls import path
from . import views

app_name='requests'

urlpatterns=[
    path("order/new/",views.order_page,name="order_page"),
    path("update/<order_id>/",views.order_update_page ,name="order_update_page"),
    path("delete/<order_id>/",views.delete_order,name="delete_order"),
    path("order/details/<order_id>/",views.order_details, name="order_details")
]