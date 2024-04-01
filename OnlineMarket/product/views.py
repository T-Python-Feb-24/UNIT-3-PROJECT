from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Product,Comment,Review
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.


# list صفحة الهوم تعرض بس صورة وتحويل لصفحة الشوب الي هي 
def home_view(request:HttpRequest):

    return render(request, 'product/home.html')




# عرض المنتجات مع امكانية اضافتها للسله
def product_list_view(request:HttpRequest):

    if "cat" in request.GET:
        products_list = Product.objects.filter(category=request.GET["cat"])
    else:
        products_list = Product.objects.all()

    paginator = Paginator(products_list, 4)  # عرض 4 منتجات في كل صفحة
    page_number = request.GET.get('page')

    try:
        products = paginator.page(page_number)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    return render(request, "product/product_list.html", {"products": products, "categories": Product.categories.choices})


# تشمل محتوى العنصر والكومنت والريلايتد
def product_detail_view(request:HttpRequest,product_id):
    try:
        
        product = Product.objects.get(pk=product_id)
        comments=Comment.objects.filter(product=product)
        reviews=Review.objects.filter(product=product)
        related = Product.objects.filter(category=product.category).exclude(id=product_id)[:4]
    except Product.DoesNotExist:
        return render(request)
    except Exception as e:
        print(e)

    return render(request, 'product/product_detail.html' ,{"product":product ,"comments":comments,"reviews":reviews ,"related":related})

#اضافة المنتجات بس للموظف staff
def product_add_view(request:HttpRequest):

    if not request.user.is_staff :
        return render(request, "product/not_found.html")

    if request.method == 'POST':
        try:
            new_product = Product(
                name=request.POST["name"], 
                description=request.POST["description"], 
                category= request.POST["category"], 
                price= request.POST["price"],
                quantity= request.POST["quantity"],
                image=request.FILES["image"])
            
            new_product.save()
            return redirect("product:product_list_view")
        except Exception as e:
            print(e)

    return render(request,"product/product_add.html", {"categories" : Product.categories.choices})

# التعديل فقط staff
def product_edit_view(request:HttpRequest,product_id):

    if not request.user.is_staff:
        return render(request, "product/not_found.html")

    product = Product.objects.get(pk=product_id)

    if request.method == "POST":
        try:
            product.name = request.POST["name"]
            product.description = request.POST["description"]
            product.category = request.POST["category"]
            product.price = request.POST["price"]
            product.quantity=request.POST["quantity"]
            product.image = request.FILES.get("image", product.image)
            product.save()
            return redirect("product:product_detail_view", product_id = product.id)
        except Exception as e:
            print(e)
    return render(request, 'product/product_edit.html',{"product":product ,"categories" : Product.categories.choices})


#الحذف فقط للموظف
def product_delete_view(request:HttpRequest,product_id):
     if not request.user.is_staff:
        return render(request, "product/not_found.html")
     try:
        product = Product.objects.get(pk=product_id)
        product.delete()
     except Exception as e:
        print(e)
     return redirect('product:home_view')

def add_comment_view(request:HttpRequest,product_id):
 
 if not request.user.is_authenticated:
        return redirect("accounts:login_user_view")
 
 if request.method == "POST":
        
        product_object = Product.objects.get(pk=product_id)
        new_comment = Comment(
            product=product_object,
            user=request.user,
            content=request.POST["content"]
              )
        new_comment.save()

    
 return redirect("product:product_detail_view", product_id=product_object.id)

def add_rating_view(request:HttpRequest,product_id):

    if not request.user.is_authenticated:
        return redirect("accounts:login_user_view")
    if request.method == "POST":
        
        product_object = Product.objects.get(pk=product_id)
        rating = int(request.POST.get("rating",0))
        if rating < 1 or rating >5:
            return redirect("product:product_detail_view",product_id)
        new_review = Review(
            product=product_object,
            user=request.user,
            rating=rating
              )
        new_review.save()

    return redirect('product:product_detail_view', product_id=product_object.id)