from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
# from datetime import datetime, timedelta , date
from .models import Task , Note , Journal 

# Home page
def home_page(request:HttpRequest):

    tasks = Task.objects.all()    
    return render(request, "main/home_page.html", {"tasks": tasks,})



# View tasks
def tasks(request:HttpRequest):

    tasks = Task.objects.all()
    return render(request, 'home_page.html', {'tasks': tasks})



# Add task 
def task_list(request:HttpRequest):

    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        deadline = request.POST.get('')
        task = Task(title=title, description=description, deadline=deadline)
        task.save()
        return redirect('main:tasks')
    return render(request, 'main/task_list.html', {'tasks': tasks})


# Dashboard
def dashboard(request:HttpRequest):
    dashboard = Task.objects.all()

    return render(request, "main/dashboard.html", {"dashboard":dashboard})



# Journal 
def journal(request:HttpRequest):
    if not request.user.is_authenticated:
        return redirect("accounts:sign_in")
    
    if request.method == 'POST':
        journal = Journal(user=request.user, title=request.POST['title'])
        journal.save()
        return redirect('main:journal')
    
    return render(request, "main/journal.html")



# Reading list
def reading_list(request:HttpRequest):

    if request.method == 'POST':
        try:
            title = request.POST.get('title')
            description = request.POST.get('description')
            read = Task(title=title, description=description)
            read.save()
            return redirect('main:reading_list')
        except Exception as e:
            print(e)
    
    return render(request, 'main/reading_list.html')


# Note 
def notes(request:HttpRequest):

    if request.method == "POST":
        new_note = Note(title=request.POST["title"] , context=request.POST["context"])
        new_note.save()

    return render(request, "main/notes.html")



# Yearly Goals 
def yearly_goals(request:HttpRequest):

    if request.method == 'POST':
        title = request.POST.get('title')
        title.save()

        return redirect('main:yearly_goals')
    return render(request, 'main/yearly_goals.html')