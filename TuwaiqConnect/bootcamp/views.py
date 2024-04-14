from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from.models import Bootcamp,Evaluation,Student


# Create your views here.

def all_bootcamps(request :HttpRequest):
    #this is the home page of the superuser(admin)
    bootcamps = Bootcamp.objects.all()
    
    return render(request,"bootcamp/all_bootcamps.html",{"bootcamps":bootcamps})

def add_bootcamp(request : HttpRequest):
    # only the admin can access this page 
    if request.method == "POST":   
        bootcamp = Bootcamp(
            bootcamp_name = request.POST["bootcamp_name"],
            desc = request.POST["desc"],
            objectives = request.POST["objectives"],
            location = request.POST["location"],
            start_date = request.POST["start_date"],
            end_date = request.POST["end_date"]
    )
        bootcamp.save()
    return render(request,"bootcamp/new_bootcamp.html")


def bootcamp_details(request: HttpRequest, bootcamp_id):
    bootcamp = Bootcamp.objects.get(pk=bootcamp_id)
    evaluations = Evaluation.objects.filter(bootcamp_id=bootcamp_id)
    students = bootcamp.students.all()
    
    student_evaluations = {student: evaluations.filter(student=student) for student in students}
    
    return render(request, "bootcamp/bootcamp_details.html", {"bootcamp": bootcamp,"student_evaluations": student_evaluations})


# def students_evaluation(request :HttpRequest,bootcamp_id):
    
#     bootcamp = Bootcamp.objects.get(pk=bootcamp_id)
#     students = bootcamp.students.all()
    
        
        
#     if request.method =="POST":  
#         evaluation = Evaluation(
#         student = Student,
#         bootcamp = Bootcamp,
#         attendance_rate = request.POST["attendance_rate"], 
#         grades_rate =request.POST["grades_rate"]
#         )
#         evaluation.save()
    
        
#     return render(request,"bootcamp/students_evaluation.html",{"bootcamp":bootcamp,"students":students,"evaluation":evaluation})



def update_bootcamp ():
    pass 

def delete_bootcamp():
    pass


