from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User
# Create your views here.

def register_user_view(request:HttpRequest):
   msg = None
   if request.method == "POST":
       try:
          
          new_user = User.objects.create_user(username=request.POST["username"], email=request.POST["email"], first_name=request.POST["first_name"], last_name=request.POST["last_name"], password=request.POST["password"])
          new_user.save()
   

   return render(request,"accounts/register.html")

   except IntegrityError as e:
            msg = "Username already exists. Please choose a different username."
            print(e)

      except Exception as e:
            msg = "Something went wrong. Please try again."
            print(e)
    

    return render(request, "accounts/register.html", {"msg" : msg})

def login_user_view(request:HttpRequest):
   if request.user.is_authenticated:
       logout(request)

   return redirect('accounts:login_user_view')
def logout_user_view(request:HttpRequest):
   try:
       user_object =user.objects.get(username=user_name)
   except:
       
       return redirect('accounts:login_user_view')
#اخطاا

