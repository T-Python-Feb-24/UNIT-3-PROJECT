from django.db.models.manager import BaseManager
from django.shortcuts import redirect, render
from django.http import HttpRequest, QueryDict
from .models import Product, Product_image
from main.validator import validat, ValidationError
from django.core.paginator import Paginator


def search_product_view(request: HttpRequest):
   return render(request, "product/search_product.html")


def add_product_view(request: HttpRequest):
   if not (request.user.is_staff or request.user.has_perm("product.add_product")):
      return render(request, "main/no_permission.html")
   if request.method == "POST":
      images = request.FILES.getlist("images")
      print(images)
      new_product = Product.objects.create(
          name=request.POST.get("name"),
          model=request.POST.get("model"),
          category=request.POST.get("category"),
          price=request.POST.get("price"),
          in_stock=request.POST.get("in_stock", False),
      )

      for image in images:
         Product_image.objects.create(product=new_product, image=image)

      return redirect("product:product_detail_view", product_name=new_product.name)

   return render(request, "product/add_product.html", {"categories": Product.categories_choices.choices})


def product_detail_view(request: HttpRequest, product_pk):
   try:
      product = Product.objects.get(pk=product_pk)

   except Exception as e:
      print(e)
   return render(request, "product/product_detail.html", {"product": product})


def product_by_category(request: HttpRequest, category: str):
   msg = None
   try:
      products: BaseManager[Product] = Product.objects.filter(
         category=category)
      print(Product_image.objects.get(pk=1).image.name)
      pages = Paginator(products.order_by('-created_at'), per_page=3)
      req = request.GET
      if "page" in req:
         if int(req.get("page")) in pages.page_range:
            products = pages.get_page(req.get("page"))
      else:
         products = pages.get_page(1)
      return render(request, "product/product_by_category.html",
                    {"products": products, "pages": pages, "category": category})
   except Product.DoesNotExist:
      msg = "لا يوجد منتجات حاليا"
      return render(request, "product/product_by_category.html", {"msg": msg})

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
