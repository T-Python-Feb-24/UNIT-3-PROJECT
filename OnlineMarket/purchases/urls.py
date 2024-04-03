from django.urls import path
from . import views

app_name  = "purchases"

urlpatterns = [
    path("add/<product_id>/", views.product_cart_view, name="product_cart_view"),
    path("user/cart/", views.cart_view, name="cart_view"),
    path("delete/cart/<product_id>/", views.delete_product_view, name="delete_product_view"),
    path("checkout/", views.checkout_view, name="checkout_view"),
    
    #path("order/", views.order_complete_view, name="order_complete_view"),
]