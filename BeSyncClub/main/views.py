from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from datetime import date, timedelta
import math

from .models import Event
from accounts.models import Student



def index_view(request: HttpRequest):

    events = Event.objects.all()
    return render(request, "main/index.html", {"events" : events})



def add_event_view(request: HttpRequest):

    #limit access to this view for only staff (club members)
    
    if request.method == 'POST':
        try:
            new_event = Event(
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

        #is_book or not 

    except Event.DoesNotExist:
        return render(request, "main/not_found.html") #####

    return render(request, "main/event_detail.html", {"event" : event})



def delete_event_view(request:HttpRequest, event_id):

    #limit access to this view for only staff
   
    try:
        event = Event.objects.get(pk=event_id)
        event.delete()
    except Exception as e:
        print(e)
    
    return redirect("main:index_view")



def all_events_view(request:HttpRequest):

    events = Event.objects.all()

    return render(request, "main/all_events.html", {"events" : events})
