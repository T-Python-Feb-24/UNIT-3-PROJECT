from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from main.models import Post
from .models import Favorite
from django.contrib.auth.models import User


# Create your views here.


def add_remove_favorites_view(request: HttpRequest, post_id):

    if not request.user.is_authenticated:
        return redirect("accounts:login_user_view")
    
    try:
        post = Post.objects.get(pk=post_id)

        #check if user already favored this post
        favored_post = Favorite.objects.filter(user=request.user, post=post).first()

        if not favored_post:
            favorite = Favorite(user=request.user, post=post)
            favorite.save()
        else:
            #delete favorite if already exists
            favored_post.delete()
    
    except Exception as e:
        print(e)


    return redirect("main:post_detail_view", post_id=post_id)


def user_favorites_view(request: HttpRequest):

    

    return render(request, "favorites/favorites.html")