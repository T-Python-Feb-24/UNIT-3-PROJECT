from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Recipes,Comment,Suggestions
from django.contrib.auth.models import User
from accounts.models import ProfileUser
from favorites.models import Favorite


def home(requset:HttpRequest):
    
    recipes=Recipes.objects.all().order_by('-published_at')[0:3]

    return render(requset,"main/home.html",{"recipes":recipes})


def add_recipes(requset:HttpRequest):
    if not requset.user.is_staff:
        return render(requset,"main:not_found.html")
 
    if requset.method== 'POST':
        try:
            new_recipes=Recipes(
                user=requset.user,
                name=requset.POST["name"], 
                content=requset.POST["content"],
                time_coocking=requset.POST["time_coocking"],  
                image=requset.FILES["image"],
                category=requset.POST["category"],
                number_people=requset.POST["number_people"],
            )
            new_recipes.save()
            return redirect("main:all_recipes")
        except Exception as e:
            print(e)
 
    return render(requset,"main/add_recipes.html",{"Category":Recipes.categories.choices})
    

def all_recipes(requset:HttpRequest):
    if "cat" in requset.GET:
        recipes= Recipes.objects.filter(category = requset.GET["cat"])
    else:
        recipes = Recipes.objects.all().order_by("-published_at")
    
    return render(requset,"main/all_recipes.html", {"recipes" : recipes, "Category":Recipes.categories.choices})


def detail_recipes(requset:HttpRequest,recipes_id):
    try:
        recipes= Recipes.objects.get(pk=recipes_id)
        comments=Comment.objects.filter(Recipes=recipes)
        suggestions=Suggestions.objects.filter(Recipes=recipes)
        is_favored =requset.user.is_authenticated and  Favorite.objects.filter(user=requset.user, recipes=recipes).exists()

        
        
    except Recipes.DoesNotExist:
        pass
    except Exception as e:
        print(e)
    return render(requset ,"main/detail_recipes.html", {"recipes":recipes,'comments':comments ,"suggestions":suggestions , "is_favored":is_favored})


def update_recipes(requset:HttpRequest,recipes_id):
    recipes=Recipes.objects.get(pk=recipes_id)
    if requset.method == "POST":
        try:
            recipes.name=requset.POST["name"]
            recipes.content=requset.POST["content"]
            recipes.time_coocking=requset.POST["time_coocking"] 
            recipes.number_people=requset.POST["number_people"] 
            recipes.image= requset.FILES.get("image",recipes.image)
            recipes.category=requset.POST['category']
            recipes.save()
            return redirect("main:detail_recipes",recipes_id=recipes.id)
        except Exception as e:
            print(e)

    return render(requset, "main/update_recipes.html", {"recipes":recipes, "Category":Recipes.categories.choices})


def delete_recipes(requset:HttpRequest,recipes_id):
    try:
        recipes= Recipes.objects.get(pk=recipes_id)
        recipes.delete()
    except Exception as e:
        print(e)
    return redirect('main:home')



def recipes_search(requset:HttpRequest):
    recipes= []

    if "search" in requset.GET:
        recipes= Recipes.objects.filter(name__contains=requset.GET["search"])


    return render(requset, "main/recipes_search.html", {"recipes" :  recipes})

def suggestions(request: HttpRequest,recipes_id ):
    if request.method == "POST":
        try:
            recipes= Recipes.objects.get(pk=recipes_id)
            new_suggestions = Suggestions(Recipes=recipes,user=request.user, content=request.POST["content"])
            new_suggestions.save()
            return redirect("main:detail_recipes",recipes_id=recipes.id)  #msg
        except Exception as e:
                print(e)


def suggestions_msg(request:HttpRequest):
    if request.user.is_staff == None:
     return redirect("main:home")
    try:
        msg=Suggestions.objects.all()
    except Exception as e:
            print(e)
            msg = ['msg empty'] 
    return render( request,'main/suggestions_msg.html',{"msg":msg})
    

def add_comment(request:HttpRequest, recipes_id):
    if not request.user.is_authenticated:
        return redirect("accounts:login_user")
    
    if request.method == "POST":
        try:
            recipes= Recipes.objects.get(pk=recipes_id)
            new_comment = Comment(Recipes=recipes,
                                  user=request.user, 
                                  content=request.POST["content"],
                                  evaluation=request.POST["evaluation"])
            new_comment.save()
        except Exception as e:
                print(e)
    
    return redirect("main:detail_recipes", recipes_id=recipes.id)
