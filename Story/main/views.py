from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from .models import Story,Comment,ContactMessage
import openai
from dotenv import load_dotenv
from django.contrib.auth.decorators import login_required
import os
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.http import HttpResponseForbidden,HttpRequest, HttpResponse
from django.db.models import Q
from bookmarks_likes.models import Like
from django.db.models import Count


dotenv_path = os.path.join(os.path.dirname(__file__), 'key.env')
load_dotenv(dotenv_path=dotenv_path)


def home(request):
    most_liked_stories = Story.objects.annotate(num_likes=Count('liked_by')).order_by('-num_likes')[:5]

    recent_stories = Story.objects.all().order_by('-created_at')[:10]

    return render(request, 'main/home.html', {
        'most_liked_stories': most_liked_stories,
        'recent_stories': recent_stories
    })

from django.shortcuts import render, redirect
from .models import Story

def add_story(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        category = request.POST.get('category')
        content = request.POST.get('content', '')  

        if not content.strip():
            prompt = f"{name} is a {category} story. {description} Once upon a time,"
            try:
                content = get_completion(prompt)
            except Exception as e:
                print("API generation failed:", e)
                messages.error(request, f"AI generation failed. Error: {str(e)}")
                return render(request, 'main/add_story.html', {'CATEGORY_CHOICES': Story.CATEGORY_CHOICES})

        try:
            new_story = Story.objects.create(
                name=name,
                description=description,
                category=category,
                content=content
            )
            messages.success(request, "Story added successfully.")
            return redirect('main:all_stories')
        except Exception as e:
            messages.error(request, f"Failed to save story. Error: {str(e)}")
        
        return render(request, 'main/add_story.html', {'CATEGORY_CHOICES': Story.CATEGORY_CHOICES})
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
    try:
        story = Story.objects.get(pk=pk)
    except Story.DoesNotExist:
        return render(request, "main/no_access.html")  

    lines = story.content.split('\n')
    is_bookmarked = False
    user_has_liked = False
    recommended_stories = Story.objects.filter(~Q(pk=pk), category=story.category)[:3]

    if request.user.is_authenticated:
        is_bookmarked = story.saved_by.filter(pk=request.user.pk).exists()
        user_has_liked = Like.objects.filter(user=request.user, story=story).exists()

    lines_per_page = 20
    segments = ['\n'.join(lines[i:i + lines_per_page]) for i in range(0, len(lines), lines_per_page)]
    paginator = Paginator(segments, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    comments = story.comment_set.all()

    return render(request, 'main/show_story.html', {
        'story': story,
        'page_obj': page_obj,
        'comments': comments,
        'is_bookmarked': is_bookmarked,
        'recommended_stories': recommended_stories,
        'user_has_liked': user_has_liked,
    })



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

    return redirect('main:all_stories')  


def all_stories(request):
    query = request.GET.get('q')
    category = request.GET.get('category')
    stories = Story.objects.all()

    if query:
        stories = stories.filter(Q(name__icontains=query) | Q(description__icontains=query))

    if category:
        stories = stories.filter(category=category)

    return render(request, 'main/all_stories.html', {
        'stories': stories,
        'category_query': category,  
        'category_choices': Story.CATEGORY_CHOICES  
    })



def add_comment(request, story_id):
    if request.method == "POST":
        try:
            story_object = get_object_or_404(Story, pk=story_id)
            content = request.POST.get('content')
            user = request.user  
            new_comment = Comment.objects.create(Story=story_object, user=user, content=content)
            return redirect('main:show_story', pk=story_id)
        except KeyError:
            pass
    
    return redirect('main:show_story', pk=story_id)

@login_required
def delete_comment(request, comment_id, story_id):
    comment = get_object_or_404(Comment, id=comment_id)

    if request.user == comment.user or request.user.is_staff:
        comment.delete()
        return redirect('main:show_story', pk=story_id)
    else:
        return HttpResponseForbidden("You are not allowed to delete this comment.")

def contact_us(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        
        return redirect('contact_us_messages')

    return render(request, 'main/contact_us.html')

def save_contact_message(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        ContactMessage.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            message=message
        )
        return redirect('main:home')
    else:
        pass

def contact_us_messages(request):

    if not request.user.is_superuser:
        return render(request, "main/no_access.html")  

    messages = ContactMessage.objects.all()
    return render(request, 'main/contact_us_messages.html', {'messages': messages})

def category_stories(request, category_name):
    stories = Story.objects.filter(category=category_name)  
    return render(request, 'main/category_stories.html', {'stories': stories, 'category_name': category_name})

def dark_mode(requset: HttpRequest):

    response = redirect("main:home")
    response.set_cookie("mode", "dark")

    return response


def light_mode(requset: HttpRequest):

    response = redirect("main:home")
    response.set_cookie("mode", "light")

    return response

def no_access(request):
    return render(request, 'main/no_access.html', {'message': 'You do not have permission to access this page.'})


def about_us(request):
    return render(request, 'main/about_us.html')

def faq(request):
    return render(request, 'main/faq.html')

def help_page(request):
    return render(request, 'main/Help.html')