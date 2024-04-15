from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from .models import Contact
from requests.models import Rating,Order
from django.db.models import Avg
from django.contrib.auth.models import User


# Create your views here.
def index_page(request:HttpRequest):
    
    ratings = Rating.objects.all()
    average_rating = ratings.aggregate(avg_rating=Avg('rate'))['avg_rating']

    count=User.objects.count()
    order_count=Order.objects.count()
    average_rating=round(average_rating,2)
    print(average_rating,count,order_count)
    print("kkk")

    return render(request,"main/index_page.html",{'average_rating': average_rating,"count":count,"order_count":order_count})



def about_page(request:HttpRequest):

    return render(request,"main/about_page.html")



def contact_page(request):
    msg1=None
    msg2=None
    if request.method == 'POST':
        
        username = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        if not(username and email and subject and message):
            msg2="Please fill out all the fields."
        else:
            contact = Contact(username=username, email=email, subject=subject, message=message)
            contact.save()
            msg1="Your message was sent"

    return render(request, 'main/contact_page.html',{"msg1":msg1,"msg2":msg2})

def no_permission(request:HttpRequest):

    return render(request,"main/no_permission.html")