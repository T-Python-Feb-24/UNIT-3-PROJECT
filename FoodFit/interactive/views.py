from django.shortcuts import render
from django.http import HttpRequest
# Create your views here.

def user_recipe(request: HttpRequest):
    return render(request ,"main/user_recipes.html")


def add_user_recipe(request: HttpRequest):
    return render(request ,"main/add_user_recipe.html")



def user_recipe_detail(request: HttpRequest):
    return render(request ,"main/user_recipe_detail.html")