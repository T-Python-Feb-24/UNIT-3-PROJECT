from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from main.models import Product
from .models import Favorite
from django.contrib.auth.models import User


# Create your views here.


def add_remove_favorites_view(request: HttpRequest, prodect_id):

   if not request.user.is_authenticated:
      return redirect("accounts:login_user_view")

   try:
      prodect = Product.objects.get(pk=prodect.pk)

      # check if user already favored this post
      favored_prodect = Favorite.objects.filter(
         user=request.user, prodect=prodect).first()

      if not favored_prodect:
         favorite = Favorite(user=request.user, post=prodect)
         favorite.save()
      else:
         # delete favorite if already exists
         favored_prodect.delete()

   except Exception as e:
      print(e)

   return redirect("main:post_detail_view", prodect_id=prodect_id)


def user_favorites_view(request: HttpRequest):
   try:
      msg = None
      users = request.user.f
   except User.DoesNotExist:
      msg = "Your wishlist is empty. Add some products to your wishlist by clicking the  button in product page."
      return render(request, "account/favorite.html", {"msg": msg})

   return render(request, "favorites/favoriteas.html", {"users": users})
