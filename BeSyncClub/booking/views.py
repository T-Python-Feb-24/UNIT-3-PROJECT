from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from main.models import Event
from .models import Booking
from django.contrib.auth.models import User

# Create your views here.

def book_ticket_view(request: HttpRequest, event_id):

    if not request.user.is_authenticated:
        return redirect("accounts:login_user_view")
    
    try:
        event = Event.objects.get(pk=event_id)

        #check if user already booked this event
        booked_event = Booking.objects.filter(user=request.user, event=event).first()

        if not booked_event:
            book = Booking(user=request.user, event=event)
            book.save()
        else:
            #delete booking if already exists
            booked_event.delete()
    
    except Exception as e:
        print(e)


    return redirect("main:event_detail_view", event_id=event_id)


def user_booking_view(request: HttpRequest):

    return render(request, "booking/user_booking.html")