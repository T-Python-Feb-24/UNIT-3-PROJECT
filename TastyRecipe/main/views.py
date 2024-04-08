from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

import math
from .models import Recipe, Contact, Review
from accounts.models import Saved

# Create your views here.

def home(request:HttpRequest):

    #get user info
    if request.user.is_authenticated:
        print(request.user.first_name)
    
    recipes = Recipe.objects.all().order_by('-created_at')[0:4]

    reviews = Review.objects.all().order_by('-created_at')[0:5]

    return render(request,'main/home.html', {'recipes' : recipes, "reviews": reviews})

def add_recipe(request:HttpRequest):

    if not request.user.is_authenticated:
        return render(request, "no_permission.html")

    if request.method == 'POST':
        try:
            new_recipe = Recipe(
                user = request.user,
                title = request.POST["title"], 
                brief = request.POST["brief"], 
                ingredients = request.POST["ingredients"],
                instructions = request.POST["instructions"],
                time_estimate = request.POST["time_estimate"],
                image = request.FILES.get("image", Recipe.image.field.default),
                category = request.POST['category']
            )
            new_recipe.save()
            
        except Exception as e:
            print(e)
        return redirect("main:home")

    return render(request, "main/add_recipe.html", {'category' : Recipe.Categories.choices})

def all_recipes(request:HttpRequest):
    if "cat" in request.GET:
        recipes = Recipe.objects.filter(category = request.GET["cat"])
    else:
        recipes = Recipe.objects.all().order_by("-created_at") 
    
    limit = 4
    pages_count = [str(n) for n in range(1, math.ceil(recipes.count()/limit)+1)]
    start = (int(request.GET.get("page", 1))-1)*limit
    end = (start)+limit

    print(list(pages_count))

    recipes = recipes[start:end]

    return render(request, "main/all_recipes.html", {"recipes" : recipes, "category" : Recipe.Categories.choices, "pages_count":pages_count})

def recipe_detail(request:HttpRequest, recipe_id):
        message = None
        try:
            recipe = Recipe.objects.get(pk=recipe_id)

            reviews = Review.objects.filter(recipe=recipe) #this is to get the comments on the above post using filter
            is_saved = request.user.is_authenticated and  Saved.objects.filter(user=request.user, recipe=recipe).exists()
        except Recipe.DoesNotExist:
            return render(request, "404.html")
        except Exception as e:
            message = f"Something went wrong {e}"            
            print(e)
        

        return render(request, "main/recipe_detail.html", {"recipe" : recipe, "reviews": reviews, "is_saved" : is_saved, "message" : message})

def update_recipe(request:HttpRequest, recipe_id):
        message = None
        if not request.user.is_staff:
            return render(request, "no_permission.html")

        try:
            recipe = Recipe.objects.get(pk=recipe_id)
        except Recipe.DoesNotExist:
            return render(request, "404.html")

        if request.method == "POST":
            try:
                recipe.title = request.POST["title"]
                recipe.brief = request.POST["brief"]
                recipe.ingredients = request.POST["ingredients"]
                recipe.instructions = request.POST["instructions"]
                recipe.time_estimate = request.POST["time_estimate"]
                recipe.image = request.FILES.get("image", recipe.image)
                recipe.category = request.POST['category']
                recipe.save()
            except Recipe.DoesNotExist:
                return render(request, "404.html")
            except Exception as e:
                message = f"Something went wrong {e}"
                print(e)
            return redirect("main:recipe_detail", recipe_id= recipe.id)

        return render(request, 'main/update_recipe.html', {"recipe" : recipe, 'category' : Recipe.Categories.choices, "message" : message})

def delete_recipe(request:HttpRequest, recipe_id):

    if not request.user.is_authenticated and request.user.username != recipe.user.username:
        return render(request, "no_permission.html")

    try:
        recipe = Recipe.objects.get(pk=recipe_id)
    except Recipe.DoesNotExist:
        return render(request, "404.html")
    
    try:
        recipe.delete()
    except Exception as e:
        print(e)
    
    return redirect("main:home")

def search(request: HttpRequest):
    recipes = []
    try: 
        if "search" in request.GET:
            recipes = Recipe.objects.filter(title__contains=request.GET["search"])

        # if "date" in request.GET and len(request.GET["date"]) > 4:
        #     first_date = date.fromisoformat(request.GET["date"])
        #     end_date = first_date + timedelta(days=1)
        #     plants = plants.filter(created_at__gte=first_date, created_at__lt=end_date)
    except Exception as e:
        print(e)
    
    context = {"recipes" : recipes}
    return render(request,"main/search.html", context)

def contact(request:HttpRequest):
        if request.method == 'POST':
            try:
                new_con = Contact(
                    first_name = request.POST["first"],
                    last_name = request.POST["last"],
                    email = request.POST["email"],
                    message = request.POST['message']
                )
                new_con.save()
                
            except Exception as e:
                print(e)
            
            # return redirect('main:message')
        return render(request, 'main/contact.html')

def messages(request:HttpRequest):

    if not request.user.is_superuser:
        return render(request, "no_permission.html")

    message = Contact.objects.all()[0:3]

    return render(request,'main/messages.html', {'message' : message})

def add_review(request:HttpRequest, recipe_id):

    if not request.user.is_authenticated:
        return redirect("accounts:login")
    
    if request.method == "POST":

            review = Recipe.objects.get(pk=recipe_id)
            new_review = Review(
            recipe=review,
            user = request.user,
            content=request.POST["content"]
            )
            new_review.save()

    return redirect("main:recipe_detail", recipe_id=review.id)
