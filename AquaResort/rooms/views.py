from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Room
# Create your views here.

def all_rooms_view(request:HttpRequest):
    selected_type = request.GET.get("type")
    rooms = Room.objects.filter(room_type=selected_type) if selected_type else Room.objects.all()
    return render(request,'rooms/all_rooms.html',{'rooms':rooms, "selected_category" : selected_type, "rooms_type" : Room.rooms_type.choices})