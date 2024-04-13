from django.contrib import messages
from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Bookmark, Like
from main.models import Story
from django.urls import path
from . import views
from django.http import HttpResponse
from django.http import JsonResponse




@login_required
def toggle_like(request, story_id):
    story = get_object_or_404(Story, pk=story_id)
    like, created = Like.objects.get_or_create(user=request.user, story=story)

    if not created:
        like.delete()
        messages.success(request, "You've unliked the story.")
    else:
        messages.success(request, "You've liked the story.")

    return redirect('main:show_story', pk=story_id)


@login_required
def toggle_bookmark(request, story_id):
    story = get_object_or_404(Story, pk=story_id)
    if request.user in story.saved_by.all():
        story.saved_by.remove(request.user)
    else:
        story.saved_by.add(request.user)
    messages.success(request, "Bookmark updated successfully.") 
    return redirect('main:show_story', pk=story_id)




@login_required
def saved_stories(request):
    saved_stories = request.user.saved_stories.all()
    return render(request, 'bookmarks_likes/saved_stories.html', {'stories': saved_stories})



