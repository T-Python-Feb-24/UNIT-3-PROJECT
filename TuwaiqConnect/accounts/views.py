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

                orgnaization =  Orgnization(
                    user=user,
                    about = request.POST["about"],
                    logo = request.FILES.get("logo")
                )
                orgnaization.save()
                orgnaization.is_active = False
                # Here add it to the orgnaization group 
                msg= "You have been successfully registered!"
                
        except IntegrityError:
            msg = "username already exists! Try with different username!"
        except Exception as e:
            msg=f"something went wrong, {e}"
     
    return render(request,"accounts/orgnaization_register.html",{"msg":msg})



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


# def user_login(request :HttpRequest):
#     if request.method == "POST":
#         try:
#             user = authenticate(
#             username=request.POST["username"],
#             password=request.POST["password"]
#             )
        
#             if user is not None:
#                 login(request,user) 
#                 return redirect("main:home_page")
#         #staff condition : 
#             if user is not None : 
#                 pass
#         #Orgnization condition : 
#             # تسوين دخول بالقروبات  بس اخر شيي
#             if user is not None : 
#                 pass
#         #students condition : 
#             if user is not None : 
#                 pass
            
#         except Exception as e:
#             print(e.__class__)
               
#     return render (request,"accounts/login.html")

# لا تنسين شرط اذا كان مسجل ما يطلع له صفحات الدخول خير شر او مايقدر يرجع للهوم بيج الاساسيه حقت الموقع 
def organization_login(request :HttpRequest):
    # الهوم بيج حق الجهات
    if request.method == "POST":
        try:
            user = authenticate(
            username=request.POST["username"],
            password=request.POST["password"]
            )
        
            if user is not None:
                login(request,user) 
                return redirect("orgnaization:organization_home_page")
        except Exception as e:
            print(e)
            
    return render(request,"accounts/organization_login.html")


def student_login(request :HttpRequest):
    # تودينه عالهوم بيج حقت الطلاب
    if request.method == "POST":
        try:
            user = authenticate(
            username=request.POST["username"],
            password=request.POST["password"]
            )
        
            if user is not None:
                login(request,user) 
                return redirect("main:home_page")
        except Exception as e:
            print(e)
            
    return render(request,"accounts/student_login.html")


def staff_login(request :HttpRequest):
    # الهوم بيج حق الستاف 
    if request.method == "POST":
        try:
            user = authenticate(
            username=request.POST["username"],
            password=request.POST["password"]
            )
        
            if user is not None:
                login(request,user) 
                return redirect("main:home_page")
        except Exception as e:
            print(e)
            
    return render(request,"accounts/staff_login.html")


def user_logout(request:HttpRequest):
    
    if request.user.is_authenticated:
        logout(request)
    return redirect("main:home_page")
    
    
