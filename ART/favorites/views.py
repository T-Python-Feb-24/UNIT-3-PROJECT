from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from main.models import Blog
from .models import Favorite
from django.contrib.auth.models import User


# Create your views here.


def add_remove_favorites_view(request: HttpRequest, blog_id):

    if not request.user.is_authenticated:
        return redirect("account:login_user_view")
    
    try:
        art = Blog.objects.get(pk=blog_id)

        #check if user already favored this post
        favored_post = Favorite.objects.filter(user=request.user, Blog=art).first()

        if not favored_post:
            favorite = Favorite(user=request.user, Blog=art)
            favorite.save()
        else:
            #delete favorite if already exists
            favored_post.delete()
    
    except Exception as e:
        print(e)


    return redirect("main:detail_images", blog_id=blog_id)


def user_favorites_view(request: HttpRequest):

    

    return render(request, "favorites/favorites.html")