from django.shortcuts import render,redirect
from django.http import HttpRequest, HttpResponse
from.models import Project 
from accounts.models import Student
from django.db import transaction

# Create your views here.

def student_profile(request : HttpRequest,student_username):
    
    student = Student.objects.get(user__username=student_username)
    
    return render(request,"student/student_profile.html",{"student":student})
    

#new project 
def new_project(request : HttpRequest):
    
    if request.method == "POST":
        student = request.user.student
        project = Project(
            Student= student,
            project_type = request.POST.get("project_type","personal"),
            screenshot = request.FILES.get("screenshot"),
            name = request.POST["name"],
            desc = request.POST["desc"],
            link = request.POST["link"]
        )
        project.save()

    return render(request,"student/new_project.html",{"types":Project.types.choices})


#update student profile 
def update_student(request : HttpRequest,student_username):
    
    student = Student.objects.get(user__username=student_username)
    msg =""
    if request.method == "POST":
        try:
            with transaction.atomic():
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
        
        except Exception as e :
            msg = "something went wrong ! "
                
    return render(request,"student/update_student.html",{"student":student,"msg":msg})


#update project 
def update_project (request : HttpRequest, project_id):
    project = Project.objects.get(pk=project_id)
    
    if request.method == "POST":
        project.project_type = request.POST.get("project_type")
        project.screenshot = request.FILES.get("screenshot",project.screenshot)
        project.name = request.POST["name"]
        project.desc = request.POST["desc"]
        project.link = request.POST["link"]
        project.save()
        
        return redirect("student:student_profile",project.Student.user.username)
        
    return render(request,"student/update_project.html",{"project":project,"types":Project.types.choices})
    
     
def delete_project(request : HttpRequest):
    
    return render()