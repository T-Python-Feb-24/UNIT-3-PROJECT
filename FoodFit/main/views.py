from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import json , requests

# Create your views here.

def home(request:HttpRequest):

  if request.user.is_authenticated:
     print(request.user.first_name)
  return render(request,"main/Home.html")

 



def search_food(request: HttpRequest):
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
  return render(request,"main/search_food.html" ,{"api" :api_object })
 else:
  return render(request,"main/search_food.html" ,{"query" :"enter vaild input" })
 