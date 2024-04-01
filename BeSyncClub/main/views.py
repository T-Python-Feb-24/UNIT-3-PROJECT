from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from datetime import date, timedelta
# Create your views here.


def index_view(request: HttpRequest):

    return render(request, "main/index.html")
