from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.db import transaction, IntegrityError
from django.contrib.auth import authenticate, login, logout
from .models import User
def register_view(request:HttpRequest):
    msg = None
    if request.method == "POST":
        
     try:
        new_user = User.objects.create_user(username=request.POST["username"], email=request.POST["email"], first_name=request.POST["first_name"], last_name=request.POST["last_name"], password=request.POST["password"])
        new_user.save()    
        return redirect("accounts:login_user_view")

     except IntegrityError as e:
        msg = "Username already exists. Please choose a different username."
        print(e)

     except Exception as e:
        msg = "Something went wrong. Please try again."
        print(e)
    return render(request, "accounts/register.html", {"msg" : msg})

def login_view(request):
    msg = None
    if request.method == "POST":
        user = authenticate(request, username=request.POST["username"], password=request.POST["password"])
        if user:
            
            login(request, user)
            return redirect("main:index_view")
        else:
            msg = "Username or Password is wrong. Try again..."
    return render(request, "accounts/login.html", {"msg" : msg})

def logout_user_view(request:HttpRequest):
    if request.user.is_authenticated:
        logout(request)
    
    return redirect('accounts:login')
