from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, HttpResponseForbidden
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.shortcuts import get_object_or_404
from .models import Profile
from django.contrib.auth.decorators import login_required
from .decorators import login_required_or_no_access 


@login_required_or_no_access
def user_detail(request, username):
    try:
        user_profile = User.objects.get(username=username)
    except User.DoesNotExist:
        return redirect('main:no_access')  

    if request.user.username != username and not request.user.is_superuser:
        return redirect('main:no_access') 

    return render(request, 'user_info/user_detail.html', {'user': user_profile})


def register_user(request: HttpRequest):
    msg = None

    if request.method == "POST":
        try:
            new_user = User.objects.create_user(
                username=request.POST["username"],
                email=request.POST["email"],
                first_name=request.POST["first_name"],
                last_name=request.POST["last_name"],
                password=request.POST["password"]
            )
            new_user.save()
            return redirect("user_info:user_login")
        except IntegrityError:
            msg = "Username already exists. Please choose a different username."

    return render(request, "user_info/register.html", {"msg": msg})



def user_login(request:HttpRequest):
    msg = None

    if request.method == "POST":
        user = authenticate(request, username=request.POST["username"], password=request.POST["password"])

        if user:
            login(request, user)
            return redirect("main:home")
        else:
            msg = "Username or Password is wrong. Try again..."
    

    return render(request, "user_info/login.html", {"msg" : msg})


def user_logout(request:HttpRequest):
    if request.user.is_authenticated:
        logout(request)
    
    return redirect('user_info:user_login')


@login_required
def profile_update(request):
    profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        if request.user == profile.user:
            profile.about = request.POST.get('about', profile.about)
            profile.user.first_name = request.POST.get('first_name', profile.user.first_name)
            profile.user.last_name = request.POST.get('last_name', profile.user.last_name)
            profile.user.email = request.POST.get('email', profile.user.email)
            if request.FILES.get('avatar'):
                profile.avatar = request.FILES['avatar']
            profile.save()
            profile.user.save()
            return redirect('user_info:user_detail', username=request.user.username)
        else:
            return HttpResponseForbidden("You are not authorized to perform this action.")

    return render(request, 'user_info/profile_update.html', {'profile': profile})