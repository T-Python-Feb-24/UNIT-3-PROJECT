from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from datetime import date, timedelta
import math
from .models import Course


# Create your views here.
def index_view(request: HttpRequest):
    posts = Course.objects.all()
    return render(request, "main/base.html")

def add_courses_view(request: HttpRequest):

    if not (request.user.is_staff and request.user.has_perm("main.add_courses")):
        return render(request, "main/not.html")
    if request.method == 'POST':
        try:
            new_post = Course(coursename=request.POST['coursename'], numberhours=request.POST['numberhours'], price=request.POST["price"], startdate= request.POST["startdate"], expirydate=request.POST["expirydate"], poster=request.FILES["poster"],categories=request.POST["categories"])
            new_post.save()
            return redirect("main:base_view")
        except Exception as e:
            print(e)

    return render(request, "main/add_courses.html", {"categories" : Course.COURSE_CATEGORIES})


def post_detail_view(request:HttpRequest, post_id):

    try:
        post = Course.objects.get(pk=post_id)
    except Course.DoesNotExist:
        post = None
    except Exception as e:
        print(e)


    return render(request, "main/post_detail.html", {"post" : Course})

def update_post_view(request:HttpRequest, post_id):
    pass
    return render(request, 'main/update_post.html', {"post" : Course})

def delete_post_view(request:HttpRequest, post_id):

    try:
        post = Course.objects.get(pk=post_id)
        post.delete()
    except Exception as e:
        print(e)
    

    return redirect("main:base_view")







def all_courses_view(request:HttpRequest):
    return render(request, "main/Courses_list.html")



def add_about_view(request: HttpRequest):
    return render(request, "main/about.html")

    