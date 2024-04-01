from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


# Create your views here.
def index_view(request: HttpRequest):
    return render(request, "main/base.html")

def add_courses_view(request: HttpRequest):
    return render(request, "main/add_courses.html")


def add_about_view(request: HttpRequest):
    return render(request, "main/about.html")

    