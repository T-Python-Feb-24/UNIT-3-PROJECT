from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
# Create your views here.
def index_view(request: HttpRequest):
    
    return render(request, "main/index.html")
def about(request: HttpRequest):
    
    return render(request, "main/about.html")

# def contact_view(request):
#     if request.method == "POST":
       
#         first_name = request.POST.get('first_name', '')
#         last_name = request.POST.get('last_name', '')
#         email = request.POST.get('email', '')
#         message = request.POST.get('message', '')

       
#         contact = Contact(first_name=first_name, last_name=last_name, email=email, message=message)
#         contact.save()

       
#         return redirect('main:contact_success')  