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


