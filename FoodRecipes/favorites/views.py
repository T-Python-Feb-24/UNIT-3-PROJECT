from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from main.models import Recipes
from .models import Favorite
from django.contrib.auth.models import User


# Create your views here.


def add_remove_favorites(request: HttpRequest,recipes_id):

    if not request.user.is_authenticated:
        return redirect("accounts:login_user")
    
    try:
        recipes= Recipes.objects.get(pk=recipes_id)

        
        favored_post = Favorite.objects.filter(user=request.user, recipes=recipes).first()

        if not favored_post:
            favorite = Favorite(user=request.user, recipes=recipes)
            favorite.save()
        else:
            
            favored_post.delete()
    
    except Exception as e:
        print(e)


    return redirect("main:detail_recipes", recipes_id=recipes_id)


def user_favorites(request: HttpRequest):

    

    return render(request, "favorites/favorites.html")
