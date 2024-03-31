from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Recipes,Comment,Suggestions

def home(requset:HttpRequest):

    return render(requset,"main/home.html")


def add_recipes(requset:HttpRequest):
    # if not requset.user.is_staff:
    #  return render(requset,"main:not_found.html")
 
    if requset.method== 'POST':
        try:
            new_recipes=Recipes(
                name=requset.POST["name"], 
                content=requset.POST["content"],
                time_coockin=requset.POST["time_coockin"],  
                image=requset.FILES["image"],
                category=requset.POST["category"],
                number_people=requset.POST["number_people"],
            )
            new_recipes.save()
            return redirect("main:home")
        except Exception as e:
            print(e)
 
    return render(requset,"main/add_recipes.html",{"Category":Recipes.categories.choices})
    

def all_recipes(requset:HttpRequest):
    if "cat" in requset.GET:
        recipes= Recipes.objects.filter(categroy = requset.GET["cat"])
    else:
        recipes = Recipes.objects.all().order_by("-published_at")
    
    return render(requset,"main/all_recipes.html", {"recipes" : recipes, "Category":Recipes.categories.choices})

def detail_recipes(requset:HttpRequest,recipes_id):
    try:
        recipes= Recipes.objects.get(pk=recipes_id)
        
    except Recipes.DoesNotExist:
        pass
    except Exception as e:
        print(e)
    return render(requset ,"main/detail_plants.html", {"recipes":recipes,})



def recipes_search(requset:HttpRequest):
    pass

def Suggestions(requset:HttpRequest):
    pass
