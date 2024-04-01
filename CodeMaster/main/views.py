from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from .models import Contact
# Create your views here.
def index_page(request:HttpRequest):
    
    return render(request,"main/index_page.html")



def about_page(request:HttpRequest):

    return render(request,"main/about_page.html")



def contact_page(request):

    if request.method == 'POST':
        username = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        contact = Contact(username=username, email=email, subject=subject, message=message)
        contact.save()

        return redirect('main:index_page')

    return render(request, 'main/contact_page.html')