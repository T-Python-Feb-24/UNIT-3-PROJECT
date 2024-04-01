from django.shortcuts import render,redirect
from django.http import HttpRequest
# Create your views here.
def order_page(request:HttpRequest):

    return render(request,"requests/order_page.html")