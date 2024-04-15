from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Booking
from main.models import Place
from django.contrib import messages

@login_required
def buy_now(request, place_id):
    place = get_object_or_404(Place, pk=place_id)

   
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        
        if not full_name or not email or not phone_number:
            messages.error(request, 'All fields are required.')
            return redirect('booking:buy_now', place_id=place_id)
        
        Booking.objects.create(
            user=request.user,
            place=place,
            full_name=full_name,
            email=email,
            phone_number=phone_number,
        )
        messages.success(request, 'Purchase successful!')
        return redirect('booking:buy_success')  
    
    return render(request, 'booking/buy_now.html', {'place': place})

@login_required
def book_now(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        
        
        existing_bookings = Booking.objects.filter(
            place=place,
            check_in_date__lte=end_date,
            check_out_date__gte=start_date
        )
        
        if existing_bookings.exists():
            messages.error(request, 'This place is already booked for the selected dates.')
            return redirect('booking:book_now', place_id=place_id)  
        
        
        if not full_name or not email or not phone_number or not start_date or not end_date:
            messages.error(request, 'All fields are required.')
            return redirect('booking:book_now', place_id=place_id)
        
        
        Booking.objects.create(
            user=request.user,
            place=place,
            check_in_date=start_date,
            check_out_date=end_date,
            full_name=full_name,
            email=email,
            phone_number=phone_number
        )
        messages.success(request, 'Booking successful!')
        return redirect('booking:book_success')  
    
    return render(request, 'booking/book_now.html', {'place': place})

@login_required
def buy_success(request):
    return render(request, 'booking/buy_success.html')

@login_required
def book_success(request):
    return render(request, 'booking/book_success.html')
