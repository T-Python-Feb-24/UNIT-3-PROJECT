from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from datetime import datetime, timedelta , date
from .models import Task , Comment , Project
from django.db.models import Q
from django.core.mail import send_mail
from django.http import JsonResponse



# Create your views here.

def home_page(request:HttpRequest):

    tasks = Task.objects.all()
    projects = Project.objects.all()
    comments = Comment.objects.all().order_by('-created_at')[:5]
    # important_events = Event.objects.filter(is_important=True)

    return render(request, "main/home_page.html", {
        "tasks": tasks,
        "projects": projects,
        "comments": comments,
        # "important_events": important_events
    })




def tasks(request:HttpRequest):

    tasks = Task.objects.all()
    return render(request, 'home_page.html', {'tasks': tasks})


def create_task(request):

    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        priority = request.POST.get('priority')
        task = Task(title=title, description=description, priority=priority)
        task.save()
        return redirect('main:tasks')
    return render(request, 'home_page.html')



def task_search(request: HttpRequest):
    tasks = Task.objects.all()

    if "search" in request.GET:
        search_query = request.GET["search"]
        tasks = tasks.filter(
            Q(title__contains=search_query) |
            Q(priority__name__contains=search_query) |
            Q(status__contains=search_query)
        )

    if "due_date" in request.GET and len(request.GET["due_date"]) > 4:
        due_date_str = request.GET["due_date"]
        due_date = datetime.strptime(due_date_str, "%Y-%m-%d").date()
        tasks = tasks.filter(due_date=due_date)

    return render(request, "main/search.html", {"tasks": tasks})




def add_comment(request:HttpRequest, project_id):

    if not request.user.is_authenticated:
        return redirect("accounts:sign_in")

    if request.method == "POST":
        task_object = Task.objects.get(pk=project_id)
        new_comment = Comment(post=task_object,user=request.user, content=request.POST["content"])
        new_comment.save()

    
    return redirect("main:task_detail", project_id=project_id)





def task_detail(request:HttpRequest, project_id):

    try:
        task = Task.objects.get(pk=project_id)
        comments = Comment.objects.filter(task =task) 

    except Task.DoesNotExist:
        return render(request, "main/not_found.html")
    except Exception as e:
        print(e)


    return render(request, "main/task_detail.html", {"task" : task, "comments" : comments })




def dashboard(request:HttpRequest):

    return render(request, "main/dashboard.html" )




def send_email(request:HttpRequest):
    
    if request.method == 'POST':
        recipient_email = request.POST.get('recipient_email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        send_mail(subject, message, 'your-email@example.com', [recipient_email])

        return JsonResponse({'success': True})

    return render(request, 'dashboard.html')