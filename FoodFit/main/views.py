from django.shortcuts import render , redirect
from django.http import HttpRequest, HttpResponse
import json , requests
from .models import Recipe ,Comment , Contact
from favorites.models import RecipeFavorite
from django.contrib import messages


# Create your views here.

def home(request:HttpRequest):

  recipes = Recipe.objects.order_by("-quantity")[0:3]
  return render(request,"main/Home.html",{"recipes":recipes})

 

def all_recipe(request: HttpRequest):
  if "categories" in request.GET:
        recipes = Recipe.objects.filter(category=request.GET["categories"])
  else:
        recipes = Recipe.objects.all
  return render(request,"main/all_recipe.html" , {"recipes" : recipes , "category" : Recipe.categories.choices})




def add_recipe (request:HttpRequest):
  if not request.user.is_staff:
      return redirect('main:not_allowed_page')
    
  if request.method =="POST":
        try:
            new_recipe=Recipe(
            title=request.POST["title"],
            about=request.POST["about"],
            ingredients=request.POST["ingredients"],
            quantity=request.POST["quantity"],
            fat=request.POST["fat"],
            sugar=request.POST["sugar"],
            sodium=request.POST["sodium"],
            potassium=request.POST["potassium"],
            protien=request.POST["protien"],
            carb=request.POST["carb"],
            calories=request.POST["calories"],
            category=request.POST["category"],
            image=request.FILES.get("image")
            )

            new_recipe.save()
            return redirect('main:all_recipe_page')

        except Exception as e:
            print(e)
        return redirect('main:home')
    
  return render(request,"main/add_recipe.html",{"category" : Recipe.categories.choices})




def update_recipe (request:HttpRequest,recipe_id):
    if not request.user.is_staff:
      return redirect('main:not_allowed_page')
    recipe=Recipe.objects.get(pk=recipe_id)

    if request.method == "POST":
      try:
         recipe.title=request.POST["title"]
         recipe.about=request.POST["about"]
         recipe.ingredients=request.POST["ingredients"]
         recipe.quantity=request.POST["quantity"]
         recipe.fat=request.POST["fat"]
         recipe.sugar=request.POST["sugar"]
         recipe.sodium=request.POST["sodium"]
         recipe.potassium=request.POST["potassium"]
         recipe.protien=request.POST["protien"]
         recipe.carb=request.POST["carb"]
         recipe.calories=request.POST["calories"]
         recipe.category=request.POST["category"]
         recipe.image=request.FILES.get("image",recipe.image)
            
         recipe.save()
         return redirect('main:detail_recipe_page')
      except Recipe.DoesNotExist:
         return redirect('main:home')
      except Exception as e:
            print(e)
            return redirect('main:detail_recipe_page' , recipe_id=recipe.id)
      
    return render(request,"main/update_recipe.html", {"recipe" : recipe , "category" : Recipe.categories.choices })



def delete_recipe (request:HttpRequest , recipe_id):
  if not request.user.is_staff:
      return redirect('main:not_allowed_page')
  try:
    recipe=Recipe.objects.get(pk=recipe_id)
    recipe.delete()
  except Recipe.DoesNotExist:
    recipe=None
  except Exception as e:
    print(e)

    
  return redirect('main:home')




def detail_recipe (request:HttpRequest,recipe_id):
   try:
        recipe=Recipe.objects.get(pk=recipe_id)
        recipes=Recipe.objects.filter(category=recipe.category).exclude(id=recipe_id)[0:3]
        comments=Comment.objects.filter(recipe=recipe).order_by("-created_at")[0:3]
        is_favored = request.user.is_authenticated and RecipeFavorite.objects.filter(user=request.user, recipe=recipe).exists()
        
   except Recipe.DoesNotExist:
        return redirect('main:home')
   except Exception as e:
            print(e)

   return render(request,"main/detail_recipe.html" , {"recipe" : recipe ,"recipes" : recipes , "comments":comments  , "is_favored":is_favored})



def search_recipe (request:HttpRequest):
  recipes=[]
  if "search" in request.GET:
    recipes=Recipe.objects.filter(title__contains=request.GET["search"])

  return render(request,"main/search_recipe.html" ,  {"recipes" : recipes})




def contact_us (request:HttpRequest):
  if request.method=="POST":
    try:
      contact_us=Contact(
        name=request.POST["name"],
        email=request.POST["email"],
        message=request.POST["message"],
        )
      contact_us.save()
      messages.success(request, "Successfully submitted.") 
      return redirect('main:contact_us_page')
    except Exception as e:
            print(e)
            messages.error(request, "An error occurred.")

  return render(request,"main/contact_us.html")



def user_message (request:HttpRequest):
  if not request.user.is_superuser:
    return redirect('main:not_allowed_page')
    
  messages=Contact.objects.all()
  return render(request,"main/user_message.html" , {"messages" : messages})


def delete_message (request:HttpRequest , msg_id):
  if not request.user.is_superuser:
    return redirect('main:not_allowed_page')
  try:
    contact=Contact.objects.get(pk=msg_id)
    contact.delete()
  except Contact.DoesNotExist:
     contact=None
  except Exception as e:
    print(e)

    
  return redirect('main:user_message_page')


def comments(request:HttpRequest , recipe_id):
  if not request.user.is_authenticated:
    return redirect('accounts:login_user_view')

  if request.method == "POST":
        recipe_comment=Recipe.objects.get(pk=recipe_id)
        comments=Comment(recipe=recipe_comment,
        user=request.user,
        content=request.POST["content"],
        )
        comments.save()

  return redirect('main:detail_recipe_page' , recipe_id=recipe_comment.id)






def search_food(request: HttpRequest):
 if not request.user.is_authenticated:
    return redirect('accounts:login_user_view')
 recipes = Recipe.objects.order_by("-quantity")[0:3]
 if request.method == "POST":
  query=request.POST['query']
  api_url = "https://api.api-ninjas.com/v1/nutrition?query="
  api_request = requests.get(api_url + query , headers={'X-Api-Key': "LieQDXn0BxDcZSrzyivcIg==KZ0HZTXbWwJgllHA"})

  try:
   api_object=json.loads(api_request.content)
   print(api_request.content)
  except Exception as e:
    api_object="error"
    print(e)
  return render(request,"main/search_food.html" ,{"api" :api_object , "recipes":recipes})
 else:
  return render(request,"main/search_food.html" ,{"query" :"enter vaild input" , "recipes":recipes })
 


def allowed(request: HttpRequest):
   return render(request,"main/allow.html")