from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, HttpResponse
from .models import Place, PlaceImage
from django.contrib import messages
def index_view(request: HttpRequest):
    
    return render(request, "main/index.html")
def about(request: HttpRequest):
    
    return render(request, "main/about.html")

def contact_view(request):
    if request.method == 'POST':
        
        messages.success(request, 'Your message has been sent successfully. We will get back to you soon.')
        return redirect('main:contact')  
    else:
     return render(request, 'main/contact_us.html')

def add_place(request):
    if request.method == 'POST':
        
        name = request.POST.get('name')
        neighborhood = request.POST.get('neighborhood')
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        price = request.POST.get('price')
        address = request.POST.get('address')
        category = request.POST.get('category')
        for_rent = request.POST.get('for_rent')
        for_sale = request.POST.get('for_sale')

       
        if name and neighborhood and latitude and longitude and price and address and category:
            
            place = Place.objects.create(
                name=name,
                neighborhood=neighborhood,
                latitude=latitude,
                longitude=longitude,
                price=price,
                address=address,
                category=category,
                
            )

            
            for i in range(1, 6):  
                image_file = request.FILES.get(f'image{i}')
                if image_file:
                    
                    place_image = PlaceImage(place=place, image=image_file)
                    place_image.save()

            
            return redirect('main/success_page')
        else:
            
            error_message = 'Please fill in all required fields.'
            return render(request, 'main/add_place.html', {'error_message': error_message})

    
    return render(request, 'main/add_place.html')

def success_page_view(request):
    return render(request, 'main/place_added_success.html')

def place_detail(request, place_id):
    
    place = get_object_or_404(Place, pk=place_id)
    
    
    return render(request, 'main/place_detail.html', {'place': place})
def services_page(request):
    return render(request, 'main/services.html')

def all_places_view(request):
    neighborhoods = Place.objects.values_list('neighborhood', flat=True).distinct()
    categories = Place.objects.values_list('category', flat=True).distinct()

    
    neighborhood = request.GET.get('neighborhood')
    category = request.GET.get('category')

   
    filtered_places = Place.objects.all()
    if neighborhood:
        filtered_places = filtered_places.filter(neighborhood=neighborhood)
    if category:
        filtered_places = filtered_places.filter(category=category)

    return render(request, 'main/all_places.html', {'neighborhoods': neighborhoods, 'categories': categories, 'filtered_places': filtered_places})

