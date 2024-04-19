from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from bootcamp.models import Bootcamp
from accounts.models import Orgnization

# Create your views here.

def organization_home_page(request :HttpRequest):
    
    return render(request,"orgnaization/organization_home_page.html")


def students_acquisition(request :HttpRequest):
    # احط اسماء المعسكرات هنا  + search باسم المعسكر

    bootcamps = Bootcamp.objects.all()
    
    return render(request,"orgnaization/students_acquisition.html",{"bootcamps":bootcamps})


def organization_profile(request :HttpRequest,organization_username):
    
    organization = Orgnization.objects.get(user__username=organization_username)
    
    return render(request,"orgnaization/organization_profile.html",{"organization": organization})

