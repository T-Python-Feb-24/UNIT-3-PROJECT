from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from django.db import transaction, IntegrityError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from main.models import Contact

# Create your views here.

def register_page(request:HttpRequest):
    if request.user.is_authenticated:
        return redirect("main:index_page")
    msg=None
    if request.method == "POST":
        try:
            new_user=User.objects.create_user(username=request.POST["username"], email=request.POST["email"], password=request.POST["password"])
            new_user.save()
            return redirect("accounts:login_page")
        except IntegrityError as e:
            msg = "Username already exists. Please choose a different username."
            print(e)
        except Exception as e:
            msg = "Something went wrong. Please try again."
            print(e) 
   


    return render(request,"accounts/register_page.html",{"msg":msg})



def login_page(request:HttpRequest):
    if request.user.is_authenticated:
        return redirect("main:index_page")

    msg=None

    if request.method=="POST":

        user= authenticate(request, username=request.POST["username"], password=request.POST["password"])

        if user:
            login(request,user)
            return redirect("main:index_page")
        else:
            msg="Username or Password incorrect Try again..."
    return render(request,"accounts/login_page.html",{"msg":msg})




def logout_user(request:HttpRequest):
    if request.user.is_authenticated:
        logout(request)

    return render(request,"main/index_page.html")


def dashborad_page(request:HttpRequest):
    if not request.user.is_authenticated:
        return redirect("main:index_page")
   
    messages = Contact.objects.all().order_by('-created_at')

    return render(request,"accounts/dashborad_page.html", {'messages': messages})
