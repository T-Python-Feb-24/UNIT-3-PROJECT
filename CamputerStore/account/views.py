from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Profile
from django.db import transaction, IntegrityError


def sign_up_view(request: HttpRequest):
   try:
      msg = None
      if request.user.is_authenticated:
         return redirect("main:index_view")
      if request.method == "POST":
         with transaction.atomic():
            # create new user
            full_name = request.POST.get("full_name").split(" ")
            first_name, last_name = full_name[0], full_name[1] if len(
               full_name) > 1 else ""
            if request.POST.get("password") != request.POST.get("confirm_password"):
               msg = "Invalid password"
               raise IntegrityError(msg)
            new_user = User.objects.create_user(
                username=request.POST.get("username"),
                email=request.POST.get("email"),
                first_name=first_name,
                last_name=last_name,
                password=request.POST.get("password")
            )

            new_user.save()
            profile = Profile.objects.create(user=new_user,
                                             phone=request.POST.get("phone"),
                                             gender=request.POST.get("gender"),
                                             about=request.POST.get("about"),
                                             avatar=request.FILES.get(
                                                 "avatar", Profile.avatar.field.get_default()),
                                             nationality=request.POST.get("nationality"))
            profile.save()
         redirect("account:login_view")

   except IntegrityError as e:
      msg = msg = "Username or Email already exist. Try again..."
      print(e)

   except Exception as e:
      msg = "Something went wrong. Please try again."
      print(e)

   return render(request, "account/sign_up.html", {"nationality": Profile.nationality_choices.choices,
                                                   "genders": Profile.gender_choices.choices,
                                                   "msg": msg})


def login_view(request: HttpRequest):
   msg = None
   next = None
   if request.user.is_authenticated:
      return redirect("main:index_view")
   if "next" in request.GET:
      next = request.GET.get("next", "")

   if request.method == "POST":
      # authenticat user
      user = authenticate(
          request,
          username=request.POST.get("username"),
          password=request.POST.get("password")
      )
      if user:
         # login user
         login(request, user)

         return redirect(request.POST.get("next") or "main:index_view")
      else:
         msg = "Username or Password is wrong. Try again..."

   return render(request, "account/login.html", {"msg": msg,
                                                 "next": next})


def logout_view(request: HttpRequest):
   if request.user.is_authenticated:
      logout(request)
   return redirect('main:index_view')


def user_profile_view(request: HttpRequest, user_name):
   try:
      msg = None
      user = User.objects.get(username=user_name)
   except User.DoesNotExist:
      msg = "User Not Found"
      return render(request, "account/user_profile.html", {"msg": msg})
   return render(request, "account/user_profile.html", {"user": user})


def update_profile_view(request: HttpRequest, user_name):
   if not request.user.username == user_name:
      return render(request, "main/no_permission.html")
   user = request.user

   if request.method == "POST":
      user.first_name = request.POST.get('first_name', user.first_name)
      user.last_name = request.POST.get('last_name', user.last_name)
      user.profile.gender = request.POST.get('about', user.profile.gender)
      user.profile.about = request.POST.get('about', user.profile.gender)
      user.profile.address = request.POST.get('about', user.profile.gender)
      user.profile.nationality = request.POST.get(
         'nationality', user.profile.nationality)
      user.profile.avatar = request.FILES.get('avatar', user.profile.avatar)
      user.profile.save()
      user.save()
      return redirect("account:user_profile_view", user_name=user.username)

   return render(request, "account/update_profile.html", {"user": user,
                                                          "nationality": Profile.nationality_choices.choices, })


def user_favorite_view(request: HttpRequest):
   try:
      msg = None
      users = request.user
   except User.DoesNotExist:
      msg = "Your wishlist is empty. Add some products to your wishlist by clicking the  button in product page."
      return render(request, "account/favorite.html", {"msg": msg})

   return render(request, "account/favorite.html", {"users": users})
