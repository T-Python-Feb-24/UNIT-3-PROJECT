from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from.models import Bootcamp


# Create your views here.

def all_bootcamps(request :HttpRequest):
    bootcamps = Bootcamp.objects.all()
    
    return render(request,"bootcamp/all_bootcamps.html",{"bootcamps":bootcamps})

def add_bootcamp(request : HttpRequest):
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


def update_bootcamp ():
    pass 

def delete_bootcamp():
    pass
