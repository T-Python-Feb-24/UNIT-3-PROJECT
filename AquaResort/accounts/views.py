from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
#import User Model
from django.contrib.auth.models import User
#import login, logout, authenticate
from django.contrib.auth import authenticate, login, logout
#For the duplicate username
from django.db import IntegrityError, transaction

from .models import Profile
#------------ Create your views here------------

def sign_up_view(request:HttpRequest):
    #This Messgae will appear if user have some issues with sign up
    msg = None

    if request.method == 'POST':
        try:
            #using transaction to ensure all operations are successfull
            with transaction.atomic():
                #create new user
                
                new_user = User.objects.create_user(
                    username=request.POST["username"], 
                    email=request.POST["email"], 
                    first_name=request.POST["first_name"], 
                    last_name=request.POST["last_name"], 
                    password=request.POST["password"]
                )
                new_user.save()

                #create profile for user
                profile = Profile(
                    user = new_user
                )
                profile.save()

                #redirect to login page
                return redirect("accounts:login_view")
        except IntegrityError as e:
            msg = "Username already exists. Please choose a different username."
            print(e)

        except Exception as e:
            msg = f"Something went wrong. Please try again... {e}"
            print(e)
    return render(request, 'accounts/sign_up.html', {'msg':msg})

def login_view(request:HttpRequest):
    #the message will appear if the user enter wrong data
    msg = None

    if request.method == 'POST':

        #Authenticate the user by username and password
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])

        #this is means if user exist    
        if user:
            login(request, user)
            return redirect('main:index_view')
        else:
            msg = "Username or Password is wrong, Please try Again!!"

    return render(request, 'accounts/login.html', {'msg':msg})

def logout_view(request:HttpRequest):
    if request.user.is_authenticated:
        logout(request)
    return redirect('main:index_view')

def profile_view(request:HttpRequest, user_name):
    try:
        user_object = User.objects.get(username=user_name)
    except:
        return render(request, "main/not_found.html")
    return render(request, 'accounts/profile.html',{"user_object":user_object})