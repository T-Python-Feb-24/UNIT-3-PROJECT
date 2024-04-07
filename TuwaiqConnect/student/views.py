from django.shortcuts import render,redirect
from django.http import HttpRequest, HttpResponse
from.models import Project 
from accounts.models import Student

# Create your views here.

def student_profile(request : HttpRequest,student_username):
    
    student = Student.objects.get(user__username=student_username)
    
    return render(request,"student/student_profile.html",{"student":student})

def new_project(request : HttpRequest):
    
    if request.method == "POST":
        student = request.user.student
        project = Project(
            Student= student,
            project_type = request.POST.get("project_type","personal"),
            screenshot = request.FILES["screenshot"],
            name = request.POST["name"],
            desc = request.POST["desc"],
            link = request.POST["link"]
        )
        project.save()

    return render(request,"student/new_project.html",{"types":Project.types.choices})

def update_student(request : HttpRequest,student_username):
    
    student = Student.objects.get(user__username=student_username)
   
    if request.method == "POST":
        
        user = student.user
        user.email = request.POST["email"]
        user.save()
        
        student.collage_name = request.POST["college_name"]
        student.graduation_year = request.POST["graduation_year"]
        student.major = request.POST["major"]
        student.GPA = request.POST["GPA"] 
        student.CV = request.FILES.get("CV",student.CV)
        student.save()
        
        return redirect("student:student_profile",student_username)
                
    return render(request,"student/update_student.html",{"student":student})

def delete_project(request : HttpRequest):
    
    return render()