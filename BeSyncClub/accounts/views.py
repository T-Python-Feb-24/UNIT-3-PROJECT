from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

#import User Model
from django.contrib.auth.models import User

#import login, logout, authenticate
from .models import CustomUser
from django.contrib.auth import authenticate, login, logout

#import transaction
from django.db import transaction, IntegrityError
# Create your views here.


def register_user_view(request:HttpRequest):
    msg = None

    if request.method == "POST":
        try:

            #using transaction to ensure all operations are successfull
            with transaction.atomic():
                #create new user
                new_user = CustomUser(
                    username=request.POST["username"], 
                    email=request.POST["email"], 
                    first_name=request.POST["first_name"], 
                    last_name=request.POST["last_name"], 
                    city =request.POST["city"], 
                    university =request.POST["university"], 
                    
                    password=request.POST["password"]
                )
                
                new_user.save()

                #redirect to login page
                return redirect("accounts:login_user_view")
        
        except IntegrityError as e:
            msg = "Username already exists. Please choose a different username."
            print(e)

        except Exception as e:
            msg = "Something went wrong. Please try again."
            print(e)
    

    return render(request, "accounts/register_user.html", {"msg" : msg})


def login_user_view(request:HttpRequest):
    msg = None

    if request.method == "POST":
        #authenticat user
        user = authenticate(request, email=request.POST["email"], password=request.POST["password"])

        if user:
            #login user
            login(request, user)
            return redirect("main:index_view")
        else:
            msg = "Email or Password is wrong. Try again..."
    
    return render(request, "accounts/login_user.html", {"msg" : msg})



def logout_user_view(request:HttpRequest):
    if request.user.is_authenticated:
        logout(request)
    
    return redirect('accounts:login_user_view')
