from django.shortcuts import render , redirect
from django.http import HttpRequest
from .models import UserRecipe , UserComment 
from favorites.models import Favorite
# Create your views here.

def users_recipe(request: HttpRequest):
    if "categories" in request.GET:
     recipes = UserRecipe.objects.filter(category=request.GET["categories"])
    else:
        recipes = UserRecipe.objects.all
    return render(request ,"main/user_recipes.html" , {"recipes" : recipes , "category" : UserRecipe.categories.choices})


def add_user_recipe(request: HttpRequest ):

    if request.method =="POST":
        try:
            new_recipe=UserRecipe(
            user=request.user,
            title=request.POST["title"],
            about=request.POST["about"],
            quantity=request.POST["quantity"],
            calories=request.POST["calories"],
            category=request.POST["category"],
            image=request.FILES.get("image")
            )

            new_recipe.save()
            return redirect('main:user_recipe_detail_page' )

        except Exception as e:
            print(e)
        return redirect('main:home')

    return render(request ,"main/add_user_recipe.html" , { "category" : UserRecipe.categories.choices})



def user_recipe_detail(request: HttpRequest , recipe_id):
 
    try:
        recipe=UserRecipe.objects.get(pk=recipe_id)
        recipes=UserRecipe.objects.filter(user=recipe.user).exclude(id=recipe_id)[0:3]
        comments=UserComment.objects.filter(recipe=recipe).order_by("-created_at")[0:3]
        is_favored = request.user.is_authenticated and  Favorite.objects.filter(user=request.user, recipe=recipe).exists()
    except UserRecipe.DoesNotExist:
        return redirect('main:home')
    except Exception as e:
            print(e)
  
    return render(request ,"main/user_recipe_detail.html" , {"recipe" : recipe ,"recipes" : recipes , "comments":comments , "is_favored":is_favored})




def delete_recipe (request:HttpRequest , recipe_id):
  #if not request.user.is_staff:
    #return render(request, "main/no_permission.html")
  try:
    recipe=UserRecipe.objects.get(pk=recipe_id)
    recipe.delete()
  except UserRecipe.DoesNotExist:
    recipe=None
  except Exception as e:
    print(e)

  return redirect('interactive:users_recipe_page')



def update_recipe (request:HttpRequest,recipe_id):
    recipe=UserRecipe.objects.get(pk=recipe_id)

    if request.method == "POST":
      try:
         recipe.title=request.POST["title"]
         recipe.about=request.POST["about"]
         recipe.quantity=request.POST["quantity"]
         recipe.calories=request.POST["calories"]
         recipe.category=request.POST["category"]
         recipe.image=request.FILES.get("image",recipe.image)
            
         recipe.save()
         return redirect('interactive:user_recipe_detail_page')
      except UserRecipe.DoesNotExist:
         return redirect('main:home')
      except Exception as e:
            print(e)
            return redirect('interactive:user_recipe_detail_page' , recipe_id=recipe.id)
      
    return render(request,"main/update_user_recipe.html", {"recipe" : recipe , "category" : UserRecipe.categories.choices })


def comments(request:HttpRequest , recipe_id):
  #if not request.user.is_authenticated:
        #return redirect('accounts/login_user_view')

    if request.method == "POST":
        recipe_comment=UserRecipe.objects.get(pk=recipe_id)
        comments=UserComment(recipe=recipe_comment,
        user=request.user,
        content=request.POST["content"],
        )
        comments.save()

    return redirect('interactive:user_recipe_detail_page' , recipe_id=recipe_comment.id)