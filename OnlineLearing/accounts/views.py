from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout




def register_user_view(request:HttpRequest):

    if request.method == "POST":
        
        try:
            
            new_user = User.objects.create_user(username=request.POST["username"], email=request.POST["email"], first_name=request.POST["first_name"], last_name=request.POST["last_name"], password=request.POST["password"])
            new_user.save()

         
            return redirect("accounts:login_user_view")

        except Exception as e:
            print(e)
    

    return render(request, "accounts/register.html")


def login_user_view(request:HttpRequest):
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
    
    return redirect('accounts:login_user_view')