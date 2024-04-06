from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from main.models import Comment
from .models import ProfileUser
from django.db import transaction, IntegrityError
from main.models import Recipes



# Create your views here.

def register_user(request:HttpRequest):
    msg = None

    if request.method == "POST":
        try:

        
            with transaction.atomic():
                
                new_user = User.objects.create_user(username=request.POST["username"], email=request.POST["email"], first_name=request.POST["first_name"], last_name=request.POST["last_name"], password=request.POST["password"])
                new_user.save()

                
                profile = ProfileUser(user=new_user, about=request.POST["about"],avatar=request.FILES.get("avatar", ProfileUser.avatar.field.get_default()))
                profile.save()

                
            return redirect("accounts:login_user")
        
        except IntegrityError as e:
            msg = "This username is already taken. Please choose a different username."
            print(e)

        except Exception as e:
            msg = "Something went wrong. Please try again."
            print(e)
    

    return render(request, "accounts/register_user.html", {"msg" : msg})


def login_user(request:HttpRequest):
    msg = None

    if request.method == "POST":
    
        user = authenticate(request, username=request.POST["username"], password=request.POST["password"])

        if user:
            
            login(request, user)
            return redirect("main:home")
        else:
            msg = "Username or Password is wrong. Try again..."
    

    return render(request, "accounts/login_user.html", {"msg" : msg})


def logout_user(request:HttpRequest):
    if request.user.is_authenticated:
        logout(request)
    
    return redirect('accounts:login_user')



def user_profile(request:HttpRequest, user_id):

    try:
        user=User.objects.get(id=user_id)
        user_profile = ProfileUser.objects.get(user=user)
        my_recipes = Recipes.objects.filter(user=user)
        
    except:
        return render(request, "main/not_found.html")

    return render(request, "accounts/user_profile.html", {"user_profile": user_profile, "my_recipes" : my_recipes})



def update_profile(request:HttpRequest):
    msg = None

    if not request.user.is_authenticated:
        return redirect("accounts:login_user")
    
    if request.method == "POST":
        
        try:

            with transaction.atomic():
                user:User = request.user

                user.first_name = request.POST["first_name"]
                user.last_name = request.POST["last_name"]
                user.email = request.POST["email"]

                user.save()
                
                try:
                    profile:ProfileUser= user.ProfileUser
                except Exception as e:
                    profile =ProfileUser(user=user)

                profile.about = request.POST["about"]
                profile.avatar = request.FILES.get("avatar", profile.avatar)

                profile.save()

                return redirect("accounts:user_profile", user_id=user.id)

        except Exception as e:
            msg = f"Something went wrong {e}"
            print(e)

    return render(request, "accounts/update_profile.html", {"msg" : msg})
