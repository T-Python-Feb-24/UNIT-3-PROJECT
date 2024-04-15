from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from.models import Bootcamp,Evaluation,Student
from django.contrib.auth.models import User

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


def students_evaluation(request:HttpRequest,bootcamp_id,student_id):  
    try:
        evaluation = Evaluation.objects.get(bootcamp_id=bootcamp_id, student_id=student_id)
    
    except Evaluation.DoesNotExist:
        evaluation = Evaluation(
            bootcamp_id=bootcamp_id, 
            student_id=student_id,
            attendance_rate=request.POST.get("attendance_rate"), 
            grades_rate=request.POST.get("grades_rate")  
            )
    
    if request.method =="POST":
        
        evaluation.attendance_rate = request.POST["attendance_rate"]
        evaluation.grades_rate = request.POST["grades_rate"]
        evaluation.save()
        
        return redirect("bootcamp:bootcamp_details",bootcamp_id )
    
    return render(request,"bootcamp/student_evaluation.html",{"student_id":student_id,"bootcamp_id":bootcamp_id,"evaluation":evaluation})

def staff_profile(request:HttpRequest,staff_username):
    
    staff =User.objects.get(username=staff_username)
    bootcamps = Bootcamp.objects.filter(staff__id=staff.id)
    
    return render (request,"bootcamp/staff_profile.html",{"staff":staff,"bootcamps":bootcamps})

def update_bootcamp ():
    pass 

def delete_bootcamp():
    pass


