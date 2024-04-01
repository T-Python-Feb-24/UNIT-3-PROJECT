from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login,logout
from .models import Student ,Orgnization
from django.db import IntegrityError
from django.db import transaction

# Create your views here.

def student_register(request : HttpRequest):
    msg=""
    
    if request.method == "POST":
        try:
            with transaction.atomic():
                user = User.objects.create_user(
                    username=request.POST["username"],
                    email=request.POST["email"],
                    first_name=request.POST["first_name"],
                    last_name=request.POST["last_name"],
                    password = request.POST["password"]
                    )
                user.save()

                student = Student(
                    user = user,
                    collage_name = request.POST["collage_name"],
                    graduation_year = request.POST["graduation_year"],
                    major = request.POST["major"],
                    GPA =request.POST["GPA"],
                    CV = request.FILES.get("CV")
                    )
                student.save()
                msg= "You have been successfully registered!"
                
        except IntegrityError:
            msg = "username already exists! Try with different username!"
        except Exception as e:
            msg=f"something went wrong, {e}"
     
    return render(request,"accounts/student_register.html",{"msg":msg })


def orgnaization_register(request : HttpRequest):
    msg=""
    if request.method == "POST":
        try:
            with transaction.atomic():
                user = User.objects.create_user(
                    username=request.POST["username"],
                    email=request.POST["email"],
                    first_name=request.POST["first_name"],
                    password = request.POST["password"]
                    )
                user.save()

                orgnaization = orgnaization(
                    user=user,
                    about = request.POST["about"],
                    logo = request.FILES.get("logo")
                )
                orgnaization.save()
                orgnaization.is_active = False
                msg= "You have been successfully registered!"
                
        except IntegrityError:
            msg = "username already exists! Try with different username!"
        except Exception as e:
            msg=f"something went wrong, {e}"
     
    return render(request,"accounts/orgnaization_register.html")



def staff_register(request : HttpRequest):
    
    if request.method == "POST":
        user = User.objects.create_user(
            username=request.POST["username"],
            email=request.POST["email"],
            first_name=request.POST["first_name"],
            last_name=request.POST["last_name"],
            password = request.POST["password"]
        )
        user.is_active = False
        user.is_staff = True
        user.save()
        
    return render (request,"accounts/staff_register.html")













# def staff_login(request :HttpRequest):
#     if request.method == "POST":
#        user = authenticate(
#            username=request.POST["username"],
#            password=request.POST["password"]
#            )
#        # returns None if the credentials aren’t valid 
#        if (user is not None and user.is_sttaf):
#            login(request,user) 
#         #    return redirect("main:home_page")
#        else:
#            pass 
#     return render (request,"accounts/login.html")

