from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from datetime import date, timedelta
import math
# Create your views here.
from .models import Post, Comment

def index_view(request: HttpRequest):

    #getting the Query Parameters
    print(request.GET)

    #get user info
    if request.user.is_authenticated:
        print(request.user.first_name)

    #limiting the result using slicing
    posts = Post.objects.all()
    comments = Comment.objects.all()


    return render(request, "main/index.html", {"posts" : posts, "comments" : comments})

def add_post_view(request: HttpRequest):

    if request.method == 'POST':
        try:
            new_post = Post(content=request.POST["content"], poster=request.FILES["poster"])
            new_post.save()
            return redirect("main:index_view")
        except Exception as e:
            print(e)

    return render(request, "main/add_post.html")

def post_detail_view(request:HttpRequest, post_id):

    try:
        #getting a  post detail
        post = Post.objects.get(pk=post_id)
        comments = Comment.objects.filter(post=post) #this is to get the comments on the above post using filter
        
    except Post.DoesNotExist:
        return render(request, "main/not_found.html")
    except Exception as e:
        print(e)


    return render(request, "main/post_detail.html", {"post" : post, "comments" : comments, })

def update_post_view(request:HttpRequest, post_id):

    post = Post.objects.get(pk=post_id)

    if request.method == "POST":
        try:
            
            post.content = request.POST["content"]
            post.poster = request.FILES.get("poster", post.poster)
            post.save()
            return redirect("main:post_detail_view", post_id=post.id)
        except Exception as e:
            print(e)

    
    return render(request, 'main/update_post.html', {"post" : post,})

def delete_post_view(request:HttpRequest, post_id):

    try:
        post = Post.objects.get(pk=post_id)
        post.delete()
    except Exception as e:
        print(e)
    

    return redirect("main:index_view")

def posts_search_view(request:HttpRequest):
    posts = []

    if "search" in request.GET:
        posts = Post.objects.filter(content__contains=request.GET["search"])

    if "date" in request.GET and len(request.GET["date"]) > 4:
        first_date = date.fromisoformat(request.GET["date"])
        end_date = first_date + timedelta(days=1)
        posts = posts.filter(published_at__gte=first_date, published_at__lt=end_date)


    return render(request, "main/search_page.html", {"posts" : posts})

def add_comment_view(request:HttpRequest, post_id):

    if not request.user.is_authenticated:
        return redirect("accounts:login_user_view")

    if request.method == "POST":
        #add new comment
        post_object = Post.objects.get(pk=post_id)
        new_comment = Comment(post=post_object,user=request.user, content=request.POST["content"])
        new_comment.save()

    
    return redirect("main:post_detail_view", post_id=post_id)