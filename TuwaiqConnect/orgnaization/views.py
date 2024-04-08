from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from bootcamp.models import Bootcamp


# Create your views here.

def organization_home_page(request :HttpRequest):
    
    return render(request,"orgnaization/organization_home_page.html")


def students_acquisition(request :HttpRequest):
    # احط اسماء المعسكرات هنا  + search باسم المعسكر

    bootcamps = Bootcamp.objects.all()
    
    return render(request,"orgnaization/students_acquisition.html",{"bootcamps":bootcamps})


def bootcamp_details(request :HttpRequest,bootcamp_id):
    
    bootcamp = Bootcamp.objects.get(pk=bootcamp_id)
    students = bootcamp.students.all()
    
    
    return render (request,"orgnaization/bootcamp_details.html",{"bootcamp":bootcamp,"students":students})