from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from product.models import Product
from .models import Favorite
from django.contrib.auth.models import User


# Create your views here.


def add_remove_favorites_view(request: HttpRequest, product_id):

    if not request.user.is_authenticated:
        return redirect("accounts:login_user_view")
    
    try:
        product = Product.objects.get(pk=product_id)

        #check if user already favored this post
        favored_product = Favorite.objects.filter(user=request.user, product=product).first()

        if not favored_product:
            favorite = Favorite(user=request.user, product=product)
            favorite.save()
           
        else:
             favored_product.delete()
    
    except Exception as e:
            print(e)
    return redirect("product:product_detail_view", product_id=product_id)
       
  

   


def user_favorites_view(request: HttpRequest):
    return render(request, "favorites/favorites.html")