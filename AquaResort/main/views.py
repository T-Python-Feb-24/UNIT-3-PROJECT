from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
import time
from rooms.models import Room
# Create your views here.
def splash_screen_view(request:HttpRequest):
    return render(request, 'main/splash.html')

def index_view(request:HttpRequest):
    time.sleep(2)
    rooms = Room.objects.all()[:3]
    gallery = [
        'https://firebasestorage.googleapis.com/v0/b/unit-3-project-d265e.appspot.com/o/gallery1.jpg?alt=media&token=4e72d7f9-d78d-4f7e-b5c8-1756654c9e7b',
        'https://firebasestorage.googleapis.com/v0/b/unit-3-project-d265e.appspot.com/o/gallery2.jpg?alt=media&token=e0746c2f-e7ae-42ad-9782-1e356505add1',
        'https://firebasestorage.googleapis.com/v0/b/unit-3-project-d265e.appspot.com/o/gallery3.jpg?alt=media&token=79035620-7d23-454f-8596-330ac9a982b1',
        'https://firebasestorage.googleapis.com/v0/b/unit-3-project-d265e.appspot.com/o/gallery4.jpg?alt=media&token=d77ec419-eb33-4959-8acf-2d14f9931b70',
        'https://firebasestorage.googleapis.com/v0/b/unit-3-project-d265e.appspot.com/o/gallery5.jpg?alt=media&token=f2914382-a81e-480c-847d-a88d2d26ee3e',
        'https://firebasestorage.googleapis.com/v0/b/unit-3-project-d265e.appspot.com/o/gallery6.jpg?alt=media&token=f1fdc747-a414-40ec-a2a6-95fe795dc8fd'
    ]
    return render(request, 'main/index.html', {'rooms':rooms, 'gallery':gallery})
