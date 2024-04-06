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
    if request.method == "POST":
        
        student = Student.objects.get(user__username=student_username)
        user = student.user_set.all
        
        user.first_name = request.POST["first_name"]
        user.last_name = request.POST["last_name"]
        user.email = request.POST["email"]
        
        save.user()
        
        student.collage_name = request.POST["collage_name"]
        student.graduation_year = request.POST["graduation_year"]
        student.major = request.POST["major"]
        student.GPA = request.POST["GPA"] 
        student.CV = request.FILES.get("CV")
        student.save()
        
        return redirect("student:student_profile")
                
        
        
    return render(request,"student/update_student.html")

def delete_project(request : HttpRequest):
    
    return render()