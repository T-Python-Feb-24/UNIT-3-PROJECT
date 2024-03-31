from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from datetime import date, timedelta
from .models import Task


# Create your views here.

def home_page(request:HttpRequest):

    return render(request, 'main/home_page.html')


