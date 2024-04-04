from django.shortcuts import render , redirect
from django.http import HttpRequest, HttpResponse
import json , requests
from .models import Recipe ,Comment , Contact
from favorites.models import RecipeFavorite

# Create your views here.

def home(request:HttpRequest):

  if request.user.is_authenticated:
     print(request.user.first_name)
  return render(request,"main/Home.html")

 

def all_recipe(request: HttpRequest):
  if "categories" in request.GET:
        recipes = Recipe.objects.filter(category=request.GET["categories"])
  else:
        recipes = Recipe.objects.all
  return render(request,"main/all_recipe.html" , {"recipes" : recipes , "category" : Recipe.categories.choices})




def add_recipe (request:HttpRequest):
  #if not request.user.is_staff:
      #return None
    
  if request.method =="POST":
        try:
            new_recipe=Recipe(
            title=request.POST["title"],
            about=request.POST["about"],
            quantity=request.POST["quantity"],
            fat=request.POST["fat"],
            protien=request.POST["protien"],
            carb=request.POST["carb"],
            calories=request.POST["calories"],
            category=request.POST["category"],
            image=request.FILES.get("image")
            )

            new_recipe.save()

        except Exception as e:
            print(e)
        return redirect('main:home')
    
  return render(request,"main/add_recipe.html",{"category" : Recipe.categories.choices})




def update_recipe (request:HttpRequest,recipe_id):
    recipe=Recipe.objects.get(pk=recipe_id)

    if request.method == "POST":
      try:
         recipe.title=request.POST["title"]
         recipe.about=request.POST["about"]
         recipe.quantity=request.POST["quantity"]
         recipe.fat=request.POST["fat"]
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
  #if not request.user.is_staff:
    #return render(request, "main/no_permission.html")
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
      return redirect('main:home')
    
    except Exception as e :
            print(e)

  return render(request,"main/contact_us.html")



def user_message (request:HttpRequest):
  #if not request.user.is_superuser:
    #return render(request, "main/no_permission.html")
    
    messages=Contact.objects.all()
    return render(request,"main/user_message.html" , {"messages" : messages})




def comments(request:HttpRequest , recipe_id):
  #if not request.user.is_authenticated:
        #return redirect('accounts/login_user_view')

    if request.method == "POST":
        recipe_comment=Recipe.objects.get(pk=recipe_id)
        comments=Comment(recipe=recipe_comment,
        user=request.user,
        content=request.POST["content"],
        )
        comments.save()

    return redirect('main:detail_recipe_page' , recipe_id=recipe_comment.id)






def search_food(request: HttpRequest):
 recipes = Recipe.objects.order_by("-fat")[0:3]
 if request.method == "POST":
  query=request.POST['query']
  api_url = "https://api.api-ninjas.com/v1/nutrition?query="
  api_request = requests.get(api_url + query , headers={'X-Api-Key': "LieQDXn0BxDcZSrzyivcIg==KZ0HZTXbWwJgllHA"})

  try:
   recipes = Recipe.objects.all()
   api_object=json.loads(api_request.content)
   print(api_request.content)
  except Exception as e:
    api_object="error"
    print(e)
  return render(request,"main/search_food.html" ,{"api" :api_object , "recipes":recipes})
 else:
  return render(request,"main/search_food.html" ,{"query" :"enter vaild input" , "recipes":recipes })
 