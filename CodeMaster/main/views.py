from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from .models import Contact
from requests.models import Rating
from django.db.models import Avg


# Create your views here.
def index_page(request:HttpRequest):
    
    ratings = Rating.objects.all()
    average_rating = ratings.aggregate(avg_rating=Avg('rate'))['avg_rating']


    return render(request,"main/index_page.html",{'average_rating': average_rating})



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

def no_permission(request:HttpRequest):

    return render(request,"main/no_permission.html")