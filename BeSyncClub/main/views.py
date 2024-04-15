from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from datetime import date, timedelta
from django.contrib.auth.models import User
from booking.models import Booking


import math

from .models import Event
from accounts.models import Student



def index_view(request: HttpRequest):

    events = Event.objects.all().order_by('-event_date')[0:3]
    members = User.objects.filter(groups__name='members')
    return render(request, "main/index.html", {"events" : events, "members" : members})



def add_event_view(request: HttpRequest):

    #limit access to this view for only staff (club members)
    if not (request.user.is_staff and request.user.has_perm("main.add_event")):
        return render(request, "main/no_permission.html")
     
    if request.method == 'POST':
        try:
            new_event = Event(
                user = request.user,
                event_title = request.POST["event_title"],
                event_description = request.POST["event_description"],
                objective = request.POST["objective"],
                event_img =request.FILES["event_img"],
                on_site = request.POST.get("on_site", False), 
                theme = request.POST["theme"],
                event_type = request.POST["event_type"],
                event_date = request.POST["event_date"],
                time_start = request.POST["time_start"],
                time_end = request.POST["time_end"]

            )
            new_event.save()  
            return redirect("main:index_view") ##pop up successfully
        except Exception as e:
            print(e)

    return render(request, "main/add_event.html", {"themes" : Event.themes.choices, "types" : Event.types.choices})



def edit_event_view(request: HttpRequest, event_id):
    
    #limit access to this view for only staff (club members)
    if not request.user.is_staff:
        return render(request, "main/no_permission.html")

    #Object from Event
    event = Event.objects.get(pk=event_id)

    try:
        event.event_title = request.POST["event_title"]
        event.event_description = request.POST["event_description"]
        event.objective = request.POST["objective"]
        event.event_img =request.FILES.get("event_img",event.event_img)
        event.on_site = request.POST.get("on_site", False)
        event.theme = request.POST["theme"]
        event.event_type = request.POST["event_type"]
        event.event_date= request.POST.get("event_date", event.event_date)
        event.time_start = request.POST.get("time_start", event.time_start)
        event.time_end = request.POST.get("time_end", event.time_end)

        event.save()
        return redirect("main:event_detail_view", event_id=event.id)

    except Exception as e:
        print(e)
    
    return render(request, "main/edit_event.html", {"event" : event, "themes" : Event.themes.choices, "types" : Event.types.choices})



def event_detail_view(request: HttpRequest, event_id):

    try:
        #getting a club detail
        event = Event.objects.get(pk=event_id)

        #related events from the same club or the same theme 
        related_events = Event.objects.filter(theme=event.theme).exclude(pk=event_id)[0:3]   

        #is_book or not 
        is_booked = request.user.is_authenticated and Booking.objects.filter(user=request.user, event=event).exists()

    except Event.DoesNotExist:
        return render(request, "main/not_found.html") 
    except Exception as e:
        print(e)
    return render(request, "main/event_detail.html", {"event" : event, "related_events" : related_events, "is_booked" : is_booked})



def delete_event_view(request:HttpRequest, event_id):

    #limit access to this view for only staff
    if not request.user.is_staff:
        return render(request, "main/no_permission.html")
   
    try:
        event = Event.objects.get(pk=event_id)
        event.delete()
    except Exception as e:
        print(e)
    
    return redirect("main:index_view")



def all_events_view(request:HttpRequest):
    
    if "them" in request.GET:
       events = Event.objects.filter(theme=request.GET["them"])
    else:
        events = Event.objects.all()    

    return render(request, "main/all_events.html", {"events" : events, "themes" : Event.themes.choices})


def search_events_view(request:HttpRequest):
    events=[]

    if "search" in request.GET:
        events = Event.objects.filter(event_title__contains=request.GET["search"])

    if "date" in request.GET and len(request.GET["date"]) > 4:
        first_date = date.fromisoformat(request.GET["date"])
        end_date = first_date + timedelta(days=1)
        events = events.filter(event_date__gte=first_date, event_date__lt=end_date)

    return render(request, "main/search_events.html",{"events" : events} )
