from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from datetime import date, timedelta
import math

from .models import Club, Event

def index_view(request: HttpRequest):

    return render(request, "main/index.html")



# def add_club_view(request: HttpRequest):
     
#     #limit access to this view for only staff (club members)
    
#     if request.method == 'POST':
#         try:
#             new_club = Club(
#                 university_name = request.POST["university_name"],
#                 about_club = request.POST["about_club"],
#                 club_email = request.POST["club_email"],##########
#                 club_header = request.FILES["club_header"],
#                 x_link = request.POST["x_link"]
#             )
#             new_club.save()
#             return redirect("main:index_view") ##pop up successfully
#         except Exception as e:
#             print(e)

#     return render(request, "main/add_club.html")



# def edit_club_view(request: HttpRequest, club_id):
    
#     return render(request, "main/edit_club.html")



# def club_detail_view(request: HttpRequest, club_id):

#     try:
#         #getting a club detail
#         club = Club.objects.get(pk=club_id)

#         #events club

#         #club members

#     except Club.DoesNotExist:
#         return render(request, "main/not_found.html") #####
    
#     return render(request, "main/club_detail.html", {"club" : club})




def add_event_view(request: HttpRequest):

    #limit access to this view for only staff (club members)
    
    if request.method == 'POST':
        try:
            new_event = Event(
                event_title = request.POST[" event_title"],
                event_description = request.POST["event_description"],
                objective = request.POST["objective"],
                event_img =request.FILES["event_img"],
                on_site = request.POST.get("on_site", False), 
                theme = request.POST["theme"],
                event_date_time = request.POST["event_date_time"]
            )
            new_event.save()
            return redirect("main:index_view") ##pop up successfully
        except Exception as e:
            print(e)

    return render(request, "main/add_event.html", {"themes" : Event.themes.choices})



def edit_event_view(request: HttpRequest, event_id):
    
    #limit access to this view for only staff (club members)

    #Object from Event
    event = Event.objects.get(pk=event_id)

    try:
        event.event_title = request.POST[" event_title"],
        event.event_description = request.POST["event_description"],
        event.objective = request.POST["objective"],
        event.event_img =request.FILES.get("event_img",event.event_img),
        event.on_site = request.POST.get("on_site", False), 
        event.theme = request.POST["theme"],
        event.event_date_time = request.POST["event_date_time"]
        event.save()
        return redirect("main:event_detail_view", event_id=event.id)

    except Exception as e:
        print(e)
    
    return render(request, "main/edit_event.html", {"event" : event, "themes" : Event.themes.choices} )



def event_detail_view(request: HttpRequest, event_id):

    try:
        #getting a club detail
        event = Event.objects.get(pk=event_id)

        #related events from the same club or the same theme 

        #is_book or not 

    except Event.DoesNotExist:
        return render(request, "main/not_found.html") #####

    return render(request, "main/event_detail.html", {"event" : event})


