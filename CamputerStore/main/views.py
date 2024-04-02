from django.shortcuts import redirect, render
from django.http import HttpRequest, QueryDict
from .models import Contactus, Prodect, Comments
from django.core.paginator import Paginator


def index_view(request: HttpRequest):

   return render(request, "main/index.html")


def about_view(request: HttpRequest):
   return render(request, "main/about.html")


def search_prodact_view(request: HttpRequest):
   return render(request, "main/search_prodect.html")
# def new_plant_view(request: HttpRequest):
#    if not request.user.is_staff or request.user.is_superuser:
#       return render(request, "main/no_permission.html")
#    if request.method == "POST":
#       new_plant = Plant.objects.create(
#           name=request.POST.get("name"),
#           about=request.POST.get("about"),
#           used_for=request.POST.get("used_for"),
#           image=request.FILES.get("image", Plant.image.field.get_default()),
#           category=request.POST.get("category"),
#           is_edible=request.POST.get("is_edible", False),
#           created_at=request.POST.get("created_at"))

#       return plant_detail_view(request, new_plant.pk)

#    return render(request, "main/add_plant.html", {"categories": Plant.category_choices.choices})


# def plant_detail_view(request: HttpRequest, plant_id):
#    try:
#       plant = Plant.objects.get(pk=plant_id)
#       relateds = Plant.objects.filter(
#           category=plant.category, is_edible=plant.is_edible).exclude(pk=plant_id)
#       comments = Comment.objects.filter(plant=plant)
#    except Plant.DoesNotExist:
#       return render(request, "404.html")
#    except Exception as e:
#       print(e)
#    return render(request, "main/plant_detail.html", {'plant': plant,
#                                                      'relateds': relateds,
#                                                      'comments': comments})


# def update_plant_view(request: HttpRequest, plant_id):
#    try:
#       if not request.user.is_staff or request.user.is_superuser:
#          return render(request, "main/no_permission.html")
#       plant = Plant.objects.get(pk=plant_id)
#       if request.method == "POST":
#          plant.name = request.POST.get("name")
#          plant.about = request.POST.get("about")
#          plant.used_for = request.POST.get("used_for")
#          plant.image = request.FILES.get("image", plant.image)
#          plant.category = request.POST.get("category")
#          plant.is_edible = request.POST.get("is_edible", False)
#          plant.save()
#          return redirect("main:plant_detail_view", plant_id)

#    except Plant.DoesNotExist:
#       return render(request, "404.html")
#    except Exception as e:
#       print(e)
#    return render(request, 'main/update_plant.html', {
#        "plant": plant, "categories": Plant.category_choices.choices})


# def delete_plant_view(request: HttpRequest, plant_id):
#    try:
#       if not request.user.is_staff or request.user.is_superuser:
#          return render(request, "main/no_permission.html")
#       plant = Plant.objects.get(pk=plant_id)
#       plant.delete()
#    except Plant.DoesNotExist:
#       return render(request, "404.html")
#    except Exception as e:
#       print(e)

#    return redirect("main:index_view")


# def search(req: QueryDict):
#    plants = Plant.objects.all()
#    if "name" in req and req.get("name") != "":
#       plants = plants.filter(name__contains=req["name"])
#    if "edible" in req and req.get("edible") != "":
#       plants = plants.filter(is_edible=req["edible"])
#    if "category" in req and req.get("category") != "":
#       plants = plants.filter(category=req["category"])
#       active_cat = req["category"]

#    else:
#       active_cat = "All"
#    pages = Paginator(plants, per_page=3)
#    if "page" in req:
#       if int(req.get("page")) in pages.page_range:
#          plants = pages.get_page(req.get("page"))
#    else:
#       plants = pages.get_page(1)
#    return pages, plants, active_cat


# def all_plants_view(request: HttpRequest):
#    pages, plants, active_cat = search(request.GET)
#    return render(request, "main/all_plants.html",
#                  {"plants": plants, "pages": pages, "active_cat": active_cat,
#                   "categories": Plant.category_choices.choices})


# def search_plants_view(request: HttpRequest):
#    pages, plants, active_cat = search(request.GET)
#    return render(request, "main/search_plant.html",
#                  {"plants": plants, "pages": pages, "active_cat": active_cat,
#                   "categories": Plant.category_choices.choices})


def contactus_view(request: HttpRequest):
   try:
      msg = None
      if request.method == "POST":
         contact = Contactus.objects.create(
            name=request.POST.get("name"),
            email=request.POST.get("email"),
            phone=request.POST.get("phone"),
            content=request.POST.get("content"),
         )
         redirect("main:index_view", context={"msg", msg})
   except Exception as e:
      print(e)
   return render(request, "main/contactus.html")


# def contactUs_messages_view(request: HttpRequest):
#    if not request.user.is_superuser:
#       return render(request, "main/no_permission.html")

#    messages = Contact.objects.all()
#    pages = Paginator(messages, per_page=8)
#    req = request.GET
#    if "page" in req:
#       if int(req.get("page")) in pages.page_range:
#          messages = pages.get_page(req.get("page"))
#    else:
#       messages = pages.get_page(1)
#    return render(request, "main/messages.html", {"pages": pages, "messages": messages})


# def add_comment_view(request: HttpRequest, plant_id):
#    if request.method == "POST":
#       plant = Plant.objects.get(pk=plant_id)
#       Comment.objects.create(
#           plant=plant,
#           user_name=request.user.username,
#           content=request.POST.get("content"))
#    return redirect("main:plant_detail_view", plant_id=plant.pk)
