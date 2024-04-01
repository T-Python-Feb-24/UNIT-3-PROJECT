from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from .models import Story
import openai
from dotenv import load_dotenv
import os
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
dotenv_path = os.path.join(os.path.dirname(__file__), 'key.env')
load_dotenv(dotenv_path=dotenv_path)


def home(request):
    return render(request, 'main/home.html')

from django.shortcuts import render, redirect
from .models import Story

def add_story(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        category = request.POST.get('category')
        content = request.POST.get('content', '')  

        try:
            if not content.strip():
                prompt = f"{name} is a {category} story. {description} Once upon a time,"
                content = get_completion(prompt)

            Story.objects.create(
                name=name,
                description=description,
                category=category,
                content=content
            )
            messages.success(request, "Story added successfully.")
        except Exception as e:
            messages.error(request, f"Failed to add story. Error: {str(e)}")
        
        return redirect('main:home')
    else:
        return render(request, 'main/add_story.html', {'CATEGORY_CHOICES': Story.CATEGORY_CHOICES})



def get_completion(prompt, model="gpt-3.5-turbo"):

    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
    model=model,
    messages=messages,

    )

    return response.choices[0].message["content"]






def show_story(request, pk):
    story = get_object_or_404(Story, pk=pk)
    lines = story.content.split('\n')  
    
    segments = ['\n'.join(lines[i:i + 20]) for i in range(0, len(lines), 3)]
    
    paginator = Paginator(segments, 1)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'main/show_story.html', {'story': story, 'page_obj': page_obj})




def update_story(request, pk):
    story = get_object_or_404(Story, pk=pk)
    if request.method == 'POST':
        story.name = request.POST.get('name', story.name)  
        story.description = request.POST.get('description', story.description)
        story.content = request.POST.get('content', story.content)
        story.category = request.POST.get('category', story.category)

        if 'image' in request.FILES:
            story.image = request.FILES['image']
        
        story.save()
        return redirect('main:all_stories')
    else:
        return render(request, 'main/update_story.html', {'story': story})


def delete_story(request, pk):
    story = get_object_or_404(Story, pk=pk)
    
    story.delete()

    return redirect('main:home')  


def all_stories(request):
    stories = Story.objects.all()
    return render(request, 'main/all_stories.html', {'stories': stories})
