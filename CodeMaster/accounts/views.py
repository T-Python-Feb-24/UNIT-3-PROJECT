from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
# Create your views here.

def login_page(request:HttpRequest):

    return render(request,"accounts/login_page.html")
