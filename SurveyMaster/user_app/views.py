from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.db import IntegrityError

def register(request):
    msg = None

    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")

        if password != password2:
            msg = "Passwords do not match. Please try again."
        else:
            try:
                user = User.objects.create_user(username=username, email=email, first_name=first_name, last_name=last_name, password=password)
                user.save()
                login(request, user)
                return redirect("main:survey_list")
            except IntegrityError:
                msg = "Username already exists. Please choose a different username."

    return render(request, "user_app/register.html", {"msg": msg})

def user_login(request):
    msg = None

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect("main:home")
        else:
            msg = "Invalid username or password. Try again..."

    return render(request, "user_app/login.html", {"msg": msg})

def user_logout(request):
    logout(request)
    return redirect('user_app:login')
