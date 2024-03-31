from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
# Create your views here.
def index_page(request:HttpRequest):
    
    return render(request,"main/index_page.html")