from django.shortcuts import render,redirect, get_object_or_404
from django.db.models import Count
from django.utils import timezone  
from django.http import HttpRequest, HttpResponse
from .models import Story , Comment
from django.http import Http404




# Create your views here.
def home(request):

    return render(request, 'main/home.html')



def add_story(request):

    if not request.user.is_staff:
        return render(request, "main/no_permission.html")

    CATEGORY_CHOICES = Story.CATEGORY_CHOICES  

    if request.method == 'POST':
        name = request.POST.get('name')
        content = request.POST.get('content')
        category = request.POST.get('category')
        image = request.FILES.get('image')  
        
        plant = Story.objects.create(
            name=name,
            content=content,
            category=category,
            image=image,  
            create_at=timezone.now()
        )
        
        return redirect('main:home')
    
    return render(request, 'main/add_story.html', {'CATEGORY_CHOICES': CATEGORY_CHOICES})

def show_story(request, pk):
    story = get_object_or_404(Story, pk=pk)
    return render(request, 'main/show_story.html', {'story': story})

def all_stories(request):
    stories = Story.objects.all()
    return render(request, 'main/all_stories.html', {'stories': stories})

