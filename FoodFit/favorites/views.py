from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Favorite , RecipeFavorite 
from django.contrib.auth.models import User
from main.models import Recipe , Comment
from interactive.models import UserRecipe

# Create your views here.


def add_remove_favorites(request: HttpRequest, recipe_id):

    if not request.user.is_authenticated:
        return redirect("accounts:login_user_view")
    
    try:
        recipe = UserRecipe.objects.get(pk=recipe_id)

        #check if user already favored this post
        favored_user_recipe = Favorite.objects.filter(user=request.user, recipe=recipe).first()

        if not favored_user_recipe:
         favorite_user = Favorite(user=request.user, recipe=recipe)
         favorite_user.save()
        else:
            #delete favorite if already exists
            favored_user_recipe.delete()
    
    except Exception as e:
        print(e)


    return redirect("interactive:user_recipe_detail_page", recipe_id=recipe_id)


def recipe_favorites(request: HttpRequest,recipe_id):

    if not request.user.is_authenticated:
        return redirect("accounts:login_user_view")
    
    try:
        recipe = Recipe.objects.get(pk=recipe_id)

        #check if user already favored this post
        favored_recipe = RecipeFavorite.objects.filter(user=request.user, recipe=recipe).first()

        if not favored_recipe:
         favorite = RecipeFavorite(user=request.user, recipe=recipe)
         favorite.save()
        else:
            #delete favorite if already exists
            favored_recipe.delete()
    
    except Exception as e:
        print(e)


    return redirect("main:detail_recipe_page", recipe_id=recipe_id)











def user_favorites(request: HttpRequest ):
   

 return render(request, "main/favorites.html")