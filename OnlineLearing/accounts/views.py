from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
# Create your views here.

def register_user_view(request:HttpRequest):
   pass
   return redirect("accounts:login_user_view")

def login_user_view(request:HttpRequest):
   pass
   return redirect('accounts:login_user_view')
def logout_user_view(request:HttpRequest):
   pass
   return redirect('accounts:login_user_view')
