from django.shortcuts import render,redirect
from django.http import HttpRequest, HttpResponse
from.models import Project 
from accounts.models import Student

# Create your views here.

def student_profile(request : HttpRequest,student_username):
    student = Student.objects.get(user=student_username)
    
    return render(request,"student/student_profile.html",{"student":student})

# def new_project(request : HttpRequest):
    
#     if request.method == "POST":
#         student = Student.objects.get(pk)
#         project = Project(
#             project_type = request.POST.get("project_type","personal"),
#             screenshot = request.FILES["screenshot"],
#             name = request.POST["name"],
#             desc = request.POST["desc"],
#             link = request.POST["link"]
#         )
#         project.save()

#     return render(request,"student/new_project.html",{"types":Project.types.choices})

